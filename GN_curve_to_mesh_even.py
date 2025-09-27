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

