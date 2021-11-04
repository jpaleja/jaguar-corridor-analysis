import arcpy

def CostSurfaceTreeLoss():  # CostSurfaceTreeLoss

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")

    Settlements = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21Settlements2019Reclassed")
    Roads = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21RoadsEuclDistReclassed")
    Population_Density = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21ColombiaWorldPopReclassed")
    Land_Use_Type = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21LandUse2019DiscreteClassCopernicusReclassed")
    Elevation = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21DEMReclassed")
    _Tree_and_Shrub_Cover = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21TreeShrubCoverReclassed")
    Tree_Loss = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21TreeLossReclassed")

    # Process: Weighted Sum
    Cost_Surface_with_Tree_Loss = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting"
    Weighted_Sum = Cost_Surface_with_Tree_Loss
    Cost_Surface_with_Tree_Loss = arcpy.ia.WeightedSum(in_rasters=[[Settlements, "Value", 1], [Roads, "Value", 1], [Population_Density, "Value", 1], [Land_Use_Type, "Value", 1], [Elevation, "VALUE", 1], [_Tree_and_Shrub_Cover, "VALUE", 1], [Tree_Loss, "VALUE", 1]])
    Cost_Surface_with_Tree_Loss.save(Weighted_Sum)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        CostSurfaceTreeLoss()
