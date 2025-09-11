import bpy, mathutils

#initialize normal_distance_deform node group
def normal_distance_deform_node_group():
    normal_distance_deform = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Normal Distance Deform")

    normal_distance_deform.color_tag = 'NONE'
    normal_distance_deform.description = ""
    normal_distance_deform.default_group_node_width = 140
    

    normal_distance_deform.is_modifier = True

    #normal_distance_deform interface
    #Socket Geometry
    geometry_socket = normal_distance_deform.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = normal_distance_deform.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Normal Distance
    normal_distance_socket = normal_distance_deform.interface.new_socket(name = "Normal Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
    normal_distance_socket.default_value = 0.10000000149011612
    normal_distance_socket.min_value = -10000.0
    normal_distance_socket.max_value = 10000.0
    normal_distance_socket.subtype = 'NONE'
    normal_distance_socket.attribute_domain = 'POINT'
    normal_distance_socket.default_input = 'VALUE'
    normal_distance_socket.structure_type = 'AUTO'

    #Socket Position Distance
    position_distance_socket = normal_distance_deform.interface.new_socket(name = "Position Distance", in_out='INPUT', socket_type = 'NodeSocketFloat')
    position_distance_socket.default_value = 0.5
    position_distance_socket.min_value = -10000.0
    position_distance_socket.max_value = 10000.0
    position_distance_socket.subtype = 'NONE'
    position_distance_socket.attribute_domain = 'POINT'
    position_distance_socket.default_input = 'VALUE'
    position_distance_socket.structure_type = 'AUTO'

    #Socket Invert Position
    invert_position_socket = normal_distance_deform.interface.new_socket(name = "Invert Position", in_out='INPUT', socket_type = 'NodeSocketBool')
    invert_position_socket.default_value = False
    invert_position_socket.attribute_domain = 'POINT'
    invert_position_socket.default_input = 'VALUE'
    invert_position_socket.structure_type = 'AUTO'

    #Socket Position Scale
    position_scale_socket = normal_distance_deform.interface.new_socket(name = "Position Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    position_scale_socket.default_value = 0.5
    position_scale_socket.min_value = -10000.0
    position_scale_socket.max_value = 10000.0
    position_scale_socket.subtype = 'NONE'
    position_scale_socket.attribute_domain = 'POINT'
    position_scale_socket.default_input = 'VALUE'
    position_scale_socket.structure_type = 'AUTO'

    #Socket Target
    target_socket = normal_distance_deform.interface.new_socket(name = "Target", in_out='INPUT', socket_type = 'NodeSocketObject')
    target_socket.attribute_domain = 'POINT'
    target_socket.default_input = 'VALUE'
    target_socket.structure_type = 'AUTO'

    #Socket Smooth Shading
    smooth_shading_socket = normal_distance_deform.interface.new_socket(name = "Smooth Shading", in_out='INPUT', socket_type = 'NodeSocketBool')
    smooth_shading_socket.default_value = False
    smooth_shading_socket.attribute_domain = 'POINT'
    smooth_shading_socket.default_input = 'VALUE'
    smooth_shading_socket.structure_type = 'AUTO'


    #initialize normal_distance_deform nodes
    #node Group Input
    group_input = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True

    #node Group Output
    group_output = normal_distance_deform.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Object Info
    object_info = normal_distance_deform.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'RELATIVE'
    #As Instance
    object_info.inputs[1].default_value = False

    #node Geometry Proximity
    geometry_proximity = normal_distance_deform.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.target_element = 'FACES'
    #Group ID
    geometry_proximity.inputs[1].default_value = 0
    #Source Position
    geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Sample Group ID
    geometry_proximity.inputs[3].default_value = 0

    #node Sample Nearest Surface
    sample_nearest_surface = normal_distance_deform.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    #Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    #Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    #node Map Range
    map_range = normal_distance_deform.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    #From Min
    map_range.inputs[1].default_value = 0.0
    #To Min
    map_range.inputs[3].default_value = 0.0
    #To Max
    map_range.inputs[4].default_value = 1.0

    #node Normal
    normal = normal_distance_deform.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    #node Mix
    mix = normal_distance_deform.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'VECTOR'
    mix.factor_mode = 'UNIFORM'

    #node Set Position
    set_position = normal_distance_deform.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Vector Math
    vector_math = normal_distance_deform.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'SCALE'

    #node Raycast
    raycast = normal_distance_deform.nodes.new("GeometryNodeRaycast")
    raycast.name = "Raycast"
    raycast.data_type = 'FLOAT'
    raycast.mapping = 'INTERPOLATED'
    raycast.inputs[1].hide = True
    raycast.inputs[2].hide = True
    raycast.inputs[4].hide = True
    raycast.outputs[0].hide = True
    raycast.outputs[3].hide = True
    raycast.outputs[4].hide = True
    #Attribute
    raycast.inputs[1].default_value = 0.0
    #Source Position
    raycast.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Ray Length
    raycast.inputs[4].default_value = 100.0

    #node Compare.001
    compare_001 = normal_distance_deform.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'GREATER_THAN'
    #B
    compare_001.inputs[1].default_value = 0.0

    #node Vector Math.001
    vector_math_001 = normal_distance_deform.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'DOT_PRODUCT'

    #node Set Mesh Normal
    set_mesh_normal = normal_distance_deform.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.domain = 'CORNER'
    set_mesh_normal.mode = 'FREE'

    #node Mix.001
    mix_001 = normal_distance_deform.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'VECTOR'
    mix_001.factor_mode = 'UNIFORM'

    #node Map Range.001
    map_range_001 = normal_distance_deform.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    #From Min
    map_range_001.inputs[1].default_value = 0.0
    #To Min
    map_range_001.inputs[3].default_value = 0.0
    #To Max
    map_range_001.inputs[4].default_value = 1.0

    #node Group Input.001
    group_input_001 = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True

    #node Group Input.002
    group_input_002 = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True

    #node Compare.002
    compare_002 = normal_distance_deform.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'LESS_THAN'
    #B
    compare_002.inputs[1].default_value = 0.0

    #node Switch
    switch = normal_distance_deform.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'BOOLEAN'

    #node Group Input.003
    group_input_003 = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True

    #node Group Input.004
    group_input_004 = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True

    #node Group Input.005
    group_input_005 = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True

    #node Set Shade Smooth
    set_shade_smooth = normal_distance_deform.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    #Selection
    set_shade_smooth.inputs[1].default_value = True

    #node Group Input.006
    group_input_006 = normal_distance_deform.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[7].hide = True





    #Set locations
    group_input.location = (433.2862854003906, 326.55938720703125)
    group_output.location = (1586.13037109375, 50.21714782714844)
    object_info.location = (-482.23907470703125, 37.69746398925781)
    geometry_proximity.location = (-144.03726196289062, 155.3904571533203)
    sample_nearest_surface.location = (-129.0723419189453, -89.26087188720703)
    map_range.location = (122.10264587402344, 415.048583984375)
    normal.location = (-465.6419677734375, -298.3287353515625)
    mix.location = (515.2764282226562, -121.13128662109375)
    set_position.location = (936.5488891601562, -9.538307189941406)
    vector_math.location = (-18.717967987060547, -489.2468566894531)
    raycast.location = (90.90194702148438, -225.33663940429688)
    compare_001.location = (542.3648681640625, -342.6121826171875)
    vector_math_001.location = (316.1346740722656, -403.2936096191406)
    set_mesh_normal.location = (1337.1661376953125, 116.88726806640625)
    mix_001.location = (502.43524169921875, 100.69566345214844)
    map_range_001.location = (128.55960083007812, 140.5310516357422)
    group_input_001.location = (-242.19384765625, 423.11688232421875)
    group_input_002.location = (-253.49351501464844, 266.2596740722656)
    compare_002.location = (539.1364135742188, -504.3208312988281)
    switch.location = (962.4971923828125, -357.72845458984375)
    group_input_003.location = (732.0783081054688, -277.106201171875)
    group_input_004.location = (-299.2347717285156, -546.9512939453125)
    group_input_005.location = (-713.2488403320312, -88.72758483886719)
    set_shade_smooth.location = (634.93359375, 310.3934326171875)
    group_input_006.location = (450.5635070800781, 207.3811492919922)

    #Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 150.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    raycast.width, raycast.height = 150.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    set_mesh_normal.width, set_mesh_normal.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    map_range_001.width, map_range_001.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0

    #initialize normal_distance_deform links
    #set_mesh_normal.Mesh -> group_output.Geometry
    normal_distance_deform.links.new(set_mesh_normal.outputs[0], group_output.inputs[0])
    #object_info.Geometry -> geometry_proximity.Geometry
    normal_distance_deform.links.new(object_info.outputs[4], geometry_proximity.inputs[0])
    #object_info.Geometry -> sample_nearest_surface.Mesh
    normal_distance_deform.links.new(object_info.outputs[4], sample_nearest_surface.inputs[0])
    #geometry_proximity.Distance -> map_range.Value
    normal_distance_deform.links.new(geometry_proximity.outputs[1], map_range.inputs[0])
    #normal.Normal -> sample_nearest_surface.Value
    normal_distance_deform.links.new(normal.outputs[0], sample_nearest_surface.inputs[1])
    #normal.Normal -> raycast.Ray Direction
    normal_distance_deform.links.new(normal.outputs[0], raycast.inputs[3])
    #object_info.Geometry -> raycast.Target Geometry
    normal_distance_deform.links.new(object_info.outputs[4], raycast.inputs[0])
    #raycast.Hit Position -> mix.A
    normal_distance_deform.links.new(raycast.outputs[1], mix.inputs[4])
    #vector_math_001.Value -> compare_001.A
    normal_distance_deform.links.new(vector_math_001.outputs[1], compare_001.inputs[0])
    #raycast.Hit Normal -> vector_math_001.Vector
    normal_distance_deform.links.new(raycast.outputs[2], vector_math_001.inputs[0])
    #sample_nearest_surface.Value -> mix_001.A
    normal_distance_deform.links.new(sample_nearest_surface.outputs[0], mix_001.inputs[4])
    #normal.Normal -> mix_001.B
    normal_distance_deform.links.new(normal.outputs[0], mix_001.inputs[5])
    #map_range.Result -> mix_001.Factor
    normal_distance_deform.links.new(map_range.outputs[0], mix_001.inputs[0])
    #mix_001.Result -> set_mesh_normal.Custom Normal
    normal_distance_deform.links.new(mix_001.outputs[1], set_mesh_normal.inputs[1])
    #geometry_proximity.Distance -> map_range_001.Value
    normal_distance_deform.links.new(geometry_proximity.outputs[1], map_range_001.inputs[0])
    #map_range_001.Result -> mix.Factor
    normal_distance_deform.links.new(map_range_001.outputs[0], mix.inputs[0])
    #mix.Result -> set_position.Position
    normal_distance_deform.links.new(mix.outputs[1], set_position.inputs[2])
    #normal.Normal -> vector_math.Vector
    normal_distance_deform.links.new(normal.outputs[0], vector_math.inputs[0])
    #vector_math.Vector -> mix.B
    normal_distance_deform.links.new(vector_math.outputs[0], mix.inputs[5])
    #group_input_001.Normal Distance -> map_range.From Max
    normal_distance_deform.links.new(group_input_001.outputs[1], map_range.inputs[2])
    #group_input_002.Position Distance -> map_range_001.From Max
    normal_distance_deform.links.new(group_input_002.outputs[2], map_range_001.inputs[2])
    #vector_math_001.Value -> compare_002.A
    normal_distance_deform.links.new(vector_math_001.outputs[1], compare_002.inputs[0])
    #compare_002.Result -> switch.True
    normal_distance_deform.links.new(compare_002.outputs[0], switch.inputs[2])
    #compare_001.Result -> switch.False
    normal_distance_deform.links.new(compare_001.outputs[0], switch.inputs[1])
    #switch.Output -> set_position.Selection
    normal_distance_deform.links.new(switch.outputs[0], set_position.inputs[1])
    #group_input_003.Invert Position -> switch.Switch
    normal_distance_deform.links.new(group_input_003.outputs[3], switch.inputs[0])
    #group_input_004.Position Scale -> vector_math.Scale
    normal_distance_deform.links.new(group_input_004.outputs[4], vector_math.inputs[3])
    #normal.Normal -> vector_math_001.Vector
    normal_distance_deform.links.new(normal.outputs[0], vector_math_001.inputs[1])
    #group_input_005.Target -> object_info.Object
    normal_distance_deform.links.new(group_input_005.outputs[5], object_info.inputs[0])
    #group_input.Geometry -> set_shade_smooth.Geometry
    normal_distance_deform.links.new(group_input.outputs[0], set_shade_smooth.inputs[0])
    #group_input_006.Smooth Shading -> set_shade_smooth.Shade Smooth
    normal_distance_deform.links.new(group_input_006.outputs[6], set_shade_smooth.inputs[2])
    #set_position.Geometry -> set_mesh_normal.Mesh
    normal_distance_deform.links.new(set_position.outputs[0], set_mesh_normal.inputs[0])
    #set_shade_smooth.Geometry -> set_position.Geometry
    normal_distance_deform.links.new(set_shade_smooth.outputs[0], set_position.inputs[0])
    return normal_distance_deform

normal_distance_deform = normal_distance_deform_node_group()

