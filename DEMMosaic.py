import arcpy

def DEMMosaic():  # DEMMosaic

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")

    ASTGTMV003_N05W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W073_dem.tif")
    ASTGTMV003_N05W075_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W075_dem.tif")
    ASTGTMV003_N05W077_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W077_dem.tif")
    ASTGTMV003_N06W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W072_dem.tif")
    ASTGTMV003_N06W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W074_dem.tif")
    ASTGTMV003_N06W077_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W077_dem.tif")
    ASTGTMV003_N07W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W072_dem.tif")
    ASTGTMV003_N07W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W074_dem.tif")
    ASTGTMV003_N07W076_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W076_dem.tif")
    ASTGTMV003_N07W078_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W078_dem.tif")
    ASTGTMV003_N08W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W073_dem.tif")
    ASTGTMV003_N08W075_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W075_dem.tif")
    ASTGTMV003_N08W077_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W077_dem.tif")
    ASTGTMV003_N09W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W072_dem.tif")
    ASTGTMV003_N09W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W074_dem.tif")
    ASTGTMV003_N09W076_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W076_dem.tif")
    ASTGTMV003_N09W078_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W078_dem.tif")
    ASTGTMV003_N10W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W073_dem.tif")
    ASTGTMV003_N10W075_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W075_dem.tif")
    ASTGTMV003_N11W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W072_dem.tif")
    ASTGTMV003_N11W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W074_dem.tif")
    ASTGTMV003_N12W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N12W072_dem.tif")
    ASTGTMV003_N05W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W072_dem.tif")
    ASTGTMV003_N05W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W074_dem.tif")
    ASTGTMV003_N05W076_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W076_dem.tif")
    ASTGTMV003_N05W078_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W078_dem.tif")
    ASTGTMV003_N06W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W073_dem.tif")
    ASTGTMV003_N06W076_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W076_dem.tif")
    ASTGTMV003_N06W078_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W078_dem.tif")
    ASTGTMV003_N07W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W073_dem.tif")
    ASTGTMV003_N07W075_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W075_dem.tif")
    ASTGTMV003_N07W077_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W077_dem.tif")
    ASTGTMV003_N08W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W072_dem.tif")
    ASTGTMV003_N08W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W074_dem.tif")
    ASTGTMV003_N08W076_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W076_dem.tif")
    ASTGTMV003_N08W078_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W078_dem.tif")
    ASTGTMV003_N09W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W073_dem.tif")
    ASTGTMV003_N09W075_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W075_dem.tif")
    ASTGTMV003_N09W077_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W077_dem.tif")
    ASTGTMV003_N10W072_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W072_dem.tif")
    ASTGTMV003_N10W074_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W074_dem.tif")
    ASTGTMV003_N10W076_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W076_dem.tif")
    ASTGTMV003_N11W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W073_dem.tif")
    ASTGTMV003_N11W075_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W075_dem.tif")
    ASTGTMV003_N12W073_dem_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N12W073_dem.tif")
    DEM = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\DEM")
    ASTGTMV003_N05W076_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W076_num.tif")
    ASTGTMV003_N05W077_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W077_num.tif")
    ASTGTMV003_N05W078_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N05W078_num.tif")
    ASTGTMV003_N06W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W072_num.tif")
    ASTGTMV003_N06W073_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W073_num.tif")
    ASTGTMV003_N06W074_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W074_num.tif")
    ASTGTMV003_N06W076_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W076_num.tif")
    ASTGTMV003_N06W077_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W077_num.tif")
    ASTGTMV003_N06W078_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N06W078_num.tif")
    ASTGTMV003_N07W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W072_num.tif")
    ASTGTMV003_N07W073_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W073_num.tif")
    ASTGTMV003_N07W074_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W074_num.tif")
    ASTGTMV003_N07W075_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W075_num.tif")
    ASTGTMV003_N07W076_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W076_num.tif")
    ASTGTMV003_N07W077_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W077_num.tif")
    ASTGTMV003_N07W078_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N07W078_num.tif")
    ASTGTMV003_N08W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W072_num.tif")
    ASTGTMV003_N08W073_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W073_num.tif")
    ASTGTMV003_N08W074_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W074_num.tif")
    ASTGTMV003_N08W075_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W075_num.tif")
    ASTGTMV003_N08W076_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W076_num.tif")
    ASTGTMV003_N08W077_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W077_num.tif")
    ASTGTMV003_N08W078_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N08W078_num.tif")
    ASTGTMV003_N09W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W072_num.tif")
    ASTGTMV003_N09W073_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W073_num.tif")
    ASTGTMV003_N09W074_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W074_num.tif")
    ASTGTMV003_N09W075_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W075_num.tif")
    ASTGTMV003_N09W076_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W076_num.tif")
    ASTGTMV003_N09W077_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W077_num.tif")
    ASTGTMV003_N09W078_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N09W078_num.tif")
    ASTGTMV003_N10W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W072_num.tif")
    ASTGTMV003_N10W073_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W073_num.tif")
    ASTGTMV003_N10W074_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W074_num.tif")
    ASTGTMV003_N10W075_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W075_num.tif")
    ASTGTMV003_N10W076_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N10W076_num.tif")
    ASTGTMV003_N11W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W072_num.tif")
    ASTGTMV003_N11W073_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W073_num.tif")
    ASTGTMV003_N11W074_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W074_num.tif")
    ASTGTMV003_N11W075_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N11W075_num.tif")
    ASTGTMV003_N12W072_num_tif = arcpy.Raster("Cost Surface Layers\\Initial Data\\DEM\\ASTGTMV003_N12W072_num.tif")

    # Process: Mosaic
    DEM_3_ = arcpy.management.Mosaic(inputs=[ASTGTMV003_N05W073_dem_tif, ASTGTMV003_N05W075_dem_tif, ASTGTMV003_N05W077_dem_tif, ASTGTMV003_N06W072_dem_tif, ASTGTMV003_N06W074_dem_tif, ASTGTMV003_N06W077_dem_tif, ASTGTMV003_N07W072_dem_tif, ASTGTMV003_N07W074_dem_tif, ASTGTMV003_N07W076_dem_tif, ASTGTMV003_N07W078_dem_tif, ASTGTMV003_N08W073_dem_tif, ASTGTMV003_N08W075_dem_tif, ASTGTMV003_N08W077_dem_tif, ASTGTMV003_N09W072_dem_tif, ASTGTMV003_N09W074_dem_tif, ASTGTMV003_N09W076_dem_tif, ASTGTMV003_N09W078_dem_tif, ASTGTMV003_N10W073_dem_tif, ASTGTMV003_N10W075_dem_tif, ASTGTMV003_N11W072_dem_tif, ASTGTMV003_N11W074_dem_tif, ASTGTMV003_N12W072_dem_tif, ASTGTMV003_N05W072_dem_tif, ASTGTMV003_N05W073_dem_tif, ASTGTMV003_N05W074_dem_tif, ASTGTMV003_N05W075_dem_tif, ASTGTMV003_N05W076_dem_tif, ASTGTMV003_N05W077_dem_tif, ASTGTMV003_N05W078_dem_tif, ASTGTMV003_N06W072_dem_tif, ASTGTMV003_N06W073_dem_tif, ASTGTMV003_N06W074_dem_tif, ASTGTMV003_N06W076_dem_tif, ASTGTMV003_N06W077_dem_tif, ASTGTMV003_N06W078_dem_tif, ASTGTMV003_N07W072_dem_tif, ASTGTMV003_N07W073_dem_tif, ASTGTMV003_N07W074_dem_tif, ASTGTMV003_N07W075_dem_tif, ASTGTMV003_N07W076_dem_tif, ASTGTMV003_N07W077_dem_tif, ASTGTMV003_N07W078_dem_tif, ASTGTMV003_N08W072_dem_tif, ASTGTMV003_N08W073_dem_tif, ASTGTMV003_N08W074_dem_tif, ASTGTMV003_N08W075_dem_tif, ASTGTMV003_N08W076_dem_tif, ASTGTMV003_N08W077_dem_tif, ASTGTMV003_N08W078_dem_tif, ASTGTMV003_N09W072_dem_tif, ASTGTMV003_N09W073_dem_tif, ASTGTMV003_N09W074_dem_tif, ASTGTMV003_N09W075_dem_tif, ASTGTMV003_N09W076_dem_tif, ASTGTMV003_N09W077_dem_tif, ASTGTMV003_N09W078_dem_tif, ASTGTMV003_N10W072_dem_tif, ASTGTMV003_N10W073_dem_tif, ASTGTMV003_N10W074_dem_tif, ASTGTMV003_N10W075_dem_tif, ASTGTMV003_N10W076_dem_tif, ASTGTMV003_N11W072_dem_tif, ASTGTMV003_N11W073_dem_tif, ASTGTMV003_N11W074_dem_tif, ASTGTMV003_N11W075_dem_tif, ASTGTMV003_N12W072_dem_tif, ASTGTMV003_N12W073_dem_tif], target=DEM, mosaic_type="LAST", colormap="FIRST", background_value=None, nodata_value=None, onebit_to_eightbit="NONE", mosaicking_tolerance=0, MatchingMethod="NONE")[0]
    DEM_3_ = arcpy.Raster(DEM_3_)

    # Process: Reclassify
    August21DEMReclassed_2_ = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21DEMReclassed"
    arcpy.ddd.Reclassify(in_raster=DEM_3_, reclass_field="Value", remap="0 1000 0;1000 2000 2;2000 3000 7;3000 5000 10;5000 6710 10", out_raster=August21DEMReclassed_2_, missing_values="DATA")
    August21DEMReclassed_2_ = arcpy.Raster(August21DEMReclassed_2_)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        DEMMosaic()
