import arcpy

def CorridorTreeLoss():  # CorridorTreeLoss

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")

    San_Lucas_5_ = arcpy.Raster("Tree Loss Cost Distance\\San Lucas")
    Choco = arcpy.Raster("Tree Loss Cost Distance\\Choco")
    San_Lucas_4_ = arcpy.Raster("Tree Loss Cost Distance\\San Lucas")
    Paramillo = arcpy.Raster("Tree Loss Cost Distance\\Paramillo")
    San_Lucas_3_ = arcpy.Raster("Tree Loss Cost Distance\\San Lucas")
    Perija = arcpy.Raster("Tree Loss Cost Distance\\Perija")
    San_Lucas_2_ = arcpy.Raster("Tree Loss Cost Distance\\San Lucas")
    Catatumbo = arcpy.Raster("Tree Loss Cost Distance\\Catatumbo")
    San_Lucas = arcpy.Raster("Tree Loss Cost Distance\\San Lucas")
    Sierra_Nevada = arcpy.Raster("Tree Loss Cost Distance\\Sierra Nevada")
    Panthera_Onca_gdb = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb"

    # Process: Corridor (5) (Corridor) (sa)
    August21CorridorTreeLossChoco = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorTreeLossChoco"
    Corridor_5_ = August21CorridorTreeLossChoco
    August21CorridorTreeLossChoco = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_5_, in_distance_raster2=Choco)
    August21CorridorTreeLossChoco.save(Corridor_5_)


    # Process: Corridor (4) (Corridor) (sa)
    August21CorridorTreeLossParamillo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorTreeLossParamillo"
    Corridor_4_ = August21CorridorTreeLossParamillo
    August21CorridorTreeLossParamillo = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_4_, in_distance_raster2=Paramillo)
    August21CorridorTreeLossParamillo.save(Corridor_4_)


    # Process: Corridor (3) (Corridor) (sa)
    August21CorridorTreeLossPerija = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorTreeLossPerija"
    Corridor_3_ = August21CorridorTreeLossPerija
    August21CorridorTreeLossPerija = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_3_, in_distance_raster2=Perija)
    August21CorridorTreeLossPerija.save(Corridor_3_)


    # Process: Corridor (2) (Corridor) (sa)
    August21CorridorTreeLossCatatumbo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorTreeLossCatatumbo"
    Corridor_2_ = August21CorridorTreeLossCatatumbo
    August21CorridorTreeLossCatatumbo = arcpy.sa.Corridor(in_distance_raster1=San_Lucas_2_, in_distance_raster2=Catatumbo)
    August21CorridorTreeLossCatatumbo.save(Corridor_2_)


    # Process: Corridor (Corridor) (sa)
    August21CorridorTreeLossSierraNevada = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CorridorTreeLossSierraNevada"
    Corridor = August21CorridorTreeLossSierraNevada
    August21CorridorTreeLossSierraNevada = arcpy.sa.Corridor(in_distance_raster1=San_Lucas, in_distance_raster2=Sierra_Nevada)
    August21CorridorTreeLossSierraNevada.save(Corridor)


    # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
    August21FinalCorridorTreeLoss = arcpy.management.MosaicToNewRaster(input_rasters=[August21CorridorTreeLossChoco, August21CorridorTreeLossParamillo, August21CorridorTreeLossPerija, August21CorridorTreeLossCatatumbo, August21CorridorTreeLossSierraNevada], output_location=Panthera_Onca_gdb, raster_dataset_name_with_extension="August21FinalCorridorTreeLoss", coordinate_system_for_the_raster="PROJCS[\"WGS_1984_UTM_Zone_18N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",-75.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0]]", pixel_type="32_BIT_UNSIGNED", cellsize=100, number_of_bands=1, mosaic_method="MINIMUM", mosaic_colormap_mode="FIRST")[0]
    August21FinalCorridorTreeLoss = arcpy.Raster(August21FinalCorridorTreeLoss)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        CorridorTreeLoss()
