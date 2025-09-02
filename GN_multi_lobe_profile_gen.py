import bpy, mathutils

#initialize lobulo_profile node group
def lobulo_profile_node_group():
    lobulo_profile = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Lobulo Profile")

    lobulo_profile.color_tag = 'NONE'
    lobulo_profile.description = ""
    lobulo_profile.default_group_node_width = 140
    

    lobulo_profile.is_modifier = True

    #lobulo_profile interface
    #Socket Geometry
    geometry_socket = lobulo_profile.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'

    #Socket Geometry
    geometry_socket_1 = lobulo_profile.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'

    #Socket Radius
    radius_socket = lobulo_profile.interface.new_socket(name = "Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_socket.default_value = 1.0
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'

    #Socket Lobulos
    lobulos_socket = lobulo_profile.interface.new_socket(name = "Lobulos", in_out='INPUT', socket_type = 'NodeSocketInt')
    lobulos_socket.default_value = 4
    lobulos_socket.min_value = 3
    lobulos_socket.max_value = 2147483647
    lobulos_socket.subtype = 'NONE'
    lobulos_socket.attribute_domain = 'POINT'

    #Socket Resolution
    resolution_socket = lobulo_profile.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_socket.default_value = 32
    resolution_socket.min_value = 3
    resolution_socket.max_value = 512
    resolution_socket.subtype = 'NONE'
    resolution_socket.attribute_domain = 'POINT'

    #Socket epsilon
    epsilon_socket = lobulo_profile.interface.new_socket(name = "epsilon", in_out='INPUT', socket_type = 'NodeSocketFloat')
    epsilon_socket.default_value = 1.2999999523162842
    epsilon_socket.min_value = -10000.0
    epsilon_socket.max_value = 10000.0
    epsilon_socket.subtype = 'NONE'
    epsilon_socket.attribute_domain = 'POINT'

    #Socket Base Polygon
    base_polygon_socket = lobulo_profile.interface.new_socket(name = "Base Polygon", in_out='INPUT', socket_type = 'NodeSocketBool')
    base_polygon_socket.default_value = False
    base_polygon_socket.attribute_domain = 'POINT'


    #initialize lobulo_profile nodes
    #node Group Output
    group_output = lobulo_profile.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Mesh Circle
    mesh_circle = lobulo_profile.nodes.new("GeometryNodeMeshCircle")
    mesh_circle.name = "Mesh Circle"
    mesh_circle.fill_type = 'NONE'

    #node Cylinder
    cylinder = lobulo_profile.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.fill_type = 'NGON'
    #Side Segments
    cylinder.inputs[1].default_value = 1
    #Fill Segments
    cylinder.inputs[2].default_value = 1
    #Depth
    cylinder.inputs[4].default_value = 2.0

    #node Instance on Points
    instance_on_points = lobulo_profile.nodes.new("GeometryNodeInstanceOnPoints")
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
    group_input_001 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True

    #node Group Input.002
    group_input_002 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True

    #node Grid
    grid = lobulo_profile.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    #Vertices X
    grid.inputs[2].default_value = 2
    #Vertices Y
    grid.inputs[3].default_value = 2

    #node Math
    math = lobulo_profile.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY_ADD'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 4.0
    #Value_002
    math.inputs[2].default_value = 1.0

    #node Mesh Boolean
    mesh_boolean = lobulo_profile.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'EXACT'
    #Self Intersection
    mesh_boolean.inputs[2].default_value = False
    #Hole Tolerant
    mesh_boolean.inputs[3].default_value = True

    #node Realize Instances
    realize_instances = lobulo_profile.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Selection
    realize_instances.inputs[1].default_value = True
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Delete Geometry
    delete_geometry = lobulo_profile.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    #node Capture Attribute
    capture_attribute = lobulo_profile.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Selection")
    capture_attribute.capture_items["Selection"].data_type = 'BOOLEAN'
    capture_attribute.domain = 'EDGE'
    #Value
    capture_attribute.inputs[1].default_value = True

    #node Merge by Distance
    merge_by_distance = lobulo_profile.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    #Selection
    merge_by_distance.inputs[1].default_value = True
    #Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    #node Group Input
    group_input = lobulo_profile.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[0].hide = True
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True

    #node Math.001
    math_001 = lobulo_profile.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Compare
    compare = lobulo_profile.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_THAN'
    #B_INT
    compare.inputs[3].default_value = 1

    #node Face Neighbors
    face_neighbors = lobulo_profile.nodes.new("GeometryNodeInputMeshFaceNeighbors")
    face_neighbors.name = "Face Neighbors"

    #node Boolean Math
    boolean_math = lobulo_profile.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'OR'

    #node Group Input.003
    group_input_003 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True

    #node Join Geometry
    join_geometry = lobulo_profile.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Math.002
    math_002 = lobulo_profile.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False
    #Value
    math_002.inputs[0].default_value = 3.1415927410125732

    #node Math.003
    math_003 = lobulo_profile.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'SINE'
    math_003.use_clamp = False

    #node Math.004
    math_004 = lobulo_profile.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'DIVIDE'
    math_004.use_clamp = False
    #Value
    math_004.inputs[0].default_value = 1.0

    #node Math.005
    math_005 = lobulo_profile.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'SUBTRACT'
    math_005.use_clamp = False

    #node Switch
    switch = lobulo_profile.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    #node Group Input.004
    group_input_004 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[6].hide = True





    #Set locations
    group_output.location = (1333.35595703125, 106.75109100341797)
    mesh_circle.location = (-272.9564514160156, 81.71915435791016)
    cylinder.location = (-439.78289794921875, -107.4948959350586)
    instance_on_points.location = (-25.90285301208496, 65.26226806640625)
    group_input_001.location = (-847.4671020507812, -70.41656494140625)
    group_input_002.location = (-1239.18701171875, 184.22674560546875)
    grid.location = (28.2603759765625, 290.0384216308594)
    math.location = (-239.08033752441406, 319.0777282714844)
    mesh_boolean.location = (456.7449951171875, 215.8912353515625)
    realize_instances.location = (162.21365356445312, 49.0821647644043)
    delete_geometry.location = (701.3767700195312, 242.34327697753906)
    capture_attribute.location = (238.3671417236328, 273.8970031738281)
    merge_by_distance.location = (881.0, 237.270751953125)
    group_input.location = (-735.3359985351562, -240.31080627441406)
    math_001.location = (-603.8327026367188, 36.23575973510742)
    compare.location = (472.9022216796875, 396.4571533203125)
    face_neighbors.location = (251.53353881835938, 392.21209716796875)
    boolean_math.location = (689.6287231445312, 378.73046875)
    group_input_003.location = (-1034.45166015625, 44.96867752075195)
    join_geometry.location = (979.29296875, 5.937093734741211)
    math_002.location = (-1260.2655029296875, 395.51837158203125)
    math_003.location = (-1075.1204833984375, 355.8777160644531)
    math_004.location = (-877.0889892578125, 362.07611083984375)
    math_005.location = (-654.2097778320312, 378.0733337402344)
    switch.location = (1171.8126220703125, 206.1226806640625)
    group_input_004.location = (915.6583862304688, 330.9488525390625)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    mesh_circle.width, mesh_circle.height = 140.0, 100.0
    cylinder.width, cylinder.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    face_neighbors.width, face_neighbors.height = 150.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0

    #initialize lobulo_profile links
    #mesh_circle.Mesh -> instance_on_points.Points
    lobulo_profile.links.new(mesh_circle.outputs[0], instance_on_points.inputs[0])
    #math_001.Value -> mesh_circle.Radius
    lobulo_profile.links.new(math_001.outputs[0], mesh_circle.inputs[1])
    #group_input_001.Radius -> cylinder.Radius
    lobulo_profile.links.new(group_input_001.outputs[1], cylinder.inputs[3])
    #group_input_002.Lobulos -> mesh_circle.Vertices
    lobulo_profile.links.new(group_input_002.outputs[2], mesh_circle.inputs[0])
    #math.Value -> grid.Size X
    lobulo_profile.links.new(math.outputs[0], grid.inputs[0])
    #math.Value -> grid.Size Y
    lobulo_profile.links.new(math.outputs[0], grid.inputs[1])
    #instance_on_points.Instances -> realize_instances.Geometry
    lobulo_profile.links.new(instance_on_points.outputs[0], realize_instances.inputs[0])
    #cylinder.Mesh -> instance_on_points.Instance
    lobulo_profile.links.new(cylinder.outputs[0], instance_on_points.inputs[2])
    #mesh_boolean.Mesh -> delete_geometry.Geometry
    lobulo_profile.links.new(mesh_boolean.outputs[0], delete_geometry.inputs[0])
    #grid.Mesh -> capture_attribute.Geometry
    lobulo_profile.links.new(grid.outputs[0], capture_attribute.inputs[0])
    #capture_attribute.Geometry -> mesh_boolean.Mesh 1
    lobulo_profile.links.new(capture_attribute.outputs[0], mesh_boolean.inputs[0])
    #delete_geometry.Geometry -> merge_by_distance.Geometry
    lobulo_profile.links.new(delete_geometry.outputs[0], merge_by_distance.inputs[0])
    #group_input.Resolution -> cylinder.Vertices
    lobulo_profile.links.new(group_input.outputs[3], cylinder.inputs[0])
    #group_input_001.Radius -> math_001.Value
    lobulo_profile.links.new(group_input_001.outputs[1], math_001.inputs[0])
    #math_001.Value -> math.Value
    lobulo_profile.links.new(math_001.outputs[0], math.inputs[0])
    #realize_instances.Geometry -> mesh_boolean.Mesh 2
    lobulo_profile.links.new(realize_instances.outputs[0], mesh_boolean.inputs[1])
    #face_neighbors.Face Count -> compare.A
    lobulo_profile.links.new(face_neighbors.outputs[1], compare.inputs[2])
    #compare.Result -> boolean_math.Boolean
    lobulo_profile.links.new(compare.outputs[0], boolean_math.inputs[0])
    #capture_attribute.Selection -> boolean_math.Boolean
    lobulo_profile.links.new(capture_attribute.outputs[1], boolean_math.inputs[1])
    #boolean_math.Boolean -> delete_geometry.Selection
    lobulo_profile.links.new(boolean_math.outputs[0], delete_geometry.inputs[1])
    #mesh_circle.Mesh -> join_geometry.Geometry
    lobulo_profile.links.new(mesh_circle.outputs[0], join_geometry.inputs[0])
    #group_input_002.Lobulos -> math_002.Value
    lobulo_profile.links.new(group_input_002.outputs[2], math_002.inputs[1])
    #math_002.Value -> math_003.Value
    lobulo_profile.links.new(math_002.outputs[0], math_003.inputs[0])
    #math_003.Value -> math_004.Value
    lobulo_profile.links.new(math_003.outputs[0], math_004.inputs[1])
    #math_004.Value -> math_005.Value
    lobulo_profile.links.new(math_004.outputs[0], math_005.inputs[0])
    #group_input_003.epsilon -> math_005.Value
    lobulo_profile.links.new(group_input_003.outputs[4], math_005.inputs[1])
    #math_005.Value -> math_001.Value
    lobulo_profile.links.new(math_005.outputs[0], math_001.inputs[1])
    #merge_by_distance.Geometry -> switch.False
    lobulo_profile.links.new(merge_by_distance.outputs[0], switch.inputs[1])
    #switch.Output -> group_output.Geometry
    lobulo_profile.links.new(switch.outputs[0], group_output.inputs[0])
    #join_geometry.Geometry -> switch.True
    lobulo_profile.links.new(join_geometry.outputs[0], switch.inputs[2])
    #group_input_004.Base Polygon -> switch.Switch
    lobulo_profile.links.new(group_input_004.outputs[5], switch.inputs[0])
    #merge_by_distance.Geometry -> join_geometry.Geometry
    lobulo_profile.links.new(merge_by_distance.outputs[0], join_geometry.inputs[0])
    return lobulo_profile

lobulo_profile = lobulo_profile_node_group()

