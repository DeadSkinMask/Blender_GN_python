import bpy, mathutils

#initialize scale_edges_by_index node group
def scale_edges_by_index_node_group():
    scale_edges_by_index = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Scale Edges By Index")

    scale_edges_by_index.color_tag = 'NONE'
    scale_edges_by_index.description = ""
    scale_edges_by_index.default_group_node_width = 140
    


    #scale_edges_by_index interface
    #Socket Geometry
    geometry_socket = scale_edges_by_index.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Input
    input_socket = scale_edges_by_index.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    input_socket.attribute_domain = 'POINT'
    input_socket.default_input = 'VALUE'
    input_socket.structure_type = 'AUTO'

    #Socket y_idx
    y_idx_socket = scale_edges_by_index.interface.new_socket(name = "y_idx", in_out='INPUT', socket_type = 'NodeSocketInt')
    y_idx_socket.default_value = 0
    y_idx_socket.min_value = -2147483648
    y_idx_socket.max_value = 2147483647
    y_idx_socket.subtype = 'NONE'
    y_idx_socket.attribute_domain = 'POINT'
    y_idx_socket.default_input = 'VALUE'
    y_idx_socket.structure_type = 'AUTO'

    #Socket From Idx
    from_idx_socket = scale_edges_by_index.interface.new_socket(name = "From Idx", in_out='INPUT', socket_type = 'NodeSocketInt')
    from_idx_socket.default_value = 2
    from_idx_socket.min_value = -2147483648
    from_idx_socket.max_value = 2147483647
    from_idx_socket.subtype = 'NONE'
    from_idx_socket.attribute_domain = 'POINT'
    from_idx_socket.default_input = 'VALUE'
    from_idx_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = scale_edges_by_index.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 0.800000011920929
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Delete Tip
    delete_tip_socket = scale_edges_by_index.interface.new_socket(name = "Delete Tip", in_out='INPUT', socket_type = 'NodeSocketBool')
    delete_tip_socket.default_value = False
    delete_tip_socket.attribute_domain = 'POINT'
    delete_tip_socket.default_input = 'VALUE'
    delete_tip_socket.structure_type = 'AUTO'

    #Socket Max Length
    max_length_socket = scale_edges_by_index.interface.new_socket(name = "Max Length", in_out='INPUT', socket_type = 'NodeSocketInt')
    max_length_socket.default_value = 2
    max_length_socket.min_value = -2147483648
    max_length_socket.max_value = 2147483647
    max_length_socket.subtype = 'NONE'
    max_length_socket.attribute_domain = 'POINT'
    max_length_socket.default_input = 'VALUE'
    max_length_socket.structure_type = 'AUTO'


    #initialize scale_edges_by_index nodes
    #node Group Output
    group_output = scale_edges_by_index.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True

    #node Repeat Input
    repeat_input = scale_edges_by_index.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    #node Repeat Output
    repeat_output = scale_edges_by_index.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 0
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")

    #node Attribute Statistic
    attribute_statistic = scale_edges_by_index.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = 'FLOAT'
    attribute_statistic.domain = 'POINT'
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[3].hide = True
    attribute_statistic.outputs[4].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    #Selection
    attribute_statistic.inputs[1].default_value = True

    #node Scale Elements
    scale_elements = scale_edges_by_index.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'EDGE'
    scale_elements.scale_mode = 'UNIFORM'

    #node Compare.001
    compare_001 = scale_edges_by_index.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'

    #node Attribute Statistic.001
    attribute_statistic_001 = scale_edges_by_index.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = 'FLOAT_VECTOR'
    attribute_statistic_001.domain = 'POINT'
    attribute_statistic_001.outputs[1].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[5].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True

    #node Position
    position = scale_edges_by_index.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Boolean Math
    boolean_math = scale_edges_by_index.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'AND'

    #node Compare.002
    compare_002 = scale_edges_by_index.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'GREATER_EQUAL'

    #node Reroute
    reroute = scale_edges_by_index.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    #node Group Input.001
    group_input_001 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True

    #node Group Input.002
    group_input_002 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True

    #node Group Input.003
    group_input_003 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True

    #node Integer Math
    integer_math = scale_edges_by_index.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.operation = 'ADD'
    #Value_001
    integer_math.inputs[1].default_value = -1

    #node Delete Geometry
    delete_geometry = scale_edges_by_index.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    #node Compare
    compare = scale_edges_by_index.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'

    #node Group Input.004
    group_input_004 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True

    #node Boolean Math.001
    boolean_math_001 = scale_edges_by_index.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'AND'

    #node Group Input.005
    group_input_005 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True

    #node Group Input.006
    group_input_006 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True

    #node Delete Geometry.001
    delete_geometry_001 = scale_edges_by_index.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'

    #node Group Input.007
    group_input_007 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True

    #node Compare.003
    compare_003 = scale_edges_by_index.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'INT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'GREATER_THAN'

    #node Integer Math.001
    integer_math_001 = scale_edges_by_index.nodes.new("FunctionNodeIntegerMath")
    integer_math_001.name = "Integer Math.001"
    integer_math_001.operation = 'ADD'

    #node Scale Elements.001
    scale_elements_001 = scale_edges_by_index.nodes.new("GeometryNodeScaleElements")
    scale_elements_001.name = "Scale Elements.001"
    scale_elements_001.domain = 'EDGE'
    scale_elements_001.scale_mode = 'UNIFORM'
    #Scale
    scale_elements_001.inputs[2].default_value = 0.0
    #Center
    scale_elements_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Compare.004
    compare_004 = scale_edges_by_index.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'INT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'EQUAL'

    #node Integer Math.002
    integer_math_002 = scale_edges_by_index.nodes.new("FunctionNodeIntegerMath")
    integer_math_002.name = "Integer Math.002"
    integer_math_002.operation = 'ADD'

    #node Group Input.008
    group_input_008 = scale_edges_by_index.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[6].hide = True


    #Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)





    #Set locations
    group_output.location = (1883.4981689453125, 222.8257293701172)
    group_input.location = (-893.00830078125, 239.95663452148438)
    repeat_input.location = (-231.33717346191406, 237.11331176757812)
    repeat_output.location = (1167.9549560546875, 191.1873016357422)
    attribute_statistic.location = (-492.2577819824219, 356.5727844238281)
    scale_elements.location = (630.9605102539062, 234.89459228515625)
    compare_001.location = (11.241935729980469, 88.52224731445312)
    attribute_statistic_001.location = (459.13812255859375, 65.34073638916016)
    position.location = (275.34423828125, -70.73832702636719)
    boolean_math.location = (243.1905059814453, 125.33544921875)
    compare_002.location = (68.56463623046875, -149.43234252929688)
    reroute.location = (-656.1904907226562, 148.1790008544922)
    group_input_001.location = (-527.68896484375, -244.07138061523438)
    group_input_002.location = (-336.8743591308594, -337.6109924316406)
    group_input_003.location = (389.564208984375, 231.85824584960938)
    integer_math.location = (-317.0000305175781, -85.46319580078125)
    delete_geometry.location = (1536.7117919921875, 293.4535827636719)
    compare.location = (928.7880249023438, 410.8216247558594)
    group_input_004.location = (535.20458984375, 443.04962158203125)
    boolean_math_001.location = (1114.1822509765625, 429.7049865722656)
    group_input_005.location = (921.9171752929688, 523.9483642578125)
    group_input_006.location = (528.267578125, -263.02239990234375)
    delete_geometry_001.location = (807.9999389648438, 207.474609375)
    group_input_007.location = (730.7371215820312, -152.52752685546875)
    compare_003.location = (976.1674194335938, -87.25277709960938)
    integer_math_001.location = (766.6038818359375, -236.57061767578125)
    scale_elements_001.location = (987.9998779296875, 209.463623046875)
    compare_004.location = (1169.0692138671875, -140.8833465576172)
    integer_math_002.location = (956.9827270507812, -294.1690979003906)
    group_input_008.location = (497.01611328125, -378.0552673339844)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    repeat_input.width, repeat_input.height = 140.0, 100.0
    repeat_output.width, repeat_output.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    reroute.width, reroute.height = 10.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer_math.width, integer_math.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    integer_math_001.width, integer_math_001.height = 140.0, 100.0
    scale_elements_001.width, scale_elements_001.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    integer_math_002.width, integer_math_002.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0

    #initialize scale_edges_by_index links
    #repeat_input.Iteration -> compare_001.A
    scale_edges_by_index.links.new(repeat_input.outputs[0], compare_001.inputs[2])
    #repeat_input.Geometry -> attribute_statistic_001.Geometry
    scale_edges_by_index.links.new(repeat_input.outputs[1], attribute_statistic_001.inputs[0])
    #position.Position -> attribute_statistic_001.Attribute
    scale_edges_by_index.links.new(position.outputs[0], attribute_statistic_001.inputs[2])
    #reroute.Output -> repeat_input.Geometry
    scale_edges_by_index.links.new(reroute.outputs[0], repeat_input.inputs[1])
    #reroute.Output -> attribute_statistic.Geometry
    scale_edges_by_index.links.new(reroute.outputs[0], attribute_statistic.inputs[0])
    #repeat_input.Geometry -> scale_elements.Geometry
    scale_edges_by_index.links.new(repeat_input.outputs[1], scale_elements.inputs[0])
    #group_input.Input -> reroute.Input
    scale_edges_by_index.links.new(group_input.outputs[0], reroute.inputs[0])
    #group_input.y_idx -> attribute_statistic.Attribute
    scale_edges_by_index.links.new(group_input.outputs[1], attribute_statistic.inputs[2])
    #integer_math.Value -> compare_001.B
    scale_edges_by_index.links.new(integer_math.outputs[0], compare_001.inputs[3])
    #group_input_001.y_idx -> integer_math.Value
    scale_edges_by_index.links.new(group_input_001.outputs[1], integer_math.inputs[0])
    #group_input_002.From Idx -> compare_002.B
    scale_edges_by_index.links.new(group_input_002.outputs[2], compare_002.inputs[3])
    #compare_002.Result -> boolean_math.Boolean
    scale_edges_by_index.links.new(compare_002.outputs[0], boolean_math.inputs[1])
    #repeat_input.Iteration -> compare_002.A
    scale_edges_by_index.links.new(repeat_input.outputs[0], compare_002.inputs[2])
    #attribute_statistic_001.Mean -> scale_elements.Center
    scale_edges_by_index.links.new(attribute_statistic_001.outputs[0], scale_elements.inputs[3])
    #boolean_math.Boolean -> attribute_statistic_001.Selection
    scale_edges_by_index.links.new(boolean_math.outputs[0], attribute_statistic_001.inputs[1])
    #boolean_math.Boolean -> scale_elements.Selection
    scale_edges_by_index.links.new(boolean_math.outputs[0], scale_elements.inputs[1])
    #compare_001.Result -> boolean_math.Boolean
    scale_edges_by_index.links.new(compare_001.outputs[0], boolean_math.inputs[0])
    #group_input_003.Scale -> scale_elements.Scale
    scale_edges_by_index.links.new(group_input_003.outputs[3], scale_elements.inputs[2])
    #boolean_math_001.Boolean -> delete_geometry.Selection
    scale_edges_by_index.links.new(boolean_math_001.outputs[0], delete_geometry.inputs[1])
    #attribute_statistic.Range -> repeat_input.Iterations
    scale_edges_by_index.links.new(attribute_statistic.outputs[5], repeat_input.inputs[0])
    #group_input_004.y_idx -> compare.A
    scale_edges_by_index.links.new(group_input_004.outputs[1], compare.inputs[2])
    #scale_elements_001.Geometry -> repeat_output.Geometry
    scale_edges_by_index.links.new(scale_elements_001.outputs[0], repeat_output.inputs[0])
    #repeat_output.Geometry -> delete_geometry.Geometry
    scale_edges_by_index.links.new(repeat_output.outputs[0], delete_geometry.inputs[0])
    #delete_geometry.Geometry -> group_output.Geometry
    scale_edges_by_index.links.new(delete_geometry.outputs[0], group_output.inputs[0])
    #attribute_statistic.Range -> compare.B
    scale_edges_by_index.links.new(attribute_statistic.outputs[5], compare.inputs[3])
    #compare.Result -> boolean_math_001.Boolean
    scale_edges_by_index.links.new(compare.outputs[0], boolean_math_001.inputs[0])
    #group_input_005.Delete Tip -> boolean_math_001.Boolean
    scale_edges_by_index.links.new(group_input_005.outputs[4], boolean_math_001.inputs[1])
    #scale_elements.Geometry -> delete_geometry_001.Geometry
    scale_edges_by_index.links.new(scale_elements.outputs[0], delete_geometry_001.inputs[0])
    #group_input_007.y_idx -> compare_003.A
    scale_edges_by_index.links.new(group_input_007.outputs[1], compare_003.inputs[2])
    #group_input_006.From Idx -> integer_math_001.Value
    scale_edges_by_index.links.new(group_input_006.outputs[2], integer_math_001.inputs[0])
    #integer_math_001.Value -> compare_003.B
    scale_edges_by_index.links.new(integer_math_001.outputs[0], compare_003.inputs[3])
    #compare_003.Result -> delete_geometry_001.Selection
    scale_edges_by_index.links.new(compare_003.outputs[0], delete_geometry_001.inputs[1])
    #delete_geometry_001.Geometry -> scale_elements_001.Geometry
    scale_edges_by_index.links.new(delete_geometry_001.outputs[0], scale_elements_001.inputs[0])
    #group_input_007.y_idx -> compare_004.A
    scale_edges_by_index.links.new(group_input_007.outputs[1], compare_004.inputs[2])
    #group_input_006.From Idx -> integer_math_002.Value
    scale_edges_by_index.links.new(group_input_006.outputs[2], integer_math_002.inputs[0])
    #integer_math_002.Value -> compare_004.B
    scale_edges_by_index.links.new(integer_math_002.outputs[0], compare_004.inputs[3])
    #compare_004.Result -> scale_elements_001.Selection
    scale_edges_by_index.links.new(compare_004.outputs[0], scale_elements_001.inputs[1])
    #group_input_008.Max Length -> integer_math_001.Value
    scale_edges_by_index.links.new(group_input_008.outputs[5], integer_math_001.inputs[1])
    #group_input_008.Max Length -> integer_math_002.Value
    scale_edges_by_index.links.new(group_input_008.outputs[5], integer_math_002.inputs[1])
    return scale_edges_by_index

scale_edges_by_index = scale_edges_by_index_node_group()

#initialize geom_hair_strands node group
def geom_hair_strands_node_group():
    geom_hair_strands = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Geom Hair Strands")

    geom_hair_strands.color_tag = 'NONE'
    geom_hair_strands.description = ""
    geom_hair_strands.default_group_node_width = 140
    

    geom_hair_strands.is_modifier = True

    #geom_hair_strands interface
    #Socket Geometry
    geometry_socket_1 = geom_hair_strands.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_2 = geom_hair_strands.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_2.attribute_domain = 'POINT'
    geometry_socket_2.default_input = 'VALUE'
    geometry_socket_2.structure_type = 'AUTO'

    #Socket Radius Scale
    radius_scale_socket = geom_hair_strands.interface.new_socket(name = "Radius Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_scale_socket.default_value = 0.10000000149011612
    radius_scale_socket.min_value = -10000.0
    radius_scale_socket.max_value = 10000.0
    radius_scale_socket.subtype = 'NONE'
    radius_scale_socket.attribute_domain = 'POINT'
    radius_scale_socket.default_input = 'VALUE'
    radius_scale_socket.structure_type = 'AUTO'

    #Socket Min Scale
    min_scale_socket = geom_hair_strands.interface.new_socket(name = "Min Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    min_scale_socket.default_value = 0.699999988079071
    min_scale_socket.min_value = -3.4028234663852886e+38
    min_scale_socket.max_value = 3.4028234663852886e+38
    min_scale_socket.subtype = 'NONE'
    min_scale_socket.attribute_domain = 'POINT'
    min_scale_socket.default_input = 'VALUE'
    min_scale_socket.structure_type = 'AUTO'

    #Socket Max Scale
    max_scale_socket = geom_hair_strands.interface.new_socket(name = "Max Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    max_scale_socket.default_value = 0.800000011920929
    max_scale_socket.min_value = -3.4028234663852886e+38
    max_scale_socket.max_value = 3.4028234663852886e+38
    max_scale_socket.subtype = 'NONE'
    max_scale_socket.attribute_domain = 'POINT'
    max_scale_socket.default_input = 'VALUE'
    max_scale_socket.structure_type = 'AUTO'

    #Socket Min Loop Cut
    min_loop_cut_socket = geom_hair_strands.interface.new_socket(name = "Min Loop Cut", in_out='INPUT', socket_type = 'NodeSocketInt')
    min_loop_cut_socket.default_value = 5
    min_loop_cut_socket.min_value = -100000
    min_loop_cut_socket.max_value = 100000
    min_loop_cut_socket.subtype = 'NONE'
    min_loop_cut_socket.attribute_domain = 'POINT'
    min_loop_cut_socket.default_input = 'VALUE'
    min_loop_cut_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket = geom_hair_strands.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 9
    seed_socket.min_value = -10000
    seed_socket.max_value = 10000
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    #Socket Resample
    resample_socket = geom_hair_strands.interface.new_socket(name = "Resample", in_out='INPUT', socket_type = 'NodeSocketInt')
    resample_socket.default_value = 16
    resample_socket.min_value = 1
    resample_socket.max_value = 100000
    resample_socket.subtype = 'NONE'
    resample_socket.attribute_domain = 'POINT'
    resample_socket.default_input = 'VALUE'
    resample_socket.structure_type = 'AUTO'

    #Socket Delete Tip
    delete_tip_socket_1 = geom_hair_strands.interface.new_socket(name = "Delete Tip", in_out='INPUT', socket_type = 'NodeSocketBool')
    delete_tip_socket_1.default_value = True
    delete_tip_socket_1.attribute_domain = 'POINT'
    delete_tip_socket_1.default_input = 'VALUE'
    delete_tip_socket_1.structure_type = 'AUTO'

    #Socket Max Length
    max_length_socket_1 = geom_hair_strands.interface.new_socket(name = "Max Length", in_out='INPUT', socket_type = 'NodeSocketInt')
    max_length_socket_1.default_value = 3
    max_length_socket_1.min_value = -2147483648
    max_length_socket_1.max_value = 2147483647
    max_length_socket_1.subtype = 'NONE'
    max_length_socket_1.attribute_domain = 'POINT'
    max_length_socket_1.default_input = 'VALUE'
    max_length_socket_1.structure_type = 'AUTO'

    #Socket Randomize Width
    randomize_width_socket = geom_hair_strands.interface.new_socket(name = "Randomize Width", in_out='INPUT', socket_type = 'NodeSocketBool')
    randomize_width_socket.default_value = True
    randomize_width_socket.attribute_domain = 'POINT'
    randomize_width_socket.default_input = 'VALUE'
    randomize_width_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket_1 = geom_hair_strands.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 3
    seed_socket_1.min_value = -10000
    seed_socket_1.max_value = 10000
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.default_input = 'VALUE'
    seed_socket_1.structure_type = 'AUTO'

    #Socket Probability
    probability_socket = geom_hair_strands.interface.new_socket(name = "Probability", in_out='INPUT', socket_type = 'NodeSocketFloat')
    probability_socket.default_value = 0.5
    probability_socket.min_value = 0.0
    probability_socket.max_value = 1.0
    probability_socket.subtype = 'FACTOR'
    probability_socket.attribute_domain = 'POINT'
    probability_socket.default_input = 'VALUE'
    probability_socket.structure_type = 'AUTO'


    #initialize geom_hair_strands nodes
    #node Group Input
    group_input_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    group_input_1.outputs[1].hide = True
    group_input_1.outputs[2].hide = True
    group_input_1.outputs[3].hide = True
    group_input_1.outputs[4].hide = True
    group_input_1.outputs[5].hide = True
    group_input_1.outputs[6].hide = True
    group_input_1.outputs[7].hide = True
    group_input_1.outputs[8].hide = True
    group_input_1.outputs[9].hide = True
    group_input_1.outputs[10].hide = True
    group_input_1.outputs[11].hide = True
    group_input_1.outputs[12].hide = True

    #node Group Output
    group_output_1 = geom_hair_strands.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Mesh to Curve
    mesh_to_curve = geom_hair_strands.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.mode = 'EDGES'
    #Selection
    mesh_to_curve.inputs[1].default_value = True

    #node Store Named Attribute
    store_named_attribute = geom_hair_strands.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'INT'
    store_named_attribute.domain = 'POINT'
    #Selection
    store_named_attribute.inputs[1].default_value = True
    #Name
    store_named_attribute.inputs[2].default_value = "x_idx"

    #node Curve to Mesh
    curve_to_mesh = geom_hair_strands.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    #Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    #node Resample Curve
    resample_curve = geom_hair_strands.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.keep_last_segment = True
    resample_curve.mode = 'COUNT'
    #Selection
    resample_curve.inputs[1].default_value = True

    #node Transform Geometry
    transform_geometry = geom_hair_strands.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[1].hide = True
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[4].hide = True
    #Translation
    transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    transform_geometry.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
    #Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Object Info
    object_info = geom_hair_strands.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'ORIGINAL'
    if "BézierCurve" in bpy.data.objects:
        object_info.inputs[0].default_value = bpy.data.objects["BézierCurve"]
    #As Instance
    object_info.inputs[1].default_value = False

    #node Radius
    radius = geom_hair_strands.nodes.new("GeometryNodeInputRadius")
    radius.name = "Radius"

    #node Math
    math = geom_hair_strands.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    #node Store Named Attribute.001
    store_named_attribute_001 = geom_hair_strands.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = 'INT'
    store_named_attribute_001.domain = 'POINT'
    #Selection
    store_named_attribute_001.inputs[1].default_value = True
    #Name
    store_named_attribute_001.inputs[2].default_value = "y_idx"

    #node Separate Geometry
    separate_geometry = geom_hair_strands.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = 'FACE'

    #node Compare
    compare_1 = geom_hair_strands.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = 'INT'
    compare_1.mode = 'ELEMENT'
    compare_1.operation = 'EQUAL'

    #node Named Attribute
    named_attribute = geom_hair_strands.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'INT'
    #Name
    named_attribute.inputs[0].default_value = "x_idx"

    #node Group
    group = geom_hair_strands.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = scale_edges_by_index

    #node Named Attribute.001
    named_attribute_001 = geom_hair_strands.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = 'INT'
    #Name
    named_attribute_001.inputs[0].default_value = "y_idx"

    #node Join Geometry
    join_geometry = geom_hair_strands.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Merge by Distance
    merge_by_distance = geom_hair_strands.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    #Selection
    merge_by_distance.inputs[1].default_value = True
    #Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    #node Frame
    frame = geom_hair_strands.nodes.new("NodeFrame")
    frame.label = "Strand Scale"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Repeat Input
    repeat_input_1 = geom_hair_strands.nodes.new("GeometryNodeRepeatInput")
    repeat_input_1.name = "Repeat Input"
    #node Repeat Output
    repeat_output_1 = geom_hair_strands.nodes.new("GeometryNodeRepeatOutput")
    repeat_output_1.name = "Repeat Output"
    repeat_output_1.active_index = 1
    repeat_output_1.inspection_index = 0
    repeat_output_1.repeat_items.clear()
    # Create item "Geometry"
    repeat_output_1.repeat_items.new('GEOMETRY', "Geometry")
    # Create item "Geometry.001"
    repeat_output_1.repeat_items.new('GEOMETRY', "Geometry.001")

    #node Attribute Statistic
    attribute_statistic_1 = geom_hair_strands.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_1.name = "Attribute Statistic"
    attribute_statistic_1.data_type = 'FLOAT'
    attribute_statistic_1.domain = 'POINT'
    attribute_statistic_1.inputs[1].hide = True
    attribute_statistic_1.outputs[0].hide = True
    attribute_statistic_1.outputs[1].hide = True
    attribute_statistic_1.outputs[2].hide = True
    attribute_statistic_1.outputs[3].hide = True
    attribute_statistic_1.outputs[4].hide = True
    attribute_statistic_1.outputs[6].hide = True
    attribute_statistic_1.outputs[7].hide = True
    #Selection
    attribute_statistic_1.inputs[1].default_value = True

    #node Named Attribute.002
    named_attribute_002 = geom_hair_strands.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.data_type = 'INT'
    #Name
    named_attribute_002.inputs[0].default_value = "x_idx"

    #node Integer Math
    integer_math_1 = geom_hair_strands.nodes.new("FunctionNodeIntegerMath")
    integer_math_1.name = "Integer Math"
    integer_math_1.operation = 'ADD'
    #Value_001
    integer_math_1.inputs[1].default_value = 0

    #node Random Value
    random_value = geom_hair_strands.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'FLOAT'

    #node Random Value.001
    random_value_001 = geom_hair_strands.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'INT'

    #node Attribute Statistic.001
    attribute_statistic_001_1 = geom_hair_strands.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001_1.name = "Attribute Statistic.001"
    attribute_statistic_001_1.data_type = 'FLOAT'
    attribute_statistic_001_1.domain = 'POINT'
    attribute_statistic_001_1.inputs[1].hide = True
    attribute_statistic_001_1.outputs[0].hide = True
    attribute_statistic_001_1.outputs[1].hide = True
    attribute_statistic_001_1.outputs[2].hide = True
    attribute_statistic_001_1.outputs[3].hide = True
    attribute_statistic_001_1.outputs[4].hide = True
    attribute_statistic_001_1.outputs[6].hide = True
    attribute_statistic_001_1.outputs[7].hide = True
    #Selection
    attribute_statistic_001_1.inputs[1].default_value = True

    #node Named Attribute.003
    named_attribute_003 = geom_hair_strands.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.data_type = 'INT'
    #Name
    named_attribute_003.inputs[0].default_value = "y_idx"

    #node Resample Curve.001
    resample_curve_001 = geom_hair_strands.nodes.new("GeometryNodeResampleCurve")
    resample_curve_001.name = "Resample Curve.001"
    resample_curve_001.keep_last_segment = True
    resample_curve_001.mode = 'COUNT'
    #Selection
    resample_curve_001.inputs[1].default_value = True
    #Count
    resample_curve_001.inputs[2].default_value = 6

    #node Group Input.001
    group_input_001_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[1].hide = True
    group_input_001_1.outputs[6].hide = True
    group_input_001_1.outputs[7].hide = True
    group_input_001_1.outputs[8].hide = True
    group_input_001_1.outputs[9].hide = True
    group_input_001_1.outputs[10].hide = True
    group_input_001_1.outputs[11].hide = True
    group_input_001_1.outputs[12].hide = True

    #node Spline Parameter
    spline_parameter = geom_hair_strands.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"

    #node Integer Math.001
    integer_math_001_1 = geom_hair_strands.nodes.new("FunctionNodeIntegerMath")
    integer_math_001_1.name = "Integer Math.001"
    integer_math_001_1.operation = 'ADD'
    #Value_001
    integer_math_001_1.inputs[1].default_value = 1

    #node Spline Parameter.001
    spline_parameter_001 = geom_hair_strands.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_001.name = "Spline Parameter.001"

    #node Group Input.002
    group_input_002_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_002_1.name = "Group Input.002"
    group_input_002_1.outputs[0].hide = True
    group_input_002_1.outputs[1].hide = True
    group_input_002_1.outputs[2].hide = True
    group_input_002_1.outputs[3].hide = True
    group_input_002_1.outputs[4].hide = True
    group_input_002_1.outputs[5].hide = True
    group_input_002_1.outputs[7].hide = True
    group_input_002_1.outputs[8].hide = True
    group_input_002_1.outputs[9].hide = True
    group_input_002_1.outputs[10].hide = True
    group_input_002_1.outputs[11].hide = True
    group_input_002_1.outputs[12].hide = True

    #node Group Input.003
    group_input_003_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_003_1.name = "Group Input.003"
    group_input_003_1.outputs[0].hide = True
    group_input_003_1.outputs[1].hide = True
    group_input_003_1.outputs[2].hide = True
    group_input_003_1.outputs[3].hide = True
    group_input_003_1.outputs[4].hide = True
    group_input_003_1.outputs[5].hide = True
    group_input_003_1.outputs[6].hide = True
    group_input_003_1.outputs[8].hide = True
    group_input_003_1.outputs[9].hide = True
    group_input_003_1.outputs[10].hide = True
    group_input_003_1.outputs[11].hide = True
    group_input_003_1.outputs[12].hide = True

    #node Group Input.004
    group_input_004_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_004_1.name = "Group Input.004"
    group_input_004_1.outputs[0].hide = True
    group_input_004_1.outputs[1].hide = True
    group_input_004_1.outputs[2].hide = True
    group_input_004_1.outputs[3].hide = True
    group_input_004_1.outputs[4].hide = True
    group_input_004_1.outputs[5].hide = True
    group_input_004_1.outputs[6].hide = True
    group_input_004_1.outputs[7].hide = True
    group_input_004_1.outputs[9].hide = True
    group_input_004_1.outputs[10].hide = True
    group_input_004_1.outputs[11].hide = True
    group_input_004_1.outputs[12].hide = True

    #node Delete Geometry
    delete_geometry_1 = geom_hair_strands.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_1.name = "Delete Geometry"
    delete_geometry_1.domain = 'POINT'
    delete_geometry_1.mode = 'ALL'

    #node Random Value.002
    random_value_002 = geom_hair_strands.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'BOOLEAN'
    #ID
    random_value_002.inputs[7].default_value = 0

    #node Subdivide Curve
    subdivide_curve = geom_hair_strands.nodes.new("GeometryNodeSubdivideCurve")
    subdivide_curve.name = "Subdivide Curve"
    #Cuts
    subdivide_curve.inputs[1].default_value = 1

    #node Group Input.005
    group_input_005_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_005_1.name = "Group Input.005"
    group_input_005_1.outputs[0].hide = True
    group_input_005_1.outputs[1].hide = True
    group_input_005_1.outputs[2].hide = True
    group_input_005_1.outputs[3].hide = True
    group_input_005_1.outputs[4].hide = True
    group_input_005_1.outputs[5].hide = True
    group_input_005_1.outputs[6].hide = True
    group_input_005_1.outputs[7].hide = True
    group_input_005_1.outputs[8].hide = True
    group_input_005_1.outputs[9].hide = True
    group_input_005_1.outputs[11].hide = True
    group_input_005_1.outputs[12].hide = True

    #node Switch
    switch = geom_hair_strands.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    #node Group Input.006
    group_input_006_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_006_1.name = "Group Input.006"
    group_input_006_1.outputs[0].hide = True
    group_input_006_1.outputs[1].hide = True
    group_input_006_1.outputs[2].hide = True
    group_input_006_1.outputs[3].hide = True
    group_input_006_1.outputs[4].hide = True
    group_input_006_1.outputs[5].hide = True
    group_input_006_1.outputs[6].hide = True
    group_input_006_1.outputs[7].hide = True
    group_input_006_1.outputs[8].hide = True
    group_input_006_1.outputs[10].hide = True
    group_input_006_1.outputs[11].hide = True
    group_input_006_1.outputs[12].hide = True

    #node Group Input.007
    group_input_007_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_007_1.name = "Group Input.007"
    group_input_007_1.outputs[0].hide = True
    group_input_007_1.outputs[1].hide = True
    group_input_007_1.outputs[2].hide = True
    group_input_007_1.outputs[3].hide = True
    group_input_007_1.outputs[4].hide = True
    group_input_007_1.outputs[5].hide = True
    group_input_007_1.outputs[6].hide = True
    group_input_007_1.outputs[7].hide = True
    group_input_007_1.outputs[8].hide = True
    group_input_007_1.outputs[9].hide = True
    group_input_007_1.outputs[10].hide = True
    group_input_007_1.outputs[12].hide = True

    #node Frame.001
    frame_001 = geom_hair_strands.nodes.new("NodeFrame")
    frame_001.label = "Randomize Points"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Group Input.008
    group_input_008_1 = geom_hair_strands.nodes.new("NodeGroupInput")
    group_input_008_1.name = "Group Input.008"
    group_input_008_1.outputs[0].hide = True
    group_input_008_1.outputs[2].hide = True
    group_input_008_1.outputs[3].hide = True
    group_input_008_1.outputs[4].hide = True
    group_input_008_1.outputs[5].hide = True
    group_input_008_1.outputs[6].hide = True
    group_input_008_1.outputs[7].hide = True
    group_input_008_1.outputs[8].hide = True
    group_input_008_1.outputs[9].hide = True
    group_input_008_1.outputs[10].hide = True
    group_input_008_1.outputs[11].hide = True
    group_input_008_1.outputs[12].hide = True


    #Process zone input Repeat Input
    repeat_input_1.pair_with_output(repeat_output_1)




    #Set parents
    separate_geometry.parent = frame
    compare_1.parent = frame
    named_attribute.parent = frame
    group.parent = frame
    named_attribute_001.parent = frame
    join_geometry.parent = frame
    delete_geometry_1.parent = frame_001
    random_value_002.parent = frame_001
    subdivide_curve.parent = frame_001
    group_input_005_1.parent = frame_001
    group_input_007_1.parent = frame_001

    #Set locations
    group_input_1.location = (-1600.632080078125, 142.4060821533203)
    group_output_1.location = (3009.982666015625, 240.5042724609375)
    mesh_to_curve.location = (-1385.0941162109375, 149.27926635742188)
    store_named_attribute.location = (-135.6676025390625, 65.6512680053711)
    curve_to_mesh.location = (470.0260009765625, 261.4013671875)
    resample_curve.location = (-527.8696899414062, 398.154296875)
    transform_geometry.location = (41.38105010986328, 35.21091842651367)
    object_info.location = (-910.5462036132812, 496.64544677734375)
    radius.location = (-194.13540649414062, 607.6942138671875)
    math.location = (51.99150085449219, 598.8920288085938)
    store_named_attribute_001.location = (-27.99420166015625, 315.86981201171875)
    separate_geometry.location = (608.3251953125, -36.477020263671875)
    compare_1.location = (447.909423828125, -183.4857177734375)
    named_attribute.location = (30.178466796875, -187.96142578125)
    group.location = (848.336181640625, -139.1028594970703)
    named_attribute_001.location = (432.435302734375, -207.6776123046875)
    join_geometry.location = (1100.748046875, -56.512298583984375)
    merge_by_distance.location = (2809.4814453125, 177.14842224121094)
    frame.location = (1219.0, 345.0)
    repeat_input_1.location = (1186.6544189453125, 282.68109130859375)
    repeat_output_1.location = (2533.19873046875, 158.05152893066406)
    attribute_statistic_1.location = (804.4732055664062, 116.55569458007812)
    named_attribute_002.location = (309.64910888671875, -28.457839965820312)
    integer_math_1.location = (1450.824462890625, -27.830190658569336)
    random_value.location = (1848.888916015625, -24.403762817382812)
    random_value_001.location = (1849.99560546875, -200.05633544921875)
    attribute_statistic_001_1.location = (1496.9271240234375, -268.4363708496094)
    named_attribute_003.location = (990.5458374023438, -279.7574462890625)
    resample_curve_001.location = (-1201.6605224609375, 166.8787384033203)
    group_input_001_1.location = (1429.2889404296875, -90.1283950805664)
    spline_parameter.location = (-361.9509582519531, 265.5516357421875)
    integer_math_001_1.location = (1008.820068359375, 95.29082489013672)
    spline_parameter_001.location = (-361.60443115234375, -161.25119018554688)
    group_input_002_1.location = (-943.141845703125, 258.7990417480469)
    group_input_003_1.location = (1574.096923828125, 448.9494323730469)
    group_input_004_1.location = (2046.984619140625, -300.775634765625)
    delete_geometry_1.location = (446.0322265625, -63.688316345214844)
    random_value_002.location = (230.51739501953125, -143.65467834472656)
    subdivide_curve.location = (228.9630126953125, -36.09751892089844)
    group_input_005_1.location = (30.3643798828125, -235.697998046875)
    switch.location = (-375.5843200683594, 112.71163940429688)
    group_input_006_1.location = (-615.6986083984375, 124.76414489746094)
    group_input_007_1.location = (33.61083984375, -174.6937713623047)
    frame_001.location = (-1078.0, -6.0)
    group_input_008_1.location = (-189.08567810058594, 504.4698791503906)

    #Set dimensions
    group_input_1.width, group_input_1.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 145.300048828125, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    radius.width, radius.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    frame.width, frame.height = 1271.0, 375.0
    repeat_input_1.width, repeat_input_1.height = 140.0, 100.0
    repeat_output_1.width, repeat_output_1.height = 140.0, 100.0
    attribute_statistic_1.width, attribute_statistic_1.height = 140.0, 100.0
    named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
    integer_math_1.width, integer_math_1.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    attribute_statistic_001_1.width, attribute_statistic_001_1.height = 140.0, 100.0
    named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
    resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
    spline_parameter.width, spline_parameter.height = 140.0, 100.0
    integer_math_001_1.width, integer_math_001_1.height = 140.0, 100.0
    spline_parameter_001.width, spline_parameter_001.height = 140.0, 100.0
    group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
    group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
    group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
    delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    subdivide_curve.width, subdivide_curve.height = 140.0, 100.0
    group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_006_1.width, group_input_006_1.height = 140.0, 100.0
    group_input_007_1.width, group_input_007_1.height = 140.0, 100.0
    frame_001.width, frame_001.height = 616.0, 318.0
    group_input_008_1.width, group_input_008_1.height = 140.0, 100.0

    #initialize geom_hair_strands links
    #store_named_attribute_001.Geometry -> curve_to_mesh.Curve
    geom_hair_strands.links.new(store_named_attribute_001.outputs[0], curve_to_mesh.inputs[0])
    #transform_geometry.Geometry -> curve_to_mesh.Profile Curve
    geom_hair_strands.links.new(transform_geometry.outputs[0], curve_to_mesh.inputs[1])
    #store_named_attribute.Geometry -> transform_geometry.Geometry
    geom_hair_strands.links.new(store_named_attribute.outputs[0], transform_geometry.inputs[0])
    #object_info.Geometry -> resample_curve.Curve
    geom_hair_strands.links.new(object_info.outputs[4], resample_curve.inputs[0])
    #math.Value -> curve_to_mesh.Scale
    geom_hair_strands.links.new(math.outputs[0], curve_to_mesh.inputs[2])
    #radius.Radius -> math.Value
    geom_hair_strands.links.new(radius.outputs[0], math.inputs[0])
    #named_attribute.Attribute -> compare_1.A
    geom_hair_strands.links.new(named_attribute.outputs[0], compare_1.inputs[2])
    #compare_1.Result -> separate_geometry.Selection
    geom_hair_strands.links.new(compare_1.outputs[0], separate_geometry.inputs[1])
    #separate_geometry.Selection -> group.Input
    geom_hair_strands.links.new(separate_geometry.outputs[0], group.inputs[0])
    #named_attribute_001.Attribute -> group.y_idx
    geom_hair_strands.links.new(named_attribute_001.outputs[0], group.inputs[1])
    #curve_to_mesh.Mesh -> repeat_input_1.Geometry
    geom_hair_strands.links.new(curve_to_mesh.outputs[0], repeat_input_1.inputs[1])
    #curve_to_mesh.Mesh -> attribute_statistic_1.Geometry
    geom_hair_strands.links.new(curve_to_mesh.outputs[0], attribute_statistic_1.inputs[0])
    #named_attribute_002.Attribute -> attribute_statistic_1.Attribute
    geom_hair_strands.links.new(named_attribute_002.outputs[0], attribute_statistic_1.inputs[2])
    #repeat_input_1.Geometry -> separate_geometry.Geometry
    geom_hair_strands.links.new(repeat_input_1.outputs[1], separate_geometry.inputs[0])
    #integer_math_1.Value -> compare_1.B
    geom_hair_strands.links.new(integer_math_1.outputs[0], compare_1.inputs[3])
    #repeat_input_1.Iteration -> integer_math_1.Value
    geom_hair_strands.links.new(repeat_input_1.outputs[0], integer_math_1.inputs[0])
    #integer_math_1.Value -> random_value.ID
    geom_hair_strands.links.new(integer_math_1.outputs[0], random_value.inputs[7])
    #integer_math_1.Value -> random_value_001.ID
    geom_hair_strands.links.new(integer_math_1.outputs[0], random_value_001.inputs[7])
    #named_attribute_003.Attribute -> attribute_statistic_001_1.Attribute
    geom_hair_strands.links.new(named_attribute_003.outputs[0], attribute_statistic_001_1.inputs[2])
    #repeat_input_1.Geometry -> attribute_statistic_001_1.Geometry
    geom_hair_strands.links.new(repeat_input_1.outputs[1], attribute_statistic_001_1.inputs[0])
    #attribute_statistic_001_1.Range -> random_value_001.Max
    geom_hair_strands.links.new(attribute_statistic_001_1.outputs[5], random_value_001.inputs[5])
    #mesh_to_curve.Curve -> resample_curve_001.Curve
    geom_hair_strands.links.new(mesh_to_curve.outputs[0], resample_curve_001.inputs[0])
    #group_input_001_1.Min Scale -> random_value.Min
    geom_hair_strands.links.new(group_input_001_1.outputs[2], random_value.inputs[2])
    #group_input_001_1.Max Scale -> random_value.Max
    geom_hair_strands.links.new(group_input_001_1.outputs[3], random_value.inputs[3])
    #group_input_001_1.Min Loop Cut -> random_value_001.Min
    geom_hair_strands.links.new(group_input_001_1.outputs[4], random_value_001.inputs[4])
    #group_input_001_1.Seed -> random_value_001.Seed
    geom_hair_strands.links.new(group_input_001_1.outputs[5], random_value_001.inputs[8])
    #group_input_001_1.Seed -> random_value.Seed
    geom_hair_strands.links.new(group_input_001_1.outputs[5], random_value.inputs[8])
    #join_geometry.Geometry -> repeat_output_1.Geometry
    geom_hair_strands.links.new(join_geometry.outputs[0], repeat_output_1.inputs[0])
    #separate_geometry.Inverted -> join_geometry.Geometry
    geom_hair_strands.links.new(separate_geometry.outputs[1], join_geometry.inputs[0])
    #merge_by_distance.Geometry -> group_output_1.Geometry
    geom_hair_strands.links.new(merge_by_distance.outputs[0], group_output_1.inputs[0])
    #separate_geometry.Selection -> repeat_output_1.Geometry.001
    geom_hair_strands.links.new(separate_geometry.outputs[0], repeat_output_1.inputs[1])
    #repeat_output_1.Geometry -> merge_by_distance.Geometry
    geom_hair_strands.links.new(repeat_output_1.outputs[0], merge_by_distance.inputs[0])
    #attribute_statistic_1.Range -> integer_math_001_1.Value
    geom_hair_strands.links.new(attribute_statistic_1.outputs[5], integer_math_001_1.inputs[0])
    #integer_math_001_1.Value -> repeat_input_1.Iterations
    geom_hair_strands.links.new(integer_math_001_1.outputs[0], repeat_input_1.inputs[0])
    #resample_curve.Curve -> store_named_attribute_001.Geometry
    geom_hair_strands.links.new(resample_curve.outputs[0], store_named_attribute_001.inputs[0])
    #spline_parameter_001.Index -> store_named_attribute.Value
    geom_hair_strands.links.new(spline_parameter_001.outputs[2], store_named_attribute.inputs[3])
    #group_input_1.Geometry -> mesh_to_curve.Mesh
    geom_hair_strands.links.new(group_input_1.outputs[0], mesh_to_curve.inputs[0])
    #spline_parameter.Index -> store_named_attribute_001.Value
    geom_hair_strands.links.new(spline_parameter.outputs[2], store_named_attribute_001.inputs[3])
    #random_value.Value -> group.Scale
    geom_hair_strands.links.new(random_value.outputs[1], group.inputs[3])
    #random_value_001.Value -> group.From Idx
    geom_hair_strands.links.new(random_value_001.outputs[2], group.inputs[2])
    #group_input_002_1.Resample -> resample_curve.Count
    geom_hair_strands.links.new(group_input_002_1.outputs[6], resample_curve.inputs[2])
    #group_input_003_1.Delete Tip -> group.Delete Tip
    geom_hair_strands.links.new(group_input_003_1.outputs[7], group.inputs[4])
    #group_input_004_1.Max Length -> group.Max Length
    geom_hair_strands.links.new(group_input_004_1.outputs[8], group.inputs[5])
    #subdivide_curve.Curve -> delete_geometry_1.Geometry
    geom_hair_strands.links.new(subdivide_curve.outputs[0], delete_geometry_1.inputs[0])
    #random_value_002.Value -> delete_geometry_1.Selection
    geom_hair_strands.links.new(random_value_002.outputs[3], delete_geometry_1.inputs[1])
    #resample_curve_001.Curve -> subdivide_curve.Curve
    geom_hair_strands.links.new(resample_curve_001.outputs[0], subdivide_curve.inputs[0])
    #group_input_005_1.Seed -> random_value_002.Seed
    geom_hair_strands.links.new(group_input_005_1.outputs[10], random_value_002.inputs[8])
    #resample_curve_001.Curve -> switch.False
    geom_hair_strands.links.new(resample_curve_001.outputs[0], switch.inputs[1])
    #delete_geometry_1.Geometry -> switch.True
    geom_hair_strands.links.new(delete_geometry_1.outputs[0], switch.inputs[2])
    #switch.Output -> store_named_attribute.Geometry
    geom_hair_strands.links.new(switch.outputs[0], store_named_attribute.inputs[0])
    #group_input_006_1.Randomize Width -> switch.Switch
    geom_hair_strands.links.new(group_input_006_1.outputs[9], switch.inputs[0])
    #group_input_007_1.Probability -> random_value_002.Probability
    geom_hair_strands.links.new(group_input_007_1.outputs[11], random_value_002.inputs[6])
    #group_input_008_1.Radius Scale -> math.Value
    geom_hair_strands.links.new(group_input_008_1.outputs[1], math.inputs[1])
    #group.Geometry -> join_geometry.Geometry
    geom_hair_strands.links.new(group.outputs[0], join_geometry.inputs[0])
    return geom_hair_strands

geom_hair_strands = geom_hair_strands_node_group()

