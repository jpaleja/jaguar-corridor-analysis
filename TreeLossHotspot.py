import arcpy

def TreeLossHotspot():  # TreeLossHotspot

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")

    TreeLoss_EmergingHotSpotAnalysis6 = "Tree Loss\\TreeLoss_EmergingHotSpotAnalysis6"
    PercentTreeShrubCoverCopernicusClipped3_2_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\PercentTreeShrubCoverCopernicusClipped3")
    Hansen_GFC_2020_v1_8_lossyear_20N_080W_tif = arcpy.Raster("Imagery\\Tree Loss - Hansen\\Hansen_GFC-2020-v1.8_lossyear_20N_080W.tif")
    Study_Area = "Study Area"
    Hansen_GFC_2020_v1_8_lossyear_10N_080W_tif = arcpy.Raster("Imagery\\Tree Loss - Hansen\\Hansen_GFC-2020-v1.8_lossyear_10N_080W.tif")
    Study_Area_2_ = "Study Area"
    Panthera_Onca_gdb = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb"

    # Process: Clip Raster
    TreeLossClipped = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLossClipped"
    arcpy.management.Clip(in_raster=Hansen_GFC_2020_v1_8_lossyear_20N_080W_tif, rectangle="-10229684.6988494 634657.233734029 -7828659.18873123 2104338.88701407", out_raster=TreeLossClipped, in_template_dataset=Study_Area, nodata_value="256", clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
    TreeLossClipped = arcpy.Raster(TreeLossClipped)

    # Process: Clip Raster
    TreeLossClipped2_2_ = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLossClipped2"
    arcpy.management.Clip(in_raster=Hansen_GFC_2020_v1_8_lossyear_10N_080W_tif, rectangle="-10229684.6988494 634657.233734029 -7828659.18873123 2104338.88701407", out_raster=TreeLossClipped2_2_, in_template_dataset=Study_Area_2_, nodata_value="255", clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
    TreeLossClipped2_2_ = arcpy.Raster(TreeLossClipped2_2_)

    # Process: Mosaic To New Raster
    CombinedTreeLossHansenClip = arcpy.management.MosaicToNewRaster(input_rasters=[TreeLossClipped, TreeLossClipped2_2_], output_location=Panthera_Onca_gdb, raster_dataset_name_with_extension="CombinedTreeLossHansenClip", coordinate_system_for_the_raster="PROJCS[\"WGS_1984_UTM_Zone_18N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-75.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", pixel_type="8_BIT_UNSIGNED", cellsize=None, number_of_bands=1, mosaic_method="LAST", mosaic_colormap_mode="FIRST")[0]
    CombinedTreeLossHansenClip = arcpy.Raster(CombinedTreeLossHansenClip)

    # Process: Raster to Point
    TreeLossPoints = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLossPoints"
    arcpy.conversion.RasterToPoint(in_raster=CombinedTreeLossHansenClip, out_point_features=TreeLossPoints, raster_field="Value")

    # Process: Create Space Time Cube By Aggregating Points
    TreeLoss6_nc = "C:\\Users\\jpale\\Downloads\\Downloads\\TreeLoss6.nc"
    arcpy.stpm.CreateSpaceTimeCube(in_features=TreeLossPoints, output_cube=TreeLoss6_nc, time_field="time", template_cube="", time_step_interval="", time_step_alignment="END_TIME", reference_time="", distance_interval="", summary_fields=[], aggregation_shape_type="FISHNET_GRID", defined_polygon_locations="", location_id="")

    # Process: Emerging Hot Spot Analysis
    TreeLoss_EmergingHotSpotAnalysis6_4_ = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLoss_EmergingHotSpotAnalysis6"
    arcpy.stpm.EmergingHotSpotAnalysis(in_cube=TreeLoss6_nc, analysis_variable="time", output_features=TreeLoss_EmergingHotSpotAnalysis6_4_, neighborhood_distance="", neighborhood_time_step=1, polygon_mask="", conceptualization_of_spatial_relationships="FIXED_DISTANCE", number_of_neighbors=None, define_global_window="ENTIRE_CUBE")

    # Process: Polygon to Raster
    TreeLossHotspots = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLossHotspots"
    arcpy.conversion.PolygonToRaster(in_features=TreeLoss_EmergingHotSpotAnalysis6_4_, value_field="PERC_HOT", out_rasterdataset=TreeLossHotspots, cell_assignment="CELL_CENTER", priority_field="NONE", cellsize="100", build_rat="BUILD")

    # Process: Reclassify
    August21TreeLossReclassed = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21TreeLossReclassed"
    Reclassify = August21TreeLossReclassed
    August21TreeLossReclassed = arcpy.sa.Reclassify(in_raster=TreeLossHotspots, reclass_field="VALUE", remap="0 20 1;20 40 2;40 60 3;60 80 4;80 100 5", missing_values="DATA")
    August21TreeLossReclassed.save(Reclassify)


    # Process: Raster to Polygon
    PercentTreeShrubCoverCopernicusClipped2 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\PercentTreeShrubCoverCopernicusClipped2"
    if August21TreeLossReclassed:
        with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
            arcpy.conversion.RasterToPolygon(in_raster=PercentTreeShrubCoverCopernicusClipped3_2_, out_polygon_features=PercentTreeShrubCoverCopernicusClipped2, simplify="SIMPLIFY", raster_field="Value", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)

    # Process: Pairwise Clip
    TreeLossHotspotClipped2 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLossHotspotClipped2"
    if August21TreeLossReclassed:
        arcpy.analysis.PairwiseClip(in_features=TreeLoss_EmergingHotSpotAnalysis6, clip_features=PercentTreeShrubCoverCopernicusClipped2, out_feature_class=TreeLossHotspotClipped2, cluster_tolerance="")

    # Process: Polygon to Raster
    TreeLossClipped2 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeLossClipped2"
    if August21TreeLossReclassed:
        arcpy.conversion.PolygonToRaster(in_features=TreeLossHotspotClipped2, value_field="PERC_HOT", out_rasterdataset=TreeLossClipped2, cell_assignment="CELL_CENTER", priority_field="NONE", cellsize="100", build_rat="BUILD")

    # Process: Reclassify
    Tree_Loss_Reclassed = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21TreeLossReclassed"
    if August21TreeLossReclassed:
        arcpy.ddd.Reclassify(in_raster=TreeLossClipped2, reclass_field="Value", remap="0 20 1;20 40 2;40 60 3;60 80 4;80 100 5;NODATA 0", out_raster=Tree_Loss_Reclassed, missing_values="DATA")
        Tree_Loss_Reclassed = arcpy.Raster(Tree_Loss_Reclassed)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        TreeLossHotspot()
