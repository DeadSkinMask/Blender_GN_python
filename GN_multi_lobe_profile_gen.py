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
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = lobulo_profile.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = lobulo_profile.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'DISTANCE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Lobulos
    lobulos_socket = lobulo_profile.interface.new_socket(name = "Lobulos", in_out='INPUT', socket_type = 'NodeSocketInt')
    lobulos_socket.default_value = 4
    lobulos_socket.min_value = 3
    lobulos_socket.max_value = 2147483647
    lobulos_socket.subtype = 'NONE'
    lobulos_socket.attribute_domain = 'POINT'
    lobulos_socket.default_input = 'VALUE'
    lobulos_socket.structure_type = 'AUTO'

    #Socket Resolution
    resolution_socket = lobulo_profile.interface.new_socket(name = "Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
    resolution_socket.default_value = 32
    resolution_socket.min_value = 3
    resolution_socket.max_value = 512
    resolution_socket.subtype = 'NONE'
    resolution_socket.attribute_domain = 'POINT'
    resolution_socket.default_input = 'VALUE'
    resolution_socket.structure_type = 'AUTO'

    #Socket epsilon
    epsilon_socket = lobulo_profile.interface.new_socket(name = "epsilon", in_out='INPUT', socket_type = 'NodeSocketFloat')
    epsilon_socket.default_value = 2.0
    epsilon_socket.min_value = -10000.0
    epsilon_socket.max_value = 10000.0
    epsilon_socket.subtype = 'NONE'
    epsilon_socket.attribute_domain = 'POINT'
    epsilon_socket.default_input = 'VALUE'
    epsilon_socket.structure_type = 'AUTO'

    #Socket Rotate
    rotate_socket = lobulo_profile.interface.new_socket(name = "Rotate", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rotate_socket.default_value = 0.0
    rotate_socket.min_value = -10000.0
    rotate_socket.max_value = 10000.0
    rotate_socket.subtype = 'NONE'
    rotate_socket.attribute_domain = 'POINT'
    rotate_socket.default_input = 'VALUE'
    rotate_socket.structure_type = 'AUTO'


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
    #Radius
    cylinder.inputs[3].default_value = 1.0
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

    #node Group Input
    group_input = lobulo_profile.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[0].hide = True
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True

    #node Group Input.003
    group_input_003 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True

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

    #node Repeat Input
    repeat_input = lobulo_profile.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    #node Repeat Output
    repeat_output = lobulo_profile.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 0
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")

    #node Realize Instances.001
    realize_instances_001 = lobulo_profile.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    #Realize All
    realize_instances_001.inputs[2].default_value = True
    #Depth
    realize_instances_001.inputs[3].default_value = 0

    #node Compare.001
    compare_001 = lobulo_profile.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'

    #node Index
    index = lobulo_profile.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    #node Mesh Boolean.001
    mesh_boolean_001 = lobulo_profile.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.operation = 'DIFFERENCE'
    mesh_boolean_001.solver = 'MANIFOLD'

    #node Store Named Attribute
    store_named_attribute = lobulo_profile.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    #Selection
    store_named_attribute.inputs[1].default_value = True
    #Name
    store_named_attribute.inputs[2].default_value = "borders"

    #node Delete Geometry
    delete_geometry = lobulo_profile.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    #node Named Attribute
    named_attribute = lobulo_profile.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'BOOLEAN'
    #Name
    named_attribute.inputs[0].default_value = "borders"

    #node Boolean Math.001
    boolean_math_001 = lobulo_profile.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'NOT'

    #node Scale Elements
    scale_elements = lobulo_profile.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'FACE'
    scale_elements.scale_mode = 'SINGLE_AXIS'
    #Selection
    scale_elements.inputs[1].default_value = True
    #Scale
    scale_elements.inputs[2].default_value = 0.0
    #Center
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Axis
    scale_elements.inputs[4].default_value = (0.0, 0.0, 1.0)

    #node Delete Geometry.001
    delete_geometry_001 = lobulo_profile.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'

    #node Face Area
    face_area = lobulo_profile.nodes.new("GeometryNodeInputMeshFaceArea")
    face_area.name = "Face Area"

    #node Group Input.005
    group_input_005 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True

    #node Realize Instances
    realize_instances = lobulo_profile.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.inputs[1].hide = True
    realize_instances.inputs[2].hide = True
    realize_instances.inputs[3].hide = True
    #Selection
    realize_instances.inputs[1].default_value = True
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Bounding Box
    bounding_box = lobulo_profile.nodes.new("GeometryNodeBoundBox")
    bounding_box.name = "Bounding Box"
    bounding_box.inputs[1].hide = True
    bounding_box.outputs[1].hide = True
    bounding_box.outputs[2].hide = True
    #Use Radius
    bounding_box.inputs[1].default_value = True

    #node Transform Geometry
    transform_geometry = lobulo_profile.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[1].hide = True
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[4].hide = True
    #Translation
    transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry.inputs[3].default_value = (1.100000023841858, 1.100000023841858, 0.5)

    #node Math
    math = lobulo_profile.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'RADIANS'
    math.use_clamp = False

    #node Scale Elements.001
    scale_elements_001 = lobulo_profile.nodes.new("GeometryNodeScaleElements")
    scale_elements_001.name = "Scale Elements.001"
    scale_elements_001.domain = 'EDGE'
    scale_elements_001.scale_mode = 'UNIFORM'
    #Selection
    scale_elements_001.inputs[1].default_value = True
    #Center
    scale_elements_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Transform Geometry.001
    transform_geometry_001 = lobulo_profile.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Combine XYZ
    combine_xyz = lobulo_profile.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Y
    combine_xyz.inputs[1].default_value = 0.0

    #node Math.001
    math_001 = lobulo_profile.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'RADIANS'
    math_001.use_clamp = False

    #node Group Input.006
    group_input_006 = lobulo_profile.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[6].hide = True


    #Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)
    #Iterations
    repeat_input.inputs[0].default_value = 1





    #Set locations
    group_output.location = (2414.088134765625, -387.35980224609375)
    mesh_circle.location = (-268.1220397949219, -391.7825622558594)
    cylinder.location = (-264.57611083984375, -597.151611328125)
    instance_on_points.location = (-64.86080169677734, -474.3516845703125)
    group_input_001.location = (1817.8111572265625, -440.03912353515625)
    group_input_002.location = (-1333.3409423828125, -513.4461669921875)
    group_input.location = (-460.61431884765625, -690.8408203125)
    group_input_003.location = (-916.443115234375, -704.4942626953125)
    math_002.location = (-1112.280029296875, -433.14239501953125)
    math_003.location = (-927.135009765625, -472.78302001953125)
    math_004.location = (-729.103515625, -466.58465576171875)
    math_005.location = (-506.2243347167969, -450.58740234375)
    repeat_input.location = (234.64703369140625, -371.9570007324219)
    repeat_output.location = (1189.39599609375, -352.0542907714844)
    realize_instances_001.location = (608.413330078125, -363.0114440917969)
    compare_001.location = (434.03515625, -416.43939208984375)
    index.location = (211.80337524414062, -560.7274169921875)
    mesh_boolean_001.location = (817.30322265625, -261.25628662109375)
    store_named_attribute.location = (992.0535278320312, -297.8452453613281)
    delete_geometry.location = (1397.120849609375, -343.8625183105469)
    named_attribute.location = (1004.3880615234375, -538.3595581054688)
    boolean_math_001.location = (1189.0745849609375, -525.9686279296875)
    scale_elements.location = (1590.376220703125, -327.5885925292969)
    delete_geometry_001.location = (1819.8270263671875, -292.6676025390625)
    face_area.location = (1611.5355224609375, -240.51776123046875)
    group_input_005.location = (-484.540771484375, -325.99114990234375)
    realize_instances.location = (151.0387725830078, -225.8817138671875)
    bounding_box.location = (325.9540710449219, -199.91140747070312)
    transform_geometry.location = (494.9978942871094, -195.058349609375)
    math.location = (-743.24267578125, -633.185302734375)
    scale_elements_001.location = (2003.941650390625, -292.2198791503906)
    transform_geometry_001.location = (2208.740478515625, -303.8370361328125)
    combine_xyz.location = (1997.4674072265625, -488.4549560546875)
    math_001.location = (1818.5968017578125, -533.2515869140625)
    group_input_006.location = (1603.9521484375, -620.0919189453125)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    mesh_circle.width, mesh_circle.height = 140.0, 100.0
    cylinder.width, cylinder.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    repeat_input.width, repeat_input.height = 140.0, 100.0
    repeat_output.width, repeat_output.height = 140.0, 100.0
    realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    face_area.width, face_area.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    bounding_box.width, bounding_box.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    scale_elements_001.width, scale_elements_001.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0

    #initialize lobulo_profile links
    #mesh_circle.Mesh -> instance_on_points.Points
    lobulo_profile.links.new(mesh_circle.outputs[0], instance_on_points.inputs[0])
    #group_input.Resolution -> cylinder.Vertices
    lobulo_profile.links.new(group_input.outputs[3], cylinder.inputs[0])
    #group_input_002.Lobulos -> math_002.Value
    lobulo_profile.links.new(group_input_002.outputs[2], math_002.inputs[1])
    #math_002.Value -> math_003.Value
    lobulo_profile.links.new(math_002.outputs[0], math_003.inputs[0])
    #math_003.Value -> math_004.Value
    lobulo_profile.links.new(math_003.outputs[0], math_004.inputs[1])
    #math_004.Value -> math_005.Value
    lobulo_profile.links.new(math_004.outputs[0], math_005.inputs[0])
    #cylinder.Mesh -> instance_on_points.Instance
    lobulo_profile.links.new(cylinder.outputs[0], instance_on_points.inputs[2])
    #instance_on_points.Instances -> repeat_input.Geometry
    lobulo_profile.links.new(instance_on_points.outputs[0], repeat_input.inputs[1])
    #repeat_input.Geometry -> realize_instances_001.Geometry
    lobulo_profile.links.new(repeat_input.outputs[1], realize_instances_001.inputs[0])
    #compare_001.Result -> realize_instances_001.Selection
    lobulo_profile.links.new(compare_001.outputs[0], realize_instances_001.inputs[1])
    #repeat_input.Iteration -> compare_001.A
    lobulo_profile.links.new(repeat_input.outputs[0], compare_001.inputs[2])
    #index.Index -> compare_001.B
    lobulo_profile.links.new(index.outputs[0], compare_001.inputs[3])
    #realize_instances_001.Geometry -> mesh_boolean_001.Mesh 2
    lobulo_profile.links.new(realize_instances_001.outputs[0], mesh_boolean_001.inputs[1])
    #mesh_boolean_001.Intersecting Edges -> store_named_attribute.Value
    lobulo_profile.links.new(mesh_boolean_001.outputs[1], store_named_attribute.inputs[3])
    #mesh_boolean_001.Mesh -> store_named_attribute.Geometry
    lobulo_profile.links.new(mesh_boolean_001.outputs[0], store_named_attribute.inputs[0])
    #store_named_attribute.Geometry -> repeat_output.Geometry
    lobulo_profile.links.new(store_named_attribute.outputs[0], repeat_output.inputs[0])
    #repeat_output.Geometry -> delete_geometry.Geometry
    lobulo_profile.links.new(repeat_output.outputs[0], delete_geometry.inputs[0])
    #boolean_math_001.Boolean -> delete_geometry.Selection
    lobulo_profile.links.new(boolean_math_001.outputs[0], delete_geometry.inputs[1])
    #named_attribute.Attribute -> boolean_math_001.Boolean
    lobulo_profile.links.new(named_attribute.outputs[0], boolean_math_001.inputs[0])
    #delete_geometry.Geometry -> scale_elements.Geometry
    lobulo_profile.links.new(delete_geometry.outputs[0], scale_elements.inputs[0])
    #scale_elements.Geometry -> delete_geometry_001.Geometry
    lobulo_profile.links.new(scale_elements.outputs[0], delete_geometry_001.inputs[0])
    #face_area.Area -> delete_geometry_001.Selection
    lobulo_profile.links.new(face_area.outputs[0], delete_geometry_001.inputs[1])
    #group_input_005.Lobulos -> mesh_circle.Vertices
    lobulo_profile.links.new(group_input_005.outputs[2], mesh_circle.inputs[0])
    #instance_on_points.Instances -> realize_instances.Geometry
    lobulo_profile.links.new(instance_on_points.outputs[0], realize_instances.inputs[0])
    #realize_instances.Geometry -> bounding_box.Geometry
    lobulo_profile.links.new(realize_instances.outputs[0], bounding_box.inputs[0])
    #bounding_box.Bounding Box -> transform_geometry.Geometry
    lobulo_profile.links.new(bounding_box.outputs[0], transform_geometry.inputs[0])
    #group_input_003.epsilon -> math.Value
    lobulo_profile.links.new(group_input_003.outputs[4], math.inputs[0])
    #math.Value -> math_005.Value
    lobulo_profile.links.new(math.outputs[0], math_005.inputs[1])
    #math_005.Value -> mesh_circle.Radius
    lobulo_profile.links.new(math_005.outputs[0], mesh_circle.inputs[1])
    #delete_geometry_001.Geometry -> scale_elements_001.Geometry
    lobulo_profile.links.new(delete_geometry_001.outputs[0], scale_elements_001.inputs[0])
    #group_input_001.Scale -> scale_elements_001.Scale
    lobulo_profile.links.new(group_input_001.outputs[1], scale_elements_001.inputs[2])
    #scale_elements_001.Geometry -> transform_geometry_001.Geometry
    lobulo_profile.links.new(scale_elements_001.outputs[0], transform_geometry_001.inputs[0])
    #combine_xyz.Vector -> transform_geometry_001.Rotation
    lobulo_profile.links.new(combine_xyz.outputs[0], transform_geometry_001.inputs[2])
    #math_001.Value -> combine_xyz.Z
    lobulo_profile.links.new(math_001.outputs[0], combine_xyz.inputs[2])
    #group_input_006.Rotate -> math_001.Value
    lobulo_profile.links.new(group_input_006.outputs[5], math_001.inputs[0])
    #transform_geometry_001.Geometry -> group_output.Geometry
    lobulo_profile.links.new(transform_geometry_001.outputs[0], group_output.inputs[0])
    #transform_geometry.Geometry -> mesh_boolean_001.Mesh 1
    lobulo_profile.links.new(transform_geometry.outputs[0], mesh_boolean_001.inputs[0])
    return lobulo_profile

lobulo_profile = lobulo_profile_node_group()

