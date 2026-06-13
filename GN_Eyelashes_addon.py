import bpy, mathutils

#initialize _ee_convert_value node group
def _ee_convert_value_node_group():
    _ee_convert_value = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".EE_Convert Value")

    _ee_convert_value.color_tag = 'NONE'
    _ee_convert_value.description = ""
    _ee_convert_value.default_group_node_width = 140
    


    #_ee_convert_value interface
    #Socket N
    n_socket = _ee_convert_value.interface.new_socket(name = "N", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    n_socket.default_value = 0.0
    n_socket.min_value = -3.4028234663852886e+38
    n_socket.max_value = 3.4028234663852886e+38
    n_socket.subtype = 'NONE'
    n_socket.attribute_domain = 'POINT'
    n_socket.default_input = 'VALUE'
    n_socket.structure_type = 'AUTO'

    #Socket -N
    _n_socket = _ee_convert_value.interface.new_socket(name = "-N", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _n_socket.default_value = 0.0
    _n_socket.min_value = -3.4028234663852886e+38
    _n_socket.max_value = 3.4028234663852886e+38
    _n_socket.subtype = 'NONE'
    _n_socket.attribute_domain = 'POINT'
    _n_socket.default_input = 'VALUE'
    _n_socket.structure_type = 'AUTO'

    #Socket 1 - N
    _1___n_socket = _ee_convert_value.interface.new_socket(name = "1 - N", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1___n_socket.default_value = 0.0
    _1___n_socket.min_value = -3.4028234663852886e+38
    _1___n_socket.max_value = 3.4028234663852886e+38
    _1___n_socket.subtype = 'NONE'
    _1___n_socket.attribute_domain = 'POINT'
    _1___n_socket.default_input = 'VALUE'
    _1___n_socket.structure_type = 'AUTO'

    #Socket 1 / N
    _1___n_socket_1 = _ee_convert_value.interface.new_socket(name = "1 / N", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1___n_socket_1.default_value = 0.0
    _1___n_socket_1.min_value = -3.4028234663852886e+38
    _1___n_socket_1.max_value = 3.4028234663852886e+38
    _1___n_socket_1.subtype = 'NONE'
    _1___n_socket_1.attribute_domain = 'POINT'
    _1___n_socket_1.default_input = 'VALUE'
    _1___n_socket_1.structure_type = 'AUTO'

    #Socket 2N
    _2n_socket = _ee_convert_value.interface.new_socket(name = "2N", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2n_socket.default_value = 0.0
    _2n_socket.min_value = -3.4028234663852886e+38
    _2n_socket.max_value = 3.4028234663852886e+38
    _2n_socket.subtype = 'NONE'
    _2n_socket.attribute_domain = 'POINT'
    _2n_socket.default_input = 'VALUE'
    _2n_socket.structure_type = 'AUTO'

    #Socket N / 2
    n___2_socket = _ee_convert_value.interface.new_socket(name = "N / 2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    n___2_socket.default_value = 0.0
    n___2_socket.min_value = -3.4028234663852886e+38
    n___2_socket.max_value = 3.4028234663852886e+38
    n___2_socket.subtype = 'NONE'
    n___2_socket.attribute_domain = 'POINT'
    n___2_socket.default_input = 'VALUE'
    n___2_socket.structure_type = 'AUTO'

    #Socket N
    n_socket_1 = _ee_convert_value.interface.new_socket(name = "N", in_out='INPUT', socket_type = 'NodeSocketFloat')
    n_socket_1.default_value = 0.0
    n_socket_1.min_value = -3.4028234663852886e+38
    n_socket_1.max_value = 3.4028234663852886e+38
    n_socket_1.subtype = 'NONE'
    n_socket_1.attribute_domain = 'POINT'
    n_socket_1.default_input = 'VALUE'
    n_socket_1.structure_type = 'AUTO'


    #initialize _ee_convert_value nodes
    #node Math.003
    math_003 = _ee_convert_value.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'SUBTRACT'
    math_003.use_clamp = False
    #Value
    math_003.inputs[0].default_value = 1.0

    #node Math.004
    math_004 = _ee_convert_value.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'DIVIDE'
    math_004.use_clamp = False
    #Value
    math_004.inputs[0].default_value = 1.0

    #node Math.002
    math_002 = _ee_convert_value.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    #Value_001
    math_002.inputs[1].default_value = -1.0

    #node Reroute.003
    reroute_003 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketFloat"
    #node Reroute.004
    reroute_004 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketFloat"
    #node Reroute.005
    reroute_005 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketFloat"
    #node Reroute.006
    reroute_006 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketFloat"
    #node Reroute.002
    reroute_002 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketFloat"
    #node Reroute.001
    reroute_001 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketFloat"
    #node Reroute
    reroute = _ee_convert_value.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketFloat"
    #node Reroute.008
    reroute_008 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloat"
    #node Reroute.010
    reroute_010 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketFloat"
    #node Reroute.011
    reroute_011 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.socket_idname = "NodeSocketFloat"
    #node Reroute.007
    reroute_007 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloat"
    #node Reroute.009
    reroute_009 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketFloat"
    #node Math.005
    math_005 = _ee_convert_value.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    #Value_001
    math_005.inputs[1].default_value = 2.0

    #node Reroute.012
    reroute_012 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.socket_idname = "NodeSocketFloat"
    #node Reroute.013
    reroute_013 = _ee_convert_value.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.socket_idname = "NodeSocketFloat"
    #node Math.006
    math_006 = _ee_convert_value.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    #Value_001
    math_006.inputs[1].default_value = 0.5

    #node Group Output
    group_output = _ee_convert_value.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input.001
    group_input_001 = _ee_convert_value.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"





    #Set locations
    math_003.location = (541.3670654296875, -20.05063247680664)
    math_004.location = (741.8734130859375, -20.05063247680664)
    math_002.location = (340.86077880859375, -20.05063247680664)
    reroute_003.location = (481.2152099609375, 80.20252990722656)
    reroute_004.location = (681.7215576171875, 80.20252990722656)
    reroute_005.location = (541.3670654296875, 60.15190124511719)
    reroute_006.location = (741.8734130859375, 40.10126495361328)
    reroute_002.location = (280.7088623046875, 80.20252990722656)
    reroute_001.location = (882.2278442382812, 80.20252990722656)
    reroute.location = (1082.734130859375, 80.20252990722656)
    reroute_008.location = (1283.240478515625, 40.10126495361328)
    reroute_010.location = (942.3797607421875, 20.05063247680664)
    reroute_011.location = (1283.240478515625, 20.05063247680664)
    reroute_007.location = (1283.240478515625, 60.15190124511719)
    reroute_009.location = (1283.240478515625, 80.20252990722656)
    math_005.location = (942.3797607421875, -20.05063247680664)
    reroute_012.location = (1142.8861083984375, 0.0)
    reroute_013.location = (1283.240478515625, 0.0)
    math_006.location = (1142.8861083984375, -20.05063247680664)
    group_output.location = (1483.746826171875, -20.05063247680664)
    group_input_001.location = (80.20252990722656, -20.05063247680664)

    #Set dimensions
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    reroute_003.width, reroute_003.height = 16.0, 100.0
    reroute_004.width, reroute_004.height = 16.0, 100.0
    reroute_005.width, reroute_005.height = 16.0, 100.0
    reroute_006.width, reroute_006.height = 16.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    reroute.width, reroute.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0
    reroute_010.width, reroute_010.height = 16.0, 100.0
    reroute_011.width, reroute_011.height = 16.0, 100.0
    reroute_007.width, reroute_007.height = 16.0, 100.0
    reroute_009.width, reroute_009.height = 16.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    reroute_012.width, reroute_012.height = 16.0, 100.0
    reroute_013.width, reroute_013.height = 16.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0

    #initialize _ee_convert_value links
    #reroute_002.Output -> math_002.Value
    _ee_convert_value.links.new(reroute_002.outputs[0], math_002.inputs[0])
    #reroute_003.Output -> math_003.Value
    _ee_convert_value.links.new(reroute_003.outputs[0], math_003.inputs[1])
    #reroute_004.Output -> math_004.Value
    _ee_convert_value.links.new(reroute_004.outputs[0], math_004.inputs[1])
    #reroute_004.Output -> reroute_001.Input
    _ee_convert_value.links.new(reroute_004.outputs[0], reroute_001.inputs[0])
    #reroute_002.Output -> reroute_003.Input
    _ee_convert_value.links.new(reroute_002.outputs[0], reroute_003.inputs[0])
    #reroute_003.Output -> reroute_004.Input
    _ee_convert_value.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    #math_002.Value -> reroute_005.Input
    _ee_convert_value.links.new(math_002.outputs[0], reroute_005.inputs[0])
    #math_003.Value -> reroute_006.Input
    _ee_convert_value.links.new(math_003.outputs[0], reroute_006.inputs[0])
    #reroute_005.Output -> reroute_007.Input
    _ee_convert_value.links.new(reroute_005.outputs[0], reroute_007.inputs[0])
    #reroute_006.Output -> reroute_008.Input
    _ee_convert_value.links.new(reroute_006.outputs[0], reroute_008.inputs[0])
    #reroute_009.Output -> group_output.N
    _ee_convert_value.links.new(reroute_009.outputs[0], group_output.inputs[0])
    #reroute_007.Output -> group_output.-N
    _ee_convert_value.links.new(reroute_007.outputs[0], group_output.inputs[1])
    #reroute_008.Output -> group_output.1 - N
    _ee_convert_value.links.new(reroute_008.outputs[0], group_output.inputs[2])
    #reroute_011.Output -> group_output.1 / N
    _ee_convert_value.links.new(reroute_011.outputs[0], group_output.inputs[3])
    #group_input_001.N -> reroute_002.Input
    _ee_convert_value.links.new(group_input_001.outputs[0], reroute_002.inputs[0])
    #reroute_001.Output -> math_005.Value
    _ee_convert_value.links.new(reroute_001.outputs[0], math_005.inputs[0])
    #reroute_001.Output -> reroute.Input
    _ee_convert_value.links.new(reroute_001.outputs[0], reroute.inputs[0])
    #reroute.Output -> math_006.Value
    _ee_convert_value.links.new(reroute.outputs[0], math_006.inputs[0])
    #reroute.Output -> reroute_009.Input
    _ee_convert_value.links.new(reroute.outputs[0], reroute_009.inputs[0])
    #math_004.Value -> reroute_010.Input
    _ee_convert_value.links.new(math_004.outputs[0], reroute_010.inputs[0])
    #reroute_010.Output -> reroute_011.Input
    _ee_convert_value.links.new(reroute_010.outputs[0], reroute_011.inputs[0])
    #math_005.Value -> reroute_012.Input
    _ee_convert_value.links.new(math_005.outputs[0], reroute_012.inputs[0])
    #reroute_012.Output -> reroute_013.Input
    _ee_convert_value.links.new(reroute_012.outputs[0], reroute_013.inputs[0])
    #reroute_013.Output -> group_output.2N
    _ee_convert_value.links.new(reroute_013.outputs[0], group_output.inputs[4])
    #math_006.Value -> group_output.N / 2
    _ee_convert_value.links.new(math_006.outputs[0], group_output.inputs[5])
    return _ee_convert_value

_ee_convert_value = _ee_convert_value_node_group()

#initialize _ee_shrinkwrap_to_surface node group
def _ee_shrinkwrap_to_surface_node_group():
    _ee_shrinkwrap_to_surface = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".EE_Shrinkwrap to Surface")

    _ee_shrinkwrap_to_surface.color_tag = 'NONE'
    _ee_shrinkwrap_to_surface.description = ""
    _ee_shrinkwrap_to_surface.default_group_node_width = 140
    


    #_ee_shrinkwrap_to_surface interface
    #Socket Geometry
    geometry_socket = _ee_shrinkwrap_to_surface.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Position
    position_socket = _ee_shrinkwrap_to_surface.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    position_socket.default_value = (0.0, 0.0, 0.0)
    position_socket.min_value = -3.4028234663852886e+38
    position_socket.max_value = 3.4028234663852886e+38
    position_socket.subtype = 'NONE'
    position_socket.attribute_domain = 'POINT'
    position_socket.default_input = 'VALUE'
    position_socket.structure_type = 'AUTO'

    #Socket Normal
    normal_socket = _ee_shrinkwrap_to_surface.interface.new_socket(name = "Normal", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    normal_socket.default_value = (0.0, 0.0, 0.0)
    normal_socket.min_value = -3.4028234663852886e+38
    normal_socket.max_value = 3.4028234663852886e+38
    normal_socket.subtype = 'NONE'
    normal_socket.attribute_domain = 'POINT'
    normal_socket.default_input = 'VALUE'
    normal_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = _ee_shrinkwrap_to_surface.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Object
    object_socket = _ee_shrinkwrap_to_surface.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
    object_socket.attribute_domain = 'POINT'
    object_socket.default_input = 'VALUE'
    object_socket.structure_type = 'AUTO'

    #Socket Offset
    offset_socket = _ee_shrinkwrap_to_surface.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    offset_socket.default_value = 0.0
    offset_socket.min_value = -10000.0
    offset_socket.max_value = 10000.0
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'


    #initialize _ee_shrinkwrap_to_surface nodes
    #node Position
    position = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Object Info
    object_info = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'RELATIVE'
    #As Instance
    object_info.inputs[1].default_value = False

    #node Normal
    normal = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = True

    #node Sample Nearest Surface.001
    sample_nearest_surface_001 = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface_001.name = "Sample Nearest Surface.001"
    sample_nearest_surface_001.data_type = 'FLOAT_VECTOR'
    #Group ID
    sample_nearest_surface_001.inputs[2].default_value = 0
    #Sample Position
    sample_nearest_surface_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Sample Group ID
    sample_nearest_surface_001.inputs[4].default_value = 0

    #node Group Input
    group_input = _ee_shrinkwrap_to_surface.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.use_custom_color = True
    group_input.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True

    #node Vector Math
    vector_math = _ee_shrinkwrap_to_surface.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.hide = True
    vector_math.operation = 'SCALE'

    #node Reroute.003
    reroute_003_1 = _ee_shrinkwrap_to_surface.nodes.new("NodeReroute")
    reroute_003_1.name = "Reroute.003"
    reroute_003_1.socket_idname = "NodeSocketVector"
    #node Group Input.002
    group_input_002 = _ee_shrinkwrap_to_surface.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.use_custom_color = True
    group_input_002.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True

    #node Math.001
    math_001 = _ee_shrinkwrap_to_surface.nodes.new("ShaderNodeMath")
    math_001.label = "scale down"
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False
    #Value_001
    math_001.inputs[1].default_value = 0.0010000000474974513

    #node Group Input.001
    group_input_001_1 = _ee_shrinkwrap_to_surface.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.use_custom_color = True
    group_input_001_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[2].hide = True
    group_input_001_1.outputs[3].hide = True

    #node Sample Nearest Surface
    sample_nearest_surface = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    #Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    #Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    #node Capture Attribute
    capture_attribute = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Value")
    capture_attribute.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'POINT'

    #node Capture Attribute.001
    capture_attribute_001 = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.active_index = 0
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new('FLOAT', "Value")
    capture_attribute_001.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_001.domain = 'POINT'

    #node Group Output
    group_output_1 = _ee_shrinkwrap_to_surface.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Set Position.001
    set_position_001 = _ee_shrinkwrap_to_surface.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    #Selection
    set_position_001.inputs[1].default_value = True

    #node Reroute
    reroute_1 = _ee_shrinkwrap_to_surface.nodes.new("NodeReroute")
    reroute_1.label = "position"
    reroute_1.name = "Reroute"
    reroute_1.socket_idname = "NodeSocketVector"
    #node Reroute.001
    reroute_001_1 = _ee_shrinkwrap_to_surface.nodes.new("NodeReroute")
    reroute_001_1.label = "normal"
    reroute_001_1.name = "Reroute.001"
    reroute_001_1.socket_idname = "NodeSocketVector"




    #Set locations
    position.location = (-94.07795715332031, 30.14276123046875)
    object_info.location = (-286.0059814453125, 169.7423553466797)
    normal.location = (-96.19467163085938, -159.37918090820312)
    sample_nearest_surface_001.location = (-94.97129821777344, -35.51994323730469)
    group_input.location = (-94.52082061767578, 246.6599884033203)
    vector_math.location = (96.14240264892578, -118.03341674804688)
    reroute_003_1.location = (289.91473388671875, 92.31758880615234)
    group_input_002.location = (-276.6195373535156, -224.77577209472656)
    math_001.location = (-95.42521667480469, -221.72085571289062)
    group_input_001_1.location = (-464.1229553222656, 56.59653091430664)
    sample_nearest_surface.location = (-94.97129821777344, 153.9923858642578)
    capture_attribute.location = (518.0183715820312, 186.14047241210938)
    capture_attribute_001.location = (518.2865600585938, 58.65657043457031)
    group_output_1.location = (725.1205444335938, 140.4317169189453)
    set_position_001.location = (287.65570068359375, 79.357666015625)
    reroute_1.location = (428.7943115234375, 120.49238586425781)
    reroute_001_1.location = (428.7943115234375, 92.31758880615234)

    #Set dimensions
    position.width, position.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    sample_nearest_surface_001.width, sample_nearest_surface_001.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    reroute_003_1.width, reroute_003_1.height = 16.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    reroute_1.width, reroute_1.height = 16.0, 100.0
    reroute_001_1.width, reroute_001_1.height = 16.0, 100.0

    #initialize _ee_shrinkwrap_to_surface links
    #math_001.Value -> vector_math.Scale
    _ee_shrinkwrap_to_surface.links.new(math_001.outputs[0], vector_math.inputs[3])
    #vector_math.Vector -> set_position_001.Offset
    _ee_shrinkwrap_to_surface.links.new(vector_math.outputs[0], set_position_001.inputs[3])
    #sample_nearest_surface_001.Value -> vector_math.Vector
    _ee_shrinkwrap_to_surface.links.new(sample_nearest_surface_001.outputs[0], vector_math.inputs[0])
    #sample_nearest_surface.Value -> set_position_001.Position
    _ee_shrinkwrap_to_surface.links.new(sample_nearest_surface.outputs[0], set_position_001.inputs[2])
    #position.Position -> sample_nearest_surface.Value
    _ee_shrinkwrap_to_surface.links.new(position.outputs[0], sample_nearest_surface.inputs[1])
    #normal.Normal -> sample_nearest_surface_001.Value
    _ee_shrinkwrap_to_surface.links.new(normal.outputs[0], sample_nearest_surface_001.inputs[1])
    #object_info.Geometry -> sample_nearest_surface.Mesh
    _ee_shrinkwrap_to_surface.links.new(object_info.outputs[4], sample_nearest_surface.inputs[0])
    #object_info.Geometry -> sample_nearest_surface_001.Mesh
    _ee_shrinkwrap_to_surface.links.new(object_info.outputs[4], sample_nearest_surface_001.inputs[0])
    #group_input.Geometry -> set_position_001.Geometry
    _ee_shrinkwrap_to_surface.links.new(group_input.outputs[0], set_position_001.inputs[0])
    #capture_attribute_001.Geometry -> group_output_1.Geometry
    _ee_shrinkwrap_to_surface.links.new(capture_attribute_001.outputs[0], group_output_1.inputs[0])
    #group_input_002.Offset -> math_001.Value
    _ee_shrinkwrap_to_surface.links.new(group_input_002.outputs[2], math_001.inputs[0])
    #sample_nearest_surface.Value -> reroute_1.Input
    _ee_shrinkwrap_to_surface.links.new(sample_nearest_surface.outputs[0], reroute_1.inputs[0])
    #reroute_003_1.Output -> reroute_001_1.Input
    _ee_shrinkwrap_to_surface.links.new(reroute_003_1.outputs[0], reroute_001_1.inputs[0])
    #sample_nearest_surface_001.Value -> reroute_003_1.Input
    _ee_shrinkwrap_to_surface.links.new(sample_nearest_surface_001.outputs[0], reroute_003_1.inputs[0])
    #group_input_001_1.Object -> object_info.Object
    _ee_shrinkwrap_to_surface.links.new(group_input_001_1.outputs[1], object_info.inputs[0])
    #set_position_001.Geometry -> capture_attribute.Geometry
    _ee_shrinkwrap_to_surface.links.new(set_position_001.outputs[0], capture_attribute.inputs[0])
    #capture_attribute.Geometry -> capture_attribute_001.Geometry
    _ee_shrinkwrap_to_surface.links.new(capture_attribute.outputs[0], capture_attribute_001.inputs[0])
    #reroute_001_1.Output -> capture_attribute_001.Value
    _ee_shrinkwrap_to_surface.links.new(reroute_001_1.outputs[0], capture_attribute_001.inputs[1])
    #reroute_1.Output -> capture_attribute.Value
    _ee_shrinkwrap_to_surface.links.new(reroute_1.outputs[0], capture_attribute.inputs[1])
    #capture_attribute.Value -> group_output_1.Position
    _ee_shrinkwrap_to_surface.links.new(capture_attribute.outputs[1], group_output_1.inputs[1])
    #capture_attribute_001.Value -> group_output_1.Normal
    _ee_shrinkwrap_to_surface.links.new(capture_attribute_001.outputs[1], group_output_1.inputs[2])
    return _ee_shrinkwrap_to_surface

_ee_shrinkwrap_to_surface = _ee_shrinkwrap_to_surface_node_group()

#initialize _ee_contrast node group
def _ee_contrast_node_group():
    _ee_contrast = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".EE_Contrast")

    _ee_contrast.color_tag = 'NONE'
    _ee_contrast.description = ""
    _ee_contrast.default_group_node_width = 140
    


    #_ee_contrast interface
    #Socket Value
    value_socket = _ee_contrast.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    #Socket Value
    value_socket_1 = _ee_contrast.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_1.default_value = 1.0
    value_socket_1.min_value = -10000.0
    value_socket_1.max_value = 10000.0
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'
    value_socket_1.hide_value = True
    value_socket_1.default_input = 'VALUE'
    value_socket_1.structure_type = 'AUTO'

    #Socket Contrast
    contrast_socket = _ee_contrast.interface.new_socket(name = "Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat')
    contrast_socket.default_value = 0.0
    contrast_socket.min_value = 0.0
    contrast_socket.max_value = 1.0
    contrast_socket.subtype = 'FACTOR'
    contrast_socket.attribute_domain = 'POINT'
    contrast_socket.default_input = 'VALUE'
    contrast_socket.structure_type = 'AUTO'


    #initialize _ee_contrast nodes
    #node Group Output
    group_output_2 = _ee_contrast.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    #node Map Range
    map_range = _ee_contrast.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    #To Min
    map_range.inputs[3].default_value = 0.0
    #To Max
    map_range.inputs[4].default_value = 1.0

    #node Mix
    mix = _ee_contrast.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'FLOAT'
    mix.factor_mode = 'UNIFORM'
    #A_Float
    mix.inputs[2].default_value = 0.0
    #B_Float
    mix.inputs[3].default_value = 0.49900001287460327

    #node Math.004
    math_004_1 = _ee_contrast.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.hide = True
    math_004_1.operation = 'SUBTRACT'
    math_004_1.use_clamp = False
    #Value
    math_004_1.inputs[0].default_value = 1.0

    #node Group Input
    group_input_1 = _ee_contrast.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"





    #Set locations
    group_output_2.location = (278.6736755371094, 0.0)
    map_range.location = (88.67367553710938, 128.08419799804688)
    mix.location = (-105.78258514404297, -31.419042587280273)
    math_004_1.location = (-105.78258514404297, -169.3558807373047)
    group_input_1.location = (-305.7825622558594, 26.172258377075195)

    #Set dimensions
    group_output_2.width, group_output_2.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0

    #initialize _ee_contrast links
    #mix.Result -> math_004_1.Value
    _ee_contrast.links.new(mix.outputs[0], math_004_1.inputs[1])
    #math_004_1.Value -> map_range.From Max
    _ee_contrast.links.new(math_004_1.outputs[0], map_range.inputs[2])
    #mix.Result -> map_range.From Min
    _ee_contrast.links.new(mix.outputs[0], map_range.inputs[1])
    #group_input_1.Value -> map_range.Value
    _ee_contrast.links.new(group_input_1.outputs[0], map_range.inputs[0])
    #map_range.Result -> group_output_2.Value
    _ee_contrast.links.new(map_range.outputs[0], group_output_2.inputs[0])
    #group_input_1.Contrast -> mix.Factor
    _ee_contrast.links.new(group_input_1.outputs[1], mix.inputs[0])
    return _ee_contrast

_ee_contrast = _ee_contrast_node_group()

#initialize _ee_easing__bezier_ node group
def _ee_easing__bezier__node_group():
    _ee_easing__bezier_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".EE_Easing (Bezier)")

    _ee_easing__bezier_.color_tag = 'NONE'
    _ee_easing__bezier_.description = ""
    _ee_easing__bezier_.default_group_node_width = 140
    


    #_ee_easing__bezier_ interface
    #Socket Value
    value_socket_2 = _ee_easing__bezier_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_2.default_value = 0.0
    value_socket_2.min_value = -3.4028234663852886e+38
    value_socket_2.max_value = 3.4028234663852886e+38
    value_socket_2.subtype = 'NONE'
    value_socket_2.attribute_domain = 'POINT'
    value_socket_2.default_input = 'VALUE'
    value_socket_2.structure_type = 'AUTO'

    #Socket Value
    value_socket_3 = _ee_easing__bezier_.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_3.default_value = 0.0
    value_socket_3.min_value = -3.4028234663852886e+38
    value_socket_3.max_value = 3.4028234663852886e+38
    value_socket_3.subtype = 'NONE'
    value_socket_3.attribute_domain = 'POINT'
    value_socket_3.hide_value = True
    value_socket_3.default_input = 'VALUE'
    value_socket_3.structure_type = 'AUTO'

    #Socket Ease In
    ease_in_socket = _ee_easing__bezier_.interface.new_socket(name = "Ease In", in_out='INPUT', socket_type = 'NodeSocketFloat')
    ease_in_socket.default_value = 0.0
    ease_in_socket.min_value = 0.0
    ease_in_socket.max_value = 1.0
    ease_in_socket.subtype = 'FACTOR'
    ease_in_socket.attribute_domain = 'POINT'
    ease_in_socket.default_input = 'VALUE'
    ease_in_socket.structure_type = 'AUTO'

    #Socket Ease Out
    ease_out_socket = _ee_easing__bezier_.interface.new_socket(name = "Ease Out", in_out='INPUT', socket_type = 'NodeSocketFloat')
    ease_out_socket.default_value = 0.0
    ease_out_socket.min_value = 0.0
    ease_out_socket.max_value = 1.0
    ease_out_socket.subtype = 'FACTOR'
    ease_out_socket.attribute_domain = 'POINT'
    ease_out_socket.default_input = 'VALUE'
    ease_out_socket.structure_type = 'AUTO'


    #initialize _ee_easing__bezier_ nodes
    #node Group Input
    group_input_2 = _ee_easing__bezier_.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    #node Group Output
    group_output_3 = _ee_easing__bezier_.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    #node Reroute.001
    reroute_001_2 = _ee_easing__bezier_.nodes.new("NodeReroute")
    reroute_001_2.name = "Reroute.001"
    reroute_001_2.socket_idname = "NodeSocketFloat"
    #node Bezier Segment
    bezier_segment = _ee_easing__bezier_.nodes.new("GeometryNodeCurvePrimitiveBezierSegment")
    bezier_segment.name = "Bezier Segment"
    bezier_segment.mode = 'OFFSET'
    bezier_segment.inputs[0].hide = True
    bezier_segment.inputs[1].hide = True
    bezier_segment.inputs[4].hide = True
    #Resolution
    bezier_segment.inputs[0].default_value = 1001
    #Start
    bezier_segment.inputs[1].default_value = (0.0, 0.0, 0.0)
    #End
    bezier_segment.inputs[4].default_value = (1.0, 1.0, 0.0)

    #node Resample Curve.001
    resample_curve_001 = _ee_easing__bezier_.nodes.new("GeometryNodeResampleCurve")
    resample_curve_001.name = "Resample Curve.001"
    resample_curve_001.keep_last_segment = False
    resample_curve_001.mode = 'EVALUATED'
    #Selection
    resample_curve_001.inputs[1].default_value = True

    #node Sample Curve
    sample_curve = _ee_easing__bezier_.nodes.new("GeometryNodeSampleCurve")
    sample_curve.name = "Sample Curve"
    sample_curve.data_type = 'FLOAT'
    sample_curve.mode = 'FACTOR'
    sample_curve.use_all_curves = True
    sample_curve.outputs[1].hide = True
    sample_curve.outputs[2].hide = True
    sample_curve.outputs[3].hide = True

    #node Combine XYZ.002
    combine_xyz_002 = _ee_easing__bezier_.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[1].hide = True
    combine_xyz_002.inputs[2].hide = True
    #Y
    combine_xyz_002.inputs[1].default_value = 0.0
    #Z
    combine_xyz_002.inputs[2].default_value = 0.0

    #node Combine XYZ.001
    combine_xyz_001 = _ee_easing__bezier_.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.inputs[1].hide = True
    combine_xyz_001.inputs[2].hide = True
    #Y
    combine_xyz_001.inputs[1].default_value = 0.0
    #Z
    combine_xyz_001.inputs[2].default_value = 0.0

    #node Position
    position_1 = _ee_easing__bezier_.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"

    #node Separate XYZ
    separate_xyz = _ee_easing__bezier_.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[0].hide = True
    separate_xyz.outputs[2].hide = True

    #node Mix.002
    mix_002 = _ee_easing__bezier_.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'FLOAT'
    mix_002.factor_mode = 'UNIFORM'
    #A_Float
    mix_002.inputs[2].default_value = 0.0
    #B_Float
    mix_002.inputs[3].default_value = -1.0

    #node Mix.001
    mix_001 = _ee_easing__bezier_.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'FLOAT'
    mix_001.factor_mode = 'UNIFORM'
    #A_Float
    mix_001.inputs[2].default_value = 0.0
    #B_Float
    mix_001.inputs[3].default_value = 1.0





    #Set locations
    group_input_2.location = (-512.3368530273438, 0.0)
    group_output_3.location = (532.0421142578125, 216.75790405273438)
    reroute_001_2.location = (-295.5789489746094, 39.410526275634766)
    bezier_segment.location = (-68.96841430664062, 0.0)
    resample_curve_001.location = (108.37895202636719, 0.0)
    sample_curve.location = (354.6947326660156, 216.75790405273438)
    combine_xyz_002.location = (-68.96841430664062, -237.6895751953125)
    combine_xyz_001.location = (-68.96841430664062, -139.163330078125)
    position_1.location = (108.37895202636719, -237.6895751953125)
    separate_xyz.location = (108.37895202636719, -139.163330078125)
    mix_002.location = (-256.1684265136719, -277.1001281738281)
    mix_001.location = (-256.1684265136719, -139.1632843017578)

    #Set dimensions
    group_input_2.width, group_input_2.height = 140.0, 100.0
    group_output_3.width, group_output_3.height = 140.0, 100.0
    reroute_001_2.width, reroute_001_2.height = 16.0, 100.0
    bezier_segment.width, bezier_segment.height = 140.0, 100.0
    resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
    sample_curve.width, sample_curve.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    position_1.width, position_1.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    mix_002.width, mix_002.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0

    #initialize _ee_easing__bezier_ links
    #separate_xyz.Y -> sample_curve.Value
    _ee_easing__bezier_.links.new(separate_xyz.outputs[1], sample_curve.inputs[1])
    #combine_xyz_001.Vector -> bezier_segment.Start Handle
    _ee_easing__bezier_.links.new(combine_xyz_001.outputs[0], bezier_segment.inputs[2])
    #resample_curve_001.Curve -> sample_curve.Curves
    _ee_easing__bezier_.links.new(resample_curve_001.outputs[0], sample_curve.inputs[0])
    #mix_001.Result -> combine_xyz_001.X
    _ee_easing__bezier_.links.new(mix_001.outputs[0], combine_xyz_001.inputs[0])
    #bezier_segment.Curve -> resample_curve_001.Curve
    _ee_easing__bezier_.links.new(bezier_segment.outputs[0], resample_curve_001.inputs[0])
    #reroute_001_2.Output -> sample_curve.Factor
    _ee_easing__bezier_.links.new(reroute_001_2.outputs[0], sample_curve.inputs[2])
    #position_1.Position -> separate_xyz.Vector
    _ee_easing__bezier_.links.new(position_1.outputs[0], separate_xyz.inputs[0])
    #combine_xyz_002.Vector -> bezier_segment.End Handle
    _ee_easing__bezier_.links.new(combine_xyz_002.outputs[0], bezier_segment.inputs[3])
    #group_input_2.Value -> reroute_001_2.Input
    _ee_easing__bezier_.links.new(group_input_2.outputs[0], reroute_001_2.inputs[0])
    #sample_curve.Value -> group_output_3.Value
    _ee_easing__bezier_.links.new(sample_curve.outputs[0], group_output_3.inputs[0])
    #mix_002.Result -> combine_xyz_002.X
    _ee_easing__bezier_.links.new(mix_002.outputs[0], combine_xyz_002.inputs[0])
    #group_input_2.Ease In -> mix_001.Factor
    _ee_easing__bezier_.links.new(group_input_2.outputs[1], mix_001.inputs[0])
    #group_input_2.Ease Out -> mix_002.Factor
    _ee_easing__bezier_.links.new(group_input_2.outputs[2], mix_002.inputs[0])
    return _ee_easing__bezier_

_ee_easing__bezier_ = _ee_easing__bezier__node_group()

#initialize _ee_curve_range node group
def _ee_curve_range_node_group():
    _ee_curve_range = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".EE_Curve Range")

    _ee_curve_range.color_tag = 'NONE'
    _ee_curve_range.description = ""
    _ee_curve_range.default_group_node_width = 140
    

    _ee_curve_range.is_modifier = True

    #_ee_curve_range interface
    #Socket Preview Graph
    preview_graph_socket = _ee_curve_range.interface.new_socket(name = "Preview Graph", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    preview_graph_socket.attribute_domain = 'POINT'
    preview_graph_socket.default_input = 'VALUE'
    preview_graph_socket.structure_type = 'AUTO'

    #Socket Value
    value_socket_4 = _ee_curve_range.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_4.default_value = 0.0
    value_socket_4.min_value = -3.4028234663852886e+38
    value_socket_4.max_value = 3.4028234663852886e+38
    value_socket_4.subtype = 'NONE'
    value_socket_4.attribute_domain = 'POINT'
    value_socket_4.default_input = 'VALUE'
    value_socket_4.structure_type = 'AUTO'

    #Socket Mode
    mode_socket = _ee_curve_range.interface.new_socket(name = "Mode", in_out='INPUT', socket_type = 'NodeSocketBool')
    mode_socket.default_value = False
    mode_socket.attribute_domain = 'POINT'
    mode_socket.default_input = 'VALUE'
    mode_socket.structure_type = 'AUTO'

    #Socket Position
    position_socket_1 = _ee_curve_range.interface.new_socket(name = "Position", in_out='INPUT', socket_type = 'NodeSocketFloat')
    position_socket_1.default_value = 0.5
    position_socket_1.min_value = 0.0
    position_socket_1.max_value = 1.0
    position_socket_1.subtype = 'FACTOR'
    position_socket_1.attribute_domain = 'POINT'
    position_socket_1.default_input = 'VALUE'
    position_socket_1.structure_type = 'AUTO'

    #Socket Spread
    spread_socket = _ee_curve_range.interface.new_socket(name = "Spread", in_out='INPUT', socket_type = 'NodeSocketFloat')
    spread_socket.default_value = 0.0
    spread_socket.min_value = 0.0
    spread_socket.max_value = 1.0
    spread_socket.subtype = 'FACTOR'
    spread_socket.attribute_domain = 'POINT'
    spread_socket.default_input = 'VALUE'
    spread_socket.structure_type = 'AUTO'

    #Socket Contrast
    contrast_socket_1 = _ee_curve_range.interface.new_socket(name = "Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat')
    contrast_socket_1.default_value = 0.0
    contrast_socket_1.min_value = 0.0
    contrast_socket_1.max_value = 1.0
    contrast_socket_1.subtype = 'FACTOR'
    contrast_socket_1.attribute_domain = 'POINT'
    contrast_socket_1.default_input = 'VALUE'
    contrast_socket_1.structure_type = 'AUTO'

    #Socket Ease In
    ease_in_socket_1 = _ee_curve_range.interface.new_socket(name = "Ease In", in_out='INPUT', socket_type = 'NodeSocketFloat')
    ease_in_socket_1.default_value = 0.0
    ease_in_socket_1.min_value = 0.0
    ease_in_socket_1.max_value = 1.0
    ease_in_socket_1.subtype = 'FACTOR'
    ease_in_socket_1.attribute_domain = 'POINT'
    ease_in_socket_1.default_input = 'VALUE'
    ease_in_socket_1.structure_type = 'AUTO'

    #Socket Ease Out
    ease_out_socket_1 = _ee_curve_range.interface.new_socket(name = "Ease Out", in_out='INPUT', socket_type = 'NodeSocketFloat')
    ease_out_socket_1.default_value = 0.0
    ease_out_socket_1.min_value = 0.0
    ease_out_socket_1.max_value = 1.0
    ease_out_socket_1.subtype = 'FACTOR'
    ease_out_socket_1.attribute_domain = 'POINT'
    ease_out_socket_1.default_input = 'VALUE'
    ease_out_socket_1.structure_type = 'AUTO'

    #Socket Adaptive Ease
    adaptive_ease_socket = _ee_curve_range.interface.new_socket(name = "Adaptive Ease", in_out='INPUT', socket_type = 'NodeSocketBool')
    adaptive_ease_socket.default_value = False
    adaptive_ease_socket.attribute_domain = 'POINT'
    adaptive_ease_socket.default_input = 'VALUE'
    adaptive_ease_socket.structure_type = 'AUTO'

    #Socket Min
    min_socket = _ee_curve_range.interface.new_socket(name = "Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e+38
    min_socket.max_value = 3.4028234663852886e+38
    min_socket.subtype = 'NONE'
    min_socket.attribute_domain = 'POINT'
    min_socket.default_input = 'VALUE'
    min_socket.structure_type = 'AUTO'

    #Socket Max
    max_socket = _ee_curve_range.interface.new_socket(name = "Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e+38
    max_socket.max_value = 3.4028234663852886e+38
    max_socket.subtype = 'NONE'
    max_socket.attribute_domain = 'POINT'
    max_socket.default_input = 'VALUE'
    max_socket.structure_type = 'AUTO'

    #Socket Plateau
    plateau_socket = _ee_curve_range.interface.new_socket(name = "Plateau", in_out='INPUT', socket_type = 'NodeSocketFloat')
    plateau_socket.default_value = 0.0
    plateau_socket.min_value = 0.0
    plateau_socket.max_value = 1.0
    plateau_socket.subtype = 'FACTOR'
    plateau_socket.attribute_domain = 'POINT'
    plateau_socket.default_input = 'VALUE'
    plateau_socket.structure_type = 'AUTO'


    #initialize _ee_curve_range nodes
    #node Frame
    frame = _ee_curve_range.nodes.new("NodeFrame")
    frame.label = "Preview Graph"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame.label_size = 20
    frame.shrink = True

    #node Frame.001
    frame_001 = _ee_curve_range.nodes.new("NodeFrame")
    frame_001.label = "Mode 1"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Frame.003
    frame_003 = _ee_curve_range.nodes.new("NodeFrame")
    frame_003.label = "Adaptive Contrast"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.12999999523162842, 0.12999999523162842, 0.12999999523162842)
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Frame.002
    frame_002 = _ee_curve_range.nodes.new("NodeFrame")
    frame_002.label = "Mode 2"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Switch
    switch = _ee_curve_range.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'FLOAT'

    #node Map Range.001
    map_range_001 = _ee_curve_range.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = False
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    #From Min
    map_range_001.inputs[1].default_value = 0.0
    #From Max
    map_range_001.inputs[2].default_value = 1.0

    #node Group Output
    group_output_4 = _ee_curve_range.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True

    #node Group Input.005
    group_input_005 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.use_custom_color = True
    group_input_005.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True

    #node Group Input.001
    group_input_001_2 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_001_2.name = "Group Input.001"
    group_input_001_2.use_custom_color = True
    group_input_001_2.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_001_2.outputs[1].hide = True
    group_input_001_2.outputs[2].hide = True
    group_input_001_2.outputs[3].hide = True
    group_input_001_2.outputs[4].hide = True
    group_input_001_2.outputs[5].hide = True
    group_input_001_2.outputs[6].hide = True
    group_input_001_2.outputs[7].hide = True
    group_input_001_2.outputs[8].hide = True
    group_input_001_2.outputs[9].hide = True
    group_input_001_2.outputs[10].hide = True

    #node Resample Curve
    resample_curve = _ee_curve_range.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.keep_last_segment = False
    resample_curve.mode = 'COUNT'
    resample_curve.inputs[1].hide = True
    resample_curve.inputs[2].hide = True
    resample_curve.inputs[3].hide = True
    #Selection
    resample_curve.inputs[1].default_value = True
    #Count
    resample_curve.inputs[2].default_value = 301

    #node Combine XYZ
    combine_xyz = _ee_curve_range.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.inputs[0].hide = True
    combine_xyz.inputs[2].hide = True
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Z
    combine_xyz.inputs[2].default_value = 0.0

    #node Set Position
    set_position = _ee_curve_range.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[2].hide = True
    #Selection
    set_position.inputs[1].default_value = True
    #Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Curve Line
    curve_line = _ee_curve_range.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'POINTS'
    curve_line.inputs[0].hide = True
    curve_line.inputs[1].hide = True
    curve_line.inputs[2].hide = True
    curve_line.inputs[3].hide = True
    #Start
    curve_line.inputs[0].default_value = (0.0, 0.0, 0.0)
    #End
    curve_line.inputs[1].default_value = (1.0, 0.0, 0.0)

    #node Curve to Mesh
    curve_to_mesh = _ee_curve_range.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.inputs[1].hide = True
    curve_to_mesh.inputs[3].hide = True
    #Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    #Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    #node Math.001
    math_001_1 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'ADD'
    math_001_1.use_clamp = False

    #node Mix
    mix_1 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_1.name = "Mix"
    mix_1.blend_type = 'MIX'
    mix_1.clamp_factor = True
    mix_1.clamp_result = False
    mix_1.data_type = 'FLOAT'
    mix_1.factor_mode = 'UNIFORM'
    #A_Float
    mix_1.inputs[2].default_value = 3.5
    #B_Float
    mix_1.inputs[3].default_value = -0.5

    #node Spline Parameter.001
    spline_parameter_001 = _ee_curve_range.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_001.name = "Spline Parameter.001"
    spline_parameter_001.outputs[1].hide = True
    spline_parameter_001.outputs[2].hide = True

    #node Group Input.003
    group_input_003 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.use_custom_color = True
    group_input_003.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True

    #node Group Input.009
    group_input_009 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.use_custom_color = True
    group_input_009.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True

    #node Math.002
    math_002_1 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'PINGPONG'
    math_002_1.use_clamp = False
    #Value_001
    math_002_1.inputs[1].default_value = 2.0

    #node Math.004
    math_004_2 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_004_2.name = "Math.004"
    math_004_2.operation = 'SUBTRACT'
    math_004_2.use_clamp = True
    #Value_001
    math_004_2.inputs[1].default_value = 0.5

    #node Mix.006
    mix_006 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_006.name = "Mix.006"
    mix_006.blend_type = 'MIX'
    mix_006.clamp_factor = True
    mix_006.clamp_result = False
    mix_006.data_type = 'FLOAT'
    mix_006.factor_mode = 'UNIFORM'
    #A_Float
    mix_006.inputs[2].default_value = 0.12399999797344208
    #B_Float
    mix_006.inputs[3].default_value = 0.8759999871253967

    #node Group Input.002
    group_input_002_1 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_002_1.name = "Group Input.002"
    group_input_002_1.use_custom_color = True
    group_input_002_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_002_1.outputs[0].hide = True
    group_input_002_1.outputs[2].hide = True
    group_input_002_1.outputs[3].hide = True
    group_input_002_1.outputs[4].hide = True
    group_input_002_1.outputs[5].hide = True
    group_input_002_1.outputs[6].hide = True
    group_input_002_1.outputs[7].hide = True
    group_input_002_1.outputs[8].hide = True
    group_input_002_1.outputs[9].hide = True
    group_input_002_1.outputs[10].hide = True

    #node Mix.007
    mix_007 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_007.name = "Mix.007"
    mix_007.blend_type = 'MIX'
    mix_007.clamp_factor = True
    mix_007.clamp_result = False
    mix_007.data_type = 'FLOAT'
    mix_007.factor_mode = 'UNIFORM'

    #node Group Input.008
    group_input_008 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.use_custom_color = True
    group_input_008.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[8].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True

    #node Mix.024
    mix_024 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_024.name = "Mix.024"
    mix_024.blend_type = 'MIX'
    mix_024.clamp_factor = True
    mix_024.clamp_result = False
    mix_024.data_type = 'FLOAT'
    mix_024.factor_mode = 'UNIFORM'
    #A_Float
    mix_024.inputs[2].default_value = 0.5
    #B_Float
    mix_024.inputs[3].default_value = 1.0

    #node Spline Parameter.003
    spline_parameter_003 = _ee_curve_range.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_003.name = "Spline Parameter.003"
    spline_parameter_003.outputs[1].hide = True
    spline_parameter_003.outputs[2].hide = True

    #node Math.040
    math_040 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.operation = 'ADD'
    math_040.use_clamp = False

    #node Math.037
    math_037 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.operation = 'ADD'
    math_037.use_clamp = False

    #node Math.039
    math_039 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.operation = 'ADD'
    math_039.use_clamp = False
    #Value
    math_039.inputs[0].default_value = 1.0

    #node Math.036
    math_036 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.operation = 'ADD'
    math_036.use_clamp = False
    #Value_001
    math_036.inputs[1].default_value = 0.5

    #node Map Range.002
    map_range_002 = _ee_curve_range.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.clamp = True
    map_range_002.data_type = 'FLOAT'
    map_range_002.interpolation_type = 'LINEAR'
    #From Max
    map_range_002.inputs[2].default_value = 1.0
    #To Min
    map_range_002.inputs[3].default_value = 0.0
    #To Max
    map_range_002.inputs[4].default_value = 1.0

    #node Mix.021
    mix_021 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_021.name = "Mix.021"
    mix_021.blend_type = 'MIX'
    mix_021.clamp_factor = True
    mix_021.clamp_result = False
    mix_021.data_type = 'FLOAT'
    mix_021.factor_mode = 'UNIFORM'
    #A_Float
    mix_021.inputs[2].default_value = 0.0
    #B_Float
    mix_021.inputs[3].default_value = 0.5

    #node Mix.022
    mix_022 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_022.name = "Mix.022"
    mix_022.blend_type = 'MIX'
    mix_022.clamp_factor = True
    mix_022.clamp_result = False
    mix_022.data_type = 'FLOAT'
    mix_022.factor_mode = 'UNIFORM'

    #node Mix.025
    mix_025 = _ee_curve_range.nodes.new("ShaderNodeMix")
    mix_025.name = "Mix.025"
    mix_025.blend_type = 'MIX'
    mix_025.clamp_factor = True
    mix_025.clamp_result = False
    mix_025.data_type = 'FLOAT'
    mix_025.factor_mode = 'UNIFORM'
    #A_Float
    mix_025.inputs[2].default_value = -0.5
    #B_Float
    mix_025.inputs[3].default_value = -1.0

    #node Group Input.013
    group_input_013 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.use_custom_color = True
    group_input_013.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[2].hide = True
    group_input_013.outputs[3].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True

    #node Group Input.014
    group_input_014 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.use_custom_color = True
    group_input_014.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[2].hide = True
    group_input_014.outputs[3].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[7].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[10].hide = True

    #node Group Input.017
    group_input_017 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_017.name = "Group Input.017"
    group_input_017.use_custom_color = True
    group_input_017.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_017.outputs[0].hide = True
    group_input_017.outputs[1].hide = True
    group_input_017.outputs[2].hide = True
    group_input_017.outputs[3].hide = True
    group_input_017.outputs[6].hide = True
    group_input_017.outputs[7].hide = True
    group_input_017.outputs[8].hide = True
    group_input_017.outputs[9].hide = True
    group_input_017.outputs[10].hide = True

    #node Math.041
    math_041 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_041.name = "Math.041"
    math_041.operation = 'MULTIPLY'
    math_041.use_clamp = False

    #node Group Input.016
    group_input_016 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_016.name = "Group Input.016"
    group_input_016.use_custom_color = True
    group_input_016.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_016.outputs[0].hide = True
    group_input_016.outputs[1].hide = True
    group_input_016.outputs[2].hide = True
    group_input_016.outputs[4].hide = True
    group_input_016.outputs[5].hide = True
    group_input_016.outputs[6].hide = True
    group_input_016.outputs[7].hide = True
    group_input_016.outputs[8].hide = True
    group_input_016.outputs[9].hide = True
    group_input_016.outputs[10].hide = True

    #node Float Curve.003
    float_curve_003 = _ee_curve_range.nodes.new("ShaderNodeFloatCurve")
    float_curve_003.name = "Float Curve.003"
    #mapping settings
    float_curve_003.mapping.extend = 'EXTRAPOLATED'
    float_curve_003.mapping.tone = 'STANDARD'
    float_curve_003.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_003.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_003.mapping.clip_min_x = 0.0
    float_curve_003.mapping.clip_min_y = 0.0
    float_curve_003.mapping.clip_max_x = 1.0
    float_curve_003.mapping.clip_max_y = 1.0
    float_curve_003.mapping.use_clip = True
    #curve 0
    float_curve_003_curve_0 = float_curve_003.mapping.curves[0]
    float_curve_003_curve_0_point_0 = float_curve_003_curve_0.points[0]
    float_curve_003_curve_0_point_0.location = (0.0, 0.0)
    float_curve_003_curve_0_point_0.handle_type = 'AUTO'
    float_curve_003_curve_0_point_1 = float_curve_003_curve_0.points[1]
    float_curve_003_curve_0_point_1.location = (0.5, 0.5)
    float_curve_003_curve_0_point_1.handle_type = 'VECTOR'
    float_curve_003_curve_0_point_2 = float_curve_003_curve_0.points.new(1.0, 0.9800000190734863)
    float_curve_003_curve_0_point_2.handle_type = 'AUTO'
    #update curve after changes
    float_curve_003.mapping.update()
    #Factor
    float_curve_003.inputs[0].default_value = 1.0

    #node Switch.022
    switch_022 = _ee_curve_range.nodes.new("GeometryNodeSwitch")
    switch_022.name = "Switch.022"
    switch_022.input_type = 'FLOAT'
    #False
    switch_022.inputs[1].default_value = 1.0

    #node Group Input.015
    group_input_015 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_015.name = "Group Input.015"
    group_input_015.use_custom_color = True
    group_input_015.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_015.outputs[0].hide = True
    group_input_015.outputs[1].hide = True
    group_input_015.outputs[3].hide = True
    group_input_015.outputs[4].hide = True
    group_input_015.outputs[5].hide = True
    group_input_015.outputs[7].hide = True
    group_input_015.outputs[8].hide = True
    group_input_015.outputs[9].hide = True
    group_input_015.outputs[10].hide = True

    #node Float Curve.002
    float_curve_002 = _ee_curve_range.nodes.new("ShaderNodeFloatCurve")
    float_curve_002.name = "Float Curve.002"
    #mapping settings
    float_curve_002.mapping.extend = 'EXTRAPOLATED'
    float_curve_002.mapping.tone = 'STANDARD'
    float_curve_002.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_002.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_002.mapping.clip_min_x = 0.0
    float_curve_002.mapping.clip_min_y = 0.0
    float_curve_002.mapping.clip_max_x = 1.0
    float_curve_002.mapping.clip_max_y = 1.0
    float_curve_002.mapping.use_clip = True
    #curve 0
    float_curve_002_curve_0 = float_curve_002.mapping.curves[0]
    float_curve_002_curve_0_point_0 = float_curve_002_curve_0.points[0]
    float_curve_002_curve_0_point_0.location = (0.0, 0.0)
    float_curve_002_curve_0_point_0.handle_type = 'AUTO'
    float_curve_002_curve_0_point_1 = float_curve_002_curve_0.points[1]
    float_curve_002_curve_0_point_1.location = (0.25, 1.0)
    float_curve_002_curve_0_point_1.handle_type = 'AUTO_CLAMPED'
    float_curve_002_curve_0_point_2 = float_curve_002_curve_0.points.new(0.75, 1.0)
    float_curve_002_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
    float_curve_002_curve_0_point_3 = float_curve_002_curve_0.points.new(1.0, 0.0)
    float_curve_002_curve_0_point_3.handle_type = 'AUTO'
    #update curve after changes
    float_curve_002.mapping.update()
    #Factor
    float_curve_002.inputs[0].default_value = 1.0

    #node Group Input.012
    group_input_012 = _ee_curve_range.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.use_custom_color = True
    group_input_012.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True

    #node Math.035
    math_035 = _ee_curve_range.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.operation = 'PINGPONG'
    math_035.use_clamp = True

    #node Group.002
    group_002 = _ee_curve_range.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = _ee_contrast

    #node Group.003
    group_003 = _ee_curve_range.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = _ee_easing__bezier_

    #node Group.065
    group_065 = _ee_curve_range.nodes.new("GeometryNodeGroup")
    group_065.name = "Group.065"
    group_065.node_tree = _ee_contrast

    #node Group.063
    group_063 = _ee_curve_range.nodes.new("GeometryNodeGroup")
    group_063.name = "Group.063"
    group_063.node_tree = _ee_easing__bezier_




    #Set parents
    frame_003.parent = frame_001
    resample_curve.parent = frame
    combine_xyz.parent = frame
    set_position.parent = frame
    curve_line.parent = frame
    curve_to_mesh.parent = frame
    math_001_1.parent = frame_001
    mix_1.parent = frame_001
    spline_parameter_001.parent = frame_001
    group_input_003.parent = frame_001
    group_input_009.parent = frame_001
    math_002_1.parent = frame_001
    math_004_2.parent = frame_001
    mix_006.parent = frame_003
    group_input_002_1.parent = frame_003
    mix_007.parent = frame_003
    group_input_008.parent = frame_003
    mix_024.parent = frame_002
    spline_parameter_003.parent = frame_002
    math_040.parent = frame_002
    math_037.parent = frame_002
    math_039.parent = frame_002
    math_036.parent = frame_002
    map_range_002.parent = frame_002
    mix_021.parent = frame_002
    mix_022.parent = frame_002
    mix_025.parent = frame_002
    group_input_013.parent = frame_002
    group_input_014.parent = frame_002
    group_input_017.parent = frame_002
    math_041.parent = frame_002
    group_input_016.parent = frame_002
    float_curve_003.parent = frame_002
    switch_022.parent = frame_002
    group_input_015.parent = frame_002
    float_curve_002.parent = frame_002
    group_input_012.parent = frame_002
    math_035.parent = frame_002
    group_002.parent = frame_001
    group_003.parent = frame_001
    group_065.parent = frame_002
    group_063.parent = frame_002

    #Set locations
    frame.location = (1110.5806884765625, 225.3225860595703)
    frame_001.location = (-1246.45166015625, 510.225830078125)
    frame_003.location = (29.0322265625, -41.032257080078125)
    frame_002.location = (-1374.5806884765625, 113.06451416015625)
    switch.location = (729.0947265625, 295.5789489746094)
    map_range_001.location = (906.442138671875, 295.5789489746094)
    group_output_4.location = (1911.6329345703125, 317.9295959472656)
    group_input_005.location = (729.0947265625, 118.23158264160156)
    group_input_001_2.location = (729.0970458984375, 363.0343017578125)
    resample_curve.location = (210.1767578125, -139.77001953125)
    combine_xyz.location = (210.1767578125, -39.30488586425781)
    set_position.location = (391.013916015625, -39.30488586425781)
    curve_line.location = (29.3394775390625, -139.77001953125)
    curve_to_mesh.location = (571.8511962890625, -39.30488586425781)
    math_001_1.location = (820.629638671875, -98.678955078125)
    mix_1.location = (620.7021484375, -102.37332153320312)
    spline_parameter_001.location = (621.7346801757812, -39.563140869140625)
    group_input_003.location = (1412.5858154296875, -207.89175415039062)
    group_input_009.location = (1215.8358154296875, -252.14273071289062)
    math_002_1.location = (1017.6823120117188, -94.80465698242188)
    math_004_2.location = (1214.7349853515625, -92.47665405273438)
    mix_006.location = (215.2574462890625, -144.57418823242188)
    group_input_002_1.location = (28.801513671875, -88.72442626953125)
    mix_007.location = (394.57635498046875, -39.737823486328125)
    group_input_008.location = (215.32421875, -41.585205078125)
    mix_024.location = (247.9866943359375, -242.6783447265625)
    spline_parameter_003.location = (429.78704833984375, -39.23883056640625)
    math_040.location = (606.6658325195312, -39.41949462890625)
    math_037.location = (784.3739013671875, -72.5040283203125)
    math_039.location = (785.2219848632812, -183.23931884765625)
    math_036.location = (960.505859375, -74.11383056640625)
    map_range_002.location = (1334.2510986328125, -90.5010986328125)
    mix_021.location = (431.94049072265625, -319.3843994140625)
    mix_022.location = (429.631591796875, -107.209716796875)
    mix_025.location = (250.3768310546875, -110.39666748046875)
    group_input_013.location = (250.4478759765625, -41.59185791015625)
    group_input_014.location = (28.6834716796875, -345.5286865234375)
    group_input_017.location = (1337.232421875, -344.9959716796875)
    math_041.location = (1559.50537109375, -419.2152099609375)
    group_input_016.location = (1740.8759765625, -370.3109130859375)
    float_curve_003.location = (1041.70458984375, -253.933837890625)
    switch_022.location = (1042.4910888671875, -604.5072021484375)
    group_input_015.location = (854.863037109375, -513.1708984375)
    float_curve_002.location = (756.4918212890625, -605.359375)
    group_input_012.location = (561.212890625, -864.582763671875)
    math_035.location = (1145.393798828125, -89.1983642578125)
    group_002.location = (1411.78759765625, -92.47665405273438)
    group_003.location = (1608.8402099609375, -92.47665405273438)
    group_065.location = (1739.3172607421875, -256.9854736328125)
    group_063.location = (1560.3048095703125, -257.5050048828125)

    #Set dimensions
    frame.width, frame.height = 740.774169921875, 265.9677429199219
    frame_001.width, frame_001.height = 1777.8065185546875, 363.90325927734375
    frame_003.width, frame_003.height = 563.48388671875, 293.8387451171875
    frame_002.width, frame_002.height = 1909.8065185546875, 943.3870849609375
    switch.width, switch.height = 140.0, 100.0
    map_range_001.width, map_range_001.height = 140.0, 100.0
    group_output_4.width, group_output_4.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    mix_1.width, mix_1.height = 140.0, 100.0
    spline_parameter_001.width, spline_parameter_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    math_004_2.width, math_004_2.height = 140.0, 100.0
    mix_006.width, mix_006.height = 140.0, 100.0
    group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
    mix_007.width, mix_007.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    mix_024.width, mix_024.height = 140.0, 100.0
    spline_parameter_003.width, spline_parameter_003.height = 140.0, 100.0
    math_040.width, math_040.height = 140.0, 100.0
    math_037.width, math_037.height = 140.0, 100.0
    math_039.width, math_039.height = 140.0, 100.0
    math_036.width, math_036.height = 140.0, 100.0
    map_range_002.width, map_range_002.height = 140.0, 100.0
    mix_021.width, mix_021.height = 140.0, 100.0
    mix_022.width, mix_022.height = 140.0, 100.0
    mix_025.width, mix_025.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    math_041.width, math_041.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    float_curve_003.width, float_curve_003.height = 240.0, 100.0
    switch_022.width, switch_022.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    float_curve_002.width, float_curve_002.height = 240.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    math_035.width, math_035.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    group_003.width, group_003.height = 140.0, 100.0
    group_065.width, group_065.height = 140.0, 100.0
    group_063.width, group_063.height = 140.0, 100.0

    #initialize _ee_curve_range links
    #math_004_2.Value -> group_002.Value
    _ee_curve_range.links.new(math_004_2.outputs[0], group_002.inputs[0])
    #spline_parameter_001.Factor -> math_001_1.Value
    _ee_curve_range.links.new(spline_parameter_001.outputs[0], math_001_1.inputs[0])
    #math_001_1.Value -> math_002_1.Value
    _ee_curve_range.links.new(math_001_1.outputs[0], math_002_1.inputs[0])
    #group_002.Value -> group_003.Value
    _ee_curve_range.links.new(group_002.outputs[0], group_003.inputs[0])
    #math_002_1.Value -> math_004_2.Value
    _ee_curve_range.links.new(math_002_1.outputs[0], math_004_2.inputs[0])
    #group_003.Value -> switch.False
    _ee_curve_range.links.new(group_003.outputs[0], switch.inputs[1])
    #map_range_001.Result -> group_output_4.Value
    _ee_curve_range.links.new(map_range_001.outputs[0], group_output_4.inputs[1])
    #group_input_001_2.Mode -> switch.Switch
    _ee_curve_range.links.new(group_input_001_2.outputs[0], switch.inputs[0])
    #group_input_003.Ease Out -> group_003.Ease Out
    _ee_curve_range.links.new(group_input_003.outputs[5], group_003.inputs[2])
    #group_input_003.Ease In -> group_003.Ease In
    _ee_curve_range.links.new(group_input_003.outputs[4], group_003.inputs[1])
    #switch.Output -> map_range_001.Value
    _ee_curve_range.links.new(switch.outputs[0], map_range_001.inputs[0])
    #group_input_005.Min -> map_range_001.To Min
    _ee_curve_range.links.new(group_input_005.outputs[7], map_range_001.inputs[3])
    #group_input_005.Max -> map_range_001.To Max
    _ee_curve_range.links.new(group_input_005.outputs[8], map_range_001.inputs[4])
    #set_position.Geometry -> curve_to_mesh.Curve
    _ee_curve_range.links.new(set_position.outputs[0], curve_to_mesh.inputs[0])
    #curve_line.Curve -> resample_curve.Curve
    _ee_curve_range.links.new(curve_line.outputs[0], resample_curve.inputs[0])
    #resample_curve.Curve -> set_position.Geometry
    _ee_curve_range.links.new(resample_curve.outputs[0], set_position.inputs[0])
    #combine_xyz.Vector -> set_position.Offset
    _ee_curve_range.links.new(combine_xyz.outputs[0], set_position.inputs[3])
    #map_range_001.Result -> combine_xyz.Y
    _ee_curve_range.links.new(map_range_001.outputs[0], combine_xyz.inputs[1])
    #curve_to_mesh.Mesh -> group_output_4.Preview Graph
    _ee_curve_range.links.new(curve_to_mesh.outputs[0], group_output_4.inputs[0])
    #group_input_009.Contrast -> group_002.Contrast
    _ee_curve_range.links.new(group_input_009.outputs[3], group_002.inputs[1])
    #math_036.Value -> math_035.Value
    _ee_curve_range.links.new(math_036.outputs[0], math_035.inputs[0])
    #math_037.Value -> math_036.Value
    _ee_curve_range.links.new(math_037.outputs[0], math_036.inputs[0])
    #math_040.Value -> math_037.Value
    _ee_curve_range.links.new(math_040.outputs[0], math_037.inputs[0])
    #mix_021.Result -> math_037.Value
    _ee_curve_range.links.new(mix_021.outputs[0], math_037.inputs[1])
    #mix_021.Result -> math_039.Value
    _ee_curve_range.links.new(mix_021.outputs[0], math_039.inputs[1])
    #math_039.Value -> math_035.Value
    _ee_curve_range.links.new(math_039.outputs[0], math_035.inputs[1])
    #spline_parameter_003.Factor -> math_040.Value
    _ee_curve_range.links.new(spline_parameter_003.outputs[0], math_040.inputs[0])
    #mix_022.Result -> math_040.Value
    _ee_curve_range.links.new(mix_022.outputs[0], math_040.inputs[1])
    #group_input_014.Plateau -> mix_021.Factor
    _ee_curve_range.links.new(group_input_014.outputs[9], mix_021.inputs[0])
    #group_input_014.Plateau -> mix_024.Factor
    _ee_curve_range.links.new(group_input_014.outputs[9], mix_024.inputs[0])
    #group_input_014.Plateau -> mix_025.Factor
    _ee_curve_range.links.new(group_input_014.outputs[9], mix_025.inputs[0])
    #map_range_002.Result -> group_063.Value
    _ee_curve_range.links.new(map_range_002.outputs[0], group_063.inputs[0])
    #math_035.Value -> map_range_002.Value
    _ee_curve_range.links.new(math_035.outputs[0], map_range_002.inputs[0])
    #mix_025.Result -> mix_022.B
    _ee_curve_range.links.new(mix_025.outputs[0], mix_022.inputs[3])
    #mix_024.Result -> mix_022.A
    _ee_curve_range.links.new(mix_024.outputs[0], mix_022.inputs[2])
    #math_041.Value -> group_063.Ease Out
    _ee_curve_range.links.new(math_041.outputs[0], group_063.inputs[2])
    #group_063.Value -> group_065.Value
    _ee_curve_range.links.new(group_063.outputs[0], group_065.inputs[0])
    #float_curve_002.Value -> switch_022.True
    _ee_curve_range.links.new(float_curve_002.outputs[0], switch_022.inputs[2])
    #switch_022.Output -> math_041.Value
    _ee_curve_range.links.new(switch_022.outputs[0], math_041.inputs[1])
    #group_input_012.Position -> float_curve_002.Value
    _ee_curve_range.links.new(group_input_012.outputs[1], float_curve_002.inputs[1])
    #group_input_013.Position -> mix_022.Factor
    _ee_curve_range.links.new(group_input_013.outputs[1], mix_022.inputs[0])
    #group_input_017.Ease Out -> math_041.Value
    _ee_curve_range.links.new(group_input_017.outputs[5], math_041.inputs[0])
    #group_input_017.Ease In -> group_063.Ease In
    _ee_curve_range.links.new(group_input_017.outputs[4], group_063.inputs[1])
    #group_input_016.Contrast -> group_065.Contrast
    _ee_curve_range.links.new(group_input_016.outputs[3], group_065.inputs[1])
    #group_input_015.Adaptive Ease -> switch_022.Switch
    _ee_curve_range.links.new(group_input_015.outputs[6], switch_022.inputs[0])
    #group_065.Value -> switch.True
    _ee_curve_range.links.new(group_065.outputs[0], switch.inputs[2])
    #float_curve_003.Value -> map_range_002.From Min
    _ee_curve_range.links.new(float_curve_003.outputs[0], map_range_002.inputs[1])
    #group_input_015.Spread -> float_curve_003.Value
    _ee_curve_range.links.new(group_input_015.outputs[2], float_curve_003.inputs[1])
    #mix_1.Result -> math_001_1.Value
    _ee_curve_range.links.new(mix_1.outputs[0], math_001_1.inputs[1])
    #group_input_002_1.Position -> mix_006.Factor
    _ee_curve_range.links.new(group_input_002_1.outputs[1], mix_006.inputs[0])
    #mix_006.Result -> mix_007.B
    _ee_curve_range.links.new(mix_006.outputs[0], mix_007.inputs[3])
    #group_input_002_1.Position -> mix_007.A
    _ee_curve_range.links.new(group_input_002_1.outputs[1], mix_007.inputs[2])
    #group_input_008.Contrast -> mix_007.Factor
    _ee_curve_range.links.new(group_input_008.outputs[3], mix_007.inputs[0])
    #mix_007.Result -> mix_1.Factor
    _ee_curve_range.links.new(mix_007.outputs[0], mix_1.inputs[0])
    return _ee_curve_range

_ee_curve_range = _ee_curve_range_node_group()

#initialize _ee_randomize_control node group
def _ee_randomize_control_node_group():
    _ee_randomize_control = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = ".EE_Randomize Control")

    _ee_randomize_control.color_tag = 'NONE'
    _ee_randomize_control.description = ""
    _ee_randomize_control.default_group_node_width = 140
    


    #_ee_randomize_control interface
    #Socket Value
    value_socket_5 = _ee_randomize_control.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_5.default_value = 0.0
    value_socket_5.min_value = -3.4028234663852886e+38
    value_socket_5.max_value = 3.4028234663852886e+38
    value_socket_5.subtype = 'NONE'
    value_socket_5.attribute_domain = 'POINT'
    value_socket_5.default_input = 'VALUE'
    value_socket_5.structure_type = 'AUTO'

    #Socket Control
    control_socket = _ee_randomize_control.interface.new_socket(name = "Control", in_out='INPUT', socket_type = 'NodeSocketFloat')
    control_socket.default_value = 0.0
    control_socket.min_value = -3.4028234663852886e+38
    control_socket.max_value = 3.4028234663852886e+38
    control_socket.subtype = 'NONE'
    control_socket.attribute_domain = 'POINT'
    control_socket.hide_value = True
    control_socket.default_input = 'VALUE'
    control_socket.structure_type = 'AUTO'

    #Socket Factor
    factor_socket = _ee_randomize_control.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
    factor_socket.default_value = 0.0
    factor_socket.min_value = 0.0
    factor_socket.max_value = 1.0
    factor_socket.subtype = 'FACTOR'
    factor_socket.attribute_domain = 'POINT'
    factor_socket.default_input = 'VALUE'
    factor_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = _ee_randomize_control.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -10000.0
    scale_socket.max_value = 10000.0
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Panel Random Settings
    random_settings_panel = _ee_randomize_control.interface.new_panel("Random Settings")
    #Socket Min
    min_socket_1 = _ee_randomize_control.interface.new_socket(name = "Min", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = random_settings_panel)
    min_socket_1.default_value = 0.5
    min_socket_1.min_value = -3.4028234663852886e+38
    min_socket_1.max_value = 3.4028234663852886e+38
    min_socket_1.subtype = 'NONE'
    min_socket_1.attribute_domain = 'POINT'
    min_socket_1.default_input = 'VALUE'
    min_socket_1.structure_type = 'AUTO'

    #Socket Max
    max_socket_1 = _ee_randomize_control.interface.new_socket(name = "Max", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = random_settings_panel)
    max_socket_1.default_value = 2.0
    max_socket_1.min_value = -3.4028234663852886e+38
    max_socket_1.max_value = 3.4028234663852886e+38
    max_socket_1.subtype = 'NONE'
    max_socket_1.attribute_domain = 'POINT'
    max_socket_1.default_input = 'VALUE'
    max_socket_1.structure_type = 'AUTO'

    #Socket ID
    id_socket = _ee_randomize_control.interface.new_socket(name = "ID", in_out='INPUT', socket_type = 'NodeSocketInt', parent = random_settings_panel)
    id_socket.default_value = 0
    id_socket.min_value = -2147483648
    id_socket.max_value = 2147483647
    id_socket.subtype = 'NONE'
    id_socket.attribute_domain = 'POINT'
    id_socket.hide_value = True
    id_socket.default_input = 'VALUE'
    id_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket = _ee_randomize_control.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt', parent = random_settings_panel)
    seed_socket.default_value = 0
    seed_socket.min_value = -10000
    seed_socket.max_value = 10000
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'



    #initialize _ee_randomize_control nodes
    #node Math.003
    math_003_1 = _ee_randomize_control.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'MULTIPLY'
    math_003_1.use_clamp = False

    #node Group Output
    group_output_5 = _ee_randomize_control.nodes.new("NodeGroupOutput")
    group_output_5.name = "Group Output"
    group_output_5.is_active_output = True

    #node Mix.001
    mix_001_1 = _ee_randomize_control.nodes.new("ShaderNodeMix")
    mix_001_1.name = "Mix.001"
    mix_001_1.blend_type = 'MIX'
    mix_001_1.clamp_factor = True
    mix_001_1.clamp_result = False
    mix_001_1.data_type = 'FLOAT'
    mix_001_1.factor_mode = 'UNIFORM'

    #node Group Input.003
    group_input_003_1 = _ee_randomize_control.nodes.new("NodeGroupInput")
    group_input_003_1.name = "Group Input.003"
    group_input_003_1.use_custom_color = True
    group_input_003_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_003_1.outputs[0].hide = True
    group_input_003_1.outputs[2].hide = True
    group_input_003_1.outputs[3].hide = True
    group_input_003_1.outputs[4].hide = True
    group_input_003_1.outputs[5].hide = True
    group_input_003_1.outputs[6].hide = True
    group_input_003_1.outputs[7].hide = True

    #node Random Value.001
    random_value_001 = _ee_randomize_control.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'

    #node Math.002
    math_002_2 = _ee_randomize_control.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = 'MULTIPLY'
    math_002_2.use_clamp = False

    #node Group Input
    group_input_3 = _ee_randomize_control.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    group_input_3.use_custom_color = True
    group_input_3.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_3.outputs[1].hide = True
    group_input_3.outputs[2].hide = True
    group_input_3.outputs[3].hide = True
    group_input_3.outputs[4].hide = True
    group_input_3.outputs[5].hide = True
    group_input_3.outputs[6].hide = True
    group_input_3.outputs[7].hide = True

    #node Group Input.002
    group_input_002_2 = _ee_randomize_control.nodes.new("NodeGroupInput")
    group_input_002_2.name = "Group Input.002"
    group_input_002_2.use_custom_color = True
    group_input_002_2.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_002_2.outputs[0].hide = True
    group_input_002_2.outputs[1].hide = True
    group_input_002_2.outputs[3].hide = True
    group_input_002_2.outputs[4].hide = True
    group_input_002_2.outputs[5].hide = True
    group_input_002_2.outputs[6].hide = True
    group_input_002_2.outputs[7].hide = True

    #node Switch
    switch_1 = _ee_randomize_control.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = 'INT'

    #node Compare
    compare = _ee_randomize_control.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    #B_INT
    compare.inputs[3].default_value = 0

    #node ID
    id = _ee_randomize_control.nodes.new("GeometryNodeInputID")
    id.name = "ID"

    #node Reroute
    reroute_2 = _ee_randomize_control.nodes.new("NodeReroute")
    reroute_2.name = "Reroute"
    reroute_2.socket_idname = "NodeSocketInt"
    #node Group Input.001
    group_input_001_3 = _ee_randomize_control.nodes.new("NodeGroupInput")
    group_input_001_3.name = "Group Input.001"
    group_input_001_3.use_custom_color = True
    group_input_001_3.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_001_3.outputs[0].hide = True
    group_input_001_3.outputs[1].hide = True
    group_input_001_3.outputs[2].hide = True
    group_input_001_3.outputs[7].hide = True





    #Set locations
    math_003_1.location = (182.72854614257812, 97.08526611328125)
    group_output_5.location = (368.1084289550781, 95.34272766113281)
    mix_001_1.location = (-0.392120361328125, 94.4000244140625)
    group_input_003_1.location = (-182.34811401367188, 91.94091796875)
    random_value_001.location = (-365.024658203125, -74.62814331054688)
    math_002_2.location = (-184.3707275390625, -9.548917770385742)
    group_input_3.location = (-364.6441955566406, 46.44089889526367)
    group_input_002_2.location = (-1.8834583759307861, -36.6181640625)
    switch_1.location = (-549.7769775390625, -246.8330078125)
    compare.location = (-754.4105834960938, -273.2488098144531)
    id.location = (-755.3836669921875, -377.19097900390625)
    reroute_2.location = (-621.9249267578125, -199.2754364013672)
    group_input_001_3.location = (-963.0563354492188, -123.60503387451172)

    #Set dimensions
    math_003_1.width, math_003_1.height = 140.0, 100.0
    group_output_5.width, group_output_5.height = 140.0, 100.0
    mix_001_1.width, mix_001_1.height = 140.0, 100.0
    group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    math_002_2.width, math_002_2.height = 140.0, 100.0
    group_input_3.width, group_input_3.height = 140.0, 100.0
    group_input_002_2.width, group_input_002_2.height = 140.0, 100.0
    switch_1.width, switch_1.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    id.width, id.height = 140.0, 100.0
    reroute_2.width, reroute_2.height = 16.0, 100.0
    group_input_001_3.width, group_input_001_3.height = 140.0, 100.0

    #initialize _ee_randomize_control links
    #group_input_3.Control -> mix_001_1.A
    _ee_randomize_control.links.new(group_input_3.outputs[0], mix_001_1.inputs[2])
    #group_input_3.Control -> math_002_2.Value
    _ee_randomize_control.links.new(group_input_3.outputs[0], math_002_2.inputs[0])
    #random_value_001.Value -> math_002_2.Value
    _ee_randomize_control.links.new(random_value_001.outputs[1], math_002_2.inputs[1])
    #math_002_2.Value -> mix_001_1.B
    _ee_randomize_control.links.new(math_002_2.outputs[0], mix_001_1.inputs[3])
    #mix_001_1.Result -> math_003_1.Value
    _ee_randomize_control.links.new(mix_001_1.outputs[0], math_003_1.inputs[0])
    #math_003_1.Value -> group_output_5.Value
    _ee_randomize_control.links.new(math_003_1.outputs[0], group_output_5.inputs[0])
    #group_input_001_3.Min -> random_value_001.Min
    _ee_randomize_control.links.new(group_input_001_3.outputs[3], random_value_001.inputs[2])
    #group_input_001_3.Max -> random_value_001.Max
    _ee_randomize_control.links.new(group_input_001_3.outputs[4], random_value_001.inputs[3])
    #group_input_001_3.Seed -> random_value_001.Seed
    _ee_randomize_control.links.new(group_input_001_3.outputs[6], random_value_001.inputs[8])
    #group_input_002_2.Scale -> math_003_1.Value
    _ee_randomize_control.links.new(group_input_002_2.outputs[2], math_003_1.inputs[1])
    #group_input_003_1.Factor -> mix_001_1.Factor
    _ee_randomize_control.links.new(group_input_003_1.outputs[1], mix_001_1.inputs[0])
    #group_input_001_3.ID -> compare.A
    _ee_randomize_control.links.new(group_input_001_3.outputs[5], compare.inputs[2])
    #compare.Result -> switch_1.Switch
    _ee_randomize_control.links.new(compare.outputs[0], switch_1.inputs[0])
    #id.ID -> switch_1.True
    _ee_randomize_control.links.new(id.outputs[0], switch_1.inputs[2])
    #reroute_2.Output -> switch_1.False
    _ee_randomize_control.links.new(reroute_2.outputs[0], switch_1.inputs[1])
    #switch_1.Output -> random_value_001.ID
    _ee_randomize_control.links.new(switch_1.outputs[0], random_value_001.inputs[7])
    #group_input_001_3.ID -> reroute_2.Input
    _ee_randomize_control.links.new(group_input_001_3.outputs[5], reroute_2.inputs[0])
    return _ee_randomize_control

_ee_randomize_control = _ee_randomize_control_node_group()

#initialize eyelashgen node group
def eyelashgen_node_group():
    eyelashgen = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "EyelashGen")

    eyelashgen.color_tag = 'NONE'
    eyelashgen.description = ""
    eyelashgen.default_group_node_width = 140
    

    eyelashgen.is_modifier = True

    #eyelashgen interface
    #Socket Geometry
    geometry_socket_2 = eyelashgen.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_2.attribute_domain = 'POINT'
    geometry_socket_2.default_input = 'VALUE'
    geometry_socket_2.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_3 = eyelashgen.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_3.attribute_domain = 'POINT'
    geometry_socket_3.default_input = 'VALUE'
    geometry_socket_3.structure_type = 'AUTO'

    #Socket Face Mesh
    face_mesh_socket = eyelashgen.interface.new_socket(name = "Face Mesh", in_out='INPUT', socket_type = 'NodeSocketObject')
    face_mesh_socket.attribute_domain = 'POINT'
    face_mesh_socket.description = "Select the face mesh of your character"
    face_mesh_socket.default_input = 'VALUE'
    face_mesh_socket.structure_type = 'AUTO'

    #Socket Material
    material_socket = eyelashgen.interface.new_socket(name = "Material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.description = "Set the material for the Eyelashes"
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    #Socket Count
    count_socket = eyelashgen.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
    count_socket.default_value = 80
    count_socket.min_value = 2
    count_socket.max_value = 100000
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'
    count_socket.description = "Total number of hairs (at Max density)"
    count_socket.default_input = 'VALUE'
    count_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket_1 = eyelashgen.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = -10000
    seed_socket_1.max_value = 10000
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.description = "Variation seed for the geometry"
    seed_socket_1.default_input = 'VALUE'
    seed_socket_1.structure_type = 'AUTO'

    #Socket Spread
    spread_socket_1 = eyelashgen.interface.new_socket(name = "Spread", in_out='INPUT', socket_type = 'NodeSocketFloat')
    spread_socket_1.default_value = 0.0
    spread_socket_1.min_value = 0.0
    spread_socket_1.max_value = 10000.0
    spread_socket_1.subtype = 'NONE'
    spread_socket_1.attribute_domain = 'POINT'
    spread_socket_1.description = "Spread the hairs around the guide curve (mesh line)"
    spread_socket_1.default_input = 'VALUE'
    spread_socket_1.structure_type = 'AUTO'

    #Socket Clump
    clump_socket = eyelashgen.interface.new_socket(name = "Clump", in_out='INPUT', socket_type = 'NodeSocketFloat')
    clump_socket.default_value = 0.0
    clump_socket.min_value = 0.0
    clump_socket.max_value = 1.0
    clump_socket.subtype = 'FACTOR'
    clump_socket.default_attribute_name = "Bend the hairs to clump them"
    clump_socket.attribute_domain = 'POINT'
    clump_socket.default_input = 'VALUE'
    clump_socket.structure_type = 'AUTO'

    #Socket Length 1
    length_1_socket = eyelashgen.interface.new_socket(name = "Length 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    length_1_socket.default_value = 1.0
    length_1_socket.min_value = 0.0
    length_1_socket.max_value = 1000.0
    length_1_socket.subtype = 'NONE'
    length_1_socket.attribute_domain = 'POINT'
    length_1_socket.description = "Length of the hairs (Side 1)"
    length_1_socket.default_input = 'VALUE'
    length_1_socket.structure_type = 'AUTO'

    #Socket Length 2
    length_2_socket = eyelashgen.interface.new_socket(name = "Length 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    length_2_socket.default_value = 1.0
    length_2_socket.min_value = 0.0
    length_2_socket.max_value = 1000.0
    length_2_socket.subtype = 'NONE'
    length_2_socket.attribute_domain = 'POINT'
    length_2_socket.description = "Length of the hairs (Side 2)"
    length_2_socket.default_input = 'VALUE'
    length_2_socket.structure_type = 'AUTO'

    #Socket Thickness 1
    thickness_1_socket = eyelashgen.interface.new_socket(name = "Thickness 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    thickness_1_socket.default_value = 1.0
    thickness_1_socket.min_value = 0.0
    thickness_1_socket.max_value = 10000.0
    thickness_1_socket.subtype = 'NONE'
    thickness_1_socket.attribute_domain = 'POINT'
    thickness_1_socket.description = "Thickness of the hairs (Side 1)"
    thickness_1_socket.default_input = 'VALUE'
    thickness_1_socket.structure_type = 'AUTO'

    #Socket Thickness 2
    thickness_2_socket = eyelashgen.interface.new_socket(name = "Thickness 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    thickness_2_socket.default_value = 1.0
    thickness_2_socket.min_value = 0.0
    thickness_2_socket.max_value = 10000.0
    thickness_2_socket.subtype = 'NONE'
    thickness_2_socket.attribute_domain = 'POINT'
    thickness_2_socket.description = "Thickness of the hairs (Side 2)"
    thickness_2_socket.default_input = 'VALUE'
    thickness_2_socket.structure_type = 'AUTO'

    #Socket Rotate 1
    rotate_1_socket = eyelashgen.interface.new_socket(name = "Rotate 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rotate_1_socket.default_value = 0.0
    rotate_1_socket.min_value = -10000.0
    rotate_1_socket.max_value = 10000.0
    rotate_1_socket.subtype = 'NONE'
    rotate_1_socket.attribute_domain = 'POINT'
    rotate_1_socket.description = "Rotate the hairs around the guide curve (Side 1)"
    rotate_1_socket.default_input = 'VALUE'
    rotate_1_socket.structure_type = 'AUTO'

    #Socket Rotate 2
    rotate_2_socket = eyelashgen.interface.new_socket(name = "Rotate 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rotate_2_socket.default_value = 0.0
    rotate_2_socket.min_value = -10000.0
    rotate_2_socket.max_value = 10000.0
    rotate_2_socket.subtype = 'NONE'
    rotate_2_socket.attribute_domain = 'POINT'
    rotate_2_socket.description = "Rotate the hairs around the guide curve (Side 2)"
    rotate_2_socket.default_input = 'VALUE'
    rotate_2_socket.structure_type = 'AUTO'

    #Socket Bend 1
    bend_1_socket = eyelashgen.interface.new_socket(name = "Bend 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bend_1_socket.default_value = 0.0
    bend_1_socket.min_value = -10000.0
    bend_1_socket.max_value = 10000.0
    bend_1_socket.subtype = 'NONE'
    bend_1_socket.attribute_domain = 'POINT'
    bend_1_socket.description = "Bend the hairs (Side 1)"
    bend_1_socket.default_input = 'VALUE'
    bend_1_socket.structure_type = 'AUTO'

    #Socket Bend 2
    bend_2_socket = eyelashgen.interface.new_socket(name = "Bend 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bend_2_socket.default_value = 0.0
    bend_2_socket.min_value = -10000.0
    bend_2_socket.max_value = 10000.0
    bend_2_socket.subtype = 'NONE'
    bend_2_socket.attribute_domain = 'POINT'
    bend_2_socket.description = "Bend the hairs (Side 2)"
    bend_2_socket.default_input = 'VALUE'
    bend_2_socket.structure_type = 'AUTO'

    #Socket Tilt 1
    tilt_1_socket = eyelashgen.interface.new_socket(name = "Tilt 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    tilt_1_socket.default_value = 0.0
    tilt_1_socket.min_value = -10000.0
    tilt_1_socket.max_value = 10000.0
    tilt_1_socket.subtype = 'NONE'
    tilt_1_socket.attribute_domain = 'POINT'
    tilt_1_socket.description = "Tilt the hairs (Side 1)"
    tilt_1_socket.default_input = 'VALUE'
    tilt_1_socket.structure_type = 'AUTO'

    #Socket Tilt 2
    tilt_2_socket = eyelashgen.interface.new_socket(name = "Tilt 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    tilt_2_socket.default_value = 0.0
    tilt_2_socket.min_value = -10000.0
    tilt_2_socket.max_value = 10000.0
    tilt_2_socket.subtype = 'NONE'
    tilt_2_socket.attribute_domain = 'POINT'
    tilt_2_socket.description = "Tilt the hairs (Side 2)"
    tilt_2_socket.default_input = 'VALUE'
    tilt_2_socket.structure_type = 'AUTO'

    #Socket Density 1
    density_1_socket = eyelashgen.interface.new_socket(name = "Density 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    density_1_socket.default_value = 1.0
    density_1_socket.min_value = 0.0
    density_1_socket.max_value = 1.0
    density_1_socket.subtype = 'FACTOR'
    density_1_socket.attribute_domain = 'POINT'
    density_1_socket.description = "Hairs density (Side 1)"
    density_1_socket.default_input = 'VALUE'
    density_1_socket.structure_type = 'AUTO'

    #Socket Density 2
    density_2_socket = eyelashgen.interface.new_socket(name = "Density 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    density_2_socket.default_value = 1.0
    density_2_socket.min_value = 0.0
    density_2_socket.max_value = 1.0
    density_2_socket.subtype = 'FACTOR'
    density_2_socket.attribute_domain = 'POINT'
    density_2_socket.description = "Hairs density (Side 2)"
    density_2_socket.default_input = 'VALUE'
    density_2_socket.structure_type = 'AUTO'

    #Socket Trim 1
    trim_1_socket = eyelashgen.interface.new_socket(name = "Trim 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    trim_1_socket.default_value = 0.0
    trim_1_socket.min_value = 0.0
    trim_1_socket.max_value = 1.0
    trim_1_socket.subtype = 'FACTOR'
    trim_1_socket.attribute_domain = 'POINT'
    trim_1_socket.description = "Trim from Side 1"
    trim_1_socket.default_input = 'VALUE'
    trim_1_socket.structure_type = 'AUTO'

    #Socket Trim 2
    trim_2_socket = eyelashgen.interface.new_socket(name = "Trim 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    trim_2_socket.default_value = 0.0
    trim_2_socket.min_value = 0.0
    trim_2_socket.max_value = 1.0
    trim_2_socket.subtype = 'FACTOR'
    trim_2_socket.attribute_domain = 'POINT'
    trim_2_socket.description = "Trim from Side 2"
    trim_2_socket.default_input = 'VALUE'
    trim_2_socket.structure_type = 'AUTO'

    #Panel Shades
    shades_panel = eyelashgen.interface.new_panel("Shades", default_closed=True)
    #Socket Root Fade
    root_fade_socket = eyelashgen.interface.new_socket(name = "Root Fade", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shades_panel)
    root_fade_socket.default_value = 0.0
    root_fade_socket.min_value = 0.0
    root_fade_socket.max_value = 1.0
    root_fade_socket.subtype = 'FACTOR'
    root_fade_socket.attribute_domain = 'POINT'
    root_fade_socket.description = "Root shade gradient"
    root_fade_socket.default_input = 'VALUE'
    root_fade_socket.structure_type = 'AUTO'

    #Socket Root Contrast
    root_contrast_socket = eyelashgen.interface.new_socket(name = "Root Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shades_panel)
    root_contrast_socket.default_value = 0.5
    root_contrast_socket.min_value = 0.0
    root_contrast_socket.max_value = 1.0
    root_contrast_socket.subtype = 'FACTOR'
    root_contrast_socket.attribute_domain = 'POINT'
    root_contrast_socket.description = "Root shade gradient contrast"
    root_contrast_socket.default_input = 'VALUE'
    root_contrast_socket.structure_type = 'AUTO'

    #Socket Tip Fade
    tip_fade_socket = eyelashgen.interface.new_socket(name = "Tip Fade", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shades_panel)
    tip_fade_socket.default_value = 0.0
    tip_fade_socket.min_value = 0.0
    tip_fade_socket.max_value = 1.0
    tip_fade_socket.subtype = 'FACTOR'
    tip_fade_socket.attribute_domain = 'POINT'
    tip_fade_socket.description = "Tip shade gradient"
    tip_fade_socket.default_input = 'VALUE'
    tip_fade_socket.structure_type = 'AUTO'

    #Socket Tip Contrast
    tip_contrast_socket = eyelashgen.interface.new_socket(name = "Tip Contrast", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shades_panel)
    tip_contrast_socket.default_value = 0.5
    tip_contrast_socket.min_value = 0.0
    tip_contrast_socket.max_value = 1.0
    tip_contrast_socket.subtype = 'FACTOR'
    tip_contrast_socket.attribute_domain = 'POINT'
    tip_contrast_socket.description = "Tip shade gradient contrast"
    tip_contrast_socket.default_input = 'VALUE'
    tip_contrast_socket.structure_type = 'AUTO'


    #Panel Options
    options_panel = eyelashgen.interface.new_panel("Options", default_closed=True)
    #Socket Flip Direction
    flip_direction_socket = eyelashgen.interface.new_socket(name = "Flip Direction", in_out='INPUT', socket_type = 'NodeSocketBool', parent = options_panel)
    flip_direction_socket.default_value = False
    flip_direction_socket.attribute_domain = 'POINT'
    flip_direction_socket.description = "Flip the direction of the guide curve (Switch sides)"
    flip_direction_socket.default_input = 'VALUE'
    flip_direction_socket.structure_type = 'AUTO'

    #Socket Offset from Face
    offset_from_face_socket = eyelashgen.interface.new_socket(name = "Offset from Face", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = options_panel)
    offset_from_face_socket.default_value = 0.0
    offset_from_face_socket.min_value = -10000.0
    offset_from_face_socket.max_value = 10000.0
    offset_from_face_socket.subtype = 'NONE'
    offset_from_face_socket.attribute_domain = 'POINT'
    offset_from_face_socket.description = "Distance of the hairs to the Face surface"
    offset_from_face_socket.default_input = 'VALUE'
    offset_from_face_socket.structure_type = 'AUTO'

    #Socket Randomize Length
    randomize_length_socket = eyelashgen.interface.new_socket(name = "Randomize Length", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = options_panel)
    randomize_length_socket.default_value = 0.5
    randomize_length_socket.min_value = 0.0
    randomize_length_socket.max_value = 1.0
    randomize_length_socket.subtype = 'FACTOR'
    randomize_length_socket.attribute_domain = 'POINT'
    randomize_length_socket.description = "Randomize the hairs length"
    randomize_length_socket.default_input = 'VALUE'
    randomize_length_socket.structure_type = 'AUTO'

    #Socket Randomize Thickness
    randomize_thickness_socket = eyelashgen.interface.new_socket(name = "Randomize Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = options_panel)
    randomize_thickness_socket.default_value = 0.5
    randomize_thickness_socket.min_value = 0.0
    randomize_thickness_socket.max_value = 1.0
    randomize_thickness_socket.subtype = 'FACTOR'
    randomize_thickness_socket.attribute_domain = 'POINT'
    randomize_thickness_socket.description = "Randomize the hairs thickness"
    randomize_thickness_socket.default_input = 'VALUE'
    randomize_thickness_socket.structure_type = 'AUTO'



    #initialize eyelashgen nodes
    #node Frame.005
    frame_005 = eyelashgen.nodes.new("NodeFrame")
    frame_005.label = "eyelash position"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_005.label_size = 20
    frame_005.shrink = True

    #node Frame.002
    frame_002_1 = eyelashgen.nodes.new("NodeFrame")
    frame_002_1.label = "rotate"
    frame_002_1.name = "Frame.002"
    frame_002_1.use_custom_color = True
    frame_002_1.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_002_1.label_size = 20
    frame_002_1.shrink = True

    #node Frame
    frame_1 = eyelashgen.nodes.new("NodeFrame")
    frame_1.label = "randomize points"
    frame_1.name = "Frame"
    frame_1.use_custom_color = True
    frame_1.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_1.label_size = 20
    frame_1.shrink = True

    #node Frame.006
    frame_006 = eyelashgen.nodes.new("NodeFrame")
    frame_006.label = "create eyelash curves"
    frame_006.name = "Frame.006"
    frame_006.use_custom_color = True
    frame_006.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_006.label_size = 17
    frame_006.shrink = True

    #node Frame.003
    frame_003_1 = eyelashgen.nodes.new("NodeFrame")
    frame_003_1.label = "tilt"
    frame_003_1.name = "Frame.003"
    frame_003_1.use_custom_color = True
    frame_003_1.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_003_1.label_size = 20
    frame_003_1.shrink = True

    #node Frame.001
    frame_001_1 = eyelashgen.nodes.new("NodeFrame")
    frame_001_1.label = "bend"
    frame_001_1.name = "Frame.001"
    frame_001_1.use_custom_color = True
    frame_001_1.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_001_1.label_size = 20
    frame_001_1.shrink = True

    #node Frame.004
    frame_004 = eyelashgen.nodes.new("NodeFrame")
    frame_004.label = "realize and resolution"
    frame_004.name = "Frame.004"
    frame_004.use_custom_color = True
    frame_004.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_004.label_size = 20
    frame_004.shrink = True

    #node Frame.010
    frame_010 = eyelashgen.nodes.new("NodeFrame")
    frame_010.label = "thickness"
    frame_010.name = "Frame.010"
    frame_010.use_custom_color = True
    frame_010.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_010.label_size = 20
    frame_010.shrink = True

    #node Frame.012
    frame_012 = eyelashgen.nodes.new("NodeFrame")
    frame_012.label = "trim"
    frame_012.name = "Frame.012"
    frame_012.use_custom_color = True
    frame_012.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_012.label_size = 20
    frame_012.shrink = True

    #node Frame.011
    frame_011 = eyelashgen.nodes.new("NodeFrame")
    frame_011.label = "density"
    frame_011.name = "Frame.011"
    frame_011.use_custom_color = True
    frame_011.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_011.label_size = 20
    frame_011.shrink = True

    #node Frame.013
    frame_013 = eyelashgen.nodes.new("NodeFrame")
    frame_013.label = "ends shade"
    frame_013.name = "Frame.013"
    frame_013.use_custom_color = True
    frame_013.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_013.label_size = 20
    frame_013.shrink = True

    #node Frame.009
    frame_009 = eyelashgen.nodes.new("NodeFrame")
    frame_009.label = "clump"
    frame_009.name = "Frame.009"
    frame_009.use_custom_color = True
    frame_009.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_009.label_size = 20
    frame_009.shrink = True

    #node Frame.008
    frame_008 = eyelashgen.nodes.new("NodeFrame")
    frame_008.label = "guide curve factor"
    frame_008.name = "Frame.008"
    frame_008.use_custom_color = True
    frame_008.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_008.label_size = 20
    frame_008.shrink = True

    #node Frame.007
    frame_007 = eyelashgen.nodes.new("NodeFrame")
    frame_007.label = "length"
    frame_007.name = "Frame.007"
    frame_007.use_custom_color = True
    frame_007.color = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    frame_007.label_size = 20
    frame_007.shrink = True

    #node Capture Attribute.001
    capture_attribute_001_1 = eyelashgen.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001_1.name = "Capture Attribute.001"
    capture_attribute_001_1.active_index = 0
    capture_attribute_001_1.capture_items.clear()
    capture_attribute_001_1.capture_items.new('FLOAT', "Value")
    capture_attribute_001_1.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_001_1.domain = 'POINT'

    #node Position.001
    position_001 = eyelashgen.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    #node Reroute.015
    reroute_015 = eyelashgen.nodes.new("NodeReroute")
    reroute_015.label = "guide normal"
    reroute_015.name = "Reroute.015"
    reroute_015.socket_idname = "NodeSocketVector"
    #node Align Euler to Vector
    align_euler_to_vector = eyelashgen.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.axis = 'Z'
    align_euler_to_vector.pivot_axis = 'AUTO'
    #Factor
    align_euler_to_vector.inputs[1].default_value = 1.0

    #node Align Euler to Vector.001
    align_euler_to_vector_001 = eyelashgen.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector_001.name = "Align Euler to Vector.001"
    align_euler_to_vector_001.axis = 'X'
    align_euler_to_vector_001.pivot_axis = 'AUTO'
    #Rotation
    align_euler_to_vector_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    #Factor
    align_euler_to_vector_001.inputs[1].default_value = 1.0

    #node Mix.005
    mix_005 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = 'MIX'
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = 'FLOAT'
    mix_005.factor_mode = 'UNIFORM'

    #node Mix.003
    mix_003 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.hide = True
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'FLOAT'
    mix_003.factor_mode = 'UNIFORM'

    #node Reroute.007
    reroute_007_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_007_1.label = "guide tangent"
    reroute_007_1.name = "Reroute.007"
    reroute_007_1.socket_idname = "NodeSocketVector"
    #node Reroute.011
    reroute_011_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_011_1.label = "guide normal"
    reroute_011_1.name = "Reroute.011"
    reroute_011_1.socket_idname = "NodeSocketVector"
    #node Reroute.012
    reroute_012_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_012_1.label = "eyelash position"
    reroute_012_1.name = "Reroute.012"
    reroute_012_1.socket_idname = "NodeSocketVector"
    #node Reroute.013
    reroute_013_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_013_1.label = "eyelash position"
    reroute_013_1.name = "Reroute.013"
    reroute_013_1.socket_idname = "NodeSocketVector"
    #node Set Position
    set_position_1 = eyelashgen.nodes.new("GeometryNodeSetPosition")
    set_position_1.name = "Set Position"
    #Selection
    set_position_1.inputs[1].default_value = True
    #Position
    set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Random Value
    random_value = eyelashgen.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'FLOAT_VECTOR'
    #ID
    random_value.inputs[7].default_value = 0

    #node Math
    math = eyelashgen.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 0.0010000000474974513

    #node Reroute.020
    reroute_020 = eyelashgen.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.socket_idname = "NodeSocketGeometry"
    #node Set Curve Tilt
    set_curve_tilt = eyelashgen.nodes.new("GeometryNodeSetCurveTilt")
    set_curve_tilt.name = "Set Curve Tilt"
    #Selection
    set_curve_tilt.inputs[1].default_value = True
    #Tilt
    set_curve_tilt.inputs[2].default_value = 0.0

    #node Curve to Points
    curve_to_points = eyelashgen.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points.name = "Curve to Points"
    curve_to_points.mode = 'COUNT'

    #node Set Point Radius
    set_point_radius = eyelashgen.nodes.new("GeometryNodeSetPointRadius")
    set_point_radius.name = "Set Point Radius"
    set_point_radius.hide = True
    #Selection
    set_point_radius.inputs[1].default_value = True
    #Radius
    set_point_radius.inputs[2].default_value = 0.0003000000142492354

    #node Reroute.010
    reroute_010_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_010_1.label = "guide normal"
    reroute_010_1.name = "Reroute.010"
    reroute_010_1.socket_idname = "NodeSocketVector"
    #node Reroute
    reroute_3 = eyelashgen.nodes.new("NodeReroute")
    reroute_3.label = "guide factor"
    reroute_3.name = "Reroute"
    reroute_3.socket_idname = "NodeSocketFloat"
    #node Reroute.002
    reroute_002_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_002_1.label = "guide factor"
    reroute_002_1.name = "Reroute.002"
    reroute_002_1.socket_idname = "NodeSocketFloat"
    #node Reroute.008
    reroute_008_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_008_1.label = "guide factor"
    reroute_008_1.name = "Reroute.008"
    reroute_008_1.socket_idname = "NodeSocketFloat"
    #node Curve Line
    curve_line_1 = eyelashgen.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_1.name = "Curve Line"
    curve_line_1.hide = True
    curve_line_1.mode = 'POINTS'
    #Start
    curve_line_1.inputs[0].default_value = (0.0, 0.0, 0.0)
    #End
    curve_line_1.inputs[1].default_value = (0.0, 0.0, 1.0)

    #node Reroute.006
    reroute_006_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_006_1.label = "guide tangent"
    reroute_006_1.name = "Reroute.006"
    reroute_006_1.socket_idname = "NodeSocketVector"
    #node Group
    group = eyelashgen.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = _ee_convert_value
    group.outputs[2].hide = True
    group.outputs[3].hide = True
    group.outputs[4].hide = True
    group.outputs[5].hide = True

    #node Group.001
    group_001 = eyelashgen.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = _ee_shrinkwrap_to_surface

    #node Group Input.002
    group_input_002_3 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_002_3.name = "Group Input.002"
    group_input_002_3.use_custom_color = True
    group_input_002_3.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_002_3.outputs[0].hide = True
    group_input_002_3.outputs[1].hide = True
    group_input_002_3.outputs[2].hide = True
    group_input_002_3.outputs[3].hide = True
    group_input_002_3.outputs[5].hide = True
    group_input_002_3.outputs[6].hide = True
    group_input_002_3.outputs[7].hide = True
    group_input_002_3.outputs[8].hide = True
    group_input_002_3.outputs[9].hide = True
    group_input_002_3.outputs[10].hide = True
    group_input_002_3.outputs[11].hide = True
    group_input_002_3.outputs[12].hide = True
    group_input_002_3.outputs[13].hide = True
    group_input_002_3.outputs[14].hide = True
    group_input_002_3.outputs[15].hide = True
    group_input_002_3.outputs[16].hide = True
    group_input_002_3.outputs[17].hide = True
    group_input_002_3.outputs[18].hide = True
    group_input_002_3.outputs[19].hide = True
    group_input_002_3.outputs[20].hide = True
    group_input_002_3.outputs[21].hide = True
    group_input_002_3.outputs[22].hide = True
    group_input_002_3.outputs[23].hide = True
    group_input_002_3.outputs[24].hide = True
    group_input_002_3.outputs[25].hide = True
    group_input_002_3.outputs[26].hide = True
    group_input_002_3.outputs[27].hide = True
    group_input_002_3.outputs[28].hide = True
    group_input_002_3.outputs[29].hide = True

    #node Group Input.009
    group_input_009_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_009_1.name = "Group Input.009"
    group_input_009_1.use_custom_color = True
    group_input_009_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_009_1.outputs[0].hide = True
    group_input_009_1.outputs[1].hide = True
    group_input_009_1.outputs[2].hide = True
    group_input_009_1.outputs[3].hide = True
    group_input_009_1.outputs[4].hide = True
    group_input_009_1.outputs[6].hide = True
    group_input_009_1.outputs[7].hide = True
    group_input_009_1.outputs[8].hide = True
    group_input_009_1.outputs[9].hide = True
    group_input_009_1.outputs[10].hide = True
    group_input_009_1.outputs[11].hide = True
    group_input_009_1.outputs[12].hide = True
    group_input_009_1.outputs[13].hide = True
    group_input_009_1.outputs[14].hide = True
    group_input_009_1.outputs[15].hide = True
    group_input_009_1.outputs[16].hide = True
    group_input_009_1.outputs[17].hide = True
    group_input_009_1.outputs[18].hide = True
    group_input_009_1.outputs[19].hide = True
    group_input_009_1.outputs[20].hide = True
    group_input_009_1.outputs[21].hide = True
    group_input_009_1.outputs[22].hide = True
    group_input_009_1.outputs[23].hide = True
    group_input_009_1.outputs[24].hide = True
    group_input_009_1.outputs[25].hide = True
    group_input_009_1.outputs[26].hide = True
    group_input_009_1.outputs[27].hide = True
    group_input_009_1.outputs[28].hide = True
    group_input_009_1.outputs[29].hide = True

    #node Group Input.001
    group_input_001_4 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_001_4.name = "Group Input.001"
    group_input_001_4.use_custom_color = True
    group_input_001_4.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_001_4.outputs[0].hide = True
    group_input_001_4.outputs[1].hide = True
    group_input_001_4.outputs[2].hide = True
    group_input_001_4.outputs[4].hide = True
    group_input_001_4.outputs[5].hide = True
    group_input_001_4.outputs[6].hide = True
    group_input_001_4.outputs[7].hide = True
    group_input_001_4.outputs[8].hide = True
    group_input_001_4.outputs[9].hide = True
    group_input_001_4.outputs[10].hide = True
    group_input_001_4.outputs[11].hide = True
    group_input_001_4.outputs[12].hide = True
    group_input_001_4.outputs[13].hide = True
    group_input_001_4.outputs[14].hide = True
    group_input_001_4.outputs[15].hide = True
    group_input_001_4.outputs[16].hide = True
    group_input_001_4.outputs[17].hide = True
    group_input_001_4.outputs[18].hide = True
    group_input_001_4.outputs[19].hide = True
    group_input_001_4.outputs[20].hide = True
    group_input_001_4.outputs[21].hide = True
    group_input_001_4.outputs[22].hide = True
    group_input_001_4.outputs[23].hide = True
    group_input_001_4.outputs[24].hide = True
    group_input_001_4.outputs[25].hide = True
    group_input_001_4.outputs[26].hide = True
    group_input_001_4.outputs[27].hide = True
    group_input_001_4.outputs[28].hide = True
    group_input_001_4.outputs[29].hide = True

    #node Group Input.003
    group_input_003_2 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_003_2.name = "Group Input.003"
    group_input_003_2.use_custom_color = True
    group_input_003_2.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_003_2.outputs[0].hide = True
    group_input_003_2.outputs[1].hide = True
    group_input_003_2.outputs[2].hide = True
    group_input_003_2.outputs[3].hide = True
    group_input_003_2.outputs[4].hide = True
    group_input_003_2.outputs[5].hide = True
    group_input_003_2.outputs[6].hide = True
    group_input_003_2.outputs[9].hide = True
    group_input_003_2.outputs[10].hide = True
    group_input_003_2.outputs[11].hide = True
    group_input_003_2.outputs[12].hide = True
    group_input_003_2.outputs[13].hide = True
    group_input_003_2.outputs[14].hide = True
    group_input_003_2.outputs[15].hide = True
    group_input_003_2.outputs[16].hide = True
    group_input_003_2.outputs[17].hide = True
    group_input_003_2.outputs[18].hide = True
    group_input_003_2.outputs[19].hide = True
    group_input_003_2.outputs[20].hide = True
    group_input_003_2.outputs[21].hide = True
    group_input_003_2.outputs[22].hide = True
    group_input_003_2.outputs[23].hide = True
    group_input_003_2.outputs[24].hide = True
    group_input_003_2.outputs[25].hide = True
    group_input_003_2.outputs[26].hide = True
    group_input_003_2.outputs[27].hide = True
    group_input_003_2.outputs[28].hide = True
    group_input_003_2.outputs[29].hide = True

    #node Group Input.006
    group_input_006 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.use_custom_color = True
    group_input_006.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True
    group_input_006.outputs[15].hide = True
    group_input_006.outputs[16].hide = True
    group_input_006.outputs[17].hide = True
    group_input_006.outputs[18].hide = True
    group_input_006.outputs[19].hide = True
    group_input_006.outputs[20].hide = True
    group_input_006.outputs[21].hide = True
    group_input_006.outputs[22].hide = True
    group_input_006.outputs[23].hide = True
    group_input_006.outputs[24].hide = True
    group_input_006.outputs[25].hide = True
    group_input_006.outputs[26].hide = True
    group_input_006.outputs[27].hide = True
    group_input_006.outputs[28].hide = True
    group_input_006.outputs[29].hide = True

    #node Group Input.015
    group_input_015_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_015_1.name = "Group Input.015"
    group_input_015_1.use_custom_color = True
    group_input_015_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_015_1.outputs[0].hide = True
    group_input_015_1.outputs[2].hide = True
    group_input_015_1.outputs[3].hide = True
    group_input_015_1.outputs[4].hide = True
    group_input_015_1.outputs[5].hide = True
    group_input_015_1.outputs[6].hide = True
    group_input_015_1.outputs[7].hide = True
    group_input_015_1.outputs[8].hide = True
    group_input_015_1.outputs[9].hide = True
    group_input_015_1.outputs[10].hide = True
    group_input_015_1.outputs[11].hide = True
    group_input_015_1.outputs[12].hide = True
    group_input_015_1.outputs[13].hide = True
    group_input_015_1.outputs[14].hide = True
    group_input_015_1.outputs[15].hide = True
    group_input_015_1.outputs[16].hide = True
    group_input_015_1.outputs[17].hide = True
    group_input_015_1.outputs[18].hide = True
    group_input_015_1.outputs[19].hide = True
    group_input_015_1.outputs[20].hide = True
    group_input_015_1.outputs[21].hide = True
    group_input_015_1.outputs[22].hide = True
    group_input_015_1.outputs[23].hide = True
    group_input_015_1.outputs[24].hide = True
    group_input_015_1.outputs[25].hide = True
    group_input_015_1.outputs[27].hide = True
    group_input_015_1.outputs[28].hide = True
    group_input_015_1.outputs[29].hide = True

    #node Instance on Points
    instance_on_points = eyelashgen.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    #Selection
    instance_on_points.inputs[1].default_value = True
    #Pick Instance
    instance_on_points.inputs[3].default_value = False
    #Instance Index
    instance_on_points.inputs[4].default_value = 0

    #node Store Named Attribute.002
    store_named_attribute_002 = eyelashgen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.use_custom_color = True
    store_named_attribute_002.color = (0.5264300107955933, 0.23484696447849274, 0.7454490065574646)
    store_named_attribute_002.data_type = 'FLOAT'
    store_named_attribute_002.domain = 'POINT'
    #Selection
    store_named_attribute_002.inputs[1].default_value = True

    #node Rotate Instances
    rotate_instances = eyelashgen.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    #Selection
    rotate_instances.inputs[1].default_value = True
    #Pivot Point
    rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Local Space
    rotate_instances.inputs[4].default_value = True

    #node Combine XYZ
    combine_xyz_1 = eyelashgen.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"
    #Y
    combine_xyz_1.inputs[1].default_value = 0.0
    #Z
    combine_xyz_1.inputs[2].default_value = 0.0

    #node Group Input.005
    group_input_005_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_005_1.name = "Group Input.005"
    group_input_005_1.use_custom_color = True
    group_input_005_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
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
    group_input_005_1.outputs[10].hide = True
    group_input_005_1.outputs[11].hide = True
    group_input_005_1.outputs[12].hide = True
    group_input_005_1.outputs[13].hide = True
    group_input_005_1.outputs[14].hide = True
    group_input_005_1.outputs[17].hide = True
    group_input_005_1.outputs[18].hide = True
    group_input_005_1.outputs[19].hide = True
    group_input_005_1.outputs[20].hide = True
    group_input_005_1.outputs[21].hide = True
    group_input_005_1.outputs[22].hide = True
    group_input_005_1.outputs[23].hide = True
    group_input_005_1.outputs[24].hide = True
    group_input_005_1.outputs[25].hide = True
    group_input_005_1.outputs[26].hide = True
    group_input_005_1.outputs[27].hide = True
    group_input_005_1.outputs[28].hide = True
    group_input_005_1.outputs[29].hide = True

    #node Mix.004
    mix_004 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.hide = True
    mix_004.blend_type = 'MIX'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'FLOAT'
    mix_004.factor_mode = 'UNIFORM'

    #node Combine XYZ.001
    combine_xyz_001_1 = eyelashgen.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001_1.name = "Combine XYZ.001"
    #X
    combine_xyz_001_1.inputs[0].default_value = 0.0
    #Z
    combine_xyz_001_1.inputs[2].default_value = 0.0

    #node Position
    position_2 = eyelashgen.nodes.new("GeometryNodeInputPosition")
    position_2.name = "Position"

    #node Vector Rotate
    vector_rotate = eyelashgen.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.invert = False
    vector_rotate.rotation_type = 'AXIS_ANGLE'

    #node Spline Parameter.001
    spline_parameter_001_1 = eyelashgen.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_001_1.name = "Spline Parameter.001"
    spline_parameter_001_1.outputs[1].hide = True
    spline_parameter_001_1.outputs[2].hide = True

    #node Reroute.004
    reroute_004_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_004_1.label = "guide tangent"
    reroute_004_1.name = "Reroute.004"
    reroute_004_1.socket_idname = "NodeSocketVector"
    #node Reroute.005
    reroute_005_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_005_1.label = "eyelash position"
    reroute_005_1.name = "Reroute.005"
    reroute_005_1.socket_idname = "NodeSocketVector"
    #node Math.001
    math_001_2 = eyelashgen.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = 'MULTIPLY'
    math_001_2.use_clamp = False

    #node Reroute.003
    reroute_003_2 = eyelashgen.nodes.new("NodeReroute")
    reroute_003_2.label = "guide factor"
    reroute_003_2.name = "Reroute.003"
    reroute_003_2.socket_idname = "NodeSocketFloat"
    #node Reroute.017
    reroute_017 = eyelashgen.nodes.new("NodeReroute")
    reroute_017.label = "guide factor"
    reroute_017.name = "Reroute.017"
    reroute_017.socket_idname = "NodeSocketFloat"
    #node Realize Instances
    realize_instances = eyelashgen.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Selection
    realize_instances.inputs[1].default_value = True
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Resample Curve
    resample_curve_1 = eyelashgen.nodes.new("GeometryNodeResampleCurve")
    resample_curve_1.name = "Resample Curve"
    resample_curve_1.keep_last_segment = False
    resample_curve_1.mode = 'COUNT'
    #Selection
    resample_curve_1.inputs[1].default_value = True
    #Count
    resample_curve_1.inputs[2].default_value = 11

    #node Reroute.021
    reroute_021 = eyelashgen.nodes.new("NodeReroute")
    reroute_021.label = "guide tangent"
    reroute_021.name = "Reroute.021"
    reroute_021.socket_idname = "NodeSocketVector"
    #node Reroute.022
    reroute_022 = eyelashgen.nodes.new("NodeReroute")
    reroute_022.label = "eyelash position"
    reroute_022.name = "Reroute.022"
    reroute_022.socket_idname = "NodeSocketVector"
    #node Reroute.016
    reroute_016 = eyelashgen.nodes.new("NodeReroute")
    reroute_016.label = "guide normal"
    reroute_016.name = "Reroute.016"
    reroute_016.socket_idname = "NodeSocketVector"
    #node Reroute.023
    reroute_023 = eyelashgen.nodes.new("NodeReroute")
    reroute_023.label = "guide tangent"
    reroute_023.name = "Reroute.023"
    reroute_023.socket_idname = "NodeSocketVector"
    #node Reroute.001
    reroute_001_3 = eyelashgen.nodes.new("NodeReroute")
    reroute_001_3.label = "eyelash position"
    reroute_001_3.name = "Reroute.001"
    reroute_001_3.socket_idname = "NodeSocketVector"
    #node ID
    id_1 = eyelashgen.nodes.new("GeometryNodeInputID")
    id_1.name = "ID"

    #node Evaluate on Domain
    evaluate_on_domain = eyelashgen.nodes.new("GeometryNodeFieldOnDomain")
    evaluate_on_domain.name = "Evaluate on Domain"
    evaluate_on_domain.data_type = 'INT'
    evaluate_on_domain.domain = 'CURVE'

    #node Float Curve
    float_curve = eyelashgen.nodes.new("ShaderNodeFloatCurve")
    float_curve.name = "Float Curve"
    #mapping settings
    float_curve.mapping.extend = 'EXTRAPOLATED'
    float_curve.mapping.tone = 'STANDARD'
    float_curve.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve.mapping.clip_min_x = 0.0
    float_curve.mapping.clip_min_y = 0.0
    float_curve.mapping.clip_max_x = 1.0
    float_curve.mapping.clip_max_y = 1.0
    float_curve.mapping.use_clip = True
    #curve 0
    float_curve_curve_0 = float_curve.mapping.curves[0]
    float_curve_curve_0_point_0 = float_curve_curve_0.points[0]
    float_curve_curve_0_point_0.location = (0.0, 0.5100002884864807)
    float_curve_curve_0_point_0.handle_type = 'AUTO'
    float_curve_curve_0_point_1 = float_curve_curve_0.points[1]
    float_curve_curve_0_point_1.location = (0.3719298839569092, 0.5899999141693115)
    float_curve_curve_0_point_1.handle_type = 'AUTO'
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 0.0)
    float_curve_curve_0_point_2.handle_type = 'AUTO'
    #update curve after changes
    float_curve.mapping.update()
    float_curve.inputs[0].hide = True
    #Factor
    float_curve.inputs[0].default_value = 1.0

    #node Math.002
    math_002_3 = eyelashgen.nodes.new("ShaderNodeMath")
    math_002_3.name = "Math.002"
    math_002_3.operation = 'MULTIPLY'
    math_002_3.use_clamp = False

    #node Compare
    compare_1 = eyelashgen.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.hide = True
    compare_1.data_type = 'FLOAT'
    compare_1.mode = 'ELEMENT'
    compare_1.operation = 'LESS_THAN'

    #node Compare.001
    compare_001 = eyelashgen.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.hide = True
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'LESS_THAN'

    #node Math.004
    math_004_3 = eyelashgen.nodes.new("ShaderNodeMath")
    math_004_3.label = "invert"
    math_004_3.name = "Math.004"
    math_004_3.hide = True
    math_004_3.operation = 'SUBTRACT'
    math_004_3.use_clamp = False
    #Value
    math_004_3.inputs[0].default_value = 1.0

    #node Boolean Math.001
    boolean_math_001 = eyelashgen.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.hide = True
    boolean_math_001.operation = 'OR'

    #node Random Value.002
    random_value_002 = eyelashgen.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'BOOLEAN'
    #ID
    random_value_002.inputs[7].default_value = 0

    #node Mix.002
    mix_002_1 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_002_1.name = "Mix.002"
    mix_002_1.hide = True
    mix_002_1.blend_type = 'MIX'
    mix_002_1.clamp_factor = True
    mix_002_1.clamp_result = False
    mix_002_1.data_type = 'FLOAT'
    mix_002_1.factor_mode = 'UNIFORM'

    #node Boolean Math
    boolean_math = eyelashgen.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'NOT'

    #node Reroute.024
    reroute_024 = eyelashgen.nodes.new("NodeReroute")
    reroute_024.label = "guide factor"
    reroute_024.name = "Reroute.024"
    reroute_024.socket_idname = "NodeSocketFloat"
    #node Reroute.014
    reroute_014 = eyelashgen.nodes.new("NodeReroute")
    reroute_014.label = "guide factor"
    reroute_014.name = "Reroute.014"
    reroute_014.socket_idname = "NodeSocketFloat"
    #node Set Position.001
    set_position_001_1 = eyelashgen.nodes.new("GeometryNodeSetPosition")
    set_position_001_1.name = "Set Position.001"
    #Selection
    set_position_001_1.inputs[1].default_value = True
    #Offset
    set_position_001_1.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Reroute.018
    reroute_018 = eyelashgen.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.socket_idname = "NodeSocketFloat"
    #node Reroute.009
    reroute_009_1 = eyelashgen.nodes.new("NodeReroute")
    reroute_009_1.name = "Reroute.009"
    reroute_009_1.socket_idname = "NodeSocketFloatFactor"
    #node Reroute.025
    reroute_025 = eyelashgen.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.socket_idname = "NodeSocketFloatFactor"
    #node Mix.007
    mix_007_1 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_007_1.name = "Mix.007"
    mix_007_1.blend_type = 'MIX'
    mix_007_1.clamp_factor = True
    mix_007_1.clamp_result = False
    mix_007_1.data_type = 'FLOAT'
    mix_007_1.factor_mode = 'UNIFORM'
    #A_Float
    mix_007_1.inputs[2].default_value = 0.5
    #B_Float
    mix_007_1.inputs[3].default_value = 0.8500000238418579

    #node Reroute.026
    reroute_026 = eyelashgen.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.socket_idname = "NodeSocketFloatFactor"
    #node Reroute.027
    reroute_027 = eyelashgen.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.socket_idname = "NodeSocketFloatFactor"
    #node Mix.008
    mix_008 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_008.name = "Mix.008"
    mix_008.blend_type = 'MIX'
    mix_008.clamp_factor = True
    mix_008.clamp_result = False
    mix_008.data_type = 'FLOAT'
    mix_008.factor_mode = 'UNIFORM'
    #A_Float
    mix_008.inputs[2].default_value = 0.5
    #B_Float
    mix_008.inputs[3].default_value = 0.15000000596046448

    #node Math.005
    math_005_1 = eyelashgen.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = 'MULTIPLY'
    math_005_1.use_clamp = False

    #node Boolean Math.002
    boolean_math_002 = eyelashgen.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = 'OR'

    #node Curve to Mesh
    curve_to_mesh_1 = eyelashgen.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_1.name = "Curve to Mesh"
    #Fill Caps
    curve_to_mesh_1.inputs[3].default_value = False

    #node Group Output
    group_output_6 = eyelashgen.nodes.new("NodeGroupOutput")
    group_output_6.name = "Group Output"
    group_output_6.is_active_output = True

    #node Delete Geometry.001
    delete_geometry_001 = eyelashgen.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'CURVE'
    delete_geometry_001.mode = 'ALL'

    #node Curve Circle
    curve_circle = eyelashgen.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    #Resolution
    curve_circle.inputs[0].default_value = 8
    #Radius
    curve_circle.inputs[4].default_value = 1.0

    #node Position.002
    position_002 = eyelashgen.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    #node Spline Parameter.003
    spline_parameter_003_1 = eyelashgen.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_003_1.name = "Spline Parameter.003"
    spline_parameter_003_1.outputs[1].hide = True
    spline_parameter_003_1.outputs[2].hide = True

    #node Reroute.019
    reroute_019 = eyelashgen.nodes.new("NodeReroute")
    reroute_019.label = "eyelash position"
    reroute_019.name = "Reroute.019"
    reroute_019.socket_idname = "NodeSocketVector"
    #node Math.003
    math_003_2 = eyelashgen.nodes.new("ShaderNodeMath")
    math_003_2.name = "Math.003"
    math_003_2.operation = 'MULTIPLY'
    math_003_2.use_clamp = False

    #node Vector Rotate.001
    vector_rotate_001 = eyelashgen.nodes.new("ShaderNodeVectorRotate")
    vector_rotate_001.name = "Vector Rotate.001"
    vector_rotate_001.invert = False
    vector_rotate_001.rotation_type = 'AXIS_ANGLE'

    #node Vector Math
    vector_math_1 = eyelashgen.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.hide = True
    vector_math_1.operation = 'CROSS_PRODUCT'

    #node Random Value.001
    random_value_001_1 = eyelashgen.nodes.new("FunctionNodeRandomValue")
    random_value_001_1.name = "Random Value.001"
    random_value_001_1.data_type = 'FLOAT'
    #Min_001
    random_value_001_1.inputs[2].default_value = -0.5
    #Max_001
    random_value_001_1.inputs[3].default_value = 0.5

    #node Mix
    mix_2 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_2.name = "Mix"
    mix_2.blend_type = 'MIX'
    mix_2.clamp_factor = True
    mix_2.clamp_result = False
    mix_2.data_type = 'FLOAT'
    mix_2.factor_mode = 'UNIFORM'
    mix_2.inputs[1].hide = True
    mix_2.inputs[2].hide = True
    mix_2.inputs[4].hide = True
    mix_2.inputs[5].hide = True
    mix_2.inputs[6].hide = True
    mix_2.inputs[7].hide = True
    mix_2.inputs[8].hide = True
    mix_2.inputs[9].hide = True
    mix_2.outputs[1].hide = True
    mix_2.outputs[2].hide = True
    mix_2.outputs[3].hide = True
    #A_Float
    mix_2.inputs[2].default_value = 0.0

    #node Evaluate on Domain.001
    evaluate_on_domain_001 = eyelashgen.nodes.new("GeometryNodeFieldOnDomain")
    evaluate_on_domain_001.name = "Evaluate on Domain.001"
    evaluate_on_domain_001.data_type = 'INT'
    evaluate_on_domain_001.domain = 'CURVE'

    #node ID.001
    id_001 = eyelashgen.nodes.new("GeometryNodeInputID")
    id_001.name = "ID.001"

    #node Mix.006
    mix_006_1 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_006_1.name = "Mix.006"
    mix_006_1.hide = True
    mix_006_1.blend_type = 'MIX'
    mix_006_1.clamp_factor = True
    mix_006_1.clamp_result = False
    mix_006_1.data_type = 'FLOAT'
    mix_006_1.factor_mode = 'UNIFORM'

    #node Mix.001
    mix_001_2 = eyelashgen.nodes.new("ShaderNodeMix")
    mix_001_2.name = "Mix.001"
    mix_001_2.hide = True
    mix_001_2.blend_type = 'MIX'
    mix_001_2.clamp_factor = True
    mix_001_2.clamp_result = False
    mix_001_2.data_type = 'FLOAT'
    mix_001_2.factor_mode = 'UNIFORM'

    #node Spline Parameter.002
    spline_parameter_002 = eyelashgen.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_002.name = "Spline Parameter.002"
    spline_parameter_002.outputs[1].hide = True
    spline_parameter_002.outputs[2].hide = True

    #node Group.005
    group_005 = eyelashgen.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = _ee_curve_range
    group_005.inputs[0].hide = True
    group_005.inputs[2].hide = True
    group_005.inputs[4].hide = True
    group_005.inputs[5].hide = True
    group_005.inputs[6].hide = True
    group_005.inputs[7].hide = True
    group_005.inputs[8].hide = True
    group_005.inputs[9].hide = True
    group_005.outputs[0].hide = True
    #Input_2
    group_005.inputs[0].default_value = False
    #Input_3
    group_005.inputs[2].default_value = 0.0
    #Input_5
    group_005.inputs[4].default_value = 0.800000011920929
    #Input_6
    group_005.inputs[5].default_value = 0.800000011920929
    #Input_9
    group_005.inputs[6].default_value = False
    #Input_10
    group_005.inputs[7].default_value = 0.0
    #Input_11
    group_005.inputs[8].default_value = 1.0
    #Socket_1
    group_005.inputs[9].default_value = 0.0

    #node Group.004
    group_004 = eyelashgen.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = _ee_curve_range
    group_004.inputs[0].hide = True
    group_004.inputs[2].hide = True
    group_004.inputs[4].hide = True
    group_004.inputs[5].hide = True
    group_004.inputs[6].hide = True
    group_004.inputs[7].hide = True
    group_004.inputs[8].hide = True
    group_004.inputs[9].hide = True
    group_004.outputs[0].hide = True
    #Input_2
    group_004.inputs[0].default_value = False
    #Input_3
    group_004.inputs[2].default_value = 0.0
    #Input_5
    group_004.inputs[4].default_value = 0.800000011920929
    #Input_6
    group_004.inputs[5].default_value = 0.800000011920929
    #Input_9
    group_004.inputs[6].default_value = False
    #Input_10
    group_004.inputs[7].default_value = 0.0
    #Input_11
    group_004.inputs[8].default_value = 1.0
    #Socket_1
    group_004.inputs[9].default_value = 0.0

    #node Group Input.007
    group_input_007 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.use_custom_color = True
    group_input_007.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True
    group_input_007.outputs[11].hide = True
    group_input_007.outputs[12].hide = True
    group_input_007.outputs[15].hide = True
    group_input_007.outputs[16].hide = True
    group_input_007.outputs[17].hide = True
    group_input_007.outputs[18].hide = True
    group_input_007.outputs[19].hide = True
    group_input_007.outputs[20].hide = True
    group_input_007.outputs[21].hide = True
    group_input_007.outputs[22].hide = True
    group_input_007.outputs[23].hide = True
    group_input_007.outputs[24].hide = True
    group_input_007.outputs[25].hide = True
    group_input_007.outputs[26].hide = True
    group_input_007.outputs[27].hide = True
    group_input_007.outputs[28].hide = True
    group_input_007.outputs[29].hide = True

    #node Group Input.012
    group_input_012_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_012_1.name = "Group Input.012"
    group_input_012_1.use_custom_color = True
    group_input_012_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_012_1.outputs[0].hide = True
    group_input_012_1.outputs[1].hide = True
    group_input_012_1.outputs[2].hide = True
    group_input_012_1.outputs[3].hide = True
    group_input_012_1.outputs[4].hide = True
    group_input_012_1.outputs[5].hide = True
    group_input_012_1.outputs[6].hide = True
    group_input_012_1.outputs[7].hide = True
    group_input_012_1.outputs[8].hide = True
    group_input_012_1.outputs[9].hide = True
    group_input_012_1.outputs[10].hide = True
    group_input_012_1.outputs[11].hide = True
    group_input_012_1.outputs[12].hide = True
    group_input_012_1.outputs[13].hide = True
    group_input_012_1.outputs[14].hide = True
    group_input_012_1.outputs[15].hide = True
    group_input_012_1.outputs[16].hide = True
    group_input_012_1.outputs[17].hide = True
    group_input_012_1.outputs[18].hide = True
    group_input_012_1.outputs[21].hide = True
    group_input_012_1.outputs[22].hide = True
    group_input_012_1.outputs[23].hide = True
    group_input_012_1.outputs[24].hide = True
    group_input_012_1.outputs[25].hide = True
    group_input_012_1.outputs[26].hide = True
    group_input_012_1.outputs[27].hide = True
    group_input_012_1.outputs[28].hide = True
    group_input_012_1.outputs[29].hide = True

    #node Group Input.013
    group_input_013_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_013_1.name = "Group Input.013"
    group_input_013_1.use_custom_color = True
    group_input_013_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_013_1.outputs[0].hide = True
    group_input_013_1.outputs[1].hide = True
    group_input_013_1.outputs[2].hide = True
    group_input_013_1.outputs[3].hide = True
    group_input_013_1.outputs[5].hide = True
    group_input_013_1.outputs[6].hide = True
    group_input_013_1.outputs[7].hide = True
    group_input_013_1.outputs[8].hide = True
    group_input_013_1.outputs[9].hide = True
    group_input_013_1.outputs[10].hide = True
    group_input_013_1.outputs[11].hide = True
    group_input_013_1.outputs[12].hide = True
    group_input_013_1.outputs[13].hide = True
    group_input_013_1.outputs[14].hide = True
    group_input_013_1.outputs[15].hide = True
    group_input_013_1.outputs[16].hide = True
    group_input_013_1.outputs[19].hide = True
    group_input_013_1.outputs[20].hide = True
    group_input_013_1.outputs[21].hide = True
    group_input_013_1.outputs[22].hide = True
    group_input_013_1.outputs[23].hide = True
    group_input_013_1.outputs[24].hide = True
    group_input_013_1.outputs[25].hide = True
    group_input_013_1.outputs[26].hide = True
    group_input_013_1.outputs[27].hide = True
    group_input_013_1.outputs[28].hide = True
    group_input_013_1.outputs[29].hide = True

    #node Group Input.014
    group_input_014_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_014_1.name = "Group Input.014"
    group_input_014_1.use_custom_color = True
    group_input_014_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_014_1.outputs[0].hide = True
    group_input_014_1.outputs[1].hide = True
    group_input_014_1.outputs[2].hide = True
    group_input_014_1.outputs[3].hide = True
    group_input_014_1.outputs[4].hide = True
    group_input_014_1.outputs[5].hide = True
    group_input_014_1.outputs[6].hide = True
    group_input_014_1.outputs[7].hide = True
    group_input_014_1.outputs[8].hide = True
    group_input_014_1.outputs[9].hide = True
    group_input_014_1.outputs[10].hide = True
    group_input_014_1.outputs[11].hide = True
    group_input_014_1.outputs[12].hide = True
    group_input_014_1.outputs[13].hide = True
    group_input_014_1.outputs[14].hide = True
    group_input_014_1.outputs[15].hide = True
    group_input_014_1.outputs[16].hide = True
    group_input_014_1.outputs[17].hide = True
    group_input_014_1.outputs[18].hide = True
    group_input_014_1.outputs[19].hide = True
    group_input_014_1.outputs[20].hide = True
    group_input_014_1.outputs[25].hide = True
    group_input_014_1.outputs[26].hide = True
    group_input_014_1.outputs[27].hide = True
    group_input_014_1.outputs[28].hide = True
    group_input_014_1.outputs[29].hide = True

    #node Group Input.008
    group_input_008_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_008_1.name = "Group Input.008"
    group_input_008_1.use_custom_color = True
    group_input_008_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_008_1.outputs[0].hide = True
    group_input_008_1.outputs[1].hide = True
    group_input_008_1.outputs[2].hide = True
    group_input_008_1.outputs[3].hide = True
    group_input_008_1.outputs[4].hide = True
    group_input_008_1.outputs[5].hide = True
    group_input_008_1.outputs[7].hide = True
    group_input_008_1.outputs[8].hide = True
    group_input_008_1.outputs[9].hide = True
    group_input_008_1.outputs[10].hide = True
    group_input_008_1.outputs[11].hide = True
    group_input_008_1.outputs[12].hide = True
    group_input_008_1.outputs[13].hide = True
    group_input_008_1.outputs[14].hide = True
    group_input_008_1.outputs[15].hide = True
    group_input_008_1.outputs[16].hide = True
    group_input_008_1.outputs[17].hide = True
    group_input_008_1.outputs[18].hide = True
    group_input_008_1.outputs[19].hide = True
    group_input_008_1.outputs[20].hide = True
    group_input_008_1.outputs[21].hide = True
    group_input_008_1.outputs[22].hide = True
    group_input_008_1.outputs[23].hide = True
    group_input_008_1.outputs[24].hide = True
    group_input_008_1.outputs[25].hide = True
    group_input_008_1.outputs[26].hide = True
    group_input_008_1.outputs[27].hide = True
    group_input_008_1.outputs[28].hide = True
    group_input_008_1.outputs[29].hide = True

    #node Group Input.011
    group_input_011 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.use_custom_color = True
    group_input_011.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[1].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[5].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True
    group_input_011.outputs[15].hide = True
    group_input_011.outputs[16].hide = True
    group_input_011.outputs[17].hide = True
    group_input_011.outputs[18].hide = True
    group_input_011.outputs[19].hide = True
    group_input_011.outputs[20].hide = True
    group_input_011.outputs[21].hide = True
    group_input_011.outputs[22].hide = True
    group_input_011.outputs[23].hide = True
    group_input_011.outputs[24].hide = True
    group_input_011.outputs[25].hide = True
    group_input_011.outputs[26].hide = True
    group_input_011.outputs[27].hide = True
    group_input_011.outputs[28].hide = True
    group_input_011.outputs[29].hide = True

    #node Group Input.004
    group_input_004 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.use_custom_color = True
    group_input_004.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True
    group_input_004.outputs[15].hide = True
    group_input_004.outputs[16].hide = True
    group_input_004.outputs[17].hide = True
    group_input_004.outputs[18].hide = True
    group_input_004.outputs[19].hide = True
    group_input_004.outputs[20].hide = True
    group_input_004.outputs[21].hide = True
    group_input_004.outputs[22].hide = True
    group_input_004.outputs[23].hide = True
    group_input_004.outputs[24].hide = True
    group_input_004.outputs[25].hide = True
    group_input_004.outputs[26].hide = True
    group_input_004.outputs[27].hide = True
    group_input_004.outputs[28].hide = True
    group_input_004.outputs[29].hide = True

    #node Set Position.002
    set_position_002 = eyelashgen.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    #Selection
    set_position_002.inputs[1].default_value = True
    #Offset
    set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Set Curve Radius
    set_curve_radius = eyelashgen.nodes.new("GeometryNodeSetCurveRadius")
    set_curve_radius.name = "Set Curve Radius"
    #Selection
    set_curve_radius.inputs[1].default_value = True

    #node Reroute.028
    reroute_028 = eyelashgen.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.socket_idname = "NodeSocketGeometry"
    #node Store Named Attribute.001
    store_named_attribute_001 = eyelashgen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.use_custom_color = True
    store_named_attribute_001.color = (0.5264300107955933, 0.23484696447849274, 0.7454490065574646)
    store_named_attribute_001.data_type = 'FLOAT'
    store_named_attribute_001.domain = 'POINT'
    #Selection
    store_named_attribute_001.inputs[1].default_value = True

    #node Spline Parameter.004
    spline_parameter_004 = eyelashgen.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_004.name = "Spline Parameter.004"
    spline_parameter_004.outputs[1].hide = True
    spline_parameter_004.outputs[2].hide = True

    #node Store Named Attribute
    store_named_attribute = eyelashgen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.use_custom_color = True
    store_named_attribute.color = (0.5264300107955933, 0.23484696447849274, 0.7454490065574646)
    store_named_attribute.data_type = 'FLOAT'
    store_named_attribute.domain = 'POINT'
    #Selection
    store_named_attribute.inputs[1].default_value = True

    #node Set Material
    set_material = eyelashgen.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Group Input.016
    group_input_016_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_016_1.name = "Group Input.016"
    group_input_016_1.use_custom_color = True
    group_input_016_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_016_1.outputs[0].hide = True
    group_input_016_1.outputs[1].hide = True
    group_input_016_1.outputs[3].hide = True
    group_input_016_1.outputs[4].hide = True
    group_input_016_1.outputs[5].hide = True
    group_input_016_1.outputs[6].hide = True
    group_input_016_1.outputs[7].hide = True
    group_input_016_1.outputs[8].hide = True
    group_input_016_1.outputs[9].hide = True
    group_input_016_1.outputs[10].hide = True
    group_input_016_1.outputs[11].hide = True
    group_input_016_1.outputs[12].hide = True
    group_input_016_1.outputs[13].hide = True
    group_input_016_1.outputs[14].hide = True
    group_input_016_1.outputs[15].hide = True
    group_input_016_1.outputs[16].hide = True
    group_input_016_1.outputs[17].hide = True
    group_input_016_1.outputs[18].hide = True
    group_input_016_1.outputs[19].hide = True
    group_input_016_1.outputs[20].hide = True
    group_input_016_1.outputs[21].hide = True
    group_input_016_1.outputs[22].hide = True
    group_input_016_1.outputs[23].hide = True
    group_input_016_1.outputs[24].hide = True
    group_input_016_1.outputs[25].hide = True
    group_input_016_1.outputs[26].hide = True
    group_input_016_1.outputs[27].hide = True
    group_input_016_1.outputs[28].hide = True
    group_input_016_1.outputs[29].hide = True

    #node Rotate Instances.001
    rotate_instances_001 = eyelashgen.nodes.new("GeometryNodeRotateInstances")
    rotate_instances_001.name = "Rotate Instances.001"
    #Selection
    rotate_instances_001.inputs[1].default_value = True
    #Pivot Point
    rotate_instances_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Local Space
    rotate_instances_001.inputs[4].default_value = True

    #node Switch
    switch_2 = eyelashgen.nodes.new("GeometryNodeSwitch")
    switch_2.name = "Switch"
    switch_2.input_type = 'FLOAT'

    #node Mesh to Curve
    mesh_to_curve = eyelashgen.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.mode = 'EDGES'
    #Selection
    mesh_to_curve.inputs[1].default_value = True

    #node Set Spline Type
    set_spline_type = eyelashgen.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type.name = "Set Spline Type"
    set_spline_type.spline_type = 'NURBS'
    #Selection
    set_spline_type.inputs[1].default_value = True

    #node Spline Parameter
    spline_parameter = eyelashgen.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"
    spline_parameter.outputs[1].hide = True
    spline_parameter.outputs[2].hide = True

    #node Capture Attribute
    capture_attribute_1 = eyelashgen.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_1.name = "Capture Attribute"
    capture_attribute_1.active_index = 0
    capture_attribute_1.capture_items.clear()
    capture_attribute_1.capture_items.new('FLOAT', "Value")
    capture_attribute_1.capture_items["Value"].data_type = 'FLOAT'
    capture_attribute_1.domain = 'POINT'

    #node Group Input
    group_input_4 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"
    group_input_4.outputs[1].hide = True
    group_input_4.outputs[2].hide = True
    group_input_4.outputs[3].hide = True
    group_input_4.outputs[4].hide = True
    group_input_4.outputs[5].hide = True
    group_input_4.outputs[6].hide = True
    group_input_4.outputs[7].hide = True
    group_input_4.outputs[8].hide = True
    group_input_4.outputs[9].hide = True
    group_input_4.outputs[10].hide = True
    group_input_4.outputs[11].hide = True
    group_input_4.outputs[12].hide = True
    group_input_4.outputs[13].hide = True
    group_input_4.outputs[14].hide = True
    group_input_4.outputs[15].hide = True
    group_input_4.outputs[16].hide = True
    group_input_4.outputs[17].hide = True
    group_input_4.outputs[18].hide = True
    group_input_4.outputs[19].hide = True
    group_input_4.outputs[20].hide = True
    group_input_4.outputs[21].hide = True
    group_input_4.outputs[22].hide = True
    group_input_4.outputs[23].hide = True
    group_input_4.outputs[24].hide = True
    group_input_4.outputs[25].hide = True
    group_input_4.outputs[26].hide = True
    group_input_4.outputs[27].hide = True
    group_input_4.outputs[28].hide = True
    group_input_4.outputs[29].hide = True

    #node Reroute.030
    reroute_030 = eyelashgen.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    reroute_030.socket_idname = "NodeSocketGeometry"
    #node Math.006
    math_006_1 = eyelashgen.nodes.new("ShaderNodeMath")
    math_006_1.label = "invert"
    math_006_1.name = "Math.006"
    math_006_1.operation = 'SUBTRACT'
    math_006_1.use_clamp = False
    #Value
    math_006_1.inputs[0].default_value = 1.0

    #node Group Input.017
    group_input_017_1 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_017_1.name = "Group Input.017"
    group_input_017_1.use_custom_color = True
    group_input_017_1.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_017_1.outputs[0].hide = True
    group_input_017_1.outputs[1].hide = True
    group_input_017_1.outputs[2].hide = True
    group_input_017_1.outputs[3].hide = True
    group_input_017_1.outputs[4].hide = True
    group_input_017_1.outputs[5].hide = True
    group_input_017_1.outputs[6].hide = True
    group_input_017_1.outputs[7].hide = True
    group_input_017_1.outputs[8].hide = True
    group_input_017_1.outputs[9].hide = True
    group_input_017_1.outputs[10].hide = True
    group_input_017_1.outputs[11].hide = True
    group_input_017_1.outputs[12].hide = True
    group_input_017_1.outputs[13].hide = True
    group_input_017_1.outputs[14].hide = True
    group_input_017_1.outputs[15].hide = True
    group_input_017_1.outputs[16].hide = True
    group_input_017_1.outputs[17].hide = True
    group_input_017_1.outputs[18].hide = True
    group_input_017_1.outputs[19].hide = True
    group_input_017_1.outputs[20].hide = True
    group_input_017_1.outputs[21].hide = True
    group_input_017_1.outputs[22].hide = True
    group_input_017_1.outputs[23].hide = True
    group_input_017_1.outputs[24].hide = True
    group_input_017_1.outputs[26].hide = True
    group_input_017_1.outputs[27].hide = True
    group_input_017_1.outputs[28].hide = True
    group_input_017_1.outputs[29].hide = True

    #node Group.002
    group_002_1 = eyelashgen.nodes.new("GeometryNodeGroup")
    group_002_1.name = "Group.002"
    group_002_1.node_tree = _ee_randomize_control
    #Socket_6
    group_002_1.inputs[2].default_value = 0.009999999776482582
    #Socket_2
    group_002_1.inputs[3].default_value = 0.5
    #Socket_3
    group_002_1.inputs[4].default_value = 2.0
    #Socket_4
    group_002_1.inputs[5].default_value = 0

    #node Group Input.010
    group_input_010 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.use_custom_color = True
    group_input_010.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[1].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True
    group_input_010.outputs[11].hide = True
    group_input_010.outputs[12].hide = True
    group_input_010.outputs[13].hide = True
    group_input_010.outputs[14].hide = True
    group_input_010.outputs[15].hide = True
    group_input_010.outputs[16].hide = True
    group_input_010.outputs[17].hide = True
    group_input_010.outputs[18].hide = True
    group_input_010.outputs[19].hide = True
    group_input_010.outputs[20].hide = True
    group_input_010.outputs[21].hide = True
    group_input_010.outputs[22].hide = True
    group_input_010.outputs[23].hide = True
    group_input_010.outputs[24].hide = True
    group_input_010.outputs[25].hide = True
    group_input_010.outputs[26].hide = True
    group_input_010.outputs[28].hide = True
    group_input_010.outputs[29].hide = True

    #node Group.003
    group_003_1 = eyelashgen.nodes.new("GeometryNodeGroup")
    group_003_1.name = "Group.003"
    group_003_1.node_tree = _ee_randomize_control
    #Socket_6
    group_003_1.inputs[2].default_value = 0.0010000000474974513
    #Socket_2
    group_003_1.inputs[3].default_value = 0.5
    #Socket_3
    group_003_1.inputs[4].default_value = 2.0

    #node Group Input.018
    group_input_018 = eyelashgen.nodes.new("NodeGroupInput")
    group_input_018.name = "Group Input.018"
    group_input_018.use_custom_color = True
    group_input_018.color = (0.624236524105072, 0.5231380462646484, 0.23704005777835846)
    group_input_018.outputs[0].hide = True
    group_input_018.outputs[1].hide = True
    group_input_018.outputs[2].hide = True
    group_input_018.outputs[3].hide = True
    group_input_018.outputs[5].hide = True
    group_input_018.outputs[6].hide = True
    group_input_018.outputs[7].hide = True
    group_input_018.outputs[8].hide = True
    group_input_018.outputs[9].hide = True
    group_input_018.outputs[10].hide = True
    group_input_018.outputs[11].hide = True
    group_input_018.outputs[12].hide = True
    group_input_018.outputs[13].hide = True
    group_input_018.outputs[14].hide = True
    group_input_018.outputs[15].hide = True
    group_input_018.outputs[16].hide = True
    group_input_018.outputs[17].hide = True
    group_input_018.outputs[18].hide = True
    group_input_018.outputs[19].hide = True
    group_input_018.outputs[20].hide = True
    group_input_018.outputs[21].hide = True
    group_input_018.outputs[22].hide = True
    group_input_018.outputs[23].hide = True
    group_input_018.outputs[24].hide = True
    group_input_018.outputs[25].hide = True
    group_input_018.outputs[26].hide = True
    group_input_018.outputs[27].hide = True
    group_input_018.outputs[29].hide = True

    #node String
    string = eyelashgen.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.string = "el_eyelash_gradient"

    #node String.001
    string_001 = eyelashgen.nodes.new("FunctionNodeInputString")
    string_001.name = "String.001"
    string_001.string = "el_hairs_gradient"

    #node String.002
    string_002 = eyelashgen.nodes.new("FunctionNodeInputString")
    string_002.name = "String.002"
    string_002.string = "el_ends_fade"

    #node Named Attribute
    named_attribute = eyelashgen.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'FLOAT'
    #Name
    named_attribute.inputs[0].default_value = "radius"

    #node Switch.001
    switch_001 = eyelashgen.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'FLOAT'
    #False
    switch_001.inputs[1].default_value = 1.0




    #Set parents
    capture_attribute_001_1.parent = frame_005
    position_001.parent = frame_005
    mix_003.parent = frame_002_1
    set_position_1.parent = frame_1
    random_value.parent = frame_1
    math.parent = frame_1
    reroute_020.parent = frame_1
    curve_line_1.parent = frame_006
    group.parent = frame_1
    group_input_002_3.parent = frame_1
    group_input_009_1.parent = frame_1
    group_input_006.parent = frame_002_1
    instance_on_points.parent = frame_006
    group_input_005_1.parent = frame_003_1
    mix_004.parent = frame_003_1
    position_2.parent = frame_001_1
    vector_rotate.parent = frame_001_1
    spline_parameter_001_1.parent = frame_001_1
    reroute_004_1.parent = frame_001_1
    reroute_005_1.parent = frame_001_1
    math_001_2.parent = frame_001_1
    realize_instances.parent = frame_004
    resample_curve_1.parent = frame_004
    id_1.parent = frame_010
    evaluate_on_domain.parent = frame_010
    float_curve.parent = frame_010
    math_002_3.parent = frame_010
    compare_1.parent = frame_012
    compare_001.parent = frame_012
    math_004_3.parent = frame_012
    boolean_math_001.parent = frame_012
    random_value_002.parent = frame_011
    mix_002_1.parent = frame_011
    boolean_math.parent = frame_011
    reroute_018.parent = frame_012
    reroute_009_1.parent = frame_013
    reroute_025.parent = frame_013
    mix_007_1.parent = frame_013
    reroute_026.parent = frame_013
    reroute_027.parent = frame_013
    mix_008.parent = frame_013
    math_005_1.parent = frame_013
    position_002.parent = frame_009
    spline_parameter_003_1.parent = frame_009
    reroute_019.parent = frame_009
    math_003_2.parent = frame_009
    vector_rotate_001.parent = frame_009
    vector_math_1.parent = frame_009
    random_value_001_1.parent = frame_009
    mix_2.parent = frame_009
    evaluate_on_domain_001.parent = frame_009
    id_001.parent = frame_009
    mix_006_1.parent = frame_001_1
    mix_001_2.parent = frame_010
    spline_parameter_002.parent = frame_010
    group_005.parent = frame_013
    group_004.parent = frame_013
    group_input_007.parent = frame_001_1
    group_input_012_1.parent = frame_012
    group_input_013_1.parent = frame_011
    group_input_014_1.parent = frame_013
    group_input_008_1.parent = frame_009
    group_input_011.parent = frame_009
    group_input_004.parent = frame_010
    spline_parameter.parent = frame_008
    capture_attribute_1.parent = frame_008
    group_002_1.parent = frame_007
    group_input_010.parent = frame_007
    group_003_1.parent = frame_010
    group_input_018.parent = frame_010

    #Set locations
    frame_005.location = (770.0, -204.0)
    frame_002_1.location = (1521.0, -357.0)
    frame_1.location = (-206.0, -253.0)
    frame_006.location = (1204.0, -173.5)
    frame_003_1.location = (1519.0, -559.0)
    frame_001_1.location = (2763.0, -208.0)
    frame_004.location = (2414.0, 126.0)
    frame_010.location = (4107.0, -133.0)
    frame_012.location = (5443.0, -132.0)
    frame_011.location = (5441.0, -401.0)
    frame_013.location = (5238.0, 347.0)
    frame_009.location = (3267.0, -157.0)
    frame_008.location = (-1501.0, -384.0)
    frame_007.location = (1204.0, -486.0)
    capture_attribute_001_1.location = (201.5948486328125, -36.152313232421875)
    position_001.location = (29.6610107421875, -41.69047546386719)
    reroute_015.location = (802.5923461914062, -594.6719970703125)
    align_euler_to_vector.location = (988.7794189453125, -448.0253601074219)
    align_euler_to_vector_001.location = (802.3024291992188, -402.51019287109375)
    mix_005.location = (1032.2939453125, -633.3995361328125)
    mix_003.location = (29.5133056640625, -40.529693603515625)
    reroute_007_1.location = (522.5789794921875, -122.29075622558594)
    reroute_011_1.location = (521.91015625, -160.94740295410156)
    reroute_012_1.location = (1205.2093505859375, -90.78250885009766)
    reroute_013_1.location = (1791.8433837890625, -90.78250885009766)
    set_position_1.location = (383.19586181640625, -36.05615234375)
    random_value.location = (385.0356140136719, -181.0723876953125)
    math.location = (195.52545166015625, -344.649169921875)
    reroute_020.location = (48.9117431640625, -92.26376342773438)
    set_curve_tilt.location = (-618.4385986328125, -341.79083251953125)
    curve_to_points.location = (-418.125, -230.33262634277344)
    set_point_radius.location = (-416.0403137207031, -195.24520874023438)
    reroute_010_1.location = (-152.7384490966797, -160.94740295410156)
    reroute_3.location = (1407.5679931640625, -785.0307006835938)
    reroute_002_1.location = (949.191650390625, -785.0307006835938)
    reroute_008_1.location = (-726.0435791015625, -785.0307006835938)
    curve_line_1.location = (29.936767578125, -36.321746826171875)
    reroute_006_1.location = (-153.5394287109375, -122.29075622558594)
    group.location = (194.953857421875, -242.99960327148438)
    group_001.location = (386.4449157714844, -292.1734313964844)
    group_input_002_3.location = (386.56854248046875, -334.00909423828125)
    group_input_009_1.location = (29.52032470703125, -347.836669921875)
    group_input_001_4.location = (-416.7564697265625, -424.4698791503906)
    group_input_003_2.location = (808.6829223632812, -680.5646362304688)
    group_input_006.location = (29.945556640625, -82.14657592773438)
    group_input_015_1.location = (386.3326110839844, -455.873291015625)
    instance_on_points.location = (32.527099609375, -71.74008178710938)
    store_named_attribute_002.location = (-818.7127075195312, -260.10186767578125)
    rotate_instances.location = (1980.1280517578125, -221.44854736328125)
    combine_xyz_1.location = (1761.242919921875, -350.74676513671875)
    group_input_005_1.location = (30.7137451171875, -89.57818603515625)
    mix_004.location = (30.4022216796875, -40.59844970703125)
    combine_xyz_001_1.location = (1762.555419921875, -556.6063232421875)
    position_2.location = (30.468017578125, -37.535369873046875)
    vector_rotate.location = (197.77392578125, -35.60791015625)
    spline_parameter_001_1.location = (29.74755859375, -183.51141357421875)
    reroute_004_1.location = (37.099609375, -134.7373046875)
    reroute_005_1.location = (37.099609375, -113.58929443359375)
    math_001_2.location = (197.67138671875, -182.47067260742188)
    reroute_003_2.location = (2599.874755859375, -785.0307006835938)
    reroute_017.location = (3815.36083984375, -785.0307006835938)
    realize_instances.location = (29.820556640625, -36.41355895996094)
    resample_curve_1.location = (196.049560546875, -37.262474060058594)
    reroute_021.location = (2615.9384765625, -122.29075622558594)
    reroute_022.location = (2615.9384765625, -90.78250885009766)
    reroute_016.location = (3146.646728515625, -160.94740295410156)
    reroute_023.location = (3146.646728515625, -122.29075622558594)
    reroute_001_3.location = (3145.593017578125, -90.78250885009766)
    id_1.location = (220.62890625, -148.92120361328125)
    evaluate_on_domain.location = (220.44677734375, -206.04632568359375)
    float_curve.location = (585.40234375, -146.22152709960938)
    math_002_3.location = (875.9716796875, -35.97648620605469)
    compare_1.location = (219.259765625, -40.532745361328125)
    compare_001.location = (219.19775390625, -84.04232788085938)
    math_004_3.location = (220.5966796875, -119.749755859375)
    boolean_math_001.location = (380.02392578125, -62.179962158203125)
    random_value_002.location = (213.2919921875, -36.520263671875)
    mix_002_1.location = (32.46875, -43.910064697265625)
    boolean_math.location = (383.11474609375, -35.592864990234375)
    reroute_024.location = (5358.31640625, -331.8680725097656)
    reroute_014.location = (5123.935546875, -785.0307006835938)
    set_position_001_1.location = (3323.2734375, 113.78012084960938)
    reroute_018.location = (98.2939453125, -88.84634399414062)
    reroute_009_1.location = (233.12841796875, -170.714111328125)
    reroute_025.location = (233.12841796875, -189.950439453125)
    mix_007_1.location = (228.12060546875, -35.91259765625)
    reroute_026.location = (367.09912109375, -170.714111328125)
    reroute_027.location = (367.09912109375, -189.950439453125)
    mix_008.location = (228.4541015625, -207.23269653320312)
    math_005_1.location = (586.00048828125, -159.091796875)
    boolean_math_002.location = (6082.92431640625, -305.1889953613281)
    curve_to_mesh_1.location = (6474.6572265625, -65.55762481689453)
    group_output_6.location = (6835.88818359375, -64.95771026611328)
    delete_geometry_001.location = (6292.44482421875, -65.55762481689453)
    curve_circle.location = (6474.6572265625, -195.7068328857422)
    position_002.location = (202.57080078125, -37.83863830566406)
    spline_parameter_003_1.location = (201.8505859375, -183.814697265625)
    reroute_019.location = (209.202392578125, -113.892578125)
    math_003_2.location = (369.77392578125, -182.77392578125)
    vector_rotate_001.location = (369.876953125, -35.91117858886719)
    vector_math_1.location = (202.556884765625, -145.16888427734375)
    random_value_001_1.location = (203.78857421875, -363.830810546875)
    mix_2.location = (203.620849609375, -253.00912475585938)
    evaluate_on_domain_001.location = (30.055419921875, -426.5260009765625)
    id_001.location = (30.238037109375, -369.40087890625)
    mix_006_1.location = (31.25830078125, -258.480224609375)
    mix_001_2.location = (31.67431640625, -103.97128295898438)
    spline_parameter_002.location = (402.22021484375, -378.61126708984375)
    group_005.location = (405.9794921875, -233.07852172851562)
    group_004.location = (405.9794921875, -94.8372802734375)
    group_input_007.location = (30.197998046875, -296.87945556640625)
    group_input_012_1.location = (30.3017578125, -142.23666381835938)
    group_input_013_1.location = (29.8564453125, -85.03158569335938)
    group_input_014_1.location = (30.24951171875, -106.92181396484375)
    group_input_008_1.location = (30.73828125, -297.9543762207031)
    group_input_011.location = (204.841064453125, -516.3284912109375)
    group_input_004.location = (29.8076171875, -140.33230590820312)
    set_position_002.location = (3880.798095703125, -70.6826400756836)
    set_curve_radius.location = (5239.86328125, -34.44737243652344)
    reroute_028.location = (4916.2783203125, -104.18264770507812)
    store_named_attribute_001.location = (4983.2763671875, 77.6964111328125)
    spline_parameter_004.location = (4777.94189453125, -22.74020004272461)
    store_named_attribute.location = (6082.92431640625, 37.86204147338867)
    set_material.location = (6661.95166015625, -65.55762481689453)
    group_input_016_1.location = (6661.95166015625, -195.7068328857422)
    rotate_instances_001.location = (2180.48828125, -221.44854736328125)
    switch_2.location = (-1058.0762939453125, -394.880126953125)
    mesh_to_curve.location = (-1833.3990478515625, -468.07879638671875)
    set_spline_type.location = (-1659.98779296875, -467.5935974121094)
    spline_parameter.location = (30.251220703125, -164.8385009765625)
    capture_attribute_1.location = (31.140380859375, -35.688690185546875)
    group_input_4.location = (-2017.349853515625, -468.07879638671875)
    reroute_030.location = (-1231.7822265625, -365.3141784667969)
    math_006_1.location = (-1238.4176025390625, -496.62481689453125)
    group_input_017_1.location = (-1237.3309326171875, -395.38140869140625)
    group_002_1.location = (30.1065673828125, -35.9349365234375)
    group_input_010.location = (30.2808837890625, -177.2078857421875)
    group_003_1.location = (402.59228515625, -59.08062744140625)
    group_input_018.location = (402.33251953125, -293.735107421875)
    string.location = (-818.7127075195312, -451.9625244140625)
    string_001.location = (4777.94189453125, 63.99867248535156)
    string_002.location = (6082.92431640625, -152.2086181640625)
    named_attribute.location = (6449.6572265625, -65.55762481689453)
    switch_001.location = (6449.6572265625, -65.55762481689453)

    #Set dimensions
    frame_005.width, frame_005.height = 372.0, 158.0
    frame_002_1.width, frame_002_1.height = 200.0, 186.0
    frame_1.width, frame_1.height = 557.0, 474.0
    frame_006.width, frame_006.height = 203.0, 308.5
    frame_003_1.width, frame_003_1.height = 201.0, 194.0
    frame_001_1.width, frame_001_1.height = 368.0, 401.0
    frame_004.width, frame_004.height = 366.0, 180.0
    frame_010.width, frame_010.height = 1046.0, 465.0
    frame_012.width, frame_012.height = 550.0, 246.0
    frame_011.width, frame_011.height = 553.0, 211.0
    frame_013.width, frame_013.height = 756.0, 360.0
    frame_009.width, frame_009.height = 540.0, 598.0
    frame_008.width, frame_008.height = 201.0, 247.0
    frame_007.width, frame_007.height = 200.0, 281.0
    capture_attribute_001_1.width, capture_attribute_001_1.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    reroute_015.width, reroute_015.height = 10.0, 100.0
    align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
    align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
    mix_005.width, mix_005.height = 140.0, 100.0
    mix_003.width, mix_003.height = 140.0, 100.0
    reroute_007_1.width, reroute_007_1.height = 10.0, 100.0
    reroute_011_1.width, reroute_011_1.height = 10.0, 100.0
    reroute_012_1.width, reroute_012_1.height = 10.0, 100.0
    reroute_013_1.width, reroute_013_1.height = 10.0, 100.0
    set_position_1.width, set_position_1.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    reroute_020.width, reroute_020.height = 10.0, 100.0
    set_curve_tilt.width, set_curve_tilt.height = 140.0, 100.0
    curve_to_points.width, curve_to_points.height = 140.0, 100.0
    set_point_radius.width, set_point_radius.height = 140.0, 100.0
    reroute_010_1.width, reroute_010_1.height = 10.0, 100.0
    reroute_3.width, reroute_3.height = 10.0, 100.0
    reroute_002_1.width, reroute_002_1.height = 10.0, 100.0
    reroute_008_1.width, reroute_008_1.height = 10.0, 100.0
    curve_line_1.width, curve_line_1.height = 140.0, 100.0
    reroute_006_1.width, reroute_006_1.height = 10.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    group_input_002_3.width, group_input_002_3.height = 140.0, 100.0
    group_input_009_1.width, group_input_009_1.height = 140.0, 100.0
    group_input_001_4.width, group_input_001_4.height = 140.0, 100.0
    group_input_003_2.width, group_input_003_2.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    group_input_015_1.width, group_input_015_1.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
    rotate_instances.width, rotate_instances.height = 140.0, 100.0
    combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
    group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
    mix_004.width, mix_004.height = 140.0, 100.0
    combine_xyz_001_1.width, combine_xyz_001_1.height = 140.0, 100.0
    position_2.width, position_2.height = 140.0, 100.0
    vector_rotate.width, vector_rotate.height = 140.0, 100.0
    spline_parameter_001_1.width, spline_parameter_001_1.height = 140.0, 100.0
    reroute_004_1.width, reroute_004_1.height = 10.0, 100.0
    reroute_005_1.width, reroute_005_1.height = 10.0, 100.0
    math_001_2.width, math_001_2.height = 140.0, 100.0
    reroute_003_2.width, reroute_003_2.height = 10.0, 100.0
    reroute_017.width, reroute_017.height = 10.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    resample_curve_1.width, resample_curve_1.height = 140.0, 100.0
    reroute_021.width, reroute_021.height = 10.0, 100.0
    reroute_022.width, reroute_022.height = 10.0, 100.0
    reroute_016.width, reroute_016.height = 10.0, 100.0
    reroute_023.width, reroute_023.height = 10.0, 100.0
    reroute_001_3.width, reroute_001_3.height = 10.0, 100.0
    id_1.width, id_1.height = 140.0, 100.0
    evaluate_on_domain.width, evaluate_on_domain.height = 140.0, 100.0
    float_curve.width, float_curve.height = 240.0, 100.0
    math_002_3.width, math_002_3.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    math_004_3.width, math_004_3.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    mix_002_1.width, mix_002_1.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    reroute_024.width, reroute_024.height = 10.0, 100.0
    reroute_014.width, reroute_014.height = 10.0, 100.0
    set_position_001_1.width, set_position_001_1.height = 140.0, 100.0
    reroute_018.width, reroute_018.height = 10.0, 100.0
    reroute_009_1.width, reroute_009_1.height = 10.0, 100.0
    reroute_025.width, reroute_025.height = 10.0, 100.0
    mix_007_1.width, mix_007_1.height = 140.0, 100.0
    reroute_026.width, reroute_026.height = 10.0, 100.0
    reroute_027.width, reroute_027.height = 10.0, 100.0
    mix_008.width, mix_008.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
    curve_to_mesh_1.width, curve_to_mesh_1.height = 140.0, 100.0
    group_output_6.width, group_output_6.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    spline_parameter_003_1.width, spline_parameter_003_1.height = 140.0, 100.0
    reroute_019.width, reroute_019.height = 10.0, 100.0
    math_003_2.width, math_003_2.height = 140.0, 100.0
    vector_rotate_001.width, vector_rotate_001.height = 140.0, 100.0
    vector_math_1.width, vector_math_1.height = 140.0, 100.0
    random_value_001_1.width, random_value_001_1.height = 140.0, 100.0
    mix_2.width, mix_2.height = 140.0, 100.0
    evaluate_on_domain_001.width, evaluate_on_domain_001.height = 140.0, 100.0
    id_001.width, id_001.height = 140.0, 100.0
    mix_006_1.width, mix_006_1.height = 140.0, 100.0
    mix_001_2.width, mix_001_2.height = 140.0, 100.0
    spline_parameter_002.width, spline_parameter_002.height = 140.0, 100.0
    group_005.width, group_005.height = 140.0, 100.0
    group_004.width, group_004.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    group_input_012_1.width, group_input_012_1.height = 140.0, 100.0
    group_input_013_1.width, group_input_013_1.height = 140.0, 100.0
    group_input_014_1.width, group_input_014_1.height = 140.0, 100.0
    group_input_008_1.width, group_input_008_1.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    set_curve_radius.width, set_curve_radius.height = 140.0, 100.0
    reroute_028.width, reroute_028.height = 10.0, 100.0
    store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
    spline_parameter_004.width, spline_parameter_004.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    group_input_016_1.width, group_input_016_1.height = 140.0, 100.0
    rotate_instances_001.width, rotate_instances_001.height = 140.0, 100.0
    switch_2.width, switch_2.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    set_spline_type.width, set_spline_type.height = 140.0, 100.0
    spline_parameter.width, spline_parameter.height = 140.0, 100.0
    capture_attribute_1.width, capture_attribute_1.height = 140.0, 100.0
    group_input_4.width, group_input_4.height = 140.0, 100.0
    reroute_030.width, reroute_030.height = 10.0, 100.0
    math_006_1.width, math_006_1.height = 140.0, 100.0
    group_input_017_1.width, group_input_017_1.height = 140.0, 100.0
    group_002_1.width, group_002_1.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    group_003_1.width, group_003_1.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    string.width, string.height = 140.0, 100.0
    string_001.width, string_001.height = 140.0, 100.0
    string_002.width, string_002.height = 140.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0

    #initialize eyelashgen links
    #group_input_4.Geometry -> mesh_to_curve.Mesh
    eyelashgen.links.new(group_input_4.outputs[0], mesh_to_curve.inputs[0])
    #set_curve_tilt.Curve -> curve_to_points.Curve
    eyelashgen.links.new(set_curve_tilt.outputs[0], curve_to_points.inputs[0])
    #curve_to_points.Points -> set_point_radius.Points
    eyelashgen.links.new(curve_to_points.outputs[0], set_point_radius.inputs[0])
    #set_material.Geometry -> group_output_6.Geometry
    eyelashgen.links.new(set_material.outputs[0], group_output_6.inputs[0])
    #mesh_to_curve.Curve -> set_spline_type.Curve
    eyelashgen.links.new(mesh_to_curve.outputs[0], set_spline_type.inputs[0])
    #random_value.Value -> set_position_1.Offset
    eyelashgen.links.new(random_value.outputs[0], set_position_1.inputs[3])
    #group.N -> random_value.Max
    eyelashgen.links.new(group.outputs[0], random_value.inputs[1])
    #group.-N -> random_value.Min
    eyelashgen.links.new(group.outputs[1], random_value.inputs[0])
    #math.Value -> group.N
    eyelashgen.links.new(math.outputs[0], group.inputs[0])
    #group_input_001_4.Count -> curve_to_points.Count
    eyelashgen.links.new(group_input_001_4.outputs[3], curve_to_points.inputs[1])
    #group_input_002_3.Seed -> random_value.Seed
    eyelashgen.links.new(group_input_002_3.outputs[4], random_value.inputs[8])
    #set_position_1.Geometry -> group_001.Geometry
    eyelashgen.links.new(set_position_1.outputs[0], group_001.inputs[0])
    #curve_line_1.Curve -> instance_on_points.Instance
    eyelashgen.links.new(curve_line_1.outputs[0], instance_on_points.inputs[2])
    #set_spline_type.Curve -> capture_attribute_1.Geometry
    eyelashgen.links.new(set_spline_type.outputs[0], capture_attribute_1.inputs[0])
    #spline_parameter.Factor -> capture_attribute_1.Value
    eyelashgen.links.new(spline_parameter.outputs[0], capture_attribute_1.inputs[1])
    #align_euler_to_vector.Rotation -> instance_on_points.Rotation
    eyelashgen.links.new(align_euler_to_vector.outputs[0], instance_on_points.inputs[5])
    #capture_attribute_001_1.Geometry -> instance_on_points.Points
    eyelashgen.links.new(capture_attribute_001_1.outputs[0], instance_on_points.inputs[0])
    #instance_on_points.Instances -> rotate_instances.Instances
    eyelashgen.links.new(instance_on_points.outputs[0], rotate_instances.inputs[0])
    #mix_003.Result -> combine_xyz_1.X
    eyelashgen.links.new(mix_003.outputs[0], combine_xyz_1.inputs[0])
    #reroute_3.Output -> mix_003.Factor
    eyelashgen.links.new(reroute_3.outputs[0], mix_003.inputs[0])
    #reroute_007_1.Output -> align_euler_to_vector_001.Vector
    eyelashgen.links.new(reroute_007_1.outputs[0], align_euler_to_vector_001.inputs[2])
    #resample_curve_1.Curve -> set_position_001_1.Geometry
    eyelashgen.links.new(resample_curve_1.outputs[0], set_position_001_1.inputs[0])
    #position_2.Position -> vector_rotate.Vector
    eyelashgen.links.new(position_2.outputs[0], vector_rotate.inputs[0])
    #vector_rotate.Vector -> set_position_001_1.Position
    eyelashgen.links.new(vector_rotate.outputs[0], set_position_001_1.inputs[2])
    #reroute_004_1.Output -> vector_rotate.Axis
    eyelashgen.links.new(reroute_004_1.outputs[0], vector_rotate.inputs[2])
    #rotate_instances_001.Instances -> realize_instances.Geometry
    eyelashgen.links.new(rotate_instances_001.outputs[0], realize_instances.inputs[0])
    #realize_instances.Geometry -> resample_curve_1.Curve
    eyelashgen.links.new(realize_instances.outputs[0], resample_curve_1.inputs[0])
    #group_001.Geometry -> capture_attribute_001_1.Geometry
    eyelashgen.links.new(group_001.outputs[0], capture_attribute_001_1.inputs[0])
    #position_001.Position -> capture_attribute_001_1.Value
    eyelashgen.links.new(position_001.outputs[0], capture_attribute_001_1.inputs[1])
    #reroute_005_1.Output -> vector_rotate.Center
    eyelashgen.links.new(reroute_005_1.outputs[0], vector_rotate.inputs[1])
    #spline_parameter_001_1.Factor -> math_001_2.Value
    eyelashgen.links.new(spline_parameter_001_1.outputs[0], math_001_2.inputs[0])
    #math_001_2.Value -> vector_rotate.Angle
    eyelashgen.links.new(math_001_2.outputs[0], vector_rotate.inputs[3])
    #reroute_002_1.Output -> reroute_3.Input
    eyelashgen.links.new(reroute_002_1.outputs[0], reroute_3.inputs[0])
    #reroute_003_2.Output -> mix_006_1.Factor
    eyelashgen.links.new(reroute_003_2.outputs[0], mix_006_1.inputs[0])
    #mix_006_1.Result -> math_001_2.Value
    eyelashgen.links.new(mix_006_1.outputs[0], math_001_2.inputs[1])
    #reroute_3.Output -> mix_004.Factor
    eyelashgen.links.new(reroute_3.outputs[0], mix_004.inputs[0])
    #reroute_3.Output -> reroute_003_2.Input
    eyelashgen.links.new(reroute_3.outputs[0], reroute_003_2.inputs[0])
    #reroute_021.Output -> reroute_004_1.Input
    eyelashgen.links.new(reroute_021.outputs[0], reroute_004_1.inputs[0])
    #reroute_022.Output -> reroute_005_1.Input
    eyelashgen.links.new(reroute_022.outputs[0], reroute_005_1.inputs[0])
    #group_002_1.Value -> instance_on_points.Scale
    eyelashgen.links.new(group_002_1.outputs[0], instance_on_points.inputs[6])
    #curve_to_points.Tangent -> reroute_006_1.Input
    eyelashgen.links.new(curve_to_points.outputs[1], reroute_006_1.inputs[0])
    #reroute_006_1.Output -> reroute_007_1.Input
    eyelashgen.links.new(reroute_006_1.outputs[0], reroute_007_1.inputs[0])
    #capture_attribute_001_1.Value -> reroute_012_1.Input
    eyelashgen.links.new(capture_attribute_001_1.outputs[1], reroute_012_1.inputs[0])
    #reroute_012_1.Output -> reroute_013_1.Input
    eyelashgen.links.new(reroute_012_1.outputs[0], reroute_013_1.inputs[0])
    #delete_geometry_001.Geometry -> curve_to_mesh_1.Curve
    eyelashgen.links.new(delete_geometry_001.outputs[0], curve_to_mesh_1.inputs[0])
    #curve_circle.Curve -> curve_to_mesh_1.Profile Curve
    eyelashgen.links.new(curve_circle.outputs[0], curve_to_mesh_1.inputs[1])
    #store_named_attribute_001.Geometry -> set_curve_radius.Curve
    eyelashgen.links.new(store_named_attribute_001.outputs[0], set_curve_radius.inputs[0])
    #math_002_3.Value -> set_curve_radius.Radius
    eyelashgen.links.new(math_002_3.outputs[0], set_curve_radius.inputs[2])
    #evaluate_on_domain.Value -> group_003_1.ID
    eyelashgen.links.new(evaluate_on_domain.outputs[0], group_003_1.inputs[5])
    #id_1.ID -> evaluate_on_domain.Value
    eyelashgen.links.new(id_1.outputs[0], evaluate_on_domain.inputs[0])
    #group_003_1.Value -> math_002_3.Value
    eyelashgen.links.new(group_003_1.outputs[0], math_002_3.inputs[0])
    #spline_parameter_002.Factor -> float_curve.Value
    eyelashgen.links.new(spline_parameter_002.outputs[0], float_curve.inputs[1])
    #float_curve.Value -> math_002_3.Value
    eyelashgen.links.new(float_curve.outputs[0], math_002_3.inputs[1])
    #reroute_015.Output -> align_euler_to_vector.Vector
    eyelashgen.links.new(reroute_015.outputs[0], align_euler_to_vector.inputs[2])
    #curve_to_points.Normal -> reroute_010_1.Input
    eyelashgen.links.new(curve_to_points.outputs[2], reroute_010_1.inputs[0])
    #reroute_010_1.Output -> reroute_011_1.Input
    eyelashgen.links.new(reroute_010_1.outputs[0], reroute_011_1.inputs[0])
    #reroute_011_1.Output -> reroute_015.Input
    eyelashgen.links.new(reroute_011_1.outputs[0], reroute_015.inputs[0])
    #reroute_011_1.Output -> reroute_016.Input
    eyelashgen.links.new(reroute_011_1.outputs[0], reroute_016.inputs[0])
    #reroute_016.Output -> vector_math_1.Vector
    eyelashgen.links.new(reroute_016.outputs[0], vector_math_1.inputs[1])
    #position_002.Position -> vector_rotate_001.Vector
    eyelashgen.links.new(position_002.outputs[0], vector_rotate_001.inputs[0])
    #vector_rotate_001.Vector -> set_position_002.Position
    eyelashgen.links.new(vector_rotate_001.outputs[0], set_position_002.inputs[2])
    #vector_math_1.Vector -> vector_rotate_001.Axis
    eyelashgen.links.new(vector_math_1.outputs[0], vector_rotate_001.inputs[2])
    #reroute_019.Output -> vector_rotate_001.Center
    eyelashgen.links.new(reroute_019.outputs[0], vector_rotate_001.inputs[1])
    #spline_parameter_003_1.Factor -> math_003_2.Value
    eyelashgen.links.new(spline_parameter_003_1.outputs[0], math_003_2.inputs[0])
    #math_003_2.Value -> vector_rotate_001.Angle
    eyelashgen.links.new(math_003_2.outputs[0], vector_rotate_001.inputs[3])
    #reroute_003_2.Output -> reroute_017.Input
    eyelashgen.links.new(reroute_003_2.outputs[0], reroute_017.inputs[0])
    #set_position_001_1.Geometry -> set_position_002.Geometry
    eyelashgen.links.new(set_position_001_1.outputs[0], set_position_002.inputs[0])
    #reroute_007_1.Output -> reroute_021.Input
    eyelashgen.links.new(reroute_007_1.outputs[0], reroute_021.inputs[0])
    #reroute_013_1.Output -> reroute_022.Input
    eyelashgen.links.new(reroute_013_1.outputs[0], reroute_022.inputs[0])
    #reroute_023.Output -> vector_math_1.Vector
    eyelashgen.links.new(reroute_023.outputs[0], vector_math_1.inputs[0])
    #reroute_021.Output -> reroute_023.Input
    eyelashgen.links.new(reroute_021.outputs[0], reroute_023.inputs[0])
    #reroute_001_3.Output -> reroute_019.Input
    eyelashgen.links.new(reroute_001_3.outputs[0], reroute_019.inputs[0])
    #reroute_022.Output -> reroute_001_3.Input
    eyelashgen.links.new(reroute_022.outputs[0], reroute_001_3.inputs[0])
    #id_001.ID -> evaluate_on_domain_001.Value
    eyelashgen.links.new(id_001.outputs[0], evaluate_on_domain_001.inputs[0])
    #evaluate_on_domain_001.Value -> random_value_001_1.ID
    eyelashgen.links.new(evaluate_on_domain_001.outputs[0], random_value_001_1.inputs[7])
    #random_value_001_1.Value -> mix_2.B
    eyelashgen.links.new(random_value_001_1.outputs[1], mix_2.inputs[3])
    #mix_2.Result -> math_003_2.Value
    eyelashgen.links.new(mix_2.outputs[0], math_003_2.inputs[1])
    #reroute_008_1.Output -> reroute_002_1.Input
    eyelashgen.links.new(reroute_008_1.outputs[0], reroute_002_1.inputs[0])
    #reroute_002_1.Output -> mix_005.Factor
    eyelashgen.links.new(reroute_002_1.outputs[0], mix_005.inputs[0])
    #mix_005.Result -> group_002_1.Control
    eyelashgen.links.new(mix_005.outputs[0], group_002_1.inputs[0])
    #group_input_003_2.Length 1 -> mix_005.A
    eyelashgen.links.new(group_input_003_2.outputs[7], mix_005.inputs[2])
    #group_input_003_2.Length 2 -> mix_005.B
    eyelashgen.links.new(group_input_003_2.outputs[8], mix_005.inputs[3])
    #store_named_attribute_002.Geometry -> set_curve_tilt.Curve
    eyelashgen.links.new(store_named_attribute_002.outputs[0], set_curve_tilt.inputs[0])
    #align_euler_to_vector_001.Rotation -> align_euler_to_vector.Rotation
    eyelashgen.links.new(align_euler_to_vector_001.outputs[0], align_euler_to_vector.inputs[0])
    #combine_xyz_1.Vector -> rotate_instances.Rotation
    eyelashgen.links.new(combine_xyz_1.outputs[0], rotate_instances.inputs[2])
    #group_input_005_1.Tilt 1 -> mix_004.A
    eyelashgen.links.new(group_input_005_1.outputs[15], mix_004.inputs[2])
    #group_input_005_1.Tilt 2 -> mix_004.B
    eyelashgen.links.new(group_input_005_1.outputs[16], mix_004.inputs[3])
    #group_input_006.Rotate 1 -> mix_003.A
    eyelashgen.links.new(group_input_006.outputs[11], mix_003.inputs[2])
    #group_input_006.Rotate 2 -> mix_003.B
    eyelashgen.links.new(group_input_006.outputs[12], mix_003.inputs[3])
    #group_input_007.Bend 1 -> mix_006_1.A
    eyelashgen.links.new(group_input_007.outputs[13], mix_006_1.inputs[2])
    #group_input_007.Bend 2 -> mix_006_1.B
    eyelashgen.links.new(group_input_007.outputs[14], mix_006_1.inputs[3])
    #group_input_008_1.Clump -> mix_2.Factor
    eyelashgen.links.new(group_input_008_1.outputs[6], mix_2.inputs[0])
    #group_input_009_1.Spread -> math.Value
    eyelashgen.links.new(group_input_009_1.outputs[5], math.inputs[0])
    #group_input_010.Seed -> group_002_1.Seed
    eyelashgen.links.new(group_input_010.outputs[4], group_002_1.inputs[6])
    #group_input_011.Seed -> random_value_001_1.Seed
    eyelashgen.links.new(group_input_011.outputs[4], random_value_001_1.inputs[8])
    #reroute_020.Output -> set_position_1.Geometry
    eyelashgen.links.new(reroute_020.outputs[0], set_position_1.inputs[0])
    #group_input_004.Thickness 1 -> mix_001_2.A
    eyelashgen.links.new(group_input_004.outputs[9], mix_001_2.inputs[2])
    #reroute_017.Output -> mix_001_2.Factor
    eyelashgen.links.new(reroute_017.outputs[0], mix_001_2.inputs[0])
    #group_input_004.Thickness 2 -> mix_001_2.B
    eyelashgen.links.new(group_input_004.outputs[10], mix_001_2.inputs[3])
    #mix_001_2.Result -> group_003_1.Control
    eyelashgen.links.new(mix_001_2.outputs[0], group_003_1.inputs[0])
    #curve_to_mesh_1.Mesh -> set_material.Geometry
    eyelashgen.links.new(curve_to_mesh_1.outputs[0], set_material.inputs[0])
    #mix_002_1.Result -> random_value_002.Probability
    eyelashgen.links.new(mix_002_1.outputs[0], random_value_002.inputs[6])
    #group_input_013_1.Density 1 -> mix_002_1.A
    eyelashgen.links.new(group_input_013_1.outputs[17], mix_002_1.inputs[2])
    #group_input_013_1.Density 2 -> mix_002_1.B
    eyelashgen.links.new(group_input_013_1.outputs[18], mix_002_1.inputs[3])
    #switch_2.Output -> reroute_008_1.Input
    eyelashgen.links.new(switch_2.outputs[0], reroute_008_1.inputs[0])
    #group_input_013_1.Seed -> random_value_002.Seed
    eyelashgen.links.new(group_input_013_1.outputs[4], random_value_002.inputs[8])
    #random_value_002.Value -> boolean_math.Boolean
    eyelashgen.links.new(random_value_002.outputs[3], boolean_math.inputs[0])
    #store_named_attribute.Geometry -> delete_geometry_001.Geometry
    eyelashgen.links.new(store_named_attribute.outputs[0], delete_geometry_001.inputs[0])
    #reroute_018.Output -> compare_1.A
    eyelashgen.links.new(reroute_018.outputs[0], compare_1.inputs[0])
    #reroute_017.Output -> reroute_014.Input
    eyelashgen.links.new(reroute_017.outputs[0], reroute_014.inputs[0])
    #math_004_3.Value -> compare_001.A
    eyelashgen.links.new(math_004_3.outputs[0], compare_001.inputs[0])
    #group_input_012_1.Trim 1 -> compare_1.B
    eyelashgen.links.new(group_input_012_1.outputs[19], compare_1.inputs[1])
    #group_input_012_1.Trim 2 -> compare_001.B
    eyelashgen.links.new(group_input_012_1.outputs[20], compare_001.inputs[1])
    #compare_001.Result -> boolean_math_001.Boolean
    eyelashgen.links.new(compare_001.outputs[0], boolean_math_001.inputs[1])
    #compare_1.Result -> boolean_math_001.Boolean
    eyelashgen.links.new(compare_1.outputs[0], boolean_math_001.inputs[0])
    #reroute_024.Output -> reroute_018.Input
    eyelashgen.links.new(reroute_024.outputs[0], reroute_018.inputs[0])
    #reroute_018.Output -> math_004_3.Value
    eyelashgen.links.new(reroute_018.outputs[0], math_004_3.inputs[1])
    #boolean_math_002.Boolean -> delete_geometry_001.Selection
    eyelashgen.links.new(boolean_math_002.outputs[0], delete_geometry_001.inputs[1])
    #reroute_024.Output -> mix_002_1.Factor
    eyelashgen.links.new(reroute_024.outputs[0], mix_002_1.inputs[0])
    #boolean_math.Boolean -> boolean_math_002.Boolean
    eyelashgen.links.new(boolean_math.outputs[0], boolean_math_002.inputs[1])
    #boolean_math_001.Boolean -> boolean_math_002.Boolean
    eyelashgen.links.new(boolean_math_001.outputs[0], boolean_math_002.inputs[0])
    #reroute_014.Output -> reroute_024.Input
    eyelashgen.links.new(reroute_014.outputs[0], reroute_024.inputs[0])
    #curve_to_points.Points -> reroute_020.Input
    eyelashgen.links.new(curve_to_points.outputs[0], reroute_020.inputs[0])
    #set_curve_radius.Curve -> store_named_attribute.Geometry
    eyelashgen.links.new(set_curve_radius.outputs[0], store_named_attribute.inputs[0])
    #math_005_1.Value -> store_named_attribute.Value
    eyelashgen.links.new(math_005_1.outputs[0], store_named_attribute.inputs[3])
    #group_004.Value -> math_005_1.Value
    eyelashgen.links.new(group_004.outputs[1], math_005_1.inputs[0])
    #mix_007_1.Result -> group_004.Position
    eyelashgen.links.new(mix_007_1.outputs[0], group_004.inputs[1])
    #group_005.Value -> math_005_1.Value
    eyelashgen.links.new(group_005.outputs[1], math_005_1.inputs[1])
    #mix_008.Result -> group_005.Position
    eyelashgen.links.new(mix_008.outputs[0], group_005.inputs[1])
    #group_input_014_1.Root Fade -> mix_007_1.Factor
    eyelashgen.links.new(group_input_014_1.outputs[21], mix_007_1.inputs[0])
    #reroute_026.Output -> group_004.Contrast
    eyelashgen.links.new(reroute_026.outputs[0], group_004.inputs[3])
    #group_input_014_1.Tip Fade -> mix_008.Factor
    eyelashgen.links.new(group_input_014_1.outputs[23], mix_008.inputs[0])
    #reroute_027.Output -> group_005.Contrast
    eyelashgen.links.new(reroute_027.outputs[0], group_005.inputs[3])
    #group_input_014_1.Root Contrast -> reroute_009_1.Input
    eyelashgen.links.new(group_input_014_1.outputs[22], reroute_009_1.inputs[0])
    #group_input_014_1.Tip Contrast -> reroute_025.Input
    eyelashgen.links.new(group_input_014_1.outputs[24], reroute_025.inputs[0])
    #reroute_009_1.Output -> reroute_026.Input
    eyelashgen.links.new(reroute_009_1.outputs[0], reroute_026.inputs[0])
    #reroute_025.Output -> reroute_027.Input
    eyelashgen.links.new(reroute_025.outputs[0], reroute_027.inputs[0])
    #group_input_015_1.Face Mesh -> group_001.Object
    eyelashgen.links.new(group_input_015_1.outputs[1], group_001.inputs[1])
    #group_input_015_1.Offset from Face -> group_001.Offset
    eyelashgen.links.new(group_input_015_1.outputs[26], group_001.inputs[2])
    #reroute_028.Output -> store_named_attribute_001.Geometry
    eyelashgen.links.new(reroute_028.outputs[0], store_named_attribute_001.inputs[0])
    #set_position_002.Geometry -> reroute_028.Input
    eyelashgen.links.new(set_position_002.outputs[0], reroute_028.inputs[0])
    #spline_parameter_004.Factor -> store_named_attribute_001.Value
    eyelashgen.links.new(spline_parameter_004.outputs[0], store_named_attribute_001.inputs[3])
    #reroute_030.Output -> store_named_attribute_002.Geometry
    eyelashgen.links.new(reroute_030.outputs[0], store_named_attribute_002.inputs[0])
    #switch_2.Output -> store_named_attribute_002.Value
    eyelashgen.links.new(switch_2.outputs[0], store_named_attribute_002.inputs[3])
    #group_input_016_1.Material -> set_material.Material
    eyelashgen.links.new(group_input_016_1.outputs[2], set_material.inputs[2])
    #rotate_instances.Instances -> rotate_instances_001.Instances
    eyelashgen.links.new(rotate_instances.outputs[0], rotate_instances_001.inputs[0])
    #combine_xyz_001_1.Vector -> rotate_instances_001.Rotation
    eyelashgen.links.new(combine_xyz_001_1.outputs[0], rotate_instances_001.inputs[2])
    #mix_004.Result -> combine_xyz_001_1.Y
    eyelashgen.links.new(mix_004.outputs[0], combine_xyz_001_1.inputs[1])
    #capture_attribute_1.Geometry -> reroute_030.Input
    eyelashgen.links.new(capture_attribute_1.outputs[0], reroute_030.inputs[0])
    #capture_attribute_1.Value -> math_006_1.Value
    eyelashgen.links.new(capture_attribute_1.outputs[1], math_006_1.inputs[1])
    #math_006_1.Value -> switch_2.True
    eyelashgen.links.new(math_006_1.outputs[0], switch_2.inputs[2])
    #capture_attribute_1.Value -> switch_2.False
    eyelashgen.links.new(capture_attribute_1.outputs[1], switch_2.inputs[1])
    #group_input_017_1.Flip Direction -> switch_2.Switch
    eyelashgen.links.new(group_input_017_1.outputs[25], switch_2.inputs[0])
    #group_input_010.Randomize Length -> group_002_1.Factor
    eyelashgen.links.new(group_input_010.outputs[27], group_002_1.inputs[1])
    #group_input_018.Randomize Thickness -> group_003_1.Factor
    eyelashgen.links.new(group_input_018.outputs[28], group_003_1.inputs[1])
    #group_input_018.Seed -> group_003_1.Seed
    eyelashgen.links.new(group_input_018.outputs[4], group_003_1.inputs[6])
    #string.String -> store_named_attribute_002.Name
    eyelashgen.links.new(string.outputs[0], store_named_attribute_002.inputs[2])
    #string_001.String -> store_named_attribute_001.Name
    eyelashgen.links.new(string_001.outputs[0], store_named_attribute_001.inputs[2])
    #string_002.String -> store_named_attribute.Name
    eyelashgen.links.new(string_002.outputs[0], store_named_attribute.inputs[2])
    #named_attribute.Exists -> switch_001.Switch
    eyelashgen.links.new(named_attribute.outputs[1], switch_001.inputs[0])
    #named_attribute.Attribute -> switch_001.True
    eyelashgen.links.new(named_attribute.outputs[0], switch_001.inputs[2])
    #switch_001.Output -> curve_to_mesh_1.Scale
    eyelashgen.links.new(switch_001.outputs[0], curve_to_mesh_1.inputs[2])
    return eyelashgen

eyelashgen = eyelashgen_node_group()

