import bpy, mathutils

#initialize instancer node group
def instancer_node_group():
    instancer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Instancer")

    instancer.color_tag = 'NONE'
    instancer.description = ""
    instancer.default_group_node_width = 140
    

    instancer.is_modifier = True

    #instancer interface
    #Socket Geometry
    geometry_socket = instancer.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = instancer.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Offset
    offset_socket = instancer.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    offset_socket.default_value = 1.0
    offset_socket.min_value = -10000.0
    offset_socket.max_value = 10000.0
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'

    #Socket Iterations
    iterations_socket = instancer.interface.new_socket(name = "Iterations", in_out='INPUT', socket_type = 'NodeSocketInt')
    iterations_socket.default_value = 0
    iterations_socket.min_value = 0
    iterations_socket.max_value = 256
    iterations_socket.subtype = 'NONE'
    iterations_socket.attribute_domain = 'POINT'
    iterations_socket.default_input = 'VALUE'
    iterations_socket.structure_type = 'AUTO'

    #Socket Realize Instances
    realize_instances_socket = instancer.interface.new_socket(name = "Realize Instances", in_out='INPUT', socket_type = 'NodeSocketBool')
    realize_instances_socket.default_value = False
    realize_instances_socket.attribute_domain = 'POINT'
    realize_instances_socket.hide_value = True
    realize_instances_socket.description = "Which top-level instances to realize"
    realize_instances_socket.default_input = 'VALUE'
    realize_instances_socket.structure_type = 'AUTO'


    #initialize instancer nodes
    #node Group Input
    group_input = instancer.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True

    #node Group Output
    group_output = instancer.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Curve Line
    curve_line = instancer.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'DIRECTION'
    #Direction
    curve_line.inputs[2].default_value = (1.0, 0.0, 0.0)

    #node Combine XYZ
    combine_xyz = instancer.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #Y
    combine_xyz.inputs[1].default_value = 0.0
    #Z
    combine_xyz.inputs[2].default_value = 0.0

    #node Math
    math = instancer.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = -0.5

    #node Group Input.001
    group_input_001 = instancer.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True

    #node Math.001
    math_001 = instancer.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Resample Curve
    resample_curve = instancer.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.keep_last_segment = True
    resample_curve.mode = 'COUNT'
    #Selection
    resample_curve.inputs[1].default_value = True

    #node Group Input.002
    group_input_002 = instancer.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True

    #node Integer Math
    integer_math = instancer.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.operation = 'ADD'
    #Value_001
    integer_math.inputs[1].default_value = 1

    #node Instance on Points
    instance_on_points = instancer.nodes.new("GeometryNodeInstanceOnPoints")
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

    #node Realize Instances
    realize_instances = instancer.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Group Input.003
    group_input_003 = instancer.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[4].hide = True





    #Set locations
    group_input.location = (-220.80418395996094, -293.6068420410156)
    group_output.location = (600.8707275390625, -99.62517547607422)
    curve_line.location = (-444.8446960449219, -98.32331848144531)
    combine_xyz.location = (-627.560546875, -132.79405212402344)
    math.location = (-816.6422119140625, -129.24249267578125)
    group_input_001.location = (-1222.2972412109375, -195.84986877441406)
    math_001.location = (-994.4356689453125, -131.52230834960938)
    resample_curve.location = (-233.39578247070312, -119.62165832519531)
    group_input_002.location = (-623.5423583984375, -339.4457702636719)
    integer_math.location = (-448.4099426269531, -324.5450134277344)
    instance_on_points.location = (66.67285919189453, -28.628929138183594)
    realize_instances.location = (392.9736328125, -193.2738037109375)
    group_input_003.location = (96.82771301269531, -374.548828125)

    #Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    integer_math.width, integer_math.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0

    #initialize instancer links
    #combine_xyz.Vector -> curve_line.Start
    instancer.links.new(combine_xyz.outputs[0], curve_line.inputs[0])
    #math.Value -> combine_xyz.X
    instancer.links.new(math.outputs[0], combine_xyz.inputs[0])
    #group_input_001.Offset -> math_001.Value
    instancer.links.new(group_input_001.outputs[1], math_001.inputs[0])
    #group_input_001.Iterations -> math_001.Value
    instancer.links.new(group_input_001.outputs[2], math_001.inputs[1])
    #math_001.Value -> math.Value
    instancer.links.new(math_001.outputs[0], math.inputs[0])
    #math_001.Value -> curve_line.Length
    instancer.links.new(math_001.outputs[0], curve_line.inputs[3])
    #curve_line.Curve -> resample_curve.Curve
    instancer.links.new(curve_line.outputs[0], resample_curve.inputs[0])
    #group_input_002.Iterations -> integer_math.Value
    instancer.links.new(group_input_002.outputs[2], integer_math.inputs[0])
    #integer_math.Value -> resample_curve.Count
    instancer.links.new(integer_math.outputs[0], resample_curve.inputs[2])
    #resample_curve.Curve -> instance_on_points.Points
    instancer.links.new(resample_curve.outputs[0], instance_on_points.inputs[0])
    #realize_instances.Geometry -> group_output.Geometry
    instancer.links.new(realize_instances.outputs[0], group_output.inputs[0])
    #group_input.Geometry -> instance_on_points.Instance
    instancer.links.new(group_input.outputs[0], instance_on_points.inputs[2])
    #instance_on_points.Instances -> realize_instances.Geometry
    instancer.links.new(instance_on_points.outputs[0], realize_instances.inputs[0])
    #group_input_003.Realize Instances -> realize_instances.Selection
    instancer.links.new(group_input_003.outputs[3], realize_instances.inputs[1])
    return instancer

instancer = instancer_node_group()

