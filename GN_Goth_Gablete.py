import bpy, mathutils

#initialize curve_to_mesh_even node group
def curve_to_mesh_even_node_group():
    curve_to_mesh_even = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Curve To Mesh Even")

    curve_to_mesh_even.color_tag = 'NONE'
    curve_to_mesh_even.description = ""
    curve_to_mesh_even.default_group_node_width = 140
    


    #curve_to_mesh_even interface
    #Socket Geometry
    geometry_socket = curve_to_mesh_even.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Curve
    curve_socket = curve_to_mesh_even.interface.new_socket(name = "Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    curve_socket.attribute_domain = 'POINT'
    curve_socket.default_input = 'VALUE'
    curve_socket.structure_type = 'AUTO'

    #Socket Profile Curve
    profile_curve_socket = curve_to_mesh_even.interface.new_socket(name = "Profile Curve", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    profile_curve_socket.attribute_domain = 'POINT'
    profile_curve_socket.default_input = 'VALUE'
    profile_curve_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = curve_to_mesh_even.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.description = "Scale of the profile at each point"
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Fill Caps
    fill_caps_socket = curve_to_mesh_even.interface.new_socket(name = "Fill Caps", in_out='INPUT', socket_type = 'NodeSocketBool')
    fill_caps_socket.default_value = False
    fill_caps_socket.attribute_domain = 'POINT'
    fill_caps_socket.description = "If the profile spline is cyclic, fill the ends of the generated mesh with N-gons"
    fill_caps_socket.default_input = 'VALUE'
    fill_caps_socket.structure_type = 'AUTO'


    #initialize curve_to_mesh_even nodes
    #node Group Output
    group_output = curve_to_mesh_even.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = curve_to_mesh_even.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True

    #node Curve to Mesh
    curve_to_mesh = curve_to_mesh_even.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"

    #node Vector Math.002
    vector_math_002 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'DOT_PRODUCT'

    #node Curve Tangent
    curve_tangent = curve_to_mesh_even.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    #node Curve Handle Positions
    curve_handle_positions = curve_to_mesh_even.nodes.new("GeometryNodeInputCurveHandlePositions")
    curve_handle_positions.name = "Curve Handle Positions"
    #Relative
    curve_handle_positions.inputs[0].default_value = True

    #node Vector Math.004
    vector_math_004 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'NORMALIZE'

    #node Math.002
    math_002 = curve_to_mesh_even.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False
    #Value
    math_002.inputs[0].default_value = 1.0

    #node Frame
    frame = curve_to_mesh_even.nodes.new("NodeFrame")
    frame.label = "Scale"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Position
    position = curve_to_mesh_even.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Curve Handle Positions.001
    curve_handle_positions_001 = curve_to_mesh_even.nodes.new("GeometryNodeInputCurveHandlePositions")
    curve_handle_positions_001.name = "Curve Handle Positions.001"
    #Relative
    curve_handle_positions_001.inputs[0].default_value = True

    #node Curve Tangent.001
    curve_tangent_001 = curve_to_mesh_even.nodes.new("GeometryNodeInputTangent")
    curve_tangent_001.name = "Curve Tangent.001"

    #node Vector Math
    vector_math = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'CROSS_PRODUCT'

    #node Vector Math.001
    vector_math_001 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'NORMALIZE'

    #node Vector Math.003
    vector_math_003 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'CROSS_PRODUCT'

    #node Frame.001
    frame_001 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_001.label = "Direction Out"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Position.001
    position_001 = curve_to_mesh_even.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    #node Vector Math.005
    vector_math_005 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = 'SUBTRACT'

    #node Frame.002
    frame_002 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_002.label = "Relative Position"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Vector Math.006
    vector_math_006 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = 'DOT_PRODUCT'

    #node Frame.003
    frame_003 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_003.label = "X Component"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Vector Math.007
    vector_math_007 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.operation = 'CROSS_PRODUCT'

    #node Vector Math.008
    vector_math_008 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_008.name = "Vector Math.008"
    vector_math_008.operation = 'LENGTH'

    #node Frame.004
    frame_004 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_004.label = "Y Component"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    #node Store Named Attribute
    store_named_attribute = curve_to_mesh_even.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'FLOAT_VECTOR'
    store_named_attribute.domain = 'POINT'
    #Selection
    store_named_attribute.inputs[1].default_value = True
    #Name
    store_named_attribute.inputs[2].default_value = "direction_out"

    #node Named Attribute
    named_attribute = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'FLOAT_VECTOR'
    #Name
    named_attribute.inputs[0].default_value = "direction_out"

    #node Named Attribute.001
    named_attribute_001 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = 'FLOAT_VECTOR'
    #Name
    named_attribute_001.inputs[0].default_value = "direction_out"

    #node Named Attribute.002
    named_attribute_002 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.data_type = 'FLOAT_VECTOR'
    #Name
    named_attribute_002.inputs[0].default_value = "direction_out"

    #node Store Named Attribute.001
    store_named_attribute_001 = curve_to_mesh_even.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = 'FLOAT'
    store_named_attribute_001.domain = 'POINT'
    #Selection
    store_named_attribute_001.inputs[1].default_value = True
    #Name
    store_named_attribute_001.inputs[2].default_value = "radius_scale"

    #node Named Attribute.003
    named_attribute_003 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.data_type = 'FLOAT'
    #Name
    named_attribute_003.inputs[0].default_value = "radius_scale"

    #node Math
    math = curve_to_mesh_even.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    #node Frame.005
    frame_005 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_005.label = "Stretch X Component"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    #node Named Attribute.004
    named_attribute_004 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_004.name = "Named Attribute.004"
    named_attribute_004.data_type = 'FLOAT_VECTOR'
    #Name
    named_attribute_004.inputs[0].default_value = "direction_out"

    #node Vector Math.009
    vector_math_009 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_009.name = "Vector Math.009"
    vector_math_009.operation = 'SCALE'

    #node Frame.006
    frame_006 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_006.label = "X Vector"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    #node Store Named Attribute.002
    store_named_attribute_002 = curve_to_mesh_even.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.data_type = 'FLOAT_VECTOR'
    store_named_attribute_002.domain = 'POINT'
    #Selection
    store_named_attribute_002.inputs[1].default_value = True
    #Name
    store_named_attribute_002.inputs[2].default_value = "CP_position"

    #node Named Attribute.005
    named_attribute_005 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_005.name = "Named Attribute.005"
    named_attribute_005.data_type = 'FLOAT_VECTOR'
    #Name
    named_attribute_005.inputs[0].default_value = "CP_position"

    #node Vector Math.011
    vector_math_011 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_011.name = "Vector Math.011"
    vector_math_011.operation = 'CROSS_PRODUCT'

    #node Vector Math.012
    vector_math_012 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_012.name = "Vector Math.012"
    vector_math_012.operation = 'CROSS_PRODUCT'

    #node Vector Math.013
    vector_math_013 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_013.name = "Vector Math.013"
    vector_math_013.operation = 'NORMALIZE'

    #node Vector Math.014
    vector_math_014 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_014.name = "Vector Math.014"
    vector_math_014.operation = 'SCALE'

    #node Frame.007
    frame_007 = curve_to_mesh_even.nodes.new("NodeFrame")
    frame_007.label = "Y Vector"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    #node Vector Math.010
    vector_math_010 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_010.name = "Vector Math.010"
    vector_math_010.operation = 'ADD'

    #node Vector Math.015
    vector_math_015 = curve_to_mesh_even.nodes.new("ShaderNodeVectorMath")
    vector_math_015.name = "Vector Math.015"
    vector_math_015.operation = 'ADD'

    #node Named Attribute.006
    named_attribute_006 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_006.name = "Named Attribute.006"
    named_attribute_006.data_type = 'FLOAT_VECTOR'
    #Name
    named_attribute_006.inputs[0].default_value = "CP_position"

    #node Set Position
    set_position = curve_to_mesh_even.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Compare
    compare = curve_to_mesh_even.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'NOT_EQUAL'
    #B
    compare.inputs[1].default_value = 1.0
    #Epsilon
    compare.inputs[12].default_value = 0.0010000000474974513

    #node Named Attribute.007
    named_attribute_007 = curve_to_mesh_even.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_007.name = "Named Attribute.007"
    named_attribute_007.data_type = 'FLOAT'
    #Name
    named_attribute_007.inputs[0].default_value = "radius_scale"

    #node Set Spline Type
    set_spline_type = curve_to_mesh_even.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type.name = "Set Spline Type"
    set_spline_type.spline_type = 'BEZIER'
    #Selection
    set_spline_type.inputs[1].default_value = True

    #node Group Input.001
    group_input_001 = curve_to_mesh_even.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[4].hide = True




    #Set parents
    vector_math_002.parent = frame
    curve_tangent.parent = frame
    curve_handle_positions.parent = frame
    vector_math_004.parent = frame
    math_002.parent = frame
    curve_handle_positions_001.parent = frame_001
    curve_tangent_001.parent = frame_001
    vector_math.parent = frame_001
    vector_math_001.parent = frame_001
    vector_math_003.parent = frame_001
    position_001.parent = frame_002
    vector_math_005.parent = frame_002
    vector_math_006.parent = frame_003
    vector_math_007.parent = frame_004
    vector_math_008.parent = frame_004
    named_attribute.parent = frame_007
    named_attribute_001.parent = frame_003
    named_attribute_002.parent = frame_004
    named_attribute_003.parent = frame_005
    math.parent = frame_005
    named_attribute_004.parent = frame_006
    vector_math_009.parent = frame_006
    named_attribute_005.parent = frame_002
    vector_math_011.parent = frame_007
    vector_math_012.parent = frame_007
    vector_math_013.parent = frame_007
    vector_math_014.parent = frame_007

    #Set locations
    group_output.location = (2106.822998046875, 169.34332275390625)
    group_input.location = (-1725.4864501953125, 471.395751953125)
    curve_to_mesh.location = (-219.33807373046875, 457.4913024902344)
    vector_math_002.location = (453.5108642578125, -55.90892028808594)
    curve_tangent.location = (216.093505859375, -41.50370788574219)
    curve_handle_positions.location = (29.6954345703125, -150.22451782226562)
    vector_math_004.location = (250.5068359375, -128.96047973632812)
    math_002.location = (638.0433349609375, -35.65473937988281)
    frame.location = (-1908.0, 229.0)
    position.location = (-1525.3111572265625, 305.25732421875)
    curve_handle_positions_001.location = (37.5245361328125, -37.1571044921875)
    curve_tangent_001.location = (29.775634765625, -169.3043212890625)
    vector_math.location = (275.36865234375, -36.18682861328125)
    vector_math_001.location = (659.1822509765625, -55.63580322265625)
    vector_math_003.location = (475.4893798828125, -84.06121826171875)
    frame_001.location = (-1882.0, -104.0)
    position_001.location = (29.899658203125, -36.10670471191406)
    vector_math_005.location = (245.55511474609375, -51.86155700683594)
    frame_002.location = (-655.0, 225.0)
    vector_math_006.location = (199.99847412109375, -41.696685791015625)
    frame_003.location = (-138.0, 286.0)
    vector_math_007.location = (235.82464599609375, -35.51715087890625)
    vector_math_008.location = (405.13226318359375, -40.7626953125)
    frame_004.location = (-161.0, 37.0)
    store_named_attribute.location = (-830.2440185546875, 487.841064453125)
    named_attribute.location = (29.65655517578125, -72.69342041015625)
    named_attribute_001.location = (30.16204833984375, -35.58622741699219)
    named_attribute_002.location = (30.07098388671875, -40.989898681640625)
    store_named_attribute_001.location = (-1013.6911010742188, 497.12762451171875)
    named_attribute_003.location = (30.24176025390625, -35.76702880859375)
    math.location = (205.31671142578125, -65.07537841796875)
    frame_005.location = (289.0, 341.0)
    named_attribute_004.location = (30.15191650390625, -43.58349609375)
    vector_math_009.location = (224.05694580078125, -35.6851806640625)
    frame_006.location = (723.0, 328.0)
    store_named_attribute_002.location = (-1296.3187255859375, 498.7686462402344)
    named_attribute_005.location = (46.62091064453125, -116.89736938476562)
    vector_math_011.location = (262.69830322265625, -75.25439453125)
    vector_math_012.location = (505.40411376953125, -59.72320556640625)
    vector_math_013.location = (730.6514282226562, -79.84942626953125)
    vector_math_014.location = (1034.50830078125, -35.834716796875)
    frame_007.location = (-444.0, -185.0)
    vector_math_010.location = (1268.57470703125, 110.77999877929688)
    vector_math_015.location = (1494.831787109375, 244.63436889648438)
    named_attribute_006.location = (1262.369384765625, 286.2212829589844)
    set_position.location = (1916.822998046875, 409.9048156738281)
    compare.location = (1646.718017578125, 611.990966796875)
    named_attribute_007.location = (1411.5732421875, 573.896240234375)
    set_spline_type.location = (-1518.0635986328125, 494.8600769042969)
    group_input_001.location = (-476.35693359375, 381.10260009765625)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    curve_tangent.width, curve_tangent.height = 140.0, 100.0
    curve_handle_positions.width, curve_handle_positions.height = 150.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    frame.width, frame.height = 808.0, 277.0
    position.width, position.height = 140.0, 100.0
    curve_handle_positions_001.width, curve_handle_positions_001.height = 150.0, 100.0
    curve_tangent_001.width, curve_tangent_001.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    frame_001.width, frame_001.height = 829.0, 249.0
    position_001.width, position_001.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    frame_002.width, frame_002.height = 416.0, 268.0
    vector_math_006.width, vector_math_006.height = 140.0, 100.0
    frame_003.width, frame_003.height = 370.0, 195.0
    vector_math_007.width, vector_math_007.height = 140.0, 100.0
    vector_math_008.width, vector_math_008.height = 140.0, 100.0
    frame_004.width, frame_004.height = 575.0, 192.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
    named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
    store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
    named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    frame_005.width, frame_005.height = 375.0, 243.0
    named_attribute_004.width, named_attribute_004.height = 140.0, 100.0
    vector_math_009.width, vector_math_009.height = 140.0, 100.0
    frame_006.width, frame_006.height = 394.0, 195.0
    store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
    named_attribute_005.width, named_attribute_005.height = 140.0, 100.0
    vector_math_011.width, vector_math_011.height = 140.0, 100.0
    vector_math_012.width, vector_math_012.height = 140.0, 100.0
    vector_math_013.width, vector_math_013.height = 140.0, 100.0
    vector_math_014.width, vector_math_014.height = 140.0, 100.0
    frame_007.width, frame_007.height = 1205.0, 230.0
    vector_math_010.width, vector_math_010.height = 140.0, 100.0
    vector_math_015.width, vector_math_015.height = 140.0, 100.0
    named_attribute_006.width, named_attribute_006.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    named_attribute_007.width, named_attribute_007.height = 140.0, 100.0
    set_spline_type.width, set_spline_type.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0

    #initialize curve_to_mesh_even links
    #named_attribute.Attribute -> vector_math_012.Vector
    curve_to_mesh_even.links.new(named_attribute.outputs[0], vector_math_012.inputs[0])
    #curve_tangent.Tangent -> vector_math_002.Vector
    curve_to_mesh_even.links.new(curve_tangent.outputs[0], vector_math_002.inputs[0])
    #set_spline_type.Curve -> store_named_attribute_002.Geometry
    curve_to_mesh_even.links.new(set_spline_type.outputs[0], store_named_attribute_002.inputs[0])
    #vector_math_012.Vector -> vector_math_013.Vector
    curve_to_mesh_even.links.new(vector_math_012.outputs[0], vector_math_013.inputs[0])
    #math.Value -> vector_math_009.Scale
    curve_to_mesh_even.links.new(math.outputs[0], vector_math_009.inputs[3])
    #curve_to_mesh.Mesh -> set_position.Geometry
    curve_to_mesh_even.links.new(curve_to_mesh.outputs[0], set_position.inputs[0])
    #vector_math_003.Vector -> vector_math_001.Vector
    curve_to_mesh_even.links.new(vector_math_003.outputs[0], vector_math_001.inputs[0])
    #vector_math_008.Value -> vector_math_014.Scale
    curve_to_mesh_even.links.new(vector_math_008.outputs[1], vector_math_014.inputs[3])
    #vector_math_011.Vector -> vector_math_012.Vector
    curve_to_mesh_even.links.new(vector_math_011.outputs[0], vector_math_012.inputs[1])
    #position.Position -> store_named_attribute_002.Value
    curve_to_mesh_even.links.new(position.outputs[0], store_named_attribute_002.inputs[3])
    #curve_handle_positions_001.Right -> vector_math.Vector
    curve_to_mesh_even.links.new(curve_handle_positions_001.outputs[1], vector_math.inputs[0])
    #curve_handle_positions.Right -> vector_math_004.Vector
    curve_to_mesh_even.links.new(curve_handle_positions.outputs[1], vector_math_004.inputs[0])
    #curve_tangent_001.Tangent -> vector_math.Vector
    curve_to_mesh_even.links.new(curve_tangent_001.outputs[0], vector_math.inputs[1])
    #vector_math.Vector -> vector_math_003.Vector
    curve_to_mesh_even.links.new(vector_math.outputs[0], vector_math_003.inputs[0])
    #vector_math_015.Vector -> set_position.Position
    curve_to_mesh_even.links.new(vector_math_015.outputs[0], set_position.inputs[2])
    #named_attribute_005.Attribute -> vector_math_005.Vector
    curve_to_mesh_even.links.new(named_attribute_005.outputs[0], vector_math_005.inputs[1])
    #store_named_attribute_002.Geometry -> store_named_attribute_001.Geometry
    curve_to_mesh_even.links.new(store_named_attribute_002.outputs[0], store_named_attribute_001.inputs[0])
    #store_named_attribute.Geometry -> curve_to_mesh.Curve
    curve_to_mesh_even.links.new(store_named_attribute.outputs[0], curve_to_mesh.inputs[0])
    #vector_math_006.Value -> math.Value
    curve_to_mesh_even.links.new(vector_math_006.outputs[1], math.inputs[1])
    #vector_math_009.Vector -> vector_math_010.Vector
    curve_to_mesh_even.links.new(vector_math_009.outputs[0], vector_math_010.inputs[0])
    #vector_math_013.Vector -> vector_math_014.Vector
    curve_to_mesh_even.links.new(vector_math_013.outputs[0], vector_math_014.inputs[0])
    #named_attribute_003.Attribute -> math.Value
    curve_to_mesh_even.links.new(named_attribute_003.outputs[0], math.inputs[0])
    #named_attribute_006.Attribute -> vector_math_015.Vector
    curve_to_mesh_even.links.new(named_attribute_006.outputs[0], vector_math_015.inputs[0])
    #named_attribute_002.Attribute -> vector_math_007.Vector
    curve_to_mesh_even.links.new(named_attribute_002.outputs[0], vector_math_007.inputs[0])
    #named_attribute_007.Attribute -> compare.A
    curve_to_mesh_even.links.new(named_attribute_007.outputs[0], compare.inputs[0])
    #math_002.Value -> store_named_attribute_001.Value
    curve_to_mesh_even.links.new(math_002.outputs[0], store_named_attribute_001.inputs[3])
    #store_named_attribute_001.Geometry -> store_named_attribute.Geometry
    curve_to_mesh_even.links.new(store_named_attribute_001.outputs[0], store_named_attribute.inputs[0])
    #position_001.Position -> vector_math_005.Vector
    curve_to_mesh_even.links.new(position_001.outputs[0], vector_math_005.inputs[0])
    #named_attribute.Attribute -> vector_math_011.Vector
    curve_to_mesh_even.links.new(named_attribute.outputs[0], vector_math_011.inputs[1])
    #named_attribute_004.Attribute -> vector_math_009.Vector
    curve_to_mesh_even.links.new(named_attribute_004.outputs[0], vector_math_009.inputs[0])
    #compare.Result -> set_position.Selection
    curve_to_mesh_even.links.new(compare.outputs[0], set_position.inputs[1])
    #vector_math_007.Vector -> vector_math_008.Vector
    curve_to_mesh_even.links.new(vector_math_007.outputs[0], vector_math_008.inputs[0])
    #vector_math_014.Vector -> vector_math_010.Vector
    curve_to_mesh_even.links.new(vector_math_014.outputs[0], vector_math_010.inputs[1])
    #vector_math_005.Vector -> vector_math_011.Vector
    curve_to_mesh_even.links.new(vector_math_005.outputs[0], vector_math_011.inputs[0])
    #vector_math_005.Vector -> vector_math_007.Vector
    curve_to_mesh_even.links.new(vector_math_005.outputs[0], vector_math_007.inputs[1])
    #vector_math_004.Vector -> vector_math_002.Vector
    curve_to_mesh_even.links.new(vector_math_004.outputs[0], vector_math_002.inputs[1])
    #named_attribute_001.Attribute -> vector_math_006.Vector
    curve_to_mesh_even.links.new(named_attribute_001.outputs[0], vector_math_006.inputs[1])
    #vector_math_001.Vector -> store_named_attribute.Value
    curve_to_mesh_even.links.new(vector_math_001.outputs[0], store_named_attribute.inputs[3])
    #curve_tangent_001.Tangent -> vector_math_003.Vector
    curve_to_mesh_even.links.new(curve_tangent_001.outputs[0], vector_math_003.inputs[1])
    #vector_math_002.Value -> math_002.Value
    curve_to_mesh_even.links.new(vector_math_002.outputs[1], math_002.inputs[1])
    #vector_math_010.Vector -> vector_math_015.Vector
    curve_to_mesh_even.links.new(vector_math_010.outputs[0], vector_math_015.inputs[1])
    #vector_math_005.Vector -> vector_math_006.Vector
    curve_to_mesh_even.links.new(vector_math_005.outputs[0], vector_math_006.inputs[0])
    #group_input.Curve -> set_spline_type.Curve
    curve_to_mesh_even.links.new(group_input.outputs[0], set_spline_type.inputs[0])
    #set_position.Geometry -> group_output.Geometry
    curve_to_mesh_even.links.new(set_position.outputs[0], group_output.inputs[0])
    #group_input_001.Profile Curve -> curve_to_mesh.Profile Curve
    curve_to_mesh_even.links.new(group_input_001.outputs[1], curve_to_mesh.inputs[1])
    #group_input_001.Scale -> curve_to_mesh.Scale
    curve_to_mesh_even.links.new(group_input_001.outputs[2], curve_to_mesh.inputs[2])
    #group_input_001.Fill Caps -> curve_to_mesh.Fill Caps
    curve_to_mesh_even.links.new(group_input_001.outputs[3], curve_to_mesh.inputs[3])
    return curve_to_mesh_even

curve_to_mesh_even = curve_to_mesh_even_node_group()

#initialize select_by_index node group
def select_by_index_node_group():
    select_by_index = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Select By Index")

    select_by_index.color_tag = 'NONE'
    select_by_index.description = ""
    select_by_index.default_group_node_width = 140
    


    #select_by_index interface
    #Socket Boolean
    boolean_socket = select_by_index.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
    boolean_socket.default_value = False
    boolean_socket.attribute_domain = 'POINT'
    boolean_socket.default_input = 'VALUE'
    boolean_socket.structure_type = 'AUTO'

    #Socket Input
    input_socket = select_by_index.interface.new_socket(name = "Input", in_out='INPUT', socket_type = 'NodeSocketInt')
    input_socket.default_value = 0
    input_socket.min_value = -2147483648
    input_socket.max_value = 2147483647
    input_socket.subtype = 'NONE'
    input_socket.attribute_domain = 'POINT'
    input_socket.default_input = 'VALUE'
    input_socket.structure_type = 'AUTO'


    #initialize select_by_index nodes
    #node Group Output
    group_output_1 = select_by_index.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Group Input
    group_input_1 = select_by_index.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    #node Compare.002
    compare_002 = select_by_index.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'

    #node Index.001
    index_001 = select_by_index.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"

    #node Compare.003
    compare_003 = select_by_index.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'INT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'EQUAL'

    #node Boolean Math.001
    boolean_math_001 = select_by_index.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'OR'

    #node Integer Math
    integer_math = select_by_index.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.operation = 'ADD'
    #Value_001
    integer_math.inputs[1].default_value = 1

    #node Reroute
    reroute = select_by_index.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketInt"




    #Set locations
    group_output_1.location = (492.43511962890625, 53.86110305786133)
    group_input_1.location = (-497.9546203613281, 71.81480407714844)
    compare_002.location = (81.72785186767578, 135.3497772216797)
    index_001.location = (-149.1388397216797, -90.46559143066406)
    compare_003.location = (77.23249053955078, -16.986339569091797)
    boolean_math_001.location = (274.05853271484375, 86.59996032714844)
    integer_math.location = (-162.2977752685547, 50.86088943481445)
    reroute.location = (-268.08453369140625, 53.44475173950195)

    #Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    index_001.width, index_001.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    integer_math.width, integer_math.height = 140.0, 100.0
    reroute.width, reroute.height = 10.0, 100.0

    #initialize select_by_index links
    #reroute.Output -> compare_002.B
    select_by_index.links.new(reroute.outputs[0], compare_002.inputs[3])
    #reroute.Output -> integer_math.Value
    select_by_index.links.new(reroute.outputs[0], integer_math.inputs[0])
    #index_001.Index -> compare_002.A
    select_by_index.links.new(index_001.outputs[0], compare_002.inputs[2])
    #compare_002.Result -> boolean_math_001.Boolean
    select_by_index.links.new(compare_002.outputs[0], boolean_math_001.inputs[0])
    #compare_003.Result -> boolean_math_001.Boolean
    select_by_index.links.new(compare_003.outputs[0], boolean_math_001.inputs[1])
    #integer_math.Value -> compare_003.B
    select_by_index.links.new(integer_math.outputs[0], compare_003.inputs[3])
    #index_001.Index -> compare_003.A
    select_by_index.links.new(index_001.outputs[0], compare_003.inputs[2])
    #group_input_1.Input -> reroute.Input
    select_by_index.links.new(group_input_1.outputs[0], reroute.inputs[0])
    #boolean_math_001.Boolean -> group_output_1.Boolean
    select_by_index.links.new(boolean_math_001.outputs[0], group_output_1.inputs[0])
    return select_by_index

select_by_index = select_by_index_node_group()

#initialize gablete node group
def gablete_node_group():
    gablete = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Gablete")

    gablete.color_tag = 'NONE'
    gablete.description = ""
    gablete.default_group_node_width = 140
    

    gablete.is_modifier = True

    #gablete interface
    #Socket Geometry
    geometry_socket_1 = gablete.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_2 = gablete.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_2.attribute_domain = 'POINT'
    geometry_socket_2.default_input = 'VALUE'
    geometry_socket_2.structure_type = 'AUTO'

    #Socket top height
    top_height_socket = gablete.interface.new_socket(name = "top height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    top_height_socket.default_value = 0.0
    top_height_socket.min_value = 0.0
    top_height_socket.max_value = 1.0
    top_height_socket.subtype = 'FACTOR'
    top_height_socket.attribute_domain = 'POINT'
    top_height_socket.default_input = 'VALUE'
    top_height_socket.structure_type = 'AUTO'

    #Socket Height
    height_socket = gablete.interface.new_socket(name = "Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    height_socket.default_value = 1.0
    height_socket.min_value = 0.0
    height_socket.max_value = 3.4028234663852886e+38
    height_socket.subtype = 'NONE'
    height_socket.attribute_domain = 'POINT'
    height_socket.default_input = 'VALUE'
    height_socket.structure_type = 'AUTO'

    #Socket Width
    width_socket = gablete.interface.new_socket(name = "Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
    width_socket.default_value = 0.5
    width_socket.min_value = 0.0
    width_socket.max_value = 2.0
    width_socket.subtype = 'NONE'
    width_socket.attribute_domain = 'POINT'
    width_socket.default_input = 'VALUE'
    width_socket.structure_type = 'AUTO'

    #Socket Radius
    radius_socket = gablete.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_socket.default_value = 1.0
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'NONE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.description = "Scale of the profile at each point"
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    #Socket BG
    bg_socket = gablete.interface.new_socket(name = "BG", in_out='INPUT', socket_type = 'NodeSocketBool')
    bg_socket.default_value = False
    bg_socket.attribute_domain = 'POINT'
    bg_socket.default_input = 'VALUE'
    bg_socket.structure_type = 'AUTO'

    #Socket BG Offset
    bg_offset_socket = gablete.interface.new_socket(name = "BG Offset", in_out='INPUT', socket_type = 'NodeSocketBool')
    bg_offset_socket.default_value = True
    bg_offset_socket.attribute_domain = 'POINT'
    bg_offset_socket.default_input = 'VALUE'
    bg_offset_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket_1 = gablete.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_1.default_value = 1.0
    scale_socket_1.min_value = 0.0
    scale_socket_1.max_value = 3.4028234663852886e+38
    scale_socket_1.subtype = 'NONE'
    scale_socket_1.attribute_domain = 'POINT'
    scale_socket_1.default_input = 'VALUE'
    scale_socket_1.structure_type = 'AUTO'

    #Panel Column
    column_panel = gablete.interface.new_panel("Column")
    #Socket Resolution
    resolution_socket = gablete.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt', parent = column_panel)
    resolution_socket.default_value = 8
    resolution_socket.min_value = 3
    resolution_socket.max_value = 64
    resolution_socket.subtype = 'NONE'
    resolution_socket.attribute_domain = 'POINT'
    resolution_socket.default_input = 'VALUE'
    resolution_socket.structure_type = 'AUTO'

    #Socket Radius Ratio
    radius_ratio_socket = gablete.interface.new_socket(name = "Radius Ratio", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = column_panel)
    radius_ratio_socket.default_value = 0.5
    radius_ratio_socket.min_value = -3.4028234663852886e+38
    radius_ratio_socket.max_value = 3.4028234663852886e+38
    radius_ratio_socket.subtype = 'NONE'
    radius_ratio_socket.attribute_domain = 'POINT'
    radius_ratio_socket.default_input = 'VALUE'
    radius_ratio_socket.structure_type = 'AUTO'



    #initialize gablete nodes
    #node Group Output
    group_output_2 = gablete.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    #node Cube
    cube = gablete.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    #Vertices X
    cube.inputs[1].default_value = 2
    #Vertices Y
    cube.inputs[2].default_value = 2
    #Vertices Z
    cube.inputs[3].default_value = 2

    #node Scale Elements
    scale_elements = gablete.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'FACE'
    scale_elements.scale_mode = 'SINGLE_AXIS'
    #Scale
    scale_elements.inputs[2].default_value = 0.0
    #Center
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Axis
    scale_elements.inputs[4].default_value = (1.0, 0.0, 0.0)

    #node Compare
    compare_1 = gablete.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = 'INT'
    compare_1.mode = 'ELEMENT'
    compare_1.operation = 'EQUAL'
    #B_INT
    compare_1.inputs[3].default_value = 2

    #node Index
    index = gablete.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    #node Mesh Boolean
    mesh_boolean = gablete.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'UNION'
    mesh_boolean.solver = 'MANIFOLD'

    #node Transform Geometry
    transform_geometry = gablete.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    #Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Transform Geometry.001
    transform_geometry_001 = gablete.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Frame
    frame_1 = gablete.nodes.new("NodeFrame")
    frame_1.label = "Base Shape"
    frame_1.name = "Frame"
    frame_1.label_size = 20
    frame_1.shrink = True

    #node Scale Elements.001
    scale_elements_001 = gablete.nodes.new("GeometryNodeScaleElements")
    scale_elements_001.name = "Scale Elements.001"
    scale_elements_001.domain = 'FACE'
    scale_elements_001.scale_mode = 'SINGLE_AXIS'
    #Selection
    scale_elements_001.inputs[1].default_value = True
    #Scale
    scale_elements_001.inputs[2].default_value = 0.0
    #Center
    scale_elements_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Axis
    scale_elements_001.inputs[4].default_value = (0.0, 1.0, 0.0)

    #node Merge by Distance
    merge_by_distance = gablete.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    #Selection
    merge_by_distance.inputs[1].default_value = True
    #Distance
    merge_by_distance.inputs[2].default_value = 0.0010000020265579224

    #node Mesh to Curve
    mesh_to_curve = gablete.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.mode = 'EDGES'

    #node Face Group Boundaries
    face_group_boundaries = gablete.nodes.new("GeometryNodeMeshFaceSetBoundaries")
    face_group_boundaries.name = "Face Group Boundaries"

    #node Edges to Face Groups
    edges_to_face_groups = gablete.nodes.new("GeometryNodeEdgesToFaceGroups")
    edges_to_face_groups.name = "Edges to Face Groups"
    #Boundary Edges
    edges_to_face_groups.inputs[0].default_value = True

    #node Boolean Math
    boolean_math = gablete.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'NOT'

    #node Group
    group = gablete.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = curve_to_mesh_even
    #Socket_4
    group.inputs[3].default_value = True

    #node Quadrilateral
    quadrilateral = gablete.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    quadrilateral.name = "Quadrilateral"
    quadrilateral.mode = 'RECTANGLE'
    #Width
    quadrilateral.inputs[0].default_value = 0.10000000149011612
    #Height
    quadrilateral.inputs[1].default_value = 0.10000000149011612

    #node Delete Geometry
    delete_geometry = gablete.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    #node Compare.001
    compare_001 = gablete.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    #B
    compare_001.inputs[1].default_value = 0.0
    #Epsilon
    compare_001.inputs[12].default_value = 0.0010000000474974513

    #node Position
    position_1 = gablete.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"

    #node Separate XYZ
    separate_xyz = gablete.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    #node Trim Curve
    trim_curve = gablete.nodes.new("GeometryNodeTrimCurve")
    trim_curve.name = "Trim Curve"
    trim_curve.mode = 'FACTOR'
    #Selection
    trim_curve.inputs[1].default_value = True
    #Start
    trim_curve.inputs[2].default_value = 0.0
    #End
    trim_curve.inputs[3].default_value = 1.0

    #node Set Shade Smooth
    set_shade_smooth = gablete.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    #Selection
    set_shade_smooth.inputs[1].default_value = True
    #Shade Smooth
    set_shade_smooth.inputs[2].default_value = False

    #node Separate Geometry
    separate_geometry = gablete.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = 'POINT'

    #node Delete Geometry.001
    delete_geometry_001 = gablete.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'
    #Selection
    delete_geometry_001.inputs[1].default_value = True

    #node Group.001
    group_001 = gablete.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = select_by_index
    #Socket_1
    group_001.inputs[0].default_value = 1

    #node Group.002
    group_002 = gablete.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = select_by_index
    #Socket_1
    group_002.inputs[0].default_value = 6

    #node Separate Geometry.001
    separate_geometry_001 = gablete.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_001.name = "Separate Geometry.001"
    separate_geometry_001.domain = 'POINT'

    #node Join Geometry
    join_geometry = gablete.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Curve to Mesh
    curve_to_mesh_1 = gablete.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_1.name = "Curve to Mesh"
    #Fill Caps
    curve_to_mesh_1.inputs[3].default_value = False

    #node Curve Circle
    curve_circle = gablete.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    #Radius
    curve_circle.inputs[4].default_value = 0.10000000149011612

    #node Join Geometry.001
    join_geometry_001 = gablete.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    #node Transform Geometry.002
    transform_geometry_002 = gablete.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    #Translation
    transform_geometry_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_002.inputs[3].default_value = (0.800000011920929, 1.0, 1.0)

    #node Group Input
    group_input_2 = gablete.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    group_input_2.outputs[0].hide = True
    group_input_2.outputs[1].hide = True
    group_input_2.outputs[2].hide = True
    group_input_2.outputs[3].hide = True
    group_input_2.outputs[4].hide = True
    group_input_2.outputs[5].hide = True
    group_input_2.outputs[6].hide = True
    group_input_2.outputs[7].hide = True
    group_input_2.outputs[9].hide = True
    group_input_2.outputs[10].hide = True

    #node Combine XYZ
    combine_xyz = gablete.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #Y
    combine_xyz.inputs[1].default_value = 1.0

    #node Cube.001
    cube_001 = gablete.nodes.new("GeometryNodeMeshCube")
    cube_001.name = "Cube.001"
    #Vertices X
    cube_001.inputs[1].default_value = 2
    #Vertices Y
    cube_001.inputs[2].default_value = 2
    #Vertices Z
    cube_001.inputs[3].default_value = 2

    #node Combine XYZ.001
    combine_xyz_001 = gablete.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #X
    combine_xyz_001.inputs[0].default_value = 0.0
    #Y
    combine_xyz_001.inputs[1].default_value = 0.0

    #node Math
    math_1 = gablete.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'MULTIPLY'
    math_1.use_clamp = False
    #Value_001
    math_1.inputs[1].default_value = -0.5

    #node Math.001
    math_001 = gablete.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'SUBTRACT'
    math_001.use_clamp = False

    #node Combine XYZ.002
    combine_xyz_002 = gablete.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    #X
    combine_xyz_002.inputs[0].default_value = 0.0
    #Y
    combine_xyz_002.inputs[1].default_value = 0.0

    #node Viewer
    viewer = gablete.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.data_type = 'FLOAT'
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    #Value
    viewer.inputs[1].default_value = 0.0

    #node Math.003
    math_003 = gablete.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'ADD'
    math_003.use_clamp = False

    #node Value.001
    value_001 = gablete.nodes.new("ShaderNodeValue")
    value_001.name = "Value.001"

    value_001.outputs[0].default_value = 0.10000002384185791
    #node Combine XYZ.003
    combine_xyz_003 = gablete.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    #Y
    combine_xyz_003.inputs[1].default_value = 1.0

    #node Math.002
    math_002_1 = gablete.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'ADD'
    math_002_1.use_clamp = False
    #Value_001
    math_002_1.inputs[1].default_value = 0.30000001192092896

    #node Group Input.002
    group_input_002 = gablete.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True

    #node Math.004
    math_004 = gablete.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'ADD'
    math_004.use_clamp = False
    #Value_001
    math_004.inputs[1].default_value = 0.30000001192092896

    #node Group Input.003
    group_input_003 = gablete.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True

    #node Math.005
    math_005 = gablete.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'ADD'
    math_005.use_clamp = False
    #Value_001
    math_005.inputs[1].default_value = 0.5

    #node Group Input.004
    group_input_004 = gablete.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True

    #node Reroute
    reroute_1 = gablete.nodes.new("NodeReroute")
    reroute_1.name = "Reroute"
    reroute_1.socket_idname = "NodeSocketGeometry"
    #node Reroute.001
    reroute_001 = gablete.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketGeometry"
    #node Switch
    switch = gablete.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    #node Group Input.005
    group_input_005 = gablete.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True

    #node Transform Geometry.003
    transform_geometry_003 = gablete.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    #Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Group Input.006
    group_input_006 = gablete.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True

    #node Group Input.001
    group_input_001_1 = gablete.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[1].hide = True
    group_input_001_1.outputs[2].hide = True
    group_input_001_1.outputs[3].hide = True
    group_input_001_1.outputs[5].hide = True
    group_input_001_1.outputs[6].hide = True
    group_input_001_1.outputs[7].hide = True
    group_input_001_1.outputs[8].hide = True
    group_input_001_1.outputs[9].hide = True
    group_input_001_1.outputs[10].hide = True

    #node Math.006
    math_006 = gablete.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    #node Group Input.007
    group_input_007 = gablete.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[10].hide = True

    #node Combine XYZ.004
    combine_xyz_004 = gablete.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    #X
    combine_xyz_004.inputs[0].default_value = 0.0
    #Z
    combine_xyz_004.inputs[2].default_value = 0.0

    #node Group Input.008
    group_input_008 = gablete.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[8].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True

    #node Math.007
    math_007 = gablete.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'MULTIPLY'
    math_007.use_clamp = False
    #Value_001
    math_007.inputs[1].default_value = 0.05000000074505806

    #node Switch.001
    switch_001 = gablete.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'FLOAT'
    #False
    switch_001.inputs[1].default_value = 0.0

    #node Group Input.009
    group_input_009 = gablete.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True

    #node Scale Elements.002
    scale_elements_002 = gablete.nodes.new("GeometryNodeScaleElements")
    scale_elements_002.name = "Scale Elements.002"
    scale_elements_002.domain = 'FACE'
    scale_elements_002.scale_mode = 'UNIFORM'
    #Selection
    scale_elements_002.inputs[1].default_value = True

    #node Vector
    vector = gablete.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, 0.0)

    #node Group Input.010
    group_input_010 = gablete.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[1].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[4].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True




    #Set parents
    cube.parent = frame_1
    scale_elements.parent = frame_1
    compare_1.parent = frame_1
    index.parent = frame_1
    mesh_boolean.parent = frame_1
    transform_geometry.parent = frame_1
    transform_geometry_001.parent = frame_1
    combine_xyz.parent = frame_1
    cube_001.parent = frame_1
    combine_xyz_001.parent = frame_1
    math_1.parent = frame_1
    math_001.parent = frame_1
    combine_xyz_002.parent = frame_1
    math_003.parent = frame_1
    value_001.parent = frame_1
    combine_xyz_003.parent = frame_1
    math_002_1.parent = frame_1
    group_input_002.parent = frame_1
    math_004.parent = frame_1
    group_input_003.parent = frame_1
    math_005.parent = frame_1
    group_input_004.parent = frame_1

    #Set locations
    group_output_2.location = (3183.001953125, 360.8830871582031)
    cube.location = (808.5167236328125, -218.27685546875)
    scale_elements.location = (1087.5634765625, -479.83099365234375)
    compare_1.location = (825.9990234375, -678.3679809570312)
    index.location = (636.8003540039062, -790.560791015625)
    mesh_boolean.location = (1350.910400390625, -295.3893127441406)
    transform_geometry.location = (1091.574462890625, -56.77227783203125)
    transform_geometry_001.location = (1543.9010009765625, -357.2628479003906)
    frame_1.location = (-1234.0, 614.0)
    scale_elements_001.location = (539.0739135742188, 145.80458068847656)
    merge_by_distance.location = (817.8392333984375, 164.74183654785156)
    mesh_to_curve.location = (1348.7818603515625, 157.33026123046875)
    face_group_boundaries.location = (977.8277587890625, 9.792865753173828)
    edges_to_face_groups.location = (821.9617919921875, 8.779708862304688)
    boolean_math.location = (1165.248779296875, 48.293087005615234)
    group.location = (2022.169677734375, 231.16183471679688)
    quadrilateral.location = (1784.129150390625, 140.67347717285156)
    delete_geometry.location = (1811.5394287109375, 301.3915710449219)
    compare_001.location = (1367.4964599609375, 346.1418762207031)
    position_1.location = (996.126953125, 319.7955627441406)
    separate_xyz.location = (1175.9998779296875, 354.47113037109375)
    trim_curve.location = (1529.0001220703125, 207.81134033203125)
    set_shade_smooth.location = (2217.985595703125, 259.90460205078125)
    separate_geometry.location = (1761.34765625, 687.6531372070312)
    delete_geometry_001.location = (1811.5394287109375, 301.3915710449219)
    group_001.location = (1533.5933837890625, 698.8626708984375)
    group_002.location = (1513.7862548828125, 551.4869384765625)
    separate_geometry_001.location = (1758.9835205078125, 531.3484497070312)
    join_geometry.location = (1996.0128173828125, 726.4473266601562)
    curve_to_mesh_1.location = (2372.748779296875, 524.0256958007812)
    curve_circle.location = (2192.855224609375, 596.3146362304688)
    join_geometry_001.location = (2702.57666015625, 372.9962158203125)
    transform_geometry_002.location = (2201.313720703125, 922.1345825195312)
    group_input_2.location = (1951.688720703125, 573.8494873046875)
    combine_xyz.location = (626.90380859375, -269.8002624511719)
    cube_001.location = (833.3838500976562, -435.5557556152344)
    combine_xyz_001.location = (800.3757934570312, -70.95208740234375)
    math_1.location = (405.034912109375, -72.0421142578125)
    math_001.location = (605.14013671875, -36.46746826171875)
    combine_xyz_002.location = (1359.0343017578125, -481.7897033691406)
    viewer.location = (692.4830932617188, 360.0054931640625)
    math_003.location = (611.1142578125, -428.4637145996094)
    value_001.location = (180.821044921875, -117.46316528320312)
    combine_xyz_003.location = (638.905029296875, -617.7269287109375)
    math_002_1.location = (455.73919677734375, -672.8917846679688)
    group_input_002.location = (261.9493408203125, -739.7308959960938)
    math_004.location = (202.3056640625, -277.54864501953125)
    group_input_003.location = (30.1541748046875, -342.8173522949219)
    math_005.location = (242.91961669921875, -557.1296997070312)
    group_input_004.location = (42.4549560546875, -646.142822265625)
    reroute_1.location = (1253.908935546875, -106.17864990234375)
    reroute_001.location = (2233.065673828125, -111.36157989501953)
    switch.location = (2518.202392578125, 178.89633178710938)
    group_input_005.location = (2209.507568359375, 85.96170043945312)
    transform_geometry_003.location = (2353.159912109375, -126.44268798828125)
    group_input_006.location = (1772.946533203125, 0.15610599517822266)
    group_input_001_1.location = (1943.378662109375, 444.0098876953125)
    math_006.location = (2187.049072265625, 465.81646728515625)
    group_input_007.location = (1944.379150390625, 362.7565612792969)
    combine_xyz_004.location = (2097.323974609375, -236.81494140625)
    group_input_008.location = (1451.91015625, -331.3064880371094)
    math_007.location = (1642.9278564453125, -277.780517578125)
    switch_001.location = (1906.7767333984375, -276.5003662109375)
    group_input_009.location = (1629.44189453125, -189.4484405517578)
    scale_elements_002.location = (3003.0, 428.5052490234375)
    vector.location = (2743.467041015625, 204.56573486328125)
    group_input_010.location = (2707.986328125, 288.3183898925781)

    #Set dimensions
    group_output_2.width, group_output_2.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    frame_1.width, frame_1.height = 1714.0, 871.0
    scale_elements_001.width, scale_elements_001.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    face_group_boundaries.width, face_group_boundaries.height = 150.0, 100.0
    edges_to_face_groups.width, edges_to_face_groups.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    quadrilateral.width, quadrilateral.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    position_1.width, position_1.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    trim_curve.width, trim_curve.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    curve_to_mesh_1.width, curve_to_mesh_1.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    cube_001.width, cube_001.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    viewer.width, viewer.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    value_001.width, value_001.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    reroute_1.width, reroute_1.height = 10.0, 100.0
    reroute_001.width, reroute_001.height = 10.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    scale_elements_002.width, scale_elements_002.height = 140.0, 100.0
    vector.width, vector.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0

    #initialize gablete links
    #compare_1.Result -> scale_elements.Selection
    gablete.links.new(compare_1.outputs[0], scale_elements.inputs[1])
    #index.Index -> compare_1.A
    gablete.links.new(index.outputs[0], compare_1.inputs[2])
    #scale_elements.Geometry -> mesh_boolean.Mesh
    gablete.links.new(scale_elements.outputs[0], mesh_boolean.inputs[1])
    #cube.Mesh -> transform_geometry.Geometry
    gablete.links.new(cube.outputs[0], transform_geometry.inputs[0])
    #mesh_boolean.Mesh -> transform_geometry_001.Geometry
    gablete.links.new(mesh_boolean.outputs[0], transform_geometry_001.inputs[0])
    #transform_geometry_001.Geometry -> scale_elements_001.Geometry
    gablete.links.new(transform_geometry_001.outputs[0], scale_elements_001.inputs[0])
    #scale_elements_001.Geometry -> merge_by_distance.Geometry
    gablete.links.new(scale_elements_001.outputs[0], merge_by_distance.inputs[0])
    #merge_by_distance.Geometry -> mesh_to_curve.Mesh
    gablete.links.new(merge_by_distance.outputs[0], mesh_to_curve.inputs[0])
    #face_group_boundaries.Boundary Edges -> boolean_math.Boolean
    gablete.links.new(face_group_boundaries.outputs[0], boolean_math.inputs[0])
    #boolean_math.Boolean -> mesh_to_curve.Selection
    gablete.links.new(boolean_math.outputs[0], mesh_to_curve.inputs[1])
    #edges_to_face_groups.Face Group ID -> face_group_boundaries.Face Group ID
    gablete.links.new(edges_to_face_groups.outputs[0], face_group_boundaries.inputs[0])
    #trim_curve.Curve -> delete_geometry.Geometry
    gablete.links.new(trim_curve.outputs[0], delete_geometry.inputs[0])
    #compare_001.Result -> delete_geometry.Selection
    gablete.links.new(compare_001.outputs[0], delete_geometry.inputs[1])
    #position_1.Position -> separate_xyz.Vector
    gablete.links.new(position_1.outputs[0], separate_xyz.inputs[0])
    #separate_xyz.Z -> compare_001.A
    gablete.links.new(separate_xyz.outputs[2], compare_001.inputs[0])
    #mesh_to_curve.Curve -> trim_curve.Curve
    gablete.links.new(mesh_to_curve.outputs[0], trim_curve.inputs[0])
    #delete_geometry.Geometry -> group.Curve
    gablete.links.new(delete_geometry.outputs[0], group.inputs[0])
    #quadrilateral.Curve -> group.Profile Curve
    gablete.links.new(quadrilateral.outputs[0], group.inputs[1])
    #group.Geometry -> set_shade_smooth.Geometry
    gablete.links.new(group.outputs[0], set_shade_smooth.inputs[0])
    #trim_curve.Curve -> separate_geometry.Geometry
    gablete.links.new(trim_curve.outputs[0], separate_geometry.inputs[0])
    #group_001.Boolean -> separate_geometry.Selection
    gablete.links.new(group_001.outputs[0], separate_geometry.inputs[1])
    #group_002.Boolean -> separate_geometry_001.Selection
    gablete.links.new(group_002.outputs[0], separate_geometry_001.inputs[1])
    #trim_curve.Curve -> separate_geometry_001.Geometry
    gablete.links.new(trim_curve.outputs[0], separate_geometry_001.inputs[0])
    #separate_geometry_001.Selection -> join_geometry.Geometry
    gablete.links.new(separate_geometry_001.outputs[0], join_geometry.inputs[0])
    #transform_geometry_002.Geometry -> curve_to_mesh_1.Curve
    gablete.links.new(transform_geometry_002.outputs[0], curve_to_mesh_1.inputs[0])
    #curve_circle.Curve -> curve_to_mesh_1.Profile Curve
    gablete.links.new(curve_circle.outputs[0], curve_to_mesh_1.inputs[1])
    #scale_elements_002.Geometry -> group_output_2.Geometry
    gablete.links.new(scale_elements_002.outputs[0], group_output_2.inputs[0])
    #join_geometry.Geometry -> transform_geometry_002.Geometry
    gablete.links.new(join_geometry.outputs[0], transform_geometry_002.inputs[0])
    #group_input_2.Resolution -> curve_circle.Resolution
    gablete.links.new(group_input_2.outputs[8], curve_circle.inputs[0])
    #combine_xyz.Vector -> cube.Size
    gablete.links.new(combine_xyz.outputs[0], cube.inputs[0])
    #cube_001.Mesh -> scale_elements.Geometry
    gablete.links.new(cube_001.outputs[0], scale_elements.inputs[0])
    #math_001.Value -> combine_xyz_001.Z
    gablete.links.new(math_001.outputs[0], combine_xyz_001.inputs[2])
    #combine_xyz_001.Vector -> transform_geometry.Translation
    gablete.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
    #math_1.Value -> math_001.Value
    gablete.links.new(math_1.outputs[0], math_001.inputs[0])
    #combine_xyz_002.Vector -> transform_geometry_001.Translation
    gablete.links.new(combine_xyz_002.outputs[0], transform_geometry_001.inputs[1])
    #mesh_to_curve.Curve -> delete_geometry_001.Geometry
    gablete.links.new(mesh_to_curve.outputs[0], delete_geometry_001.inputs[0])
    #scale_elements_001.Geometry -> viewer.Geometry
    gablete.links.new(scale_elements_001.outputs[0], viewer.inputs[0])
    #value_001.Value -> math_001.Value
    gablete.links.new(value_001.outputs[0], math_001.inputs[1])
    #value_001.Value -> math_003.Value
    gablete.links.new(value_001.outputs[0], math_003.inputs[1])
    #math_003.Value -> combine_xyz_002.Z
    gablete.links.new(math_003.outputs[0], combine_xyz_002.inputs[2])
    #combine_xyz_003.Vector -> cube_001.Size
    gablete.links.new(combine_xyz_003.outputs[0], cube_001.inputs[0])
    #math_002_1.Value -> combine_xyz_003.Z
    gablete.links.new(math_002_1.outputs[0], combine_xyz_003.inputs[2])
    #group_input_002.top height -> math_002_1.Value
    gablete.links.new(group_input_002.outputs[1], math_002_1.inputs[0])
    #math_004.Value -> math_003.Value
    gablete.links.new(math_004.outputs[0], math_003.inputs[0])
    #math_004.Value -> combine_xyz.Z
    gablete.links.new(math_004.outputs[0], combine_xyz.inputs[2])
    #math_004.Value -> math_1.Value
    gablete.links.new(math_004.outputs[0], math_1.inputs[0])
    #group_input_003.Height -> math_004.Value
    gablete.links.new(group_input_003.outputs[2], math_004.inputs[0])
    #math_005.Value -> combine_xyz.X
    gablete.links.new(math_005.outputs[0], combine_xyz.inputs[0])
    #math_005.Value -> combine_xyz_003.X
    gablete.links.new(math_005.outputs[0], combine_xyz_003.inputs[0])
    #group_input_004.Width -> math_005.Value
    gablete.links.new(group_input_004.outputs[3], math_005.inputs[0])
    #merge_by_distance.Geometry -> reroute_1.Input
    gablete.links.new(merge_by_distance.outputs[0], reroute_1.inputs[0])
    #reroute_1.Output -> reroute_001.Input
    gablete.links.new(reroute_1.outputs[0], reroute_001.inputs[0])
    #switch.Output -> join_geometry_001.Geometry
    gablete.links.new(switch.outputs[0], join_geometry_001.inputs[0])
    #transform_geometry_003.Geometry -> switch.True
    gablete.links.new(transform_geometry_003.outputs[0], switch.inputs[2])
    #group_input_005.BG -> switch.Switch
    gablete.links.new(group_input_005.outputs[5], switch.inputs[0])
    #reroute_001.Output -> transform_geometry_003.Geometry
    gablete.links.new(reroute_001.outputs[0], transform_geometry_003.inputs[0])
    #group_input_006.Radius -> group.Scale
    gablete.links.new(group_input_006.outputs[4], group.inputs[2])
    #group_input_001_1.Radius -> math_006.Value
    gablete.links.new(group_input_001_1.outputs[4], math_006.inputs[0])
    #math_006.Value -> curve_to_mesh_1.Scale
    gablete.links.new(math_006.outputs[0], curve_to_mesh_1.inputs[2])
    #group_input_007.Radius Ratio -> math_006.Value
    gablete.links.new(group_input_007.outputs[9], math_006.inputs[1])
    #combine_xyz_004.Vector -> transform_geometry_003.Translation
    gablete.links.new(combine_xyz_004.outputs[0], transform_geometry_003.inputs[1])
    #switch_001.Output -> combine_xyz_004.Y
    gablete.links.new(switch_001.outputs[0], combine_xyz_004.inputs[1])
    #group_input_008.Radius -> math_007.Value
    gablete.links.new(group_input_008.outputs[4], math_007.inputs[0])
    #math_007.Value -> switch_001.True
    gablete.links.new(math_007.outputs[0], switch_001.inputs[2])
    #group_input_009.BG Offset -> switch_001.Switch
    gablete.links.new(group_input_009.outputs[6], switch_001.inputs[0])
    #join_geometry_001.Geometry -> scale_elements_002.Geometry
    gablete.links.new(join_geometry_001.outputs[0], scale_elements_002.inputs[0])
    #vector.Vector -> scale_elements_002.Center
    gablete.links.new(vector.outputs[0], scale_elements_002.inputs[3])
    #group_input_010.Scale -> scale_elements_002.Scale
    gablete.links.new(group_input_010.outputs[7], scale_elements_002.inputs[2])
    #transform_geometry.Geometry -> mesh_boolean.Mesh
    gablete.links.new(transform_geometry.outputs[0], mesh_boolean.inputs[1])
    #separate_geometry.Selection -> join_geometry.Geometry
    gablete.links.new(separate_geometry.outputs[0], join_geometry.inputs[0])
    #set_shade_smooth.Geometry -> join_geometry_001.Geometry
    gablete.links.new(set_shade_smooth.outputs[0], join_geometry_001.inputs[0])
    #curve_to_mesh_1.Mesh -> join_geometry_001.Geometry
    gablete.links.new(curve_to_mesh_1.outputs[0], join_geometry_001.inputs[0])
    return gablete

gablete = gablete_node_group()

