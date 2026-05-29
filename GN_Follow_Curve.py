import bpy, mathutils

#initialize swizzle node group
def swizzle_node_group():
    swizzle = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Swizzle")

    swizzle.color_tag = 'NONE'
    swizzle.description = ""
    swizzle.default_group_node_width = 140
    


    #swizzle interface
    #Socket Output
    output_socket = swizzle.interface.new_socket(name = "Output", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    output_socket.default_value = (0.0, 0.0, 0.0)
    output_socket.min_value = -3.4028234663852886e+38
    output_socket.max_value = 3.4028234663852886e+38
    output_socket.subtype = 'NONE'
    output_socket.attribute_domain = 'POINT'
    output_socket.default_input = 'VALUE'
    output_socket.structure_type = 'AUTO'

    #Socket Swizzle
    swizzle_socket = swizzle.interface.new_socket(name = "Swizzle", in_out='INPUT', socket_type = 'NodeSocketMenu')
    swizzle_socket.attribute_domain = 'POINT'
    swizzle_socket.default_input = 'VALUE'
    swizzle_socket.structure_type = 'AUTO'

    #Socket Vector
    vector_socket = swizzle.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
    vector_socket.default_value = (0.0, 0.0, 0.0)
    vector_socket.min_value = -10000.0
    vector_socket.max_value = 10000.0
    vector_socket.subtype = 'NONE'
    vector_socket.attribute_domain = 'POINT'
    vector_socket.default_input = 'VALUE'
    vector_socket.structure_type = 'AUTO'

    #Socket Flip
    flip_socket = swizzle.interface.new_socket(name = "Flip", in_out='INPUT', socket_type = 'NodeSocketBool')
    flip_socket.default_value = False
    flip_socket.attribute_domain = 'POINT'
    flip_socket.default_input = 'VALUE'
    flip_socket.structure_type = 'AUTO'


    #initialize swizzle nodes
    #node Group Output
    group_output = swizzle.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = swizzle.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[2].hide = True

    #node Menu Switch
    menu_switch = swizzle.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.active_index = 2
    menu_switch.data_type = 'VECTOR'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("X")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Y")
    menu_switch.enum_items[1].description = ""
    menu_switch.enum_items.new("Z")
    menu_switch.enum_items[2].description = ""

    #node Separate XYZ.001
    separate_xyz_001 = swizzle.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    #node Combine XYZ
    combine_xyz = swizzle.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"

    #node Combine XYZ.001
    combine_xyz_001 = swizzle.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"

    #node Vector Math
    vector_math = swizzle.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    #Vector_001
    vector_math.inputs[1].default_value = (-1.0, -1.0, -1.0)

    #node Switch
    switch = swizzle.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'VECTOR'

    #node Group Input.001
    group_input_001 = swizzle.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[1].hide = True
    group_input_001.outputs[3].hide = True





    #Set locations
    group_output.location = (871.1921997070312, 39.059471130371094)
    group_input.location = (-537.0686645507812, 45.19986343383789)
    menu_switch.location = (286.9527282714844, 90.30404663085938)
    separate_xyz_001.location = (-272.9709167480469, -118.23011779785156)
    combine_xyz.location = (26.267539978027344, -42.892051696777344)
    combine_xyz_001.location = (24.886356353759766, -204.77481079101562)
    vector_math.location = (497.1737976074219, 37.639259338378906)
    switch.location = (684.446044921875, 161.0345001220703)
    group_input_001.location = (291.68902587890625, 196.08843994140625)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    menu_switch.width, menu_switch.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0

    #initialize swizzle links
    #separate_xyz_001.X -> combine_xyz.Y
    swizzle.links.new(separate_xyz_001.outputs[0], combine_xyz.inputs[1])
    #separate_xyz_001.Z -> combine_xyz_001.X
    swizzle.links.new(separate_xyz_001.outputs[2], combine_xyz_001.inputs[0])
    #separate_xyz_001.Y -> combine_xyz_001.Z
    swizzle.links.new(separate_xyz_001.outputs[1], combine_xyz_001.inputs[2])
    #separate_xyz_001.Z -> combine_xyz.Z
    swizzle.links.new(separate_xyz_001.outputs[2], combine_xyz.inputs[2])
    #separate_xyz_001.Y -> combine_xyz.X
    swizzle.links.new(separate_xyz_001.outputs[1], combine_xyz.inputs[0])
    #separate_xyz_001.X -> combine_xyz_001.Y
    swizzle.links.new(separate_xyz_001.outputs[0], combine_xyz_001.inputs[1])
    #group_input.Vector -> separate_xyz_001.Vector
    swizzle.links.new(group_input.outputs[1], separate_xyz_001.inputs[0])
    #group_input.Vector -> menu_switch.X
    swizzle.links.new(group_input.outputs[1], menu_switch.inputs[1])
    #group_input.Swizzle -> menu_switch.Menu
    swizzle.links.new(group_input.outputs[0], menu_switch.inputs[0])
    #combine_xyz.Vector -> menu_switch.Y
    swizzle.links.new(combine_xyz.outputs[0], menu_switch.inputs[2])
    #combine_xyz_001.Vector -> menu_switch.Z
    swizzle.links.new(combine_xyz_001.outputs[0], menu_switch.inputs[3])
    #menu_switch.Output -> vector_math.Vector
    swizzle.links.new(menu_switch.outputs[0], vector_math.inputs[0])
    #menu_switch.Output -> switch.False
    swizzle.links.new(menu_switch.outputs[0], switch.inputs[1])
    #vector_math.Vector -> switch.True
    swizzle.links.new(vector_math.outputs[0], switch.inputs[2])
    #switch.Output -> group_output.Output
    swizzle.links.new(switch.outputs[0], group_output.inputs[0])
    #group_input_001.Flip -> switch.Switch
    swizzle.links.new(group_input_001.outputs[2], switch.inputs[0])
    swizzle_socket.default_value = 'X'
    return swizzle

swizzle = swizzle_node_group()

#initialize follow_the_spline node group
def follow_the_spline_node_group():
    follow_the_spline = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Follow The Spline")

    follow_the_spline.color_tag = 'NONE'
    follow_the_spline.description = ""
    follow_the_spline.default_group_node_width = 140
    

    follow_the_spline.is_modifier = True

    #follow_the_spline interface
    #Socket Geometry
    geometry_socket = follow_the_spline.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = follow_the_spline.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Spline
    spline_socket = follow_the_spline.interface.new_socket(name = "Spline", in_out='INPUT', socket_type = 'NodeSocketObject')
    spline_socket.attribute_domain = 'POINT'
    spline_socket.default_input = 'VALUE'
    spline_socket.structure_type = 'AUTO'

    #Socket Offset
    offset_socket = follow_the_spline.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    offset_socket.default_value = 1.0
    offset_socket.min_value = 0.0
    offset_socket.max_value = 1.0
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'

    #Socket Direction
    direction_socket = follow_the_spline.interface.new_socket(name = "Direction", in_out='INPUT', socket_type = 'NodeSocketMenu')
    direction_socket.attribute_domain = 'POINT'
    direction_socket.default_input = 'VALUE'
    direction_socket.structure_type = 'AUTO'

    #Socket Flip
    flip_socket_1 = follow_the_spline.interface.new_socket(name = "Flip", in_out='INPUT', socket_type = 'NodeSocketBool')
    flip_socket_1.default_value = True
    flip_socket_1.attribute_domain = 'POINT'
    flip_socket_1.default_input = 'VALUE'
    flip_socket_1.structure_type = 'AUTO'

    #Socket Flip Faces
    flip_faces_socket = follow_the_spline.interface.new_socket(name = "Flip Faces", in_out='INPUT', socket_type = 'NodeSocketBool')
    flip_faces_socket.default_value = True
    flip_faces_socket.attribute_domain = 'POINT'
    flip_faces_socket.hide_value = True
    flip_faces_socket.default_input = 'VALUE'
    flip_faces_socket.structure_type = 'AUTO'


    #initialize follow_the_spline nodes
    #node Group Input
    group_input_1 = follow_the_spline.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    group_input_1.outputs[2].hide = True
    group_input_1.outputs[3].hide = True
    group_input_1.outputs[4].hide = True
    group_input_1.outputs[5].hide = True

    #node Group Output
    group_output_1 = follow_the_spline.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Object Info
    object_info = follow_the_spline.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'ORIGINAL'
    #As Instance
    object_info.inputs[1].default_value = False

    #node Sample Curve
    sample_curve = follow_the_spline.nodes.new("GeometryNodeSampleCurve")
    sample_curve.name = "Sample Curve"
    sample_curve.data_type = 'FLOAT'
    sample_curve.mode = 'LENGTH'
    sample_curve.use_all_curves = False
    #Curve Index
    sample_curve.inputs[4].default_value = 0

    #node Vector Math
    vector_math_1 = follow_the_spline.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.operation = 'CROSS_PRODUCT'

    #node Capture Attribute
    capture_attribute = follow_the_spline.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Position")
    capture_attribute.capture_items["Position"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'POINT'

    #node Position
    position = follow_the_spline.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Separate XYZ
    separate_xyz = follow_the_spline.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    #node Math
    math = follow_the_spline.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False

    #node Group Input.001
    group_input_001_1 = follow_the_spline.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[1].hide = True
    group_input_001_1.outputs[3].hide = True
    group_input_001_1.outputs[4].hide = True
    group_input_001_1.outputs[5].hide = True
    group_input_001_1.outputs[6].hide = True

    #node Vector Math.001
    vector_math_001 = follow_the_spline.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SCALE'

    #node Vector Math.002
    vector_math_002 = follow_the_spline.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'SCALE'

    #node Vector Math.003
    vector_math_003 = follow_the_spline.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'ADD'

    #node Set Position
    set_position = follow_the_spline.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Selection
    set_position.inputs[1].default_value = True

    #node Group
    group = follow_the_spline.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = swizzle

    #node Group Input.002
    group_input_002 = follow_the_spline.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True

    #node Group Input.003
    group_input_003 = follow_the_spline.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True

    #node Flip Faces
    flip_faces = follow_the_spline.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"

    #node Math.001
    math_001 = follow_the_spline.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Math.002
    math_002 = follow_the_spline.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False

    #node Radius
    radius = follow_the_spline.nodes.new("GeometryNodeInputRadius")
    radius.name = "Radius"

    #node Group Input.004
    group_input_004 = follow_the_spline.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[6].hide = True

    #node Curve Length
    curve_length = follow_the_spline.nodes.new("GeometryNodeCurveLength")
    curve_length.name = "Curve Length"

    #node Math.003
    math_003 = follow_the_spline.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'DIVIDE'
    math_003.use_clamp = False

    #node Math.004
    math_004 = follow_the_spline.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    #Value_001
    math_004.inputs[1].default_value = 2.0





    #Set locations
    group_input_1.location = (-740.0967407226562, -11.20303726196289)
    group_output_1.location = (1984.9736328125, 106.22718048095703)
    object_info.location = (-413.12469482421875, -75.7213363647461)
    sample_curve.location = (524.5151977539062, -75.03360748291016)
    vector_math_1.location = (865.9254150390625, -118.73609924316406)
    capture_attribute.location = (-390.86663818359375, 88.11512756347656)
    position.location = (-637.9134521484375, 98.77671813964844)
    separate_xyz.location = (65.60941314697266, 30.817583084106445)
    math.location = (282.7178039550781, -75.13851928710938)
    group_input_001_1.location = (-143.51466369628906, -243.07164001464844)
    vector_math_001.location = (1092.1007080078125, -7.473659515380859)
    vector_math_002.location = (1103.1500244140625, 159.9424285888672)
    vector_math_003.location = (1306.181396484375, 120.94477844238281)
    set_position.location = (1514.4552001953125, 254.8991241455078)
    group.location = (-138.46771240234375, 208.90701293945312)
    group_input_002.location = (-477.165771484375, 253.7421417236328)
    group_input_003.location = (-470.60693359375, 177.08734130859375)
    flip_faces.location = (1788.39111328125, 108.175537109375)
    math_001.location = (714.20751953125, 299.1640625)
    math_002.location = (715.70068359375, 122.65873718261719)
    radius.location = (-137.3846435546875, -319.89154052734375)
    group_input_004.location = (1521.5050048828125, 16.012348175048828)
    curve_length.location = (-112.90635681152344, -92.80178833007812)
    math_003.location = (59.86236572265625, -93.01927185058594)
    math_004.location = (158.80691528320312, -308.5959777832031)

    #Set dimensions
    group_input_1.width, group_input_1.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    sample_curve.width, sample_curve.height = 140.0, 100.0
    vector_math_1.width, vector_math_1.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    flip_faces.width, flip_faces.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    radius.width, radius.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    curve_length.width, curve_length.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0

    #initialize follow_the_spline links
    #flip_faces.Mesh -> group_output_1.Geometry
    follow_the_spline.links.new(flip_faces.outputs[0], group_output_1.inputs[0])
    #group_input_1.Spline -> object_info.Object
    follow_the_spline.links.new(group_input_1.outputs[1], object_info.inputs[0])
    #sample_curve.Tangent -> vector_math_1.Vector
    follow_the_spline.links.new(sample_curve.outputs[2], vector_math_1.inputs[0])
    #sample_curve.Normal -> vector_math_1.Vector
    follow_the_spline.links.new(sample_curve.outputs[3], vector_math_1.inputs[1])
    #group_input_1.Geometry -> capture_attribute.Geometry
    follow_the_spline.links.new(group_input_1.outputs[0], capture_attribute.inputs[0])
    #position.Position -> capture_attribute.Position
    follow_the_spline.links.new(position.outputs[0], capture_attribute.inputs[1])
    #math.Value -> sample_curve.Length
    follow_the_spline.links.new(math.outputs[0], sample_curve.inputs[3])
    #separate_xyz.X -> math.Value
    follow_the_spline.links.new(separate_xyz.outputs[0], math.inputs[0])
    #vector_math_1.Vector -> vector_math_001.Vector
    follow_the_spline.links.new(vector_math_1.outputs[0], vector_math_001.inputs[0])
    #sample_curve.Normal -> vector_math_002.Vector
    follow_the_spline.links.new(sample_curve.outputs[3], vector_math_002.inputs[0])
    #vector_math_002.Vector -> vector_math_003.Vector
    follow_the_spline.links.new(vector_math_002.outputs[0], vector_math_003.inputs[0])
    #vector_math_001.Vector -> vector_math_003.Vector
    follow_the_spline.links.new(vector_math_001.outputs[0], vector_math_003.inputs[1])
    #math_001.Value -> vector_math_002.Scale
    follow_the_spline.links.new(math_001.outputs[0], vector_math_002.inputs[3])
    #capture_attribute.Geometry -> set_position.Geometry
    follow_the_spline.links.new(capture_attribute.outputs[0], set_position.inputs[0])
    #vector_math_003.Vector -> set_position.Offset
    follow_the_spline.links.new(vector_math_003.outputs[0], set_position.inputs[3])
    #sample_curve.Position -> set_position.Position
    follow_the_spline.links.new(sample_curve.outputs[1], set_position.inputs[2])
    #capture_attribute.Position -> group.Vector
    follow_the_spline.links.new(capture_attribute.outputs[1], group.inputs[1])
    #group.Output -> separate_xyz.Vector
    follow_the_spline.links.new(group.outputs[0], separate_xyz.inputs[0])
    #group_input_002.Direction -> group.Swizzle
    follow_the_spline.links.new(group_input_002.outputs[3], group.inputs[0])
    #group_input_003.Flip -> group.Flip
    follow_the_spline.links.new(group_input_003.outputs[4], group.inputs[2])
    #set_position.Geometry -> flip_faces.Mesh
    follow_the_spline.links.new(set_position.outputs[0], flip_faces.inputs[0])
    #separate_xyz.Y -> math_001.Value
    follow_the_spline.links.new(separate_xyz.outputs[1], math_001.inputs[0])
    #separate_xyz.Z -> math_002.Value
    follow_the_spline.links.new(separate_xyz.outputs[2], math_002.inputs[0])
    #math_002.Value -> vector_math_001.Scale
    follow_the_spline.links.new(math_002.outputs[0], vector_math_001.inputs[3])
    #math_004.Value -> sample_curve.Value
    follow_the_spline.links.new(math_004.outputs[0], sample_curve.inputs[1])
    #sample_curve.Value -> math_002.Value
    follow_the_spline.links.new(sample_curve.outputs[0], math_002.inputs[1])
    #sample_curve.Value -> math_001.Value
    follow_the_spline.links.new(sample_curve.outputs[0], math_001.inputs[1])
    #group_input_004.Flip Faces -> flip_faces.Selection
    follow_the_spline.links.new(group_input_004.outputs[5], flip_faces.inputs[1])
    #object_info.Geometry -> curve_length.Curve
    follow_the_spline.links.new(object_info.outputs[4], curve_length.inputs[0])
    #object_info.Geometry -> sample_curve.Curves
    follow_the_spline.links.new(object_info.outputs[4], sample_curve.inputs[0])
    #curve_length.Length -> math_003.Value
    follow_the_spline.links.new(curve_length.outputs[0], math_003.inputs[0])
    #math_003.Value -> math.Value
    follow_the_spline.links.new(math_003.outputs[0], math.inputs[1])
    #group_input_001_1.Offset -> math_003.Value
    follow_the_spline.links.new(group_input_001_1.outputs[2], math_003.inputs[1])
    #radius.Radius -> math_004.Value
    follow_the_spline.links.new(radius.outputs[0], math_004.inputs[0])
    direction_socket.default_value = 'X'
    return follow_the_spline

follow_the_spline = follow_the_spline_node_group()

