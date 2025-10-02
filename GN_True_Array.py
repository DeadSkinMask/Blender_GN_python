import bpy, mathutils

#initialize true_array node group
def true_array_node_group():
    true_array = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "True Array")

    true_array.color_tag = 'NONE'
    true_array.description = ""
    true_array.default_group_node_width = 140
    

    true_array.is_modifier = True

    #true_array interface
    #Socket Geometry
    geometry_socket = true_array.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = true_array.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Iterations
    iterations_socket = true_array.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
    iterations_socket.default_value = 0
    iterations_socket.min_value = 0
    iterations_socket.max_value = 256
    iterations_socket.subtype = 'NONE'
    iterations_socket.attribute_domain = 'POINT'
    iterations_socket.default_input = 'VALUE'
    iterations_socket.structure_type = 'AUTO'


    #initialize true_array nodes
    #node Group Input
    group_input = true_array.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Group Output
    group_output = true_array.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Curve Line
    curve_line = true_array.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'DIRECTION'
    #Direction
    curve_line.inputs[2].default_value = (1.0, 0.0, 0.0)

    #node Bounding Box
    bounding_box = true_array.nodes.new("GeometryNodeBoundBox")
    bounding_box.name = "Bounding Box"
    #Use Radius
    bounding_box.inputs[1].default_value = True

    #node Separate XYZ
    separate_xyz = true_array.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    #node Separate XYZ.001
    separate_xyz_001 = true_array.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    #node Math
    math = true_array.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'SUBTRACT'
    math.use_clamp = False

    #node Frame
    frame = true_array.nodes.new("NodeFrame")
    frame.label = "Lenght"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Math.001
    math_001 = true_array.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Math.002
    math_002 = true_array.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    #Value_001
    math_002.inputs[1].default_value = -0.5

    #node Combine XYZ
    combine_xyz = true_array.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #Y
    combine_xyz.inputs[1].default_value = 0.0
    #Z
    combine_xyz.inputs[2].default_value = 0.0

    #node Instance on Points
    instance_on_points = true_array.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    #Selection
    instance_on_points.inputs[1].default_value = True
    #Pick Instance
    instance_on_points.inputs[3].default_value = False
    #Instance Index
    instance_on_points.inputs[4].default_value = 0
    #Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    #node Group Input.001
    group_input_001 = true_array.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[1].hide = True
    group_input_001.outputs[2].hide = True

    #node Group Input.002
    group_input_002 = true_array.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True

    #node Resample Curve
    resample_curve = true_array.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.keep_last_segment = True
    resample_curve.mode = 'COUNT'
    #Selection
    resample_curve.inputs[1].default_value = True

    #node Group Input.003
    group_input_003 = true_array.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[2].hide = True

    #node Integer Math
    integer_math = true_array.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.operation = 'ADD'
    #Value_001
    integer_math.inputs[1].default_value = 1




    #Set parents
    bounding_box.parent = frame
    separate_xyz.parent = frame
    separate_xyz_001.parent = frame
    math.parent = frame

    #Set locations
    group_input.location = (-654.9926147460938, -285.4967041015625)
    group_output.location = (1614.7701416015625, -112.73299407958984)
    curve_line.location = (935.4755859375, 154.09397888183594)
    bounding_box.location = (29.51470947265625, -85.46246337890625)
    separate_xyz.location = (250.748779296875, -35.792327880859375)
    separate_xyz_001.location = (251.9305419921875, -179.03765869140625)
    math.location = (452.7893371582031, -87.94512939453125)
    frame.location = (-431.0, -163.0)
    math_001.location = (264.05633544921875, -11.542549133300781)
    math_002.location = (495.6162414550781, 149.7803192138672)
    combine_xyz.location = (716.462890625, 200.37547302246094)
    instance_on_points.location = (1416.266357421875, -56.380130767822266)
    group_input_001.location = (1037.3367919921875, -218.7570343017578)
    group_input_002.location = (66.5876235961914, -20.19506072998047)
    resample_curve.location = (1189.4615478515625, 66.36058807373047)
    group_input_003.location = (753.0302734375, -85.22478485107422)
    integer_math.location = (936.7069702148438, -72.00051879882812)

    #Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    bounding_box.width, bounding_box.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    frame.width, frame.height = 623.0, 328.0
    math_001.width, math_001.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer_math.width, integer_math.height = 140.0, 100.0

    #initialize true_array links
    #group_input.Geometry -> bounding_box.Geometry
    true_array.links.new(group_input.outputs[0], bounding_box.inputs[0])
    #bounding_box.Min -> separate_xyz.Vector
    true_array.links.new(bounding_box.outputs[1], separate_xyz.inputs[0])
    #bounding_box.Max -> separate_xyz_001.Vector
    true_array.links.new(bounding_box.outputs[2], separate_xyz_001.inputs[0])
    #separate_xyz_001.X -> math.Value
    true_array.links.new(separate_xyz_001.outputs[0], math.inputs[0])
    #separate_xyz.X -> math.Value
    true_array.links.new(separate_xyz.outputs[0], math.inputs[1])
    #math.Value -> math_001.Value
    true_array.links.new(math.outputs[0], math_001.inputs[1])
    #math_001.Value -> math_002.Value
    true_array.links.new(math_001.outputs[0], math_002.inputs[0])
    #math_001.Value -> curve_line.Length
    true_array.links.new(math_001.outputs[0], curve_line.inputs[3])
    #combine_xyz.Vector -> curve_line.Start
    true_array.links.new(combine_xyz.outputs[0], curve_line.inputs[0])
    #math_002.Value -> combine_xyz.X
    true_array.links.new(math_002.outputs[0], combine_xyz.inputs[0])
    #instance_on_points.Instances -> group_output.Geometry
    true_array.links.new(instance_on_points.outputs[0], group_output.inputs[0])
    #resample_curve.Curve -> instance_on_points.Points
    true_array.links.new(resample_curve.outputs[0], instance_on_points.inputs[0])
    #group_input_001.Geometry -> instance_on_points.Instance
    true_array.links.new(group_input_001.outputs[0], instance_on_points.inputs[2])
    #group_input_002.Iterations -> math_001.Value
    true_array.links.new(group_input_002.outputs[1], math_001.inputs[0])
    #curve_line.Curve -> resample_curve.Curve
    true_array.links.new(curve_line.outputs[0], resample_curve.inputs[0])
    #integer_math.Value -> resample_curve.Count
    true_array.links.new(integer_math.outputs[0], resample_curve.inputs[2])
    #group_input_003.Iterations -> integer_math.Value
    true_array.links.new(group_input_003.outputs[1], integer_math.inputs[0])
    return true_array

true_array = true_array_node_group()

