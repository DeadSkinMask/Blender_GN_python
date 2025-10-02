import bpy, mathutils

#initialize radial_instancer node group
def radial_instancer_node_group():
    radial_instancer = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Radial Instancer")

    radial_instancer.color_tag = 'NONE'
    radial_instancer.description = ""
    radial_instancer.default_group_node_width = 140
    

    radial_instancer.is_modifier = True

    #radial_instancer interface
    #Socket Geometry
    geometry_socket = radial_instancer.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = radial_instancer.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Instances
    instances_socket = radial_instancer.interface.new_socket(name = "Instances", in_out='INPUT', socket_type = 'NodeSocketInt')
    instances_socket.default_value = 3
    instances_socket.min_value = 3
    instances_socket.max_value = 64
    instances_socket.subtype = 'NONE'
    instances_socket.attribute_domain = 'POINT'
    instances_socket.description = "Number of points on the circle"
    instances_socket.default_input = 'VALUE'
    instances_socket.structure_type = 'AUTO'

    #Socket Radius
    radius_socket = radial_instancer.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_socket.default_value = 0.5
    radius_socket.min_value = 9.999999747378752e-05
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.description = "Distance of the points from the origin"
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    #Socket Rotate Instances
    rotate_instances_socket = radial_instancer.interface.new_socket(name = "Rotate Instances", in_out='INPUT', socket_type = 'NodeSocketRotation')
    rotate_instances_socket.default_value = (0.0, 0.0, 0.0)
    rotate_instances_socket.attribute_domain = 'POINT'
    rotate_instances_socket.default_input = 'VALUE'
    rotate_instances_socket.structure_type = 'AUTO'

    #Socket Offset Instance
    offset_instance_socket = radial_instancer.interface.new_socket(name = "Offset Instance", in_out='INPUT', socket_type = 'NodeSocketVector')
    offset_instance_socket.default_value = (0.0, 0.0, 0.0)
    offset_instance_socket.min_value = -3.4028234663852886e+38
    offset_instance_socket.max_value = 3.4028234663852886e+38
    offset_instance_socket.subtype = 'TRANSLATION'
    offset_instance_socket.attribute_domain = 'POINT'
    offset_instance_socket.default_input = 'VALUE'
    offset_instance_socket.structure_type = 'AUTO'

    #Socket Realize Instances
    realize_instances_socket = radial_instancer.interface.new_socket(name = "Realize Instances", in_out='INPUT', socket_type = 'NodeSocketBool')
    realize_instances_socket.default_value = False
    realize_instances_socket.attribute_domain = 'POINT'
    realize_instances_socket.hide_value = True
    realize_instances_socket.description = "Which top-level instances to realize"
    realize_instances_socket.default_input = 'VALUE'
    realize_instances_socket.structure_type = 'AUTO'


    #initialize radial_instancer nodes
    #node Group Input
    group_input = radial_instancer.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True

    #node Group Output
    group_output = radial_instancer.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Instance on Points
    instance_on_points = radial_instancer.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    #Selection
    instance_on_points.inputs[1].default_value = True
    #Pick Instance
    instance_on_points.inputs[3].default_value = False
    #Instance Index
    instance_on_points.inputs[4].default_value = 0
    #Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    #node Curve Circle
    curve_circle = radial_instancer.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'

    #node Align Rotation to Vector
    align_rotation_to_vector = radial_instancer.nodes.new("FunctionNodeAlignRotationToVector")
    align_rotation_to_vector.name = "Align Rotation to Vector"
    align_rotation_to_vector.axis = 'X'
    align_rotation_to_vector.pivot_axis = 'AUTO'
    #Rotation
    align_rotation_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    #Factor
    align_rotation_to_vector.inputs[1].default_value = 1.0

    #node Curve Tangent
    curve_tangent = radial_instancer.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    #node Transform Geometry
    transform_geometry = radial_instancer.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    #Translation
    transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Combine XYZ
    combine_xyz = radial_instancer.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Y
    combine_xyz.inputs[1].default_value = 0.0

    #node Group Input.001
    group_input_001 = radial_instancer.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True

    #node Group Input.002
    group_input_002 = radial_instancer.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True

    #node Math.003
    math_003 = radial_instancer.nodes.new("ShaderNodeMath")
    math_003.label = "Mult PI/2"
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = 1.5707963705062866

    #node Group Input.003
    group_input_003 = radial_instancer.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True

    #node Rotate Instances
    rotate_instances = radial_instancer.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    #Selection
    rotate_instances.inputs[1].default_value = True
    #Pivot Point
    rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Local Space
    rotate_instances.inputs[4].default_value = True

    #node Group Input.004
    group_input_004 = radial_instancer.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True

    #node Realize Instances
    realize_instances = radial_instancer.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Group Input.005
    group_input_005 = radial_instancer.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[6].hide = True

    #node Transform Geometry.001
    transform_geometry_001 = radial_instancer.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Group Input.006
    group_input_006 = radial_instancer.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True





    #Set locations
    group_input.location = (-524.0214233398438, 161.30313110351562)
    group_output.location = (726.0441284179688, -10.241470336914062)
    instance_on_points.location = (60.88013458251953, 105.1318130493164)
    curve_circle.location = (-530.1019897460938, 464.47735595703125)
    align_rotation_to_vector.location = (-299.7496643066406, -159.43502807617188)
    curve_tangent.location = (-492.7156677246094, -220.88363647460938)
    transform_geometry.location = (-249.4485626220703, 442.5208740234375)
    combine_xyz.location = (-531.4025268554688, 303.71539306640625)
    group_input_001.location = (-750.2466430664062, 509.6000671386719)
    group_input_002.location = (-954.3473510742188, 295.3671569824219)
    math_003.location = (-733.2393188476562, 323.2262878417969)
    group_input_003.location = (-757.3587036132812, 434.52081298828125)
    rotate_instances.location = (259.6103820800781, 31.00379753112793)
    group_input_004.location = (52.249671936035156, -191.74761962890625)
    realize_instances.location = (496.5585021972656, -41.96648025512695)
    group_input_005.location = (243.93826293945312, -196.86834716796875)
    transform_geometry_001.location = (-307.4187927246094, 130.85789489746094)
    group_input_006.location = (-530.4274291992188, 52.43915557861328)

    #Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    align_rotation_to_vector.width, align_rotation_to_vector.height = 140.0, 100.0
    curve_tangent.width, curve_tangent.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    rotate_instances.width, rotate_instances.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0

    #initialize radial_instancer links
    #realize_instances.Geometry -> group_output.Geometry
    radial_instancer.links.new(realize_instances.outputs[0], group_output.inputs[0])
    #transform_geometry_001.Geometry -> instance_on_points.Instance
    radial_instancer.links.new(transform_geometry_001.outputs[0], instance_on_points.inputs[2])
    #transform_geometry.Geometry -> instance_on_points.Points
    radial_instancer.links.new(transform_geometry.outputs[0], instance_on_points.inputs[0])
    #align_rotation_to_vector.Rotation -> instance_on_points.Rotation
    radial_instancer.links.new(align_rotation_to_vector.outputs[0], instance_on_points.inputs[5])
    #curve_tangent.Tangent -> align_rotation_to_vector.Vector
    radial_instancer.links.new(curve_tangent.outputs[0], align_rotation_to_vector.inputs[2])
    #curve_circle.Curve -> transform_geometry.Geometry
    radial_instancer.links.new(curve_circle.outputs[0], transform_geometry.inputs[0])
    #combine_xyz.Vector -> transform_geometry.Rotation
    radial_instancer.links.new(combine_xyz.outputs[0], transform_geometry.inputs[2])
    #group_input_001.Instances -> curve_circle.Resolution
    radial_instancer.links.new(group_input_001.outputs[1], curve_circle.inputs[0])
    #group_input_002.Instances -> math_003.Value
    radial_instancer.links.new(group_input_002.outputs[1], math_003.inputs[0])
    #math_003.Value -> combine_xyz.Z
    radial_instancer.links.new(math_003.outputs[0], combine_xyz.inputs[2])
    #group_input_003.Radius -> curve_circle.Radius
    radial_instancer.links.new(group_input_003.outputs[2], curve_circle.inputs[4])
    #instance_on_points.Instances -> rotate_instances.Instances
    radial_instancer.links.new(instance_on_points.outputs[0], rotate_instances.inputs[0])
    #group_input_004.Rotate Instances -> rotate_instances.Rotation
    radial_instancer.links.new(group_input_004.outputs[3], rotate_instances.inputs[2])
    #rotate_instances.Instances -> realize_instances.Geometry
    radial_instancer.links.new(rotate_instances.outputs[0], realize_instances.inputs[0])
    #group_input_005.Realize Instances -> realize_instances.Selection
    radial_instancer.links.new(group_input_005.outputs[5], realize_instances.inputs[1])
    #group_input.Geometry -> transform_geometry_001.Geometry
    radial_instancer.links.new(group_input.outputs[0], transform_geometry_001.inputs[0])
    #group_input_006.Offset Instance -> transform_geometry_001.Translation
    radial_instancer.links.new(group_input_006.outputs[4], transform_geometry_001.inputs[1])
    return radial_instancer

radial_instancer = radial_instancer_node_group()

