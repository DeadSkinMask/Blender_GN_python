import bpy, mathutils

#initialize braid node group
def braid_node_group():
    braid = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Braid")

    braid.color_tag = 'NONE'
    braid.description = ""
    braid.default_group_node_width = 140
    

    braid.is_modifier = True

    #braid interface
    #Socket Geometry
    geometry_socket = braid.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'

    #Socket Geometry
    geometry_socket_1 = braid.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'

    #Socket Level
    level_socket = braid.interface.new_socket(name = "Level", in_out='INPUT', socket_type = 'NodeSocketInt')
    level_socket.default_value = 1
    level_socket.min_value = 0
    level_socket.max_value = 6
    level_socket.subtype = 'NONE'
    level_socket.attribute_domain = 'POINT'

    #Socket Rot
    rot_socket = braid.interface.new_socket(name = "Rot", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rot_socket.default_value = 15.0
    rot_socket.min_value = -10000.0
    rot_socket.max_value = 10000.0
    rot_socket.subtype = 'NONE'
    rot_socket.attribute_domain = 'POINT'

    #Socket X
    x_socket = braid.interface.new_socket(name = "X", in_out='INPUT', socket_type = 'NodeSocketFloat')
    x_socket.default_value = 0.0
    x_socket.min_value = -10000.0
    x_socket.max_value = 10000.0
    x_socket.subtype = 'NONE'
    x_socket.attribute_domain = 'POINT'

    #Socket Y
    y_socket = braid.interface.new_socket(name = "Y", in_out='INPUT', socket_type = 'NodeSocketFloat')
    y_socket.default_value = -0.125
    y_socket.min_value = -10000.0
    y_socket.max_value = 10000.0
    y_socket.subtype = 'NONE'
    y_socket.attribute_domain = 'POINT'

    #Socket Z
    z_socket = braid.interface.new_socket(name = "Z", in_out='INPUT', socket_type = 'NodeSocketFloat')
    z_socket.default_value = -0.125
    z_socket.min_value = -10000.0
    z_socket.max_value = 10000.0
    z_socket.subtype = 'NONE'
    z_socket.attribute_domain = 'POINT'


    #initialize braid nodes
    #node Group Output
    group_output = braid.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Cube
    cube = braid.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    #Size
    cube.inputs[0].default_value = (0.5, 0.5, 1.0)
    #Vertices X
    cube.inputs[1].default_value = 2
    #Vertices Y
    cube.inputs[2].default_value = 2
    #Vertices Z
    cube.inputs[3].default_value = 2

    #node Transform Geometry
    transform_geometry = braid.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    #Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Join Geometry
    join_geometry = braid.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Transform Geometry.001
    transform_geometry_001 = braid.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Combine XYZ
    combine_xyz = braid.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"

    #node Vector Math
    vector_math = braid.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    #Vector_001
    vector_math.inputs[1].default_value = (-1.0, -1.0, -1.0)

    #node Subdivision Surface
    subdivision_surface = braid.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = 'ALL'
    subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
    #Edge Crease
    subdivision_surface.inputs[2].default_value = 0.0
    #Vertex Crease
    subdivision_surface.inputs[3].default_value = 0.0
    #Limit Surface
    subdivision_surface.inputs[4].default_value = True

    #node Group Input.001
    group_input_001 = braid.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True

    #node Vector Math.001
    vector_math_001 = braid.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    #Vector_001
    vector_math_001.inputs[1].default_value = (-1.0, -1.0, -1.0)

    #node Combine XYZ.001
    combine_xyz_001 = braid.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #Y
    combine_xyz_001.inputs[1].default_value = 0.0
    #Z
    combine_xyz_001.inputs[2].default_value = 0.0

    #node Math
    math = braid.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'RADIANS'
    math.use_clamp = False

    #node Transform Geometry.002
    transform_geometry_002 = braid.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    #Translation
    transform_geometry_002.inputs[1].default_value = (0.0, 0.0, -0.6000000238418579)
    #Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_002.inputs[3].default_value = (1.0, -1.0, -0.9999998807907104)

    #node Join Geometry.001
    join_geometry_001 = braid.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    #node Set Shade Smooth
    set_shade_smooth = braid.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    #Selection
    set_shade_smooth.inputs[1].default_value = True
    #Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    #node Group Input.002
    group_input_002 = braid.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True

    #node Group Input.003
    group_input_003 = braid.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[6].hide = True





    #Set locations
    group_output.location = (877.57470703125, 89.95954895019531)
    cube.location = (-812.1302490234375, -29.378494262695312)
    transform_geometry.location = (-90.54747772216797, -38.64954376220703)
    join_geometry.location = (124.51403045654297, 119.56190490722656)
    transform_geometry_001.location = (-63.73951721191406, 347.75640869140625)
    combine_xyz.location = (-810.0811157226562, 307.8133850097656)
    vector_math.location = (-342.5351867675781, 418.64520263671875)
    subdivision_surface.location = (-417.6832275390625, -132.32838439941406)
    group_input_001.location = (-832.4383544921875, -320.3081970214844)
    vector_math_001.location = (-344.6535949707031, 251.1472930908203)
    combine_xyz_001.location = (-780.7635498046875, 145.63211059570312)
    math.location = (-1039.69921875, 151.80670166015625)
    transform_geometry_002.location = (351.97906494140625, 334.7420959472656)
    join_geometry_001.location = (591.3783569335938, 420.0062255859375)
    set_shade_smooth.location = (698.0001220703125, 140.4985809326172)
    group_input_002.location = (-1255.626708984375, 133.50244140625)
    group_input_003.location = (-1037.5322265625, 286.2454528808594)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    subdivision_surface.width, subdivision_surface.height = 150.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0

    #initialize braid links
    #transform_geometry.Geometry -> join_geometry.Geometry
    braid.links.new(transform_geometry.outputs[0], join_geometry.inputs[0])
    #combine_xyz.Vector -> vector_math.Vector
    braid.links.new(combine_xyz.outputs[0], vector_math.inputs[0])
    #vector_math.Vector -> transform_geometry_001.Translation
    braid.links.new(vector_math.outputs[0], transform_geometry_001.inputs[1])
    #combine_xyz.Vector -> transform_geometry.Translation
    braid.links.new(combine_xyz.outputs[0], transform_geometry.inputs[1])
    #group_input_001.Level -> subdivision_surface.Level
    braid.links.new(group_input_001.outputs[1], subdivision_surface.inputs[1])
    #vector_math_001.Vector -> transform_geometry_001.Rotation
    braid.links.new(vector_math_001.outputs[0], transform_geometry_001.inputs[2])
    #combine_xyz_001.Vector -> vector_math_001.Vector
    braid.links.new(combine_xyz_001.outputs[0], vector_math_001.inputs[0])
    #combine_xyz_001.Vector -> transform_geometry.Rotation
    braid.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[2])
    #math.Value -> combine_xyz_001.X
    braid.links.new(math.outputs[0], combine_xyz_001.inputs[0])
    #join_geometry.Geometry -> transform_geometry_002.Geometry
    braid.links.new(join_geometry.outputs[0], transform_geometry_002.inputs[0])
    #join_geometry.Geometry -> join_geometry_001.Geometry
    braid.links.new(join_geometry.outputs[0], join_geometry_001.inputs[0])
    #set_shade_smooth.Geometry -> group_output.Geometry
    braid.links.new(set_shade_smooth.outputs[0], group_output.inputs[0])
    #cube.Mesh -> subdivision_surface.Mesh
    braid.links.new(cube.outputs[0], subdivision_surface.inputs[0])
    #subdivision_surface.Mesh -> transform_geometry.Geometry
    braid.links.new(subdivision_surface.outputs[0], transform_geometry.inputs[0])
    #subdivision_surface.Mesh -> transform_geometry_001.Geometry
    braid.links.new(subdivision_surface.outputs[0], transform_geometry_001.inputs[0])
    #join_geometry.Geometry -> set_shade_smooth.Geometry
    braid.links.new(join_geometry.outputs[0], set_shade_smooth.inputs[0])
    #group_input_002.Rot -> math.Value
    braid.links.new(group_input_002.outputs[2], math.inputs[0])
    #group_input_003.Y -> combine_xyz.Y
    braid.links.new(group_input_003.outputs[4], combine_xyz.inputs[1])
    #group_input_003.Z -> combine_xyz.Z
    braid.links.new(group_input_003.outputs[5], combine_xyz.inputs[2])
    #group_input_003.X -> combine_xyz.X
    braid.links.new(group_input_003.outputs[3], combine_xyz.inputs[0])
    #transform_geometry_001.Geometry -> join_geometry.Geometry
    braid.links.new(transform_geometry_001.outputs[0], join_geometry.inputs[0])
    #transform_geometry_002.Geometry -> join_geometry_001.Geometry
    braid.links.new(transform_geometry_002.outputs[0], join_geometry_001.inputs[0])
    return braid

braid = braid_node_group()

