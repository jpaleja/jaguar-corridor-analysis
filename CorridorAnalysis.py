import arcpy

def CorridorAnalysis():  # CorridorAnalysis

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageExt")
    arcpy.CheckOutExtension("ImageAnalyst")

    August21FinalCorridor_2_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21FinalCorridor")
    Panthera_JCUs_2_ = "JCU Source\\Panthera JCUs"
    COL_adm0 = "COL_adm0"

    # Process: Reclassify
    August21FinalCorridorReclass = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21FinalCorridorReclass"
    arcpy.ddd.Reclassify(in_raster=August21FinalCorridor_2_, reclass_field="Value", remap="462107 800000 1;800000 1000000 2;1000000 1200000 3;1200000 1500000 4;1500000 2200000 5;2200000 3000000 6;3000000 4000000 7;4000000 5200000 8;5200000 7000000 9;7000000 18000000 10", out_raster=August21FinalCorridorReclass, missing_values="DATA")
    August21FinalCorridorReclass = arcpy.Raster(August21FinalCorridorReclass)

    # Process: Raster to Polygon
    FinalCorridorReclassed10ManualClasses = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\New_Corridors\\FinalCorridorReclassed10ManualClasses"
    arcpy.conversion.RasterToPolygon(in_raster=August21FinalCorridorReclass, out_polygon_features=FinalCorridorReclassed10ManualClasses, simplify="SIMPLIFY", raster_field="VALUE", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)

    # Process: Erase
    FinalCorridorReclassedAllClassesClipped = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\New_Corridors\\FinalCorridorReclassedAllClassesClipped"
    arcpy.analysis.Erase(in_features=FinalCorridorReclassed10ManualClasses, erase_features=Panthera_JCUs_2_, out_feature_class=FinalCorridorReclassedAllClassesClipped, cluster_tolerance="")

    # Process: Clip
    FinalCorridorReclassedAllClassesClipped2 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\New_Corridors\\FinalCorridorReclassedAllClassesClipped2"
    arcpy.analysis.Clip(in_features=FinalCorridorReclassedAllClassesClipped, clip_features=COL_adm0, out_feature_class=FinalCorridorReclassedAllClassesClipped2, cluster_tolerance="")

    # Process: Zonal Statistics as Table
    ZonalStatsAllClasses = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\New_Corridors\\ZonalStatsAllClasses"
    arcpy.ia.ZonalStatisticsAsTable(in_zone_data=FinalCorridorReclassedAllClassesClipped2, zone_field="GRIDCODE", in_value_raster=August21FinalCorridor_2_, out_table=ZonalStatsAllClasses, ignore_nodata="DATA", statistics_type="ALL", process_as_multidimensional="CURRENT_SLICE", percentile_values=90, percentile_interpolation_type="AUTO_DETECT")
    .save(Zonal_Statistics_as_Table)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        CorridorAnalysis()
