import bpy, mathutils

#initialize half node group
def half_node_group():
    half = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Half")

    half.color_tag = 'NONE'
    half.description = ""
    half.default_group_node_width = 140
    

    half.is_modifier = True

    #half interface
    #Socket Geometry
    geometry_socket = half.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = half.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Exact
    exact_socket = half.interface.new_socket(name = "Exact", in_out='INPUT', socket_type = 'NodeSocketBool')
    exact_socket.default_value = False
    exact_socket.attribute_domain = 'POINT'
    exact_socket.default_input = 'VALUE'
    exact_socket.structure_type = 'AUTO'


    #initialize half nodes
    #node Group Input
    group_input = half.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True

    #node Group Output
    group_output = half.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Bounding Box
    bounding_box = half.nodes.new("GeometryNodeBoundBox")
    bounding_box.name = "Bounding Box"
    #Use Radius
    bounding_box.inputs[1].default_value = True

    #node Transform Geometry
    transform_geometry = half.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    #Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry.inputs[3].default_value = (1.100000023841858, 1.0, 1.100000023841858)

    #node Vector Math
    vector_math = half.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    #Vector_001
    vector_math.inputs[1].default_value = (0.0, -1.0, 0.0)

    #node Mesh Boolean
    mesh_boolean = half.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'MANIFOLD'

    #node Switch
    switch = half.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    #node Mesh Boolean.001
    mesh_boolean_001 = half.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.operation = 'DIFFERENCE'
    mesh_boolean_001.solver = 'EXACT'
    #Self Intersection
    mesh_boolean_001.inputs[2].default_value = False
    #Hole Tolerant
    mesh_boolean_001.inputs[3].default_value = True

    #node Group Input.001
    group_input_001 = half.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True

    #node Reroute
    reroute = half.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"




    #Set locations
    group_input.location = (-614.0921020507812, 281.250732421875)
    group_output.location = (754.63134765625, 355.7721252441406)
    bounding_box.location = (-371.4242248535156, 219.3772430419922)
    transform_geometry.location = (35.3781852722168, 98.54547119140625)
    vector_math.location = (-157.2532501220703, 14.302726745605469)
    mesh_boolean.location = (310.8027648925781, 250.9677734375)
    switch.location = (529.2401733398438, 375.8802490234375)
    mesh_boolean_001.location = (309.4216003417969, 495.8670349121094)
    group_input_001.location = (305.0437316894531, 597.6950073242188)
    reroute.location = (151.80252075195312, 206.2465362548828)

    #Set dimensions
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    bounding_box.width, bounding_box.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    reroute.width, reroute.height = 10.0, 100.0

    #initialize half links
    #group_input.Geometry -> bounding_box.Geometry
    half.links.new(group_input.outputs[0], bounding_box.inputs[0])
    #bounding_box.Max -> vector_math.Vector
    half.links.new(bounding_box.outputs[2], vector_math.inputs[0])
    #vector_math.Vector -> transform_geometry.Translation
    half.links.new(vector_math.outputs[0], transform_geometry.inputs[1])
    #bounding_box.Bounding Box -> transform_geometry.Geometry
    half.links.new(bounding_box.outputs[0], transform_geometry.inputs[0])
    #transform_geometry.Geometry -> mesh_boolean.Mesh 2
    half.links.new(transform_geometry.outputs[0], mesh_boolean.inputs[1])
    #reroute.Output -> mesh_boolean.Mesh 1
    half.links.new(reroute.outputs[0], mesh_boolean.inputs[0])
    #switch.Output -> group_output.Geometry
    half.links.new(switch.outputs[0], group_output.inputs[0])
    #transform_geometry.Geometry -> mesh_boolean_001.Mesh 2
    half.links.new(transform_geometry.outputs[0], mesh_boolean_001.inputs[1])
    #group_input_001.Exact -> switch.Switch
    half.links.new(group_input_001.outputs[1], switch.inputs[0])
    #mesh_boolean_001.Mesh -> switch.True
    half.links.new(mesh_boolean_001.outputs[0], switch.inputs[2])
    #mesh_boolean.Mesh -> switch.False
    half.links.new(mesh_boolean.outputs[0], switch.inputs[1])
    #reroute.Output -> mesh_boolean_001.Mesh 1
    half.links.new(reroute.outputs[0], mesh_boolean_001.inputs[0])
    #group_input.Geometry -> reroute.Input
    half.links.new(group_input.outputs[0], reroute.inputs[0])
    return half

half = half_node_group()

