import bpy, mathutils

#initialize voluta node group
def voluta_node_group():
    voluta = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Voluta")

    voluta.color_tag = 'NONE'
    voluta.description = ""
    voluta.default_group_node_width = 140
    

    voluta.is_modifier = True

    #voluta interface
    #Socket Geometry
    geometry_socket = voluta.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = voluta.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Rotations
    rotations_socket = voluta.interface.new_socket(name = "Rotations", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rotations_socket.default_value = 1.5
    rotations_socket.min_value = 0.0
    rotations_socket.max_value = 3.4028234663852886e+38
    rotations_socket.subtype = 'NONE'
    rotations_socket.attribute_domain = 'POINT'
    rotations_socket.description = "Number of times the spiral makes a full rotation"
    rotations_socket.default_input = 'VALUE'
    rotations_socket.structure_type = 'AUTO'

    #Socket End Radius
    end_radius_socket = voluta.interface.new_socket(name = "End Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
    end_radius_socket.default_value = 1.0
    end_radius_socket.min_value = -3.4028234663852886e+38
    end_radius_socket.max_value = 3.4028234663852886e+38
    end_radius_socket.subtype = 'DISTANCE'
    end_radius_socket.attribute_domain = 'POINT'
    end_radius_socket.description = "Horizontal Distance from the Z axis at the end of the spiral"
    end_radius_socket.default_input = 'VALUE'
    end_radius_socket.structure_type = 'AUTO'

    #Socket Resolution
    resolution_socket = voluta.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_socket.default_value = 16
    resolution_socket.min_value = 1
    resolution_socket.max_value = 32
    resolution_socket.attribute_domain = 'POINT'
    resolution_socket.description = "Number of points in one rotation of the spiral"
    resolution_socket.default_input = 'VALUE'
    resolution_socket.structure_type = 'AUTO'

    #Socket Angle
    angle_socket = voluta.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    angle_socket.default_value = 45.0
    angle_socket.min_value = -10000.0
    angle_socket.max_value = 10000.0
    angle_socket.subtype = 'NONE'
    angle_socket.attribute_domain = 'POINT'
    angle_socket.default_input = 'VALUE'
    angle_socket.structure_type = 'AUTO'

    #Socket X
    x_socket = voluta.interface.new_socket(name = "X", in_out='INPUT', socket_type = 'NodeSocketFloat')
    x_socket.default_value = 0.5
    x_socket.min_value = 0.0
    x_socket.max_value = 10000.0
    x_socket.subtype = 'NONE'
    x_socket.attribute_domain = 'POINT'
    x_socket.default_input = 'VALUE'
    x_socket.structure_type = 'AUTO'

    #Socket Z
    z_socket = voluta.interface.new_socket(name = "Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
    z_socket.default_value = 0.5
    z_socket.min_value = 0.0
    z_socket.max_value = 10000.0
    z_socket.subtype = 'NONE'
    z_socket.attribute_domain = 'POINT'
    z_socket.default_input = 'VALUE'
    z_socket.structure_type = 'AUTO'

    #Socket Scale A
    scale_a_socket = voluta.interface.new_socket(name = "Scale A", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_a_socket.default_value = 1.0
    scale_a_socket.min_value = -3.4028234663852886e+38
    scale_a_socket.max_value = 3.4028234663852886e+38
    scale_a_socket.subtype = 'NONE'
    scale_a_socket.attribute_domain = 'POINT'
    scale_a_socket.default_input = 'VALUE'
    scale_a_socket.structure_type = 'AUTO'

    #Socket Scale B
    scale_b_socket = voluta.interface.new_socket(name = "Scale B", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_b_socket.default_value = 1.0
    scale_b_socket.min_value = -3.4028234663852886e+38
    scale_b_socket.max_value = 3.4028234663852886e+38
    scale_b_socket.subtype = 'NONE'
    scale_b_socket.attribute_domain = 'POINT'
    scale_b_socket.default_input = 'VALUE'
    scale_b_socket.structure_type = 'AUTO'

    #Socket Rotate
    rotate_socket = voluta.interface.new_socket(name = "Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rotate_socket.default_value = 0.0
    rotate_socket.min_value = -360.0
    rotate_socket.max_value = 360.0
    rotate_socket.subtype = 'NONE'
    rotate_socket.attribute_domain = 'POINT'
    rotate_socket.default_input = 'VALUE'
    rotate_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = voluta.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Flip B
    flip_b_socket = voluta.interface.new_socket(name = "Flip B", in_out='INPUT', socket_type = 'NodeSocketBool')
    flip_b_socket.default_value = False
    flip_b_socket.attribute_domain = 'POINT'
    flip_b_socket.default_input = 'VALUE'
    flip_b_socket.structure_type = 'AUTO'


    #initialize voluta nodes
    #node Group Output
    group_output = voluta.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Spiral
    spiral = voluta.nodes.new("GeometryNodeCurveSpiral")
    spiral.name = "Spiral"
    #Start Radius
    spiral.inputs[2].default_value = 0.0
    #Height
    spiral.inputs[4].default_value = 0.0
    #Reverse
    spiral.inputs[5].default_value = False

    #node Transform Geometry
    transform_geometry = voluta.nodes.new("GeometryNodeTransform")
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

    #node Transform Geometry.001
    transform_geometry_001 = voluta.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    #Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Attribute Statistic
    attribute_statistic = voluta.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'POINT'
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[3].hide = True
    attribute_statistic.outputs[4].hide = True
    attribute_statistic.outputs[5].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True

    #node Position
    position = voluta.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Endpoint Selection
    endpoint_selection = voluta.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection.name = "Endpoint Selection"
    #Start Size
    endpoint_selection.inputs[0].default_value = 0
    #End Size
    endpoint_selection.inputs[1].default_value = 1

    #node Vector Math
    vector_math = voluta.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    #Vector_001
    vector_math.inputs[1].default_value = (-1.0, -1.0, -1.0)

    #node Group Input
    group_input = voluta.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[0].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True
    group_input.outputs[7].hide = True
    group_input.outputs[8].hide = True
    group_input.outputs[9].hide = True
    group_input.outputs[10].hide = True
    group_input.outputs[11].hide = True
    group_input.outputs[12].hide = True

    #node Curve Line
    curve_line = voluta.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'POINTS'

    #node Instance on Points
    instance_on_points = voluta.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    #Selection
    instance_on_points.inputs[1].default_value = True
    #Pick Instance
    instance_on_points.inputs[3].default_value = False
    #Instance Index
    instance_on_points.inputs[4].default_value = 0
    #Scale
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)

    #node Transform Geometry.002
    transform_geometry_002 = voluta.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    #Translation
    transform_geometry_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Group Input.001
    group_input_001 = voluta.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True
    group_input_001.outputs[11].hide = True
    group_input_001.outputs[12].hide = True

    #node Combine XYZ
    combine_xyz = voluta.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Z
    combine_xyz.inputs[2].default_value = 0.0

    #node Math.002
    math_002 = voluta.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'FRACT'
    math_002.use_clamp = False

    #node Math.003
    math_003 = voluta.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = -6.28318977355957

    #node Frame
    frame = voluta.nodes.new("NodeFrame")
    frame.label = "Compensar Rotacion"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Frame.001
    frame_001 = voluta.nodes.new("NodeFrame")
    frame_001.label = "Centrar en Endpoint"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Reroute
    reroute = voluta.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    #node Frame.002
    frame_002 = voluta.nodes.new("NodeFrame")
    frame_002.label = "Generar Espiral"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Endpoint Selection.001
    endpoint_selection_001 = voluta.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection_001.name = "Endpoint Selection.001"
    #Start Size
    endpoint_selection_001.inputs[0].default_value = 1
    #End Size
    endpoint_selection_001.inputs[1].default_value = 0

    #node Rotate Instances
    rotate_instances = voluta.nodes.new("GeometryNodeRotateInstances")
    rotate_instances.name = "Rotate Instances"
    #Pivot Point
    rotate_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Local Space
    rotate_instances.inputs[4].default_value = True

    #node Capture Attribute
    capture_attribute = voluta.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 1
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Selection")
    capture_attribute.capture_items["Selection"].data_type = 'BOOLEAN'
    capture_attribute.capture_items.new('FLOAT', "Selection.001")
    capture_attribute.capture_items["Selection.001"].data_type = 'BOOLEAN'
    capture_attribute.domain = 'POINT'

    #node Store Named Attribute
    store_named_attribute = voluta.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'FLOAT'
    store_named_attribute.domain = 'POINT'
    #Selection
    store_named_attribute.inputs[1].default_value = True
    #Name
    store_named_attribute.inputs[2].default_value = "weight"

    #node Spline Parameter
    spline_parameter = voluta.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"

    #node Realize Instances
    realize_instances = voluta.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Selection
    realize_instances.inputs[1].default_value = True
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Store Named Attribute.001
    store_named_attribute_001 = voluta.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = 'FLOAT'
    store_named_attribute_001.domain = 'POINT'
    #Name
    store_named_attribute_001.inputs[2].default_value = "weight"

    #node Reroute.001
    reroute_001 = voluta.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketBool"
    #node Named Attribute
    named_attribute = voluta.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'FLOAT'
    #Name
    named_attribute.inputs[0].default_value = "weight"

    #node Curve to Points
    curve_to_points = voluta.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points.name = "Curve to Points"
    curve_to_points.mode = 'EVALUATED'

    #node Points to Curves
    points_to_curves = voluta.nodes.new("GeometryNodePointsToCurves")
    points_to_curves.name = "Points to Curves"
    #Curve Group ID
    points_to_curves.inputs[1].default_value = 0

    #node Named Attribute.001
    named_attribute_001 = voluta.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = 'FLOAT'
    #Name
    named_attribute_001.inputs[0].default_value = "weight"

    #node Math.001
    math_001 = voluta.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'SUBTRACT'
    math_001.use_clamp = False
    #Value
    math_001.inputs[0].default_value = 2.0999999046325684

    #node Frame.003
    frame_003 = voluta.nodes.new("NodeFrame")
    frame_003.label = "Reconstruir Curvas"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Group Input.002
    group_input_002 = voluta.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    group_input_002.outputs[11].hide = True
    group_input_002.outputs[12].hide = True

    #node Group Input.003
    group_input_003 = voluta.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True
    group_input_003.outputs[11].hide = True
    group_input_003.outputs[12].hide = True

    #node Group Input.004
    group_input_004 = voluta.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True

    #node Combine XYZ.001
    combine_xyz_001 = voluta.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #X
    combine_xyz_001.inputs[0].default_value = 0.0
    #Z
    combine_xyz_001.inputs[2].default_value = 0.0

    #node Math
    math = voluta.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'RADIANS'
    math.use_clamp = False

    #node Math.004
    math_004 = voluta.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    #Value_001
    math_004.inputs[1].default_value = -1.0

    #node Group Input.005
    group_input_005 = voluta.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True
    group_input_005.outputs[11].hide = True
    group_input_005.outputs[12].hide = True

    #node Vector Math.001
    vector_math_001 = voluta.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    #Vector_001
    vector_math_001.inputs[1].default_value = (-1.0, 0.0, -1.0)

    #node Combine XYZ.002
    combine_xyz_002 = voluta.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    #Y
    combine_xyz_002.inputs[1].default_value = 0.0

    #node Group Input.006
    group_input_006 = voluta.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True

    #node Group Input.007
    group_input_007 = voluta.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True
    group_input_007.outputs[11].hide = True
    group_input_007.outputs[12].hide = True

    #node Scale Instances
    scale_instances = voluta.nodes.new("GeometryNodeScaleInstances")
    scale_instances.name = "Scale Instances"
    #Center
    scale_instances.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Local Space
    scale_instances.inputs[4].default_value = True

    #node Endpoint Selection.002
    endpoint_selection_002 = voluta.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection_002.name = "Endpoint Selection.002"
    #Start Size
    endpoint_selection_002.inputs[0].default_value = 0
    #End Size
    endpoint_selection_002.inputs[1].default_value = 1

    #node Scale Instances.001
    scale_instances_001 = voluta.nodes.new("GeometryNodeScaleInstances")
    scale_instances_001.name = "Scale Instances.001"
    #Center
    scale_instances_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Local Space
    scale_instances_001.inputs[4].default_value = True

    #node Group Input.008
    group_input_008 = voluta.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    group_input_008.outputs[11].hide = True
    group_input_008.outputs[12].hide = True

    #node Group Input.009
    group_input_009 = voluta.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    group_input_009.outputs[11].hide = True
    group_input_009.outputs[12].hide = True

    #node Frame.004
    frame_004 = voluta.nodes.new("NodeFrame")
    frame_004.label = "Scale Spirals"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    #node Frame.005
    frame_005 = voluta.nodes.new("NodeFrame")
    frame_005.label = "Curve Line"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    #node Frame.006
    frame_006 = voluta.nodes.new("NodeFrame")
    frame_006.label = "Instances Rotation"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    #node Frame.007
    frame_007 = voluta.nodes.new("NodeFrame")
    frame_007.label = "Capturar Instancias"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    #node Transform Geometry.003
    transform_geometry_003 = voluta.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    #Translation
    transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Combine XYZ.003
    combine_xyz_003 = voluta.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    #X
    combine_xyz_003.inputs[0].default_value = 0.0
    #Z
    combine_xyz_003.inputs[2].default_value = 0.0

    #node Math.005
    math_005 = voluta.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'RADIANS'
    math_005.use_clamp = False

    #node Group Input.010
    group_input_010 = voluta.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[1].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[4].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[10].hide = True
    group_input_010.outputs[11].hide = True
    group_input_010.outputs[12].hide = True

    #node Combine XYZ.004
    combine_xyz_004 = voluta.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    #X
    combine_xyz_004.inputs[0].default_value = 0.0
    #Y
    combine_xyz_004.inputs[1].default_value = 3.1415927410125732

    #node Switch
    switch = voluta.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'FLOAT'
    #False
    switch.inputs[1].default_value = 0.0
    #True
    switch.inputs[2].default_value = 3.1415927410125732

    #node Group Input.011
    group_input_011 = voluta.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[1].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[4].hide = True
    group_input_011.outputs[5].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[12].hide = True

    #node Group Input.012
    group_input_012 = voluta.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[11].hide = True
    group_input_012.outputs[12].hide = True




    #Set parents
    spiral.parent = frame_002
    transform_geometry.parent = frame_002
    transform_geometry_001.parent = frame_001
    attribute_statistic.parent = frame_001
    position.parent = frame_001
    endpoint_selection.parent = frame_001
    vector_math.parent = frame_001
    group_input.parent = frame_002
    curve_line.parent = frame_005
    transform_geometry_002.parent = frame
    group_input_001.parent = frame
    combine_xyz.parent = frame
    math_002.parent = frame
    math_003.parent = frame
    reroute.parent = frame_001
    endpoint_selection_001.parent = frame_007
    rotate_instances.parent = frame_003
    capture_attribute.parent = frame_007
    store_named_attribute.parent = frame_002
    spline_parameter.parent = frame_002
    realize_instances.parent = frame_003
    store_named_attribute_001.parent = frame_003
    named_attribute.parent = frame_003
    curve_to_points.parent = frame_003
    points_to_curves.parent = frame_003
    named_attribute_001.parent = frame_003
    math_001.parent = frame_003
    group_input_002.parent = frame_002
    group_input_003.parent = frame_002
    combine_xyz_001.parent = frame_006
    math.parent = frame_006
    math_004.parent = frame_006
    group_input_005.parent = frame_006
    vector_math_001.parent = frame_005
    combine_xyz_002.parent = frame_005
    group_input_006.parent = frame_005
    group_input_007.parent = frame_005
    scale_instances.parent = frame_004
    endpoint_selection_002.parent = frame_007
    scale_instances_001.parent = frame_004
    group_input_008.parent = frame_004
    group_input_009.parent = frame_004

    #Set locations
    group_output.location = (3592.9228515625, 413.7896423339844)
    spiral.location = (230.01641845703125, -83.20565795898438)
    transform_geometry.location = (654.7460327148438, -142.12557983398438)
    transform_geometry_001.location = (644.1796875, -35.86627197265625)
    attribute_statistic.location = (259.35205078125, -129.17784118652344)
    position.location = (29.73590087890625, -368.3230285644531)
    endpoint_selection.location = (34.8466796875, -241.0882568359375)
    vector_math.location = (454.59283447265625, -110.52432250976562)
    group_input.location = (30.86407470703125, -103.14056396484375)
    curve_line.location = (636.6668701171875, -35.5987548828125)
    instance_on_points.location = (1252.9853515625, 404.2781982421875)
    transform_geometry_002.location = (923.159423828125, -36.28564453125)
    group_input_001.location = (29.65863037109375, -201.986572265625)
    combine_xyz.location = (680.938720703125, -160.5792236328125)
    math_002.location = (295.10260009765625, -155.75567626953125)
    math_003.location = (489.86956787109375, -159.36463928222656)
    frame.location = (-893.0, 125.0)
    frame_001.location = (237.0, 91.0)
    reroute.location = (138.82720947265625, -109.12057495117188)
    frame_002.location = (-866.0, 563.0)
    endpoint_selection_001.location = (35.3135986328125, -36.4180908203125)
    rotate_instances.location = (38.611083984375, -35.806121826171875)
    capture_attribute.location = (353.69873046875, -37.56219482421875)
    store_named_attribute.location = (447.006103515625, -118.57901000976562)
    spline_parameter.location = (41.243896484375, -234.62332153320312)
    realize_instances.location = (252.32421875, -66.69284057617188)
    store_named_attribute_001.location = (432.546142578125, -40.256072998046875)
    reroute_001.location = (1466.58642578125, 544.8922119140625)
    named_attribute.location = (30.203125, -325.9064025878906)
    curve_to_points.location = (615.572265625, -48.985504150390625)
    points_to_curves.location = (821.290283203125, -141.14596557617188)
    named_attribute_001.location = (581.06884765625, -253.78646850585938)
    math_001.location = (203.68212890625, -222.53668212890625)
    frame_003.location = (2055.0, 544.0)
    group_input_002.location = (30.1246337890625, -172.81951904296875)
    group_input_003.location = (32.71612548828125, -36.0294189453125)
    group_input_004.location = (-838.4755859375, 563.3768920898438)
    combine_xyz_001.location = (596.7800903320312, -35.958404541015625)
    math.location = (237.01266479492188, -68.77496337890625)
    math_004.location = (416.59722900390625, -37.913970947265625)
    group_input_005.location = (30.393646240234375, -121.58686828613281)
    vector_math_001.location = (440.769775390625, -42.52886962890625)
    combine_xyz_002.location = (229.82296752929688, -100.4671630859375)
    group_input_006.location = (29.572616577148438, -122.060546875)
    group_input_007.location = (33.40592956542969, -191.1820068359375)
    scale_instances.location = (212.016845703125, -36.32769775390625)
    endpoint_selection_002.location = (30.2025146484375, -147.781005859375)
    scale_instances_001.location = (383.3392333984375, -41.863006591796875)
    group_input_008.location = (29.9388427734375, -256.6646423339844)
    group_input_009.location = (197.8487548828125, -259.4538269042969)
    frame_004.location = (1441.0, 431.0)
    frame_005.location = (-264.0, 904.0)
    frame_006.location = (266.0, 366.0)
    frame_007.location = (617.0, 671.0)
    transform_geometry_003.location = (3368.60595703125, 426.107421875)
    combine_xyz_003.location = (3131.1318359375, 296.5494689941406)
    math_005.location = (3125.606689453125, 155.39854431152344)
    group_input_010.location = (3118.62158203125, 8.171304702758789)
    combine_xyz_004.location = (1852.7650146484375, 672.7412719726562)
    switch.location = (1644.8673095703125, 719.814208984375)
    group_input_011.location = (1447.480224609375, 713.89404296875)
    group_input_012.location = (3362.34423828125, 160.3316192626953)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    spiral.width, spiral.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    frame.width, frame.height = 1093.0, 337.0
    frame_001.width, frame_001.height = 814.0, 448.0
    reroute.width, reroute.height = 10.0, 100.0
    frame_002.width, frame_002.height = 825.0, 359.0
    endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
    rotate_instances.width, rotate_instances.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    spline_parameter.width, spline_parameter.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 10.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    curve_to_points.width, curve_to_points.height = 140.0, 100.0
    points_to_curves.width, points_to_curves.height = 140.0, 100.0
    named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    frame_003.width, frame_003.height = 991.0, 477.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    scale_instances.width, scale_instances.height = 140.0, 100.0
    endpoint_selection_002.width, endpoint_selection_002.height = 140.0, 100.0
    scale_instances_001.width, scale_instances_001.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    frame_004.width, frame_004.height = 553.0, 341.0
    frame_005.width, frame_005.height = 807.0, 273.0
    frame_006.width, frame_006.height = 767.0, 225.0
    frame_007.width, frame_007.height = 524.0, 275.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0

    #initialize voluta links
    #store_named_attribute.Geometry -> transform_geometry.Geometry
    voluta.links.new(store_named_attribute.outputs[0], transform_geometry.inputs[0])
    #reroute.Output -> transform_geometry_001.Geometry
    voluta.links.new(reroute.outputs[0], transform_geometry_001.inputs[0])
    #position.Position -> attribute_statistic.Attribute
    voluta.links.new(position.outputs[0], attribute_statistic.inputs[2])
    #endpoint_selection.Selection -> attribute_statistic.Selection
    voluta.links.new(endpoint_selection.outputs[0], attribute_statistic.inputs[1])
    #vector_math.Vector -> transform_geometry_001.Translation
    voluta.links.new(vector_math.outputs[0], transform_geometry_001.inputs[1])
    #attribute_statistic.Mean -> vector_math.Vector
    voluta.links.new(attribute_statistic.outputs[0], vector_math.inputs[0])
    #group_input.Rotations -> spiral.Rotations
    voluta.links.new(group_input.outputs[1], spiral.inputs[1])
    #capture_attribute.Geometry -> instance_on_points.Points
    voluta.links.new(capture_attribute.outputs[0], instance_on_points.inputs[0])
    #transform_geometry_001.Geometry -> instance_on_points.Instance
    voluta.links.new(transform_geometry_001.outputs[0], instance_on_points.inputs[2])
    #transform_geometry.Geometry -> transform_geometry_002.Geometry
    voluta.links.new(transform_geometry.outputs[0], transform_geometry_002.inputs[0])
    #reroute.Output -> attribute_statistic.Geometry
    voluta.links.new(reroute.outputs[0], attribute_statistic.inputs[0])
    #group_input_001.Rotations -> math_002.Value
    voluta.links.new(group_input_001.outputs[1], math_002.inputs[0])
    #math_002.Value -> math_003.Value
    voluta.links.new(math_002.outputs[0], math_003.inputs[0])
    #math_003.Value -> combine_xyz.Y
    voluta.links.new(math_003.outputs[0], combine_xyz.inputs[1])
    #combine_xyz.Vector -> transform_geometry_002.Rotation
    voluta.links.new(combine_xyz.outputs[0], transform_geometry_002.inputs[2])
    #transform_geometry_002.Geometry -> reroute.Input
    voluta.links.new(transform_geometry_002.outputs[0], reroute.inputs[0])
    #transform_geometry_003.Geometry -> group_output.Geometry
    voluta.links.new(transform_geometry_003.outputs[0], group_output.inputs[0])
    #scale_instances_001.Instances -> rotate_instances.Instances
    voluta.links.new(scale_instances_001.outputs[0], rotate_instances.inputs[0])
    #endpoint_selection_001.Selection -> capture_attribute.Selection
    voluta.links.new(endpoint_selection_001.outputs[0], capture_attribute.inputs[1])
    #curve_line.Curve -> capture_attribute.Geometry
    voluta.links.new(curve_line.outputs[0], capture_attribute.inputs[0])
    #spiral.Curve -> store_named_attribute.Geometry
    voluta.links.new(spiral.outputs[0], store_named_attribute.inputs[0])
    #spline_parameter.Factor -> store_named_attribute.Value
    voluta.links.new(spline_parameter.outputs[0], store_named_attribute.inputs[3])
    #rotate_instances.Instances -> realize_instances.Geometry
    voluta.links.new(rotate_instances.outputs[0], realize_instances.inputs[0])
    #realize_instances.Geometry -> store_named_attribute_001.Geometry
    voluta.links.new(realize_instances.outputs[0], store_named_attribute_001.inputs[0])
    #capture_attribute.Selection -> reroute_001.Input
    voluta.links.new(capture_attribute.outputs[1], reroute_001.inputs[0])
    #reroute_001.Output -> store_named_attribute_001.Selection
    voluta.links.new(reroute_001.outputs[0], store_named_attribute_001.inputs[1])
    #store_named_attribute_001.Geometry -> curve_to_points.Curve
    voluta.links.new(store_named_attribute_001.outputs[0], curve_to_points.inputs[0])
    #curve_to_points.Points -> points_to_curves.Points
    voluta.links.new(curve_to_points.outputs[0], points_to_curves.inputs[0])
    #named_attribute_001.Attribute -> points_to_curves.Weight
    voluta.links.new(named_attribute_001.outputs[0], points_to_curves.inputs[2])
    #named_attribute.Attribute -> math_001.Value
    voluta.links.new(named_attribute.outputs[0], math_001.inputs[1])
    #math_001.Value -> store_named_attribute_001.Value
    voluta.links.new(math_001.outputs[0], store_named_attribute_001.inputs[3])
    #reroute_001.Output -> rotate_instances.Selection
    voluta.links.new(reroute_001.outputs[0], rotate_instances.inputs[1])
    #group_input_002.End Radius -> spiral.End Radius
    voluta.links.new(group_input_002.outputs[2], spiral.inputs[3])
    #group_input_003.Resolution -> spiral.Resolution
    voluta.links.new(group_input_003.outputs[3], spiral.inputs[0])
    #combine_xyz_001.Vector -> instance_on_points.Rotation
    voluta.links.new(combine_xyz_001.outputs[0], instance_on_points.inputs[5])
    #math.Value -> math_004.Value
    voluta.links.new(math.outputs[0], math_004.inputs[0])
    #group_input_005.Angle -> math.Value
    voluta.links.new(group_input_005.outputs[4], math.inputs[0])
    #math.Value -> combine_xyz_001.Y
    voluta.links.new(math.outputs[0], combine_xyz_001.inputs[1])
    #vector_math_001.Vector -> curve_line.Start
    voluta.links.new(vector_math_001.outputs[0], curve_line.inputs[0])
    #combine_xyz_002.Vector -> vector_math_001.Vector
    voluta.links.new(combine_xyz_002.outputs[0], vector_math_001.inputs[0])
    #combine_xyz_002.Vector -> curve_line.End
    voluta.links.new(combine_xyz_002.outputs[0], curve_line.inputs[1])
    #group_input_006.X -> combine_xyz_002.X
    voluta.links.new(group_input_006.outputs[5], combine_xyz_002.inputs[0])
    #group_input_007.Z -> combine_xyz_002.Z
    voluta.links.new(group_input_007.outputs[6], combine_xyz_002.inputs[2])
    #instance_on_points.Instances -> scale_instances.Instances
    voluta.links.new(instance_on_points.outputs[0], scale_instances.inputs[0])
    #reroute_001.Output -> scale_instances.Selection
    voluta.links.new(reroute_001.outputs[0], scale_instances.inputs[1])
    #endpoint_selection_002.Selection -> capture_attribute.Selection.001
    voluta.links.new(endpoint_selection_002.outputs[0], capture_attribute.inputs[2])
    #scale_instances.Instances -> scale_instances_001.Instances
    voluta.links.new(scale_instances.outputs[0], scale_instances_001.inputs[0])
    #capture_attribute.Selection.001 -> scale_instances_001.Selection
    voluta.links.new(capture_attribute.outputs[2], scale_instances_001.inputs[1])
    #group_input_008.Scale B -> scale_instances.Scale
    voluta.links.new(group_input_008.outputs[8], scale_instances.inputs[2])
    #group_input_009.Scale A -> scale_instances_001.Scale
    voluta.links.new(group_input_009.outputs[7], scale_instances_001.inputs[2])
    #points_to_curves.Curves -> transform_geometry_003.Geometry
    voluta.links.new(points_to_curves.outputs[0], transform_geometry_003.inputs[0])
    #combine_xyz_003.Vector -> transform_geometry_003.Rotation
    voluta.links.new(combine_xyz_003.outputs[0], transform_geometry_003.inputs[2])
    #math_005.Value -> combine_xyz_003.Y
    voluta.links.new(math_005.outputs[0], combine_xyz_003.inputs[1])
    #group_input_010.Rotate -> math_005.Value
    voluta.links.new(group_input_010.outputs[9], math_005.inputs[0])
    #combine_xyz_004.Vector -> rotate_instances.Rotation
    voluta.links.new(combine_xyz_004.outputs[0], rotate_instances.inputs[2])
    #switch.Output -> combine_xyz_004.Z
    voluta.links.new(switch.outputs[0], combine_xyz_004.inputs[2])
    #group_input_011.Flip B -> switch.Switch
    voluta.links.new(group_input_011.outputs[11], switch.inputs[0])
    #group_input_012.Scale -> transform_geometry_003.Scale
    voluta.links.new(group_input_012.outputs[10], transform_geometry_003.inputs[3])
    return voluta

voluta = voluta_node_group()

