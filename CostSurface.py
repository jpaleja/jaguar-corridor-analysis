import arcpy

def CostSurface():  # CostSurface

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")

    # Model Environment settings
    with arcpy.EnvManager(outputCoordinateSystem="PROJCS["WGS_1984_UTM_Zone_18N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]"):
        Elevation = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\August21DEMReclassed")
        Settlements_gis_osm_landuse_a_free_1 = "Cost Surface Layers\\Initial Data\\Settlements - gis_osm_landuse_a_free_1"
        Night_Lights_F182013_v4c_web_stable_lights_avg_vis_tif_2_ = arcpy.Raster("Cost Surface Layers\\Initial Data\\Night Lights - F182013.v4c_web.stable_lights.avg_vis.tif")
        Roads_gis_osm_roads_free_1 = "Cost Surface Layers\\Initial Data\\Roads - gis_osm_roads_free_1"
        Population_density_col_ppp_2019_UNadj_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\Population density - col_ppp_2019_UNadj.tif")
        AOI = "AOI"
        Land_Use_W080N20_PROBAV_LC100_global_v3_0_1_2019_nrt_Discrete_Classification_map_EPSG_4326_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\Land Use - W080N20_PROBAV_LC100_global_v3.0.1_2019-nrt_Discrete-Classification-map_EPSG-4326.tif")
        PROBAV_LC100_global_v3_0_1_2019_nrt_Shrub_CoverFraction_layer_EPSG_4326_tif_2_ = arcpy.Raster("Cost Surface Layers\\Initial Data\\PROBAV_LC100_global_v3.0.1_2019-nrt_Shrub-CoverFraction-layer_EPSG-4326.tif")
        AOI_2_ = "AOI"
        PROBAV_LC100_global_v3_0_1_2019_nrt_Tree_CoverFraction_layer_EPSG_4326_tif_2_ = arcpy.Raster("Cost Surface Layers\\Initial Data\\PROBAV_LC100_global_v3.0.1_2019-nrt_Tree-CoverFraction-layer_EPSG-4326.tif")
        AOI_3_ = "AOI"
        Panthera_Onca_gdb_2_ = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb"

        # Process: Raster to Polygon
        LightsAtNight2013 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\LightsAtNight2013"
        arcpy.conversion.RasterToPolygon(in_raster=Night_Lights_F182013_v4c_web_stable_lights_avg_vis_tif_2_, out_polygon_features=LightsAtNight2013, simplify="SIMPLIFY", raster_field="Value", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)

        # Process: Merge
        MergedLightsAtNightOSMPlaces = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\MergedLightsAtNightOSMPlaces"
        arcpy.management.Merge(inputs=[Settlements_gis_osm_landuse_a_free_1, LightsAtNight2013], output=MergedLightsAtNightOSMPlaces, field_mappings="osm_id \"osm_id\" true true false 10 Text 0 0,First,#,Cost Surface Layers\\Initial Data\\Settlements - gis_osm_landuse_a_free_1,osm_id,0,10;code \"code\" true true false 4 Short 0 4,First,#,Cost Surface Layers\\Initial Data\\Settlements - gis_osm_landuse_a_free_1,code,-1,-1;fclass \"fclass\" true true false 28 Text 0 0,First,#,Cost Surface Layers\\Initial Data\\Settlements - gis_osm_landuse_a_free_1,fclass,0,28;name \"name\" true true false 100 Text 0 0,First,#,Cost Surface Layers\\Initial Data\\Settlements - gis_osm_landuse_a_free_1,name,0,100;Shape_Length \"Shape_Length\" false false true 0 Double 0 0,First,#,C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\LightsAtNight2013,Shape_Length,-1,-1;Shape_Area \"Shape_Area\" false false true 0 Double 0 0,First,#,C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\LightsAtNight2013,Shape_Area,-1,-1;ID \"ID\" true true false 0 Long 0 0,First,#,C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\LightsAtNight2013,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0,First,#,C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\LightsAtNight2013,GRIDCODE,-1,-1", add_source="NO_SOURCE_INFO")

        # Process: Euclidean Distance
        Euclidean_Settlements = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\Euclidean_Settlements"
        Euclidean_Distance = Euclidean_Settlements
        Output_direction_raster = ""
        Out_back_direction_raster = ""
        Euclidean_Settlements = arcpy.sa.EucDistance(in_source_data=MergedLightsAtNightOSMPlaces, maximum_distance=None, cell_size="100", out_direction_raster=Output_direction_raster, distance_method="PLANAR", in_barrier_data="", out_back_direction_raster=Out_back_direction_raster)
        Euclidean_Settlements.save(Euclidean_Distance)


        # Process: Reclassify
        Settlements = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21Settlements2019Reclassed"
        arcpy.ddd.Reclassify(in_raster=Euclidean_Settlements, reclass_field="VALUE", remap="0 20000 8;20000 40000 5;40000 80000 4;80000 160000 1;160000 189444.578125 0", out_raster=Settlements, missing_values="DATA")
        Settlements = arcpy.Raster(Settlements)

        # Process: Euclidean Distance (2)
        Euclidean_Roads = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\Euclidean_Roads"
        Euclidean_Distance_2_ = Euclidean_Roads
        Output_direction_raster_2_ = ""
        Out_back_direction_raster_2_ = ""
        Euclidean_Roads = arcpy.sa.EucDistance(in_source_data=Roads_gis_osm_roads_free_1, maximum_distance=None, cell_size="100", out_direction_raster=Output_direction_raster_2_, distance_method="PLANAR", in_barrier_data="", out_back_direction_raster=Out_back_direction_raster_2_)
        Euclidean_Roads.save(Euclidean_Distance_2_)


        # Process: Reclassify (4)
        Roads = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21RoadsEuclDistReclassed"
        arcpy.ddd.Reclassify(in_raster=Euclidean_Roads, reclass_field="VALUE", remap="0 2000 7;2000 4000 4;4000 8000 2;8000 16000 1;16000 189767.281250 0", out_raster=Roads, missing_values="DATA")
        Roads = arcpy.Raster(Roads)

        # Process: Clip Raster
        WorldPop_2_ = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\WorldPop"
        arcpy.management.Clip(in_raster=Population_density_col_ppp_2019_UNadj_tif, rectangle="-1497926.37644292 601990.309096972 1046389.64517458 2238826.54603369", out_raster=WorldPop_2_, in_template_dataset=AOI, nodata_value="-99999", clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
        WorldPop_2_ = arcpy.Raster(WorldPop_2_)

        # Process: Reclassify (5)
        Population_Density = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21ColombiaWorldPopReclassed"
        arcpy.ddd.Reclassify(in_raster=WorldPop_2_, reclass_field="VALUE", remap="0 20 1;20 40 5;40 80 7;80 160 9;160 320 10;320 500 10", out_raster=Population_Density, missing_values="DATA")
        Population_Density = arcpy.Raster(Population_Density)

        # Process: Reclassify (6)
        Land_Use_Type = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21LandUse2019DiscreteClassCopernicusReclassed"
        arcpy.ddd.Reclassify(in_raster=Land_Use_W080N20_PROBAV_LC100_global_v3_0_1_2019_nrt_Discrete_Classification_map_EPSG_4326_tif, reclass_field="Value", remap="0 10;20 2;30 5;40 8;50 10;60 6;70 0;80 6;90 2;111 1;112 0;114 0;115 0;116 1;121 1;122 0;124 0;125 0;126 1;200 10", out_raster=Land_Use_Type, missing_values="DATA")
        Land_Use_Type = arcpy.Raster(Land_Use_Type)

        # Process: Clip Raster (2)
        ShrubCoverAOI2 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\ShrubCoverAOI2"
        arcpy.management.Clip(in_raster=PROBAV_LC100_global_v3_0_1_2019_nrt_Shrub_CoverFraction_layer_EPSG_4326_tif_2_, rectangle="-1497926.37644292 601990.309096972 1046389.64517458 2238826.54603369", out_raster=ShrubCoverAOI2, in_template_dataset=AOI_2_, nodata_value="255", clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
        ShrubCoverAOI2 = arcpy.Raster(ShrubCoverAOI2)

        # Process: Clip Raster (3)
        TreeCoverAOI2 = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\TreeCoverAOI2"
        arcpy.management.Clip(in_raster=PROBAV_LC100_global_v3_0_1_2019_nrt_Tree_CoverFraction_layer_EPSG_4326_tif_2_, rectangle="-1497926.37644292 601990.309096972 1046389.64517458 2238826.54603369", out_raster=TreeCoverAOI2, in_template_dataset=AOI_3_, nodata_value="255", clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
        TreeCoverAOI2 = arcpy.Raster(TreeCoverAOI2)

        # Process: Mosaic To New Raster (2)
        PercentTreeShrubCoverCopernicusClipped3_2_ = arcpy.management.MosaicToNewRaster(input_rasters=[ShrubCoverAOI2, TreeCoverAOI2], output_location=Panthera_Onca_gdb_2_, raster_dataset_name_with_extension="PercentTreeShrubCoverCopernicusClipped3", coordinate_system_for_the_raster="PROJCS[\"WGS_1984_UTM_Zone_18N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-75.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", pixel_type="8_BIT_UNSIGNED", cellsize=100, number_of_bands=1, mosaic_method="MAXIMUM", mosaic_colormap_mode="FIRST")[0]
        PercentTreeShrubCoverCopernicusClipped3_2_ = arcpy.Raster(PercentTreeShrubCoverCopernicusClipped3_2_)

        # Process: Reclassify (2)
        _Tree_and_Shrub_Cover = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21TreeShrubCoverReclassed"
        arcpy.ddd.Reclassify(in_raster=PercentTreeShrubCoverCopernicusClipped3_2_, reclass_field="Value", remap="0 10 9;10 20 7;20 40 5;40 60 2;60 80 0;80 100 0", out_raster=_Tree_and_Shrub_Cover, missing_values="DATA")
        _Tree_and_Shrub_Cover = arcpy.Raster(_Tree_and_Shrub_Cover)

        # Process: Weighted Sum
        Cost_Surface = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceEqualWeighting"
        Weighted_Sum = Cost_Surface
        Cost_Surface = arcpy.ia.WeightedSum(in_rasters=[[Elevation, "Value", 1], [Settlements, "VALUE", 1], [Roads, "VALUE", 1], [Population_Density, "VALUE", 1], [Land_Use_Type, "VALUE", 1], [_Tree_and_Shrub_Cover, "VALUE", 1]])
        Cost_Surface.save(Weighted_Sum)


        # Process: DEM Mosaic () ()
        arcpy.ERROR_UNKNOWN_TOOLBOX.ERROR_UNKNOWN_TOOL()

        # Process: DEM Mosaic (2) () ()
        arcpy.ERROR_UNKNOWN_TOOLBOX.ERROR_UNKNOWN_TOOL()

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        CostSurface()
