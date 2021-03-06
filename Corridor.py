import arcpy

def Corridor():  # Corridor

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")

    San_Lucas_5_ = arcpy.Raster("CostDist\\San Lucas")
    Choco = arcpy.Raster("CostDist\\Choco")
    San_Lucas_4_ = arcpy.Raster("CostDist\\San Lucas")
    Paramillo = arcpy.Raster("CostDist\\Paramillo")
    San_Lucas_3_ = arcpy.Raster("CostDist\\San Lucas")
    Perija = arcpy.Raster("CostDist\\Perija")
    San_Lucas_2_ = arcpy.Raster("CostDist\\San Lucas")
    Catatumbo = arcpy.Raster("CostDist\\Catatumbo")
    Sierra_Nevada = arcpy.Raster("CostDist\\Sierra Nevada")
    San_Lucas = arcpy.Raster("CostDist\\San Lucas")
    Panthera_Onca_gdb = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb"
    August21CostDistSanLucas_August21CostDistSanLucas_2_ = arcpy.Raster("ModelBuilder\\August21CostDistSanLucas:August21CostDistSanLucas")
    August21CostDistCatatumbo_August21CostDistCatatumbo = arcpy.Raster("ModelBuilder\\August21CostDistCatatumbo:August21CostDistCatatumbo")
    August21CostDistSanLucas_August21CostDistSanLucas_3_ = arcpy.Raster("ModelBuilder\\August21CostDistSanLucas:August21CostDistSanLucas")
    August21CostDistPerija_August21CostDistPerija = arcpy.Raster("ModelBuilder\\August21CostDistPerija:August21CostDistPerija")
    August21CostDistSanLucas_August21CostDistSanLucas_5_ = arcpy.Raster("ModelBuilder\\August21CostDistSanLucas:August21CostDistSanLucas")
    August21CostDistChoco_August21CostDistChoco = arcpy.Raster("ModelBuilder\\August21CostDistChoco:August21CostDistChoco")

    # Process: Corridor (5)
    August21CorridorChoco = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorChoco"
    Corridor_5_ = August21CorridorChoco
    August21CorridorChoco = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_5_, in_distance_raster2=Choco)
    August21CorridorChoco.save(Corridor_5_)


    # Process: Corridor (4)
    August21CorridorParamillo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorParamillo"
    Corridor_4_ = August21CorridorParamillo
    August21CorridorParamillo = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_4_, in_distance_raster2=Paramillo)
    August21CorridorParamillo.save(Corridor_4_)


    # Process: Corridor (3)
    August21CorridorPerijo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorPerijo"
    Corridor_3_ = August21CorridorPerijo
    August21CorridorPerijo = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_3_, in_distance_raster2=Perija)
    August21CorridorPerijo.save(Corridor_3_)


    # Process: Corridor (2)
    August21CorridorCatatumbo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorCatatumbo"
    Corridor_2_ = August21CorridorCatatumbo
    August21CorridorCatatumbo = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_2_, in_distance_raster2=Catatumbo)
    August21CorridorCatatumbo.save(Corridor_2_)


    # Process: Corridor
    August21CorridorSierraNevada = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorSierraNevada"
    Corridor = August21CorridorSierraNevada
    August21CorridorSierraNevada = arcpy.sa.Corridor(in_distance_raster1=Sierra_Nevada, in_distance_raster2=San_Lucas)
    August21CorridorSierraNevada.save(Corridor)


    # Process: Mosaic To New Raster
    August21FinalCorridor = arcpy.management.MosaicToNewRaster(input_rasters=[August21CorridorChoco, August21CorridorParamillo, August21CorridorPerijo, August21CorridorCatatumbo, August21CorridorSierraNevada], output_location=Panthera_Onca_gdb, raster_dataset_name_with_extension="August21FinalCorridor", coordinate_system_for_the_raster="PROJCS[\"WGS_1984_UTM_Zone_18N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-75.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", pixel_type="32_BIT_UNSIGNED", cellsize=100, number_of_bands=1, mosaic_method="MINIMUM", mosaic_colormap_mode="FIRST")[0]
    August21FinalCorridor = arcpy.Raster(August21FinalCorridor)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        Corridor()
