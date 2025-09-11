import bpy, mathutils

#initialize normal_merge node group
def normal_merge_node_group():
    normal_merge = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Normal Merge")

    normal_merge.color_tag = 'NONE'
    normal_merge.description = ""
    normal_merge.default_group_node_width = 140
    

    normal_merge.is_modifier = True

    #normal_merge interface
    #Socket Geometry
    geometry_socket = normal_merge.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = normal_merge.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Object
    object_socket = normal_merge.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
    object_socket.attribute_domain = 'POINT'
    object_socket.default_input = 'VALUE'
    object_socket.structure_type = 'AUTO'

    #Socket Mix
    mix_socket = normal_merge.interface.new_socket(name = "Mix", in_out='INPUT', socket_type = 'NodeSocketFloat')
    mix_socket.default_value = 0.10000000149011612
    mix_socket.min_value = -10000.0
    mix_socket.max_value = 10000.0
    mix_socket.subtype = 'NONE'
    mix_socket.attribute_domain = 'POINT'
    mix_socket.default_input = 'VALUE'
    mix_socket.structure_type = 'AUTO'


    #initialize normal_merge nodes
    #node Group Input
    group_input = normal_merge.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True

    #node Group Output
    group_output = normal_merge.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Object Info
    object_info = normal_merge.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'RELATIVE'
    #As Instance
    object_info.inputs[1].default_value = False

    #node Geometry Proximity
    geometry_proximity = normal_merge.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.target_element = 'FACES'
    #Group ID
    geometry_proximity.inputs[1].default_value = 0
    #Source Position
    geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Sample Group ID
    geometry_proximity.inputs[3].default_value = 0

    #node Sample Nearest Surface
    sample_nearest_surface = normal_merge.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    #Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    #Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    #node Normal
    normal = normal_merge.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    #node Mix
    mix = normal_merge.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'VECTOR'
    mix.factor_mode = 'UNIFORM'

    #node Map Range
    map_range = normal_merge.nodes.new("ShaderNodeMapRange")
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

    #node Set Mesh Normal
    set_mesh_normal = normal_merge.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.domain = 'POINT'
    set_mesh_normal.mode = 'FREE'

    #node Frame
    frame = normal_merge.nodes.new("NodeFrame")
    frame.label = "Normal"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Group Input.001
    group_input_001 = normal_merge.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True

    #node Group Input.002
    group_input_002 = normal_merge.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True




    #Set parents
    object_info.parent = frame
    geometry_proximity.parent = frame
    sample_nearest_surface.parent = frame
    normal.parent = frame
    mix.parent = frame
    map_range.parent = frame
    group_input_002.parent = frame

    #Set locations
    group_input.location = (-371.3666076660156, 356.3302917480469)
    group_output.location = (43.41780090332031, 295.9292297363281)
    object_info.location = (44.708984375, -117.83367919921875)
    geometry_proximity.location = (368.57421875, -40.9495849609375)
    sample_nearest_surface.location = (363.30255126953125, -330.1787109375)
    normal.location = (29.9453125, -516.8072509765625)
    mix.location = (796.597412109375, -371.51904296875)
    map_range.location = (604.4069213867188, -35.9586181640625)
    set_mesh_normal.location = (-149.577880859375, 337.439208984375)
    frame.location = (-1369.0, 661.0)
    group_input_001.location = (-1563.5360107421875, 402.8709716796875)
    group_input_002.location = (366.50079345703125, -263.9706726074219)

    #Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 150.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    set_mesh_normal.width, set_mesh_normal.height = 140.0, 100.0
    frame.width, frame.height = 967.0, 619.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0

    #initialize normal_merge links
    #set_mesh_normal.Mesh -> group_output.Geometry
    normal_merge.links.new(set_mesh_normal.outputs[0], group_output.inputs[0])
    #object_info.Geometry -> geometry_proximity.Geometry
    normal_merge.links.new(object_info.outputs[4], geometry_proximity.inputs[0])
    #object_info.Geometry -> sample_nearest_surface.Mesh
    normal_merge.links.new(object_info.outputs[4], sample_nearest_surface.inputs[0])
    #normal.Normal -> sample_nearest_surface.Value
    normal_merge.links.new(normal.outputs[0], sample_nearest_surface.inputs[1])
    #sample_nearest_surface.Value -> mix.A
    normal_merge.links.new(sample_nearest_surface.outputs[0], mix.inputs[4])
    #normal.Normal -> mix.B
    normal_merge.links.new(normal.outputs[0], mix.inputs[5])
    #geometry_proximity.Distance -> map_range.Value
    normal_merge.links.new(geometry_proximity.outputs[1], map_range.inputs[0])
    #map_range.Result -> mix.Factor
    normal_merge.links.new(map_range.outputs[0], mix.inputs[0])
    #group_input.Geometry -> set_mesh_normal.Mesh
    normal_merge.links.new(group_input.outputs[0], set_mesh_normal.inputs[0])
    #mix.Result -> set_mesh_normal.Custom Normal
    normal_merge.links.new(mix.outputs[1], set_mesh_normal.inputs[1])
    #group_input_001.Object -> object_info.Object
    normal_merge.links.new(group_input_001.outputs[1], object_info.inputs[0])
    #group_input_002.Mix -> map_range.From Max
    normal_merge.links.new(group_input_002.outputs[2], map_range.inputs[2])
    return normal_merge

normal_merge = normal_merge_node_group()

