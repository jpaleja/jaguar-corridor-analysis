import arcpy

def CostDistance():  # CostDistance

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")

    Panthera_JCUs_5_ = "JCU Source\\Panthera JCUs"
    Panthera_JCUs_3_ = "JCU Source\\Panthera JCUs"
    Panthera_JCUs = "JCU Source\\Panthera JCUs"
    Cost_Surface_2_ = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\Cost Surface")
    Cost_Surface_3_ = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\Cost Surface")
    Cost_Surface_4_ = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\Cost Surface")
    Panthera_JCUs_7_ = "JCU Source\\Panthera JCUs"
    Cost_Surface_5_ = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\Cost Surface")
    Panthera_JCUs_9_ = "JCU Source\\Panthera JCUs"
    Cost_Surface_6_ = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\Cost Surface")
    Panthera_JCUs_11_ = "JCU Source\\Panthera JCUs"
    Cost_Surface_7_ = arcpy.Raster("Cost Surface Layers\\Reclassed Cost Surface Layers\\Cost Surface")

    # Process: Select Layer By Attribute (6)
    August21PantheraJCU_COL_13_, Count_6_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Sierra Nevada'", invert_where_clause="")

    # Process: Cost Distance (6)
    August21CostDistSierraNevada = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistSierraNevada"
    Cost_Distance_6_ = August21CostDistSierraNevada
    Output_backlink_raster_6_ = ""
    August21CostDistSierraNevada = arcpy.sa.CostDistance(in_source_data=August21PantheraJCU_COL_13_, in_cost_raster=Cost_Surface_2_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_6_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
    August21CostDistSierraNevada.save(Cost_Distance_6_)


    # Process: Select Layer By Attribute (5)
    if August21CostDistSierraNevada:
        Panthera_JCUs_2_, Count_5_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_3_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Catatumbo'", invert_where_clause="")

    # Process: Cost Distance (5)
    August21CostDistCatatumbo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistCatatumbo"
    Cost_Distance_5_ = August21CostDistCatatumbo
    Output_backlink_raster_5_ = ""
    if August21CostDistSierraNevada:
        August21CostDistCatatumbo = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_2_, in_cost_raster=Cost_Surface_3_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_5_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistCatatumbo.save(Cost_Distance_5_)


    # Process: Select Layer By Attribute
    if August21CostDistCatatumbo and August21CostDistSierraNevada:
        Panthera_JCUs_4_, Count = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_5_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Chocó'", invert_where_clause="")

    # Process: Cost Distance
    August21CostDistChoco = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistChoco"
    Cost_Distance = August21CostDistChoco
    Output_backlink_raster = ""
    if August21CostDistCatatumbo and August21CostDistSierraNevada:
        August21CostDistChoco = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_4_, in_cost_raster=Cost_Surface_4_, maximum_distance=None, out_backlink_raster=Output_backlink_raster, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistChoco.save(Cost_Distance)


    # Process: Select Layer By Attribute (2)
    if August21CostDistCatatumbo and August21CostDistChoco and August21CostDistSierraNevada:
        Panthera_JCUs_6_, Count_2_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_7_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Paramillo'", invert_where_clause="")

    # Process: Cost Distance (2)
    August21CostDistParamillo = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistParamillo"
    Cost_Distance_2_ = August21CostDistParamillo
    Output_backlink_raster_2_ = ""
    if August21CostDistCatatumbo and August21CostDistChoco and August21CostDistSierraNevada:
        August21CostDistParamillo = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_6_, in_cost_raster=Cost_Surface_5_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_2_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistParamillo.save(Cost_Distance_2_)


    # Process: Select Layer By Attribute (3)
    if August21CostDistCatatumbo and August21CostDistChoco and August21CostDistParamillo and August21CostDistSierraNevada:
        Panthera_JCUs_8_, Count_3_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_9_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'Perijá'", invert_where_clause="")

    # Process: Cost Distance (3)
    August21CostDistPerija = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistPerija"
    Cost_Distance_3_ = August21CostDistPerija
    Output_backlink_raster_3_ = ""
    if August21CostDistCatatumbo and August21CostDistChoco and August21CostDistParamillo and August21CostDistSierraNevada:
        August21CostDistPerija = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_8_, in_cost_raster=Cost_Surface_6_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_3_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistPerija.save(Cost_Distance_3_)


    # Process: Select Layer By Attribute (4)
    if August21CostDistCatatumbo and August21CostDistChoco and August21CostDistParamillo and August21CostDistPerija and August21CostDistSierraNevada:
        Panthera_JCUs_10_, Count_4_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=Panthera_JCUs_11_, selection_type="NEW_SELECTION", where_clause="JCU_Name = 'San Lucas'", invert_where_clause="")

    # Process: Cost Distance (4)
    August21CostDistSanLucas = "C:\\Users\\jpale\\Downloads\\Dissertation\\Jaguar Corridors Dissertation\\Panthera_Onca.gdb\\August21CostDistSanLucas"
    Cost_Distance_4_ = August21CostDistSanLucas
    Output_backlink_raster_4_ = ""
    if August21CostDistCatatumbo and August21CostDistChoco and August21CostDistParamillo and August21CostDistPerija and August21CostDistSierraNevada:
        August21CostDistSanLucas = arcpy.sa.CostDistance(in_source_data=Panthera_JCUs_10_, in_cost_raster=Cost_Surface_7_, maximum_distance=None, out_backlink_raster=Output_backlink_raster_4_, source_cost_multiplier="", source_start_cost="", source_resistance_rate="", source_capacity="", source_direction="")
        August21CostDistSanLucas.save(Cost_Distance_4_)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb", workspace=r"C:\Users\jpale\Downloads\Dissertation\Jaguar Corridors Dissertation\Panthera_Onca.gdb"):
        CostDistance()
