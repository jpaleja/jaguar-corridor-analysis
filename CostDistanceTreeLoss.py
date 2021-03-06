import arcpy

def CostDistanceTreeLoss():  # CostDistanceTreeLoss

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")

    Panthera_JCUs_6_ = "JCU Source\\Panthera JCUs"
    Panthera_JCUs_4_ = "JCU Source\\Panthera JCUs"
    Panthera_JCUs_2_ = "JCU Source\\Panthera JCUs"
    August21CostSurfaceTreeLossEqualWeighting = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    August21CostSurfaceTreeLossEqualWeighting_4_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    August21CostSurfaceTreeLossEqualWeighting_6_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    Panthera_JCUs_8_ = "JCU Source\\Panthera JCUs"
    August21CostSurfaceTreeLossEqualWeighting_8_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    Panthera_JCUs_10_ = "JCU Source\\Panthera JCUs"
    August21CostSurfaceTreeLossEqualWeighting_2_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    Panthera_JCUs_12_ = "JCU Source\\Panthera JCUs"
    August21CostSurfaceTreeLossEqualWeighting_3_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    August21CostSurfaceTreeLossEqualWeighting_7_ = arcpy.Raster("C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostSurfaceTreeLossEqualWeighting")
    August21PantheraJCU_COL_2_ = "JCU Source\\August21PantheraJCU_COL"

    # Process: Select Layer By Attribute (6)
    Panthera_JCUs, Count_6_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_2_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Sierra Nevada'", invert_where_clause="")

    # Process: Cost Distance (6)
    August21CostDistTreeLossSierraNevada = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistTreeLossSierraNevada"
    Cost_Distance_6_ = August21CostDistTreeLossSierraNevada
    Output_backlink_raster_6_ = ""
    August21CostDistTreeLossSierraNevada = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs, in_cost_raster=August21CostSurfaceTreeLossEqualWeighting, maximum_distance=None, out_backlink_raster=Output_backlink_raster_6_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
    August21CostDistTreeLossSierraNevada.save(Cost_Distance_6_)


    # Process: Select Layer By Attribute (5)
    if August21CostDistTreeLossSierraNevada:
        Panthera_JCUs_3_, Count_5_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_4_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Catatumbo'", invert_where_clause="")

    # Process: Cost Distance (5)
    August21CostDistTreeLossCatatumbo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistTreeLossCatatumbo"
    Cost_Distance_5_ = August21CostDistTreeLossCatatumbo
    Output_backlink_raster_5_ = ""
    if August21CostDistTreeLossSierraNevada:
        August21CostDistTreeLossCatatumbo = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_3_, in_cost_raster=August21CostSurfaceTreeLossEqualWeighting_4_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_5_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistTreeLossCatatumbo.save(Cost_Distance_5_)


    # Process: Select Layer By Attribute
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossSierraNevada:
        Panthera_JCUs_5_, Count = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_6_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Choc??'", invert_where_clause="")

    # Process: Cost Distance
    August21CostDistTreeLossChoco = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistTreeLossChoco"
    Cost_Distance = August21CostDistTreeLossChoco
    Output_backlink_raster = ""
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossSierraNevada:
        August21CostDistTreeLossChoco = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_5_, in_cost_raster=August21CostSurfaceTreeLossEqualWeighting_6_, maximum_distance=None, out_backlink_raster=Output_backlink_raster, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistTreeLossChoco.save(Cost_Distance)


    # Process: Select Layer By Attribute (2)
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossChoco and August21CostDistTreeLossSierraNevada:
        Panthera_JCUs_7_, Count_2_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_8_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Paramillo'", invert_where_clause="")

    # Process: Cost Distance (2)
    August21CostDistTreeLossParamillo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistTreeLossParamillo"
    Cost_Distance_2_ = August21CostDistTreeLossParamillo
    Output_backlink_raster_2_ = ""
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossChoco and August21CostDistTreeLossSierraNevada:
        August21CostDistTreeLossParamillo = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_7_, in_cost_raster=August21CostSurfaceTreeLossEqualWeighting_8_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_2_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistTreeLossParamillo.save(Cost_Distance_2_)


    # Process: Select Layer By Attribute (3)
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossChoco and August21CostDistTreeLossParamillo and August21CostDistTreeLossSierraNevada:
        Panthera_JCUs_9_, Count_3_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_10_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Perij??'", invert_where_clause="")

    # Process: Cost Distance (3)
    August21CostDistTreeLossPerija = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistTreeLossPerija"
    Cost_Distance_3_ = August21CostDistTreeLossPerija
    Output_backlink_raster_3_ = ""
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossChoco and August21CostDistTreeLossParamillo and August21CostDistTreeLossSierraNevada:
        August21CostDistTreeLossPerija = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_9_, in_cost_raster=August21CostSurfaceTreeLossEqualWeighting_2_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_3_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistTreeLossPerija.save(Cost_Distance_3_)


    # Process: Select Layer By Attribute (4)
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossChoco and August21CostDistTreeLossParamillo and August21CostDistTreeLossPerija and August21CostDistTreeLossSierraNevada:
        Panthera_JCUs_11_, Count_4_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_12_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'San Lucas'", invert_where_clause="")

    # Process: Cost Distance (4)
    August21CostDistTreeLossSanLucas = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistTreeLossSanLucas"
    Cost_Distance_4_ = August21CostDistTreeLossSanLucas
    Output_backlink_raster_4_ = ""
    if August21CostDistTreeLossCatatumbo and August21CostDistTreeLossChoco and August21CostDistTreeLossParamillo and August21CostDistTreeLossPerija and August21CostDistTreeLossSierraNevada:
        August21CostDistTreeLossSanLucas = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_11_, in_cost_raster=August21CostSurfaceTreeLossEqualWeighting_3_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_4_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistTreeLossSanLucas.save(Cost_Distance_4_)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        CostDistanceTreeLoss()
