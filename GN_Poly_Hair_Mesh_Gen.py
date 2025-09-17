import bpy, mathutils

#initialize boundary_select node group
def boundary_select_node_group():
    boundary_select = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Boundary Select")

    boundary_select.color_tag = 'NONE'
    boundary_select.description = ""
    boundary_select.default_group_node_width = 140
    


    #boundary_select interface
    #Socket Boundary Edge
    boundary_edge_socket = boundary_select.interface.new_socket(name = "Boundary Edge", in_out='OUTPUT', socket_type = 'NodeSocketBool')
    boundary_edge_socket.default_value = False
    boundary_edge_socket.attribute_domain = 'POINT'
    boundary_edge_socket.default_input = 'VALUE'
    boundary_edge_socket.structure_type = 'AUTO'

    #Socket Activate
    activate_socket = boundary_select.interface.new_socket(name = "Activate", in_out='INPUT', socket_type = 'NodeSocketBool')
    activate_socket.default_value = True
    activate_socket.attribute_domain = 'POINT'
    activate_socket.description = "Edges used to split faces into separate groups"
    activate_socket.default_input = 'VALUE'
    activate_socket.structure_type = 'AUTO'


    #initialize boundary_select nodes
    #node Group Output
    group_output = boundary_select.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = boundary_select.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Face Group Boundaries
    face_group_boundaries = boundary_select.nodes.new("GeometryNodeMeshFaceSetBoundaries")
    face_group_boundaries.name = "Face Group Boundaries"

    #node Edges to Face Groups
    edges_to_face_groups = boundary_select.nodes.new("GeometryNodeEdgesToFaceGroups")
    edges_to_face_groups.name = "Edges to Face Groups"

    #node Frame.007
    frame_007 = boundary_select.nodes.new("NodeFrame")
    frame_007.label = "Boundary Edge Select"
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    #node Boolean Math.004
    boolean_math_004 = boundary_select.nodes.new("FunctionNodeBooleanMath")
    boolean_math_004.name = "Boolean Math.004"
    boolean_math_004.operation = 'NOT'




    #Set parents
    face_group_boundaries.parent = frame_007
    edges_to_face_groups.parent = frame_007
    boolean_math_004.parent = frame_007

    #Set locations
    group_output.location = (509.250244140625, 0.0)
    group_input.location = (-328.4109802246094, 7.4825758934021)
    face_group_boundaries.location = (218.1240234375, -48.77008056640625)
    edges_to_face_groups.location = (30.4697265625, -48.245849609375)
    frame_007.location = (-115.0, 33.0)
    boolean_math_004.location = (404.749755859375, -36.3414306640625)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    face_group_boundaries.width, face_group_boundaries.height = 150.0, 100.0
    edges_to_face_groups.width, edges_to_face_groups.height = 140.0, 100.0
    frame_007.width, frame_007.height = 575.0, 167.0
    boolean_math_004.width, boolean_math_004.height = 140.0, 100.0

    #initialize boundary_select links
    #face_group_boundaries.Boundary Edges -> boolean_math_004.Boolean
    boundary_select.links.new(face_group_boundaries.outputs[0], boolean_math_004.inputs[0])
    #edges_to_face_groups.Face Group ID -> face_group_boundaries.Face Group ID
    boundary_select.links.new(edges_to_face_groups.outputs[0], face_group_boundaries.inputs[0])
    #boolean_math_004.Boolean -> group_output.Boundary Edge
    boundary_select.links.new(boolean_math_004.outputs[0], group_output.inputs[0])
    #group_input.Activate -> edges_to_face_groups.Boundary Edges
    boundary_select.links.new(group_input.outputs[0], edges_to_face_groups.inputs[0])
    return boundary_select

boundary_select = boundary_select_node_group()

#initialize mesh_hair_base_gen node group
def mesh_hair_base_gen_node_group():
    mesh_hair_base_gen = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Mesh Hair Base Gen")

    mesh_hair_base_gen.color_tag = 'NONE'
    mesh_hair_base_gen.description = ""
    mesh_hair_base_gen.default_group_node_width = 140
    

    mesh_hair_base_gen.is_modifier = True

    #mesh_hair_base_gen interface
    #Socket Geometry
    geometry_socket = mesh_hair_base_gen.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = mesh_hair_base_gen.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = mesh_hair_base_gen.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -10000.0
    scale_socket.max_value = 10000.0
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Level
    level_socket = mesh_hair_base_gen.interface.new_socket(name = "Level", in_out='INPUT', socket_type = 'NodeSocketInt')
    level_socket.default_value = 3
    level_socket.min_value = 0
    level_socket.max_value = 6
    level_socket.subtype = 'NONE'
    level_socket.attribute_domain = 'POINT'
    level_socket.default_input = 'VALUE'
    level_socket.structure_type = 'AUTO'

    #Socket Quarter Sphere
    quarter_sphere_socket = mesh_hair_base_gen.interface.new_socket(name = "Quarter Sphere", in_out='INPUT', socket_type = 'NodeSocketBool')
    quarter_sphere_socket.default_value = True
    quarter_sphere_socket.attribute_domain = 'POINT'
    quarter_sphere_socket.default_input = 'VALUE'
    quarter_sphere_socket.structure_type = 'AUTO'

    #Socket Front Quarter
    front_quarter_socket = mesh_hair_base_gen.interface.new_socket(name = "Front Quarter", in_out='INPUT', socket_type = 'NodeSocketBool')
    front_quarter_socket.default_value = False
    front_quarter_socket.attribute_domain = 'POINT'
    front_quarter_socket.default_input = 'VALUE'
    front_quarter_socket.structure_type = 'AUTO'

    #Socket Solidify Offset
    solidify_offset_socket = mesh_hair_base_gen.interface.new_socket(name = "Solidify Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    solidify_offset_socket.default_value = -1.0
    solidify_offset_socket.min_value = -10000.0
    solidify_offset_socket.max_value = 10000.0
    solidify_offset_socket.subtype = 'NONE'
    solidify_offset_socket.attribute_domain = 'POINT'
    solidify_offset_socket.default_input = 'VALUE'
    solidify_offset_socket.structure_type = 'AUTO'

    #Socket Hair Length
    hair_length_socket = mesh_hair_base_gen.interface.new_socket(name = "Hair Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hair_length_socket.default_value = 0.5
    hair_length_socket.min_value = -10000.0
    hair_length_socket.max_value = 10000.0
    hair_length_socket.subtype = 'NONE'
    hair_length_socket.attribute_domain = 'POINT'
    hair_length_socket.default_input = 'VALUE'
    hair_length_socket.structure_type = 'AUTO'

    #Socket Hair Resolution
    hair_resolution_socket = mesh_hair_base_gen.interface.new_socket(name = "Hair Resolution", in_out='INPUT', socket_type = 'NodeSocketInt')
    hair_resolution_socket.default_value = 10
    hair_resolution_socket.min_value = 1
    hair_resolution_socket.max_value = 100000
    hair_resolution_socket.subtype = 'NONE'
    hair_resolution_socket.attribute_domain = 'POINT'
    hair_resolution_socket.default_input = 'VALUE'
    hair_resolution_socket.structure_type = 'AUTO'

    #Socket Trim Top
    trim_top_socket = mesh_hair_base_gen.interface.new_socket(name = "Trim Top", in_out='INPUT', socket_type = 'NodeSocketFloat')
    trim_top_socket.default_value = 0.05000000074505806
    trim_top_socket.min_value = -10000.0
    trim_top_socket.max_value = 10000.0
    trim_top_socket.subtype = 'NONE'
    trim_top_socket.attribute_domain = 'POINT'
    trim_top_socket.default_input = 'VALUE'
    trim_top_socket.structure_type = 'AUTO'

    #Socket Delete
    delete_socket = mesh_hair_base_gen.interface.new_socket(name = "Delete", in_out='INPUT', socket_type = 'NodeSocketMenu')
    delete_socket.attribute_domain = 'POINT'
    delete_socket.default_input = 'VALUE'
    delete_socket.structure_type = 'AUTO'

    #Socket Hair Res By Lenght
    hair_res_by_lenght_socket = mesh_hair_base_gen.interface.new_socket(name = "Hair Res By Lenght", in_out='INPUT', socket_type = 'NodeSocketBool')
    hair_res_by_lenght_socket.default_value = True
    hair_res_by_lenght_socket.attribute_domain = 'POINT'
    hair_res_by_lenght_socket.hide_value = True
    hair_res_by_lenght_socket.default_input = 'VALUE'
    hair_res_by_lenght_socket.structure_type = 'AUTO'

    #Socket Length Res
    length_res_socket = mesh_hair_base_gen.interface.new_socket(name = "Length Res", in_out='INPUT', socket_type = 'NodeSocketFloat')
    length_res_socket.default_value = 0.10000000149011612
    length_res_socket.min_value = 0.009999999776482582
    length_res_socket.max_value = 3.4028234663852886e+38
    length_res_socket.subtype = 'DISTANCE'
    length_res_socket.attribute_domain = 'POINT'
    length_res_socket.default_input = 'VALUE'
    length_res_socket.structure_type = 'AUTO'

    #Socket Tip Scale
    tip_scale_socket = mesh_hair_base_gen.interface.new_socket(name = "Tip Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    tip_scale_socket.default_value = 0.800000011920929
    tip_scale_socket.min_value = 0.0
    tip_scale_socket.max_value = 3.4028234663852886e+38
    tip_scale_socket.subtype = 'NONE'
    tip_scale_socket.attribute_domain = 'POINT'
    tip_scale_socket.default_input = 'VALUE'
    tip_scale_socket.structure_type = 'AUTO'

    #Socket UV Mix
    uv_mix_socket = mesh_hair_base_gen.interface.new_socket(name = "UV Mix", in_out='INPUT', socket_type = 'NodeSocketFloat')
    uv_mix_socket.default_value = 1.0
    uv_mix_socket.min_value = 0.0
    uv_mix_socket.max_value = 1.0
    uv_mix_socket.subtype = 'FACTOR'
    uv_mix_socket.attribute_domain = 'POINT'
    uv_mix_socket.description = "Amount of mixing between the A and B inputs"
    uv_mix_socket.default_input = 'VALUE'
    uv_mix_socket.structure_type = 'AUTO'


    #initialize mesh_hair_base_gen nodes
    #node Group Output
    group_output_1 = mesh_hair_base_gen.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Cube
    cube = mesh_hair_base_gen.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    #Size
    cube.inputs[0].default_value = (1.0, 1.0, 1.0)
    #Vertices X
    cube.inputs[1].default_value = 2
    #Vertices Y
    cube.inputs[2].default_value = 2
    #Vertices Z
    cube.inputs[3].default_value = 2

    #node Subdivision Surface
    subdivision_surface = mesh_hair_base_gen.nodes.new("GeometryNodeSubdivisionSurface")
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
    group_input_001 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[1].hide = True
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
    group_input_001.outputs[13].hide = True
    group_input_001.outputs[14].hide = True

    #node Frame
    frame = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame.label = "Cube Sphere"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Delete Geometry
    delete_geometry = mesh_hair_base_gen.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'

    #node Compare
    compare = mesh_hair_base_gen.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'LESS_THAN'
    #B
    compare.inputs[1].default_value = 0.0

    #node Separate XYZ
    separate_xyz = mesh_hair_base_gen.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    #node Position
    position = mesh_hair_base_gen.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Compare.001
    compare_001 = mesh_hair_base_gen.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'LESS_THAN'
    #B
    compare_001.inputs[1].default_value = 0.0

    #node Switch
    switch = mesh_hair_base_gen.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'BOOLEAN'
    #False
    switch.inputs[1].default_value = False

    #node Boolean Math
    boolean_math = mesh_hair_base_gen.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'OR'

    #node Group Input.002
    group_input_002 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    group_input_002.outputs[11].hide = True
    group_input_002.outputs[12].hide = True
    group_input_002.outputs[13].hide = True
    group_input_002.outputs[14].hide = True

    #node Switch.001
    switch_001 = mesh_hair_base_gen.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'FLOAT'

    #node Group Input.003
    group_input_003 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True
    group_input_003.outputs[11].hide = True
    group_input_003.outputs[12].hide = True
    group_input_003.outputs[13].hide = True
    group_input_003.outputs[14].hide = True

    #node Math
    math = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = -1.0

    #node Frame.001
    frame_001 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_001.label = "Half-Quarter Sphere"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Separate XYZ.001
    separate_xyz_001 = mesh_hair_base_gen.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    #node Position.001
    position_001 = mesh_hair_base_gen.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    #node Compare.002
    compare_002 = mesh_hair_base_gen.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'
    #B
    compare_002.inputs[1].default_value = 0.0
    #Epsilon
    compare_002.inputs[12].default_value = 0.0010000000474974513

    #node Frame.002
    frame_002 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_002.label = "Middle Edge Selection"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Store Named Attribute
    store_named_attribute = mesh_hair_base_gen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'POINT'
    #Selection
    store_named_attribute.inputs[1].default_value = True
    #Name
    store_named_attribute.inputs[2].default_value = "middle_edge"

    #node Extrude Mesh
    extrude_mesh = mesh_hair_base_gen.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'FACES'
    #Selection
    extrude_mesh.inputs[1].default_value = True
    #Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Individual
    extrude_mesh.inputs[4].default_value = False

    #node Group Input.004
    group_input_004 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[3].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True

    #node Join Geometry
    join_geometry = mesh_hair_base_gen.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Merge by Distance
    merge_by_distance = mesh_hair_base_gen.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    #Selection
    merge_by_distance.inputs[1].default_value = True
    #Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    #node Frame.003
    frame_003 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_003.label = "Solidify"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Reroute
    reroute = mesh_hair_base_gen.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    #node Set Position
    set_position = mesh_hair_base_gen.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Vector Math
    vector_math = mesh_hair_base_gen.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    #Vector_001
    vector_math.inputs[1].default_value = (1.0, 1.0, 0.0)

    #node Position.002
    position_002 = mesh_hair_base_gen.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    #node Named Attribute
    named_attribute = mesh_hair_base_gen.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'BOOLEAN'
    #Name
    named_attribute.inputs[0].default_value = "middle_edge"

    #node Named Attribute.001
    named_attribute_001 = mesh_hair_base_gen.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = 'BOOLEAN'
    #Name
    named_attribute_001.inputs[0].default_value = "middle_edge"

    #node Separate Geometry
    separate_geometry = mesh_hair_base_gen.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = 'FACE'

    #node Sort Elements
    sort_elements = mesh_hair_base_gen.nodes.new("GeometryNodeSortElements")
    sort_elements.name = "Sort Elements"
    sort_elements.domain = 'FACE'
    #Selection
    sort_elements.inputs[1].default_value = True
    #Group ID
    sort_elements.inputs[2].default_value = 0

    #node Separate XYZ.002
    separate_xyz_002 = mesh_hair_base_gen.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"

    #node Position.003
    position_003 = mesh_hair_base_gen.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"

    #node Frame.005
    frame_005 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_005.label = "ReIndex"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    #node Mesh to Curve
    mesh_to_curve = mesh_hair_base_gen.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.mode = 'EDGES'

    #node Compare.004
    compare_004 = mesh_hair_base_gen.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'INT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'LESS_EQUAL'
    #B_INT
    compare_004.inputs[3].default_value = 1

    #node Integer Math.001
    integer_math_001 = mesh_hair_base_gen.nodes.new("FunctionNodeIntegerMath")
    integer_math_001.name = "Integer Math.001"
    integer_math_001.operation = 'MODULO'
    #Value_001
    integer_math_001.inputs[1].default_value = 4

    #node Index.001
    index_001 = mesh_hair_base_gen.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"

    #node Separate Geometry.001
    separate_geometry_001 = mesh_hair_base_gen.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry_001.name = "Separate Geometry.001"
    separate_geometry_001.domain = 'FACE'

    #node Frame.006
    frame_006 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_006.label = "Face Pairs"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    #node Mesh to Curve.001
    mesh_to_curve_001 = mesh_hair_base_gen.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve_001.name = "Mesh to Curve.001"
    mesh_to_curve_001.mode = 'EDGES'

    #node Scale Elements
    scale_elements = mesh_hair_base_gen.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'FACE'
    scale_elements.scale_mode = 'UNIFORM'
    scale_elements.inputs[1].hide = True
    scale_elements.inputs[2].hide = True
    scale_elements.inputs[3].hide = True
    scale_elements.inputs[4].hide = True
    #Selection
    scale_elements.inputs[1].default_value = True
    #Scale
    scale_elements.inputs[2].default_value = 0.0
    #Center
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Merge by Distance.001
    merge_by_distance_001 = mesh_hair_base_gen.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = 'ALL'
    merge_by_distance_001.inputs[1].hide = True
    merge_by_distance_001.inputs[2].hide = True
    #Selection
    merge_by_distance_001.inputs[1].default_value = True
    #Distance
    merge_by_distance_001.inputs[2].default_value = 0.0010000000474974513

    #node Scale Elements.001
    scale_elements_001 = mesh_hair_base_gen.nodes.new("GeometryNodeScaleElements")
    scale_elements_001.name = "Scale Elements.001"
    scale_elements_001.domain = 'FACE'
    scale_elements_001.scale_mode = 'UNIFORM'
    scale_elements_001.inputs[1].hide = True
    scale_elements_001.inputs[2].hide = True
    scale_elements_001.inputs[3].hide = True
    scale_elements_001.inputs[4].hide = True
    #Selection
    scale_elements_001.inputs[1].default_value = True
    #Scale
    scale_elements_001.inputs[2].default_value = 0.0
    #Center
    scale_elements_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Merge by Distance.002
    merge_by_distance_002 = mesh_hair_base_gen.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_002.name = "Merge by Distance.002"
    merge_by_distance_002.mode = 'ALL'
    merge_by_distance_002.inputs[1].hide = True
    merge_by_distance_002.inputs[2].hide = True
    #Selection
    merge_by_distance_002.inputs[1].default_value = True
    #Distance
    merge_by_distance_002.inputs[2].default_value = 0.0010000000474974513

    #node Join Geometry.002
    join_geometry_002 = mesh_hair_base_gen.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"

    #node Extrude Mesh.003
    extrude_mesh_003 = mesh_hair_base_gen.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_003.name = "Extrude Mesh.003"
    extrude_mesh_003.mode = 'VERTICES'
    #Selection
    extrude_mesh_003.inputs[1].default_value = True
    #Offset Scale
    extrude_mesh_003.inputs[3].default_value = 1.0

    #node Combine XYZ.001
    combine_xyz_001 = mesh_hair_base_gen.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #X
    combine_xyz_001.inputs[0].default_value = 0.0
    #Y
    combine_xyz_001.inputs[1].default_value = 0.0

    #node Math.002
    math_002 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    math_002.inputs[1].hide = True
    math_002.inputs[2].hide = True
    #Value_001
    math_002.inputs[1].default_value = -1.0

    #node Group Input.007
    group_input_007 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
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
    group_input_007.outputs[13].hide = True
    group_input_007.outputs[14].hide = True

    #node Mesh to Curve.002
    mesh_to_curve_002 = mesh_hair_base_gen.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve_002.name = "Mesh to Curve.002"
    mesh_to_curve_002.mode = 'EDGES'
    #Selection
    mesh_to_curve_002.inputs[1].default_value = True

    #node Resample Curve
    resample_curve = mesh_hair_base_gen.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.keep_last_segment = True
    resample_curve.mode = 'COUNT'

    #node Frame.008
    frame_008 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_008.label = "Hair Strands"
    frame_008.name = "Frame.008"
    frame_008.label_size = 20
    frame_008.shrink = True

    #node Group Input.009
    group_input_009 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
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
    group_input_009.outputs[13].hide = True
    group_input_009.outputs[14].hide = True

    #node Curve to Mesh
    curve_to_mesh = mesh_hair_base_gen.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    #Scale
    curve_to_mesh.inputs[2].default_value = 1.0
    #Fill Caps
    curve_to_mesh.inputs[3].default_value = False

    #node Reverse Curve
    reverse_curve = mesh_hair_base_gen.nodes.new("GeometryNodeReverseCurve")
    reverse_curve.name = "Reverse Curve"
    #Selection
    reverse_curve.inputs[1].default_value = True

    #node Set Curve Tilt
    set_curve_tilt = mesh_hair_base_gen.nodes.new("GeometryNodeSetCurveTilt")
    set_curve_tilt.name = "Set Curve Tilt"
    #Selection
    set_curve_tilt.inputs[1].default_value = True

    #node Math.008
    math_008 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'RADIANS'
    math_008.use_clamp = False
    #Value
    math_008.inputs[0].default_value = 22.5

    #node Math.001
    math_001 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Index.002
    index_002 = mesh_hair_base_gen.nodes.new("GeometryNodeInputIndex")
    index_002.name = "Index.002"

    #node Capture Attribute
    capture_attribute = mesh_hair_base_gen.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Index")
    capture_attribute.capture_items["Index"].data_type = 'INT'
    capture_attribute.domain = 'POINT'

    #node Sort Elements.001
    sort_elements_001 = mesh_hair_base_gen.nodes.new("GeometryNodeSortElements")
    sort_elements_001.name = "Sort Elements.001"
    sort_elements_001.domain = 'POINT'
    #Selection
    sort_elements_001.inputs[1].default_value = True
    #Group ID
    sort_elements_001.inputs[2].default_value = 0

    #node Separate XYZ.003
    separate_xyz_003 = mesh_hair_base_gen.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"

    #node Position.004
    position_004 = mesh_hair_base_gen.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"

    #node Frame.009
    frame_009 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_009.label = "ReIndex"
    frame_009.name = "Frame.009"
    frame_009.label_size = 20
    frame_009.shrink = True

    #node Reroute.001
    reroute_001 = mesh_hair_base_gen.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketGeometry"
    #node Reroute.002
    reroute_002 = mesh_hair_base_gen.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketGeometry"
    #node Transform Geometry
    transform_geometry = mesh_hair_base_gen.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[1].hide = True
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[4].hide = True
    #Translation
    transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Group Input
    group_input_1 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    group_input_1.outputs[0].hide = True
    group_input_1.outputs[2].hide = True
    group_input_1.outputs[3].hide = True
    group_input_1.outputs[4].hide = True
    group_input_1.outputs[5].hide = True
    group_input_1.outputs[6].hide = True
    group_input_1.outputs[7].hide = True
    group_input_1.outputs[8].hide = True
    group_input_1.outputs[9].hide = True
    group_input_1.outputs[10].hide = True
    group_input_1.outputs[11].hide = True
    group_input_1.outputs[12].hide = True
    group_input_1.outputs[13].hide = True
    group_input_1.outputs[14].hide = True

    #node Set Geometry Name
    set_geometry_name = mesh_hair_base_gen.nodes.new("GeometryNodeSetGeometryName")
    set_geometry_name.name = "Set Geometry Name"
    #Name
    set_geometry_name.inputs[1].default_value = "hair_strands"

    #node Join Geometry.003
    join_geometry_003 = mesh_hair_base_gen.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"

    #node Curve Line
    curve_line = mesh_hair_base_gen.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'POINTS'
    #End
    curve_line.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Group Input.005
    group_input_005 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True
    group_input_005.outputs[11].hide = True
    group_input_005.outputs[12].hide = True
    group_input_005.outputs[13].hide = True
    group_input_005.outputs[14].hide = True

    #node Curve to Mesh.001
    curve_to_mesh_001 = mesh_hair_base_gen.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    #Scale
    curve_to_mesh_001.inputs[2].default_value = 1.0
    #Fill Caps
    curve_to_mesh_001.inputs[3].default_value = False

    #node Endpoint Selection
    endpoint_selection = mesh_hair_base_gen.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection.name = "Endpoint Selection"
    #Start Size
    endpoint_selection.inputs[0].default_value = 0
    #End Size
    endpoint_selection.inputs[1].default_value = 1

    #node Capture Attribute.001
    capture_attribute_001 = mesh_hair_base_gen.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.active_index = 1
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new('FLOAT', "Head")
    capture_attribute_001.capture_items["Head"].data_type = 'BOOLEAN'
    capture_attribute_001.capture_items.new('FLOAT', "Tail")
    capture_attribute_001.capture_items["Tail"].data_type = 'BOOLEAN'
    capture_attribute_001.domain = 'POINT'

    #node Combine XYZ
    combine_xyz = mesh_hair_base_gen.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Y
    combine_xyz.inputs[1].default_value = 0.0

    #node Math.003
    math_003 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = -1.0

    #node Resample Curve.001
    resample_curve_001 = mesh_hair_base_gen.nodes.new("GeometryNodeResampleCurve")
    resample_curve_001.name = "Resample Curve.001"
    resample_curve_001.keep_last_segment = True
    resample_curve_001.mode = 'COUNT'
    #Selection
    resample_curve_001.inputs[1].default_value = True

    #node Group Input.006
    group_input_006 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True

    #node Trim Curve
    trim_curve = mesh_hair_base_gen.nodes.new("GeometryNodeTrimCurve")
    trim_curve.name = "Trim Curve"
    trim_curve.mode = 'LENGTH'
    #Selection
    trim_curve.inputs[1].default_value = True
    #Start_001
    trim_curve.inputs[4].default_value = 0.0

    #node Math.004
    math_004 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'SUBTRACT'
    math_004.use_clamp = False

    #node Group Input.008
    group_input_008 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
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
    group_input_008.outputs[13].hide = True
    group_input_008.outputs[14].hide = True

    #node Set Shade Smooth
    set_shade_smooth = mesh_hair_base_gen.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    #Selection
    set_shade_smooth.inputs[1].default_value = True
    #Shade Smooth
    set_shade_smooth.inputs[2].default_value = False

    #node Delete Geometry.002
    delete_geometry_002 = mesh_hair_base_gen.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.domain = 'INSTANCE'
    delete_geometry_002.mode = 'ALL'

    #node Geometry to Instance
    geometry_to_instance = mesh_hair_base_gen.nodes.new("GeometryNodeGeometryToInstance")
    geometry_to_instance.name = "Geometry to Instance"

    #node Index
    index = mesh_hair_base_gen.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    #node Compare.003
    compare_003 = mesh_hair_base_gen.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'INT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'EQUAL'

    #node Menu Switch
    menu_switch = mesh_hair_base_gen.nodes.new("GeometryNodeMenuSwitch")
    menu_switch.name = "Menu Switch"
    menu_switch.active_index = 1
    menu_switch.data_type = 'INT'
    menu_switch.enum_items.clear()
    menu_switch.enum_items.new("Nothing")
    menu_switch.enum_items[0].description = ""
    menu_switch.enum_items.new("Strands")
    menu_switch.enum_items[1].description = ""
    menu_switch.enum_items.new("Bangs")
    menu_switch.enum_items[2].description = "Bangs"
    menu_switch.enum_items.new("Cap")
    menu_switch.enum_items[3].description = ""
    #Item_3
    menu_switch.inputs[1].default_value = -1
    #Item_2
    menu_switch.inputs[2].default_value = 2
    #Item_0
    menu_switch.inputs[3].default_value = 0
    #Item_1
    menu_switch.inputs[4].default_value = 1

    #node Group Input.010
    group_input_010 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
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
    group_input_010.outputs[13].hide = True
    group_input_010.outputs[14].hide = True

    #node Realize Instances
    realize_instances = mesh_hair_base_gen.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    #Selection
    realize_instances.inputs[1].default_value = True
    #Realize All
    realize_instances.inputs[2].default_value = True
    #Depth
    realize_instances.inputs[3].default_value = 0

    #node Set Geometry Name.001
    set_geometry_name_001 = mesh_hair_base_gen.nodes.new("GeometryNodeSetGeometryName")
    set_geometry_name_001.name = "Set Geometry Name.001"
    #Name
    set_geometry_name_001.inputs[1].default_value = "Cap"

    #node Frame.004
    frame_004 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_004.label = "Bangs"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    #node Set Geometry Name.002
    set_geometry_name_002 = mesh_hair_base_gen.nodes.new("GeometryNodeSetGeometryName")
    set_geometry_name_002.name = "Set Geometry Name.002"
    #Name
    set_geometry_name_002.inputs[1].default_value = "bangs"

    #node Resample Curve.002
    resample_curve_002 = mesh_hair_base_gen.nodes.new("GeometryNodeResampleCurve")
    resample_curve_002.name = "Resample Curve.002"
    resample_curve_002.keep_last_segment = True
    resample_curve_002.mode = 'LENGTH'
    #Selection
    resample_curve_002.inputs[1].default_value = True

    #node Group Input.011
    group_input_011 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
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
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True

    #node Group Input.012
    group_input_012 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
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
    group_input_012.outputs[10].hide = True
    group_input_012.outputs[12].hide = True
    group_input_012.outputs[13].hide = True
    group_input_012.outputs[14].hide = True

    #node Group Input.013
    group_input_013 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[2].hide = True
    group_input_013.outputs[3].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[11].hide = True
    group_input_013.outputs[12].hide = True
    group_input_013.outputs[13].hide = True
    group_input_013.outputs[14].hide = True

    #node Resample Curve.003
    resample_curve_003 = mesh_hair_base_gen.nodes.new("GeometryNodeResampleCurve")
    resample_curve_003.name = "Resample Curve.003"
    resample_curve_003.keep_last_segment = True
    resample_curve_003.mode = 'LENGTH'
    #Selection
    resample_curve_003.inputs[1].default_value = True

    #node Group Input.014
    group_input_014 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[2].hide = True
    group_input_014.outputs[3].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[7].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[9].hide = True
    group_input_014.outputs[10].hide = True
    group_input_014.outputs[12].hide = True
    group_input_014.outputs[13].hide = True
    group_input_014.outputs[14].hide = True

    #node Switch.002
    switch_002 = mesh_hair_base_gen.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = 'GEOMETRY'

    #node Switch.003
    switch_003 = mesh_hair_base_gen.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.input_type = 'GEOMETRY'
    #Switch
    switch_003.inputs[0].default_value = False

    #node Frame.010
    frame_010 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_010.label = "Disable Geometry"
    frame_010.name = "Frame.010"
    frame_010.label_size = 20
    frame_010.shrink = True

    #node Scale Elements.002
    scale_elements_002 = mesh_hair_base_gen.nodes.new("GeometryNodeScaleElements")
    scale_elements_002.name = "Scale Elements.002"
    scale_elements_002.domain = 'EDGE'
    scale_elements_002.scale_mode = 'UNIFORM'
    #Center
    scale_elements_002.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Endpoint Selection.001
    endpoint_selection_001 = mesh_hair_base_gen.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection_001.name = "Endpoint Selection.001"
    #Start Size
    endpoint_selection_001.inputs[0].default_value = 1
    #End Size
    endpoint_selection_001.inputs[1].default_value = 0

    #node Group Input.015
    group_input_015 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_015.name = "Group Input.015"
    group_input_015.outputs[0].hide = True
    group_input_015.outputs[1].hide = True
    group_input_015.outputs[2].hide = True
    group_input_015.outputs[3].hide = True
    group_input_015.outputs[4].hide = True
    group_input_015.outputs[5].hide = True
    group_input_015.outputs[6].hide = True
    group_input_015.outputs[7].hide = True
    group_input_015.outputs[8].hide = True
    group_input_015.outputs[9].hide = True
    group_input_015.outputs[10].hide = True
    group_input_015.outputs[11].hide = True
    group_input_015.outputs[13].hide = True
    group_input_015.outputs[14].hide = True

    #node Face Group Boundaries.001
    face_group_boundaries_001 = mesh_hair_base_gen.nodes.new("GeometryNodeMeshFaceSetBoundaries")
    face_group_boundaries_001.name = "Face Group Boundaries.001"

    #node Edges to Face Groups.001
    edges_to_face_groups_001 = mesh_hair_base_gen.nodes.new("GeometryNodeEdgesToFaceGroups")
    edges_to_face_groups_001.name = "Edges to Face Groups.001"

    #node Boolean.001
    boolean_001 = mesh_hair_base_gen.nodes.new("FunctionNodeInputBool")
    boolean_001.name = "Boolean.001"
    boolean_001.boolean = True

    #node Frame.011
    frame_011 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_011.label = "Boundary Edge Select"
    frame_011.name = "Frame.011"
    frame_011.label_size = 20
    frame_011.shrink = True

    #node Boolean Math.005
    boolean_math_005 = mesh_hair_base_gen.nodes.new("FunctionNodeBooleanMath")
    boolean_math_005.name = "Boolean Math.005"
    boolean_math_005.operation = 'NOT'

    #node Store Named Attribute.001
    store_named_attribute_001 = mesh_hair_base_gen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = 'BOOLEAN'
    store_named_attribute_001.domain = 'EDGE'
    #Selection
    store_named_attribute_001.inputs[1].default_value = True
    #Name
    store_named_attribute_001.inputs[2].default_value = "edge_seam"

    #node Store Named Attribute.002
    store_named_attribute_002 = mesh_hair_base_gen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.data_type = 'BOOLEAN'
    store_named_attribute_002.domain = 'POINT'
    #Selection
    store_named_attribute_002.inputs[1].default_value = True
    #Name
    store_named_attribute_002.inputs[2].default_value = "edge_seam"

    #node Endpoint Selection.002
    endpoint_selection_002 = mesh_hair_base_gen.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection_002.name = "Endpoint Selection.002"
    #Start Size
    endpoint_selection_002.inputs[0].default_value = 0
    #End Size
    endpoint_selection_002.inputs[1].default_value = 1

    #node Store Named Attribute.003
    store_named_attribute_003 = mesh_hair_base_gen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.data_type = 'FLOAT2'
    store_named_attribute_003.domain = 'CORNER'
    #Selection
    store_named_attribute_003.inputs[1].default_value = True
    #Name
    store_named_attribute_003.inputs[2].default_value = "UV Map"

    #node UV Unwrap
    uv_unwrap = mesh_hair_base_gen.nodes.new("GeometryNodeUVUnwrap")
    uv_unwrap.name = "UV Unwrap"
    uv_unwrap.method = 'ANGLE_BASED'
    #Selection
    uv_unwrap.inputs[0].default_value = True
    #Margin
    uv_unwrap.inputs[2].default_value = 0.019999999552965164
    #Fill Holes
    uv_unwrap.inputs[3].default_value = True

    #node Named Attribute.002
    named_attribute_002 = mesh_hair_base_gen.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_002.name = "Named Attribute.002"
    named_attribute_002.data_type = 'BOOLEAN'
    #Name
    named_attribute_002.inputs[0].default_value = "edge_seam"

    #node Split Edges
    split_edges = mesh_hair_base_gen.nodes.new("GeometryNodeSplitEdges")
    split_edges.name = "Split Edges"

    #node Set Position.001
    set_position_001 = mesh_hair_base_gen.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    #Selection
    set_position_001.inputs[1].default_value = True
    #Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Mix
    mix = mesh_hair_base_gen.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'VECTOR'
    mix.factor_mode = 'UNIFORM'

    #node Position.005
    position_005 = mesh_hair_base_gen.nodes.new("GeometryNodeInputPosition")
    position_005.name = "Position.005"

    #node Store Named Attribute.004
    store_named_attribute_004 = mesh_hair_base_gen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_004.name = "Store Named Attribute.004"
    store_named_attribute_004.data_type = 'BOOLEAN'
    store_named_attribute_004.domain = 'POINT'
    #Selection
    store_named_attribute_004.inputs[1].default_value = True
    #Name
    store_named_attribute_004.inputs[2].default_value = "edge_seam"

    #node Trim Curve.001
    trim_curve_001 = mesh_hair_base_gen.nodes.new("GeometryNodeTrimCurve")
    trim_curve_001.name = "Trim Curve.001"
    trim_curve_001.mode = 'FACTOR'
    #Selection
    trim_curve_001.inputs[1].default_value = True
    #Start
    trim_curve_001.inputs[2].default_value = 0.0
    #End
    trim_curve_001.inputs[3].default_value = 1.0

    #node Group Input.016
    group_input_016 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_016.name = "Group Input.016"
    group_input_016.outputs[0].hide = True
    group_input_016.outputs[1].hide = True
    group_input_016.outputs[2].hide = True
    group_input_016.outputs[3].hide = True
    group_input_016.outputs[4].hide = True
    group_input_016.outputs[5].hide = True
    group_input_016.outputs[6].hide = True
    group_input_016.outputs[7].hide = True
    group_input_016.outputs[8].hide = True
    group_input_016.outputs[9].hide = True
    group_input_016.outputs[10].hide = True
    group_input_016.outputs[11].hide = True
    group_input_016.outputs[12].hide = True
    group_input_016.outputs[14].hide = True

    #node Frame.013
    frame_013 = mesh_hair_base_gen.nodes.new("NodeFrame")
    frame_013.label = "Seam"
    frame_013.name = "Frame.013"
    frame_013.label_size = 20
    frame_013.shrink = True

    #node Group
    group = mesh_hair_base_gen.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = boundary_select
    #Socket_2
    group.inputs[0].default_value = True

    #node Store Named Attribute.005
    store_named_attribute_005 = mesh_hair_base_gen.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_005.name = "Store Named Attribute.005"
    store_named_attribute_005.data_type = 'BOOLEAN'
    store_named_attribute_005.domain = 'POINT'
    #Selection
    store_named_attribute_005.inputs[1].default_value = True
    #Name
    store_named_attribute_005.inputs[2].default_value = "hair_end"

    #node Mesh to Curve.003
    mesh_to_curve_003 = mesh_hair_base_gen.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve_003.name = "Mesh to Curve.003"
    mesh_to_curve_003.mode = 'EDGES'

    #node Named Attribute.003
    named_attribute_003 = mesh_hair_base_gen.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_003.name = "Named Attribute.003"
    named_attribute_003.data_type = 'BOOLEAN'
    #Name
    named_attribute_003.inputs[0].default_value = "hair_end"

    #node Fill Curve
    fill_curve = mesh_hair_base_gen.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.mode = 'TRIANGLES'
    #Group ID
    fill_curve.inputs[1].default_value = 0

    #node Join Geometry.001
    join_geometry_001 = mesh_hair_base_gen.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    #node Transform Geometry.001
    transform_geometry_001 = mesh_hair_base_gen.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Combine XYZ.002
    combine_xyz_002 = mesh_hair_base_gen.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    #X
    combine_xyz_002.inputs[0].default_value = 0.0
    #Y
    combine_xyz_002.inputs[1].default_value = 0.0

    #node Math.005
    math_005 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    #Value_001
    math_005.inputs[1].default_value = -1.0

    #node Group Input.017
    group_input_017 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_017.name = "Group Input.017"
    group_input_017.outputs[0].hide = True
    group_input_017.outputs[1].hide = True
    group_input_017.outputs[2].hide = True
    group_input_017.outputs[3].hide = True
    group_input_017.outputs[4].hide = True
    group_input_017.outputs[5].hide = True
    group_input_017.outputs[7].hide = True
    group_input_017.outputs[8].hide = True
    group_input_017.outputs[9].hide = True
    group_input_017.outputs[10].hide = True
    group_input_017.outputs[11].hide = True
    group_input_017.outputs[12].hide = True
    group_input_017.outputs[13].hide = True
    group_input_017.outputs[14].hide = True

    #node Math.006
    math_006 = mesh_hair_base_gen.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    #node Group Input.018
    group_input_018 = mesh_hair_base_gen.nodes.new("NodeGroupInput")
    group_input_018.name = "Group Input.018"
    group_input_018.outputs[0].hide = True
    group_input_018.outputs[2].hide = True
    group_input_018.outputs[3].hide = True
    group_input_018.outputs[4].hide = True
    group_input_018.outputs[5].hide = True
    group_input_018.outputs[6].hide = True
    group_input_018.outputs[7].hide = True
    group_input_018.outputs[8].hide = True
    group_input_018.outputs[9].hide = True
    group_input_018.outputs[10].hide = True
    group_input_018.outputs[11].hide = True
    group_input_018.outputs[12].hide = True
    group_input_018.outputs[13].hide = True
    group_input_018.outputs[14].hide = True

    #node Merge by Distance.003
    merge_by_distance_003 = mesh_hair_base_gen.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_003.name = "Merge by Distance.003"
    merge_by_distance_003.mode = 'CONNECTED'
    #Selection
    merge_by_distance_003.inputs[1].default_value = True
    #Distance
    merge_by_distance_003.inputs[2].default_value = 0.0010000000474974513




    #Set parents
    cube.parent = frame
    subdivision_surface.parent = frame
    group_input_001.parent = frame
    delete_geometry.parent = frame_001
    compare.parent = frame_001
    separate_xyz.parent = frame_001
    position.parent = frame_001
    compare_001.parent = frame_001
    switch.parent = frame_001
    boolean_math.parent = frame_001
    group_input_002.parent = frame_001
    switch_001.parent = frame_001
    group_input_003.parent = frame_001
    math.parent = frame_001
    separate_xyz_001.parent = frame_002
    position_001.parent = frame_002
    compare_002.parent = frame_002
    store_named_attribute.parent = frame_002
    extrude_mesh.parent = frame_003
    group_input_004.parent = frame_003
    join_geometry.parent = frame_003
    merge_by_distance.parent = frame_003
    reroute.parent = frame_003
    set_position.parent = frame_003
    vector_math.parent = frame_003
    position_002.parent = frame_003
    named_attribute.parent = frame_003
    sort_elements.parent = frame_005
    separate_xyz_002.parent = frame_005
    position_003.parent = frame_005
    compare_004.parent = frame_006
    integer_math_001.parent = frame_006
    index_001.parent = frame_006
    separate_geometry_001.parent = frame_006
    scale_elements.parent = frame_008
    merge_by_distance_001.parent = frame_008
    scale_elements_001.parent = frame_008
    merge_by_distance_002.parent = frame_008
    join_geometry_002.parent = frame_008
    extrude_mesh_003.parent = frame_008
    combine_xyz_001.parent = frame_008
    math_002.parent = frame_008
    group_input_007.parent = frame_008
    mesh_to_curve_002.parent = frame_008
    resample_curve.parent = frame_008
    group_input_009.parent = frame_008
    reverse_curve.parent = frame_008
    set_curve_tilt.parent = frame_008
    math_008.parent = frame_008
    math_001.parent = frame_008
    index_002.parent = frame_008
    capture_attribute.parent = frame_008
    sort_elements_001.parent = frame_009
    separate_xyz_003.parent = frame_009
    position_004.parent = frame_009
    frame_009.parent = frame_008
    transform_geometry.parent = frame_010
    group_input_1.parent = frame_010
    set_geometry_name.parent = frame_008
    curve_line.parent = frame_004
    group_input_005.parent = frame_004
    curve_to_mesh_001.parent = frame_004
    endpoint_selection.parent = frame_004
    capture_attribute_001.parent = frame_004
    combine_xyz.parent = frame_004
    math_003.parent = frame_004
    resample_curve_001.parent = frame_004
    group_input_006.parent = frame_004
    trim_curve.parent = frame_004
    math_004.parent = frame_004
    group_input_008.parent = frame_004
    set_shade_smooth.parent = frame_004
    delete_geometry_002.parent = frame_010
    geometry_to_instance.parent = frame_010
    index.parent = frame_010
    compare_003.parent = frame_010
    menu_switch.parent = frame_010
    group_input_010.parent = frame_010
    realize_instances.parent = frame_010
    set_geometry_name_002.parent = frame_004
    resample_curve_002.parent = frame_008
    group_input_011.parent = frame_008
    group_input_012.parent = frame_008
    group_input_013.parent = frame_004
    resample_curve_003.parent = frame_004
    group_input_014.parent = frame_004
    switch_002.parent = frame_004
    switch_003.parent = frame_008
    scale_elements_002.parent = frame_004
    endpoint_selection_001.parent = frame_004
    group_input_015.parent = frame_004
    face_group_boundaries_001.parent = frame_011
    edges_to_face_groups_001.parent = frame_011
    boolean_001.parent = frame_011
    boolean_math_005.parent = frame_011
    store_named_attribute_002.parent = frame_013
    endpoint_selection_002.parent = frame_013
    store_named_attribute_004.parent = frame_004
    trim_curve_001.parent = frame_013
    store_named_attribute_005.parent = frame_004

    #Set locations
    group_output_1.location = (8166.5419921875, 755.16845703125)
    cube.location = (30.2105712890625, -35.99675750732422)
    subdivision_surface.location = (423.124267578125, -50.450653076171875)
    group_input_001.location = (212.071044921875, -197.1882781982422)
    frame.location = (-1192.0, 123.0)
    delete_geometry.location = (1339.317626953125, -35.57171630859375)
    compare.location = (770.491943359375, -94.140380859375)
    separate_xyz.location = (207.975830078125, -313.6423645019531)
    position.location = (30.2869873046875, -336.0654296875)
    compare_001.location = (751.4434814453125, -369.147216796875)
    switch.location = (956.2833251953125, -258.2159729003906)
    boolean_math.location = (1131.8743896484375, -143.10946655273438)
    group_input_002.location = (770.28857421875, -267.54766845703125)
    switch_001.location = (564.4404907226562, -290.3665466308594)
    group_input_003.location = (255.3426513671875, -171.56625366210938)
    math.location = (396.28369140625, -414.4344482421875)
    frame_001.location = (-1261.0, -194.0)
    separate_xyz_001.location = (207.43374633789062, -58.016387939453125)
    position_001.location = (29.744903564453125, -80.439453125)
    compare_002.location = (418.6562194824219, -35.67584228515625)
    frame_002.location = (-344.0, 151.0)
    store_named_attribute.location = (615.1507568359375, -36.40672302246094)
    extrude_mesh.location = (320.17633056640625, -114.02623748779297)
    group_input_004.location = (130.388671875, -271.7933044433594)
    join_geometry.location = (519.1848754882812, -36.3756103515625)
    merge_by_distance.location = (879.0073852539062, -55.63127136230469)
    frame_003.location = (720.1005249023438, 191.0)
    reroute.location = (35.0, -152.94888305664062)
    set_position.location = (698.8993530273438, -56.212005615234375)
    vector_math.location = (704.6419067382812, -245.62998962402344)
    position_002.location = (510.91571044921875, -383.4138488769531)
    named_attribute.location = (508.96099853515625, -137.89659118652344)
    named_attribute_001.location = (1998.952880859375, 66.57563781738281)
    separate_geometry.location = (2223.480712890625, 202.88719177246094)
    sort_elements.location = (429.8704833984375, -35.5704345703125)
    separate_xyz_002.location = (208.00732421875, -37.7847900390625)
    position_003.location = (30.3184814453125, -60.2078857421875)
    frame_005.location = (1541.0, 437.0)
    mesh_to_curve.location = (3193.396728515625, 978.84814453125)
    compare_004.location = (354.540771484375, -36.27386474609375)
    integer_math_001.location = (193.33984375, -56.3148193359375)
    index_001.location = (29.7291259765625, -98.57647705078125)
    separate_geometry_001.location = (524.411865234375, -42.0909423828125)
    frame_006.location = (2007.0, 691.0)
    mesh_to_curve_001.location = (3189.563720703125, 827.8146362304688)
    scale_elements.location = (277.9677734375, -145.557861328125)
    merge_by_distance_001.location = (455.832763671875, -167.31817626953125)
    scale_elements_001.location = (269.008056640625, -280.1917724609375)
    merge_by_distance_002.location = (458.819580078125, -288.48870849609375)
    join_geometry_002.location = (668.054443359375, -244.38311767578125)
    extrude_mesh_003.location = (890.437744140625, -201.93344116210938)
    combine_xyz_001.location = (679.03759765625, -309.9908447265625)
    math_002.location = (455.023681640625, -378.86328125)
    group_input_007.location = (242.57470703125, -431.47601318359375)
    mesh_to_curve_002.location = (1049.5771484375, -185.333740234375)
    resample_curve.location = (1230.0419921875, -115.11483764648438)
    frame_008.location = (2749.0, 621.0)
    group_input_009.location = (1045.805908203125, -109.05331420898438)
    curve_to_mesh.location = (4703.7412109375, 332.3516540527344)
    reverse_curve.location = (1435.06103515625, -373.8006591796875)
    set_curve_tilt.location = (1671.60302734375, -301.08587646484375)
    math_008.location = (1154.76708984375, -429.56939697265625)
    math_001.location = (1420.31640625, -497.6940612792969)
    index_002.location = (466.427734375, -510.5404052734375)
    capture_attribute.location = (672.4072265625, -478.49114990234375)
    sort_elements_001.location = (429.576416015625, -35.80364990234375)
    separate_xyz_003.location = (207.71337890625, -38.01800537109375)
    position_004.location = (30.0244140625, -60.44110107421875)
    frame_009.location = (30.0, -590.0)
    reroute_001.location = (4707.21923828125, -237.5545654296875)
    reroute_002.location = (2669.010498046875, -246.27389526367188)
    transform_geometry.location = (1133.11328125, -227.91302490234375)
    group_input_1.location = (662.1513671875, -350.5068359375)
    set_geometry_name.location = (1664.36279296875, -451.5813293457031)
    join_geometry_003.location = (3390.21533203125, 918.9580078125)
    curve_line.location = (626.939208984375, -209.70654296875)
    group_input_005.location = (29.970947265625, -354.0)
    curve_to_mesh_001.location = (1868.3544921875, -207.1890869140625)
    endpoint_selection.location = (1401.937255859375, -317.7808837890625)
    capture_attribute_001.location = (1636.792236328125, -227.917724609375)
    combine_xyz.location = (442.994140625, -248.8267822265625)
    math_003.location = (225.395263671875, -236.1036376953125)
    resample_curve_001.location = (1147.16650390625, -164.64697265625)
    group_input_006.location = (801.619140625, -346.8057861328125)
    trim_curve.location = (852.512939453125, -174.466552734375)
    math_004.location = (618.985595703125, -36.2481689453125)
    group_input_008.location = (226.81103515625, -99.43408203125)
    set_shade_smooth.location = (2510.4853515625, -233.412353515625)
    delete_geometry_002.location = (922.41796875, -175.90350341796875)
    geometry_to_instance.location = (381.0537109375, -436.70550537109375)
    index.location = (37.15087890625, -35.7392578125)
    compare_003.location = (426.1943359375, -75.0771484375)
    menu_switch.location = (206.3359375, -163.44085693359375)
    group_input_010.location = (29.99853515625, -160.86322021484375)
    realize_instances.location = (1312.5751953125, -237.2010498046875)
    set_geometry_name_001.location = (4836.3583984375, -7.330887794494629)
    frame_004.location = (2455.0, 1710.0)
    set_geometry_name_002.location = (2520.82666015625, -408.7220458984375)
    resample_curve_002.location = (1229.41650390625, -252.99038696289062)
    group_input_011.location = (1041.47021484375, -36.23492431640625)
    group_input_012.location = (1062.248046875, -343.13519287109375)
    group_input_013.location = (1087.1279296875, -49.7630615234375)
    resample_curve_003.location = (1153.994873046875, -326.9237060546875)
    group_input_014.location = (799.525390625, -413.6630859375)
    switch_002.location = (1399.458984375, -158.2276611328125)
    switch_003.location = (1439.74853515625, -159.37835693359375)
    frame_010.location = (4987.0, 984.0)
    scale_elements_002.location = (2083.5986328125, -193.4073486328125)
    endpoint_selection_001.location = (1397.891357421875, -423.1580810546875)
    group_input_015.location = (1866.12744140625, -400.2310791015625)
    face_group_boundaries_001.location = (393.30059814453125, -48.833221435546875)
    edges_to_face_groups_001.location = (205.64630126953125, -48.308990478515625)
    boolean_001.location = (30.08526611328125, -66.08969116210938)
    frame_011.location = (277.0, -362.0)
    boolean_math_005.location = (579.9263305664062, -36.404571533203125)
    store_named_attribute_001.location = (500.01806640625, 112.4146957397461)
    store_named_attribute_002.location = (192.602294921875, -46.953369140625)
    endpoint_selection_002.location = (29.56494140625, -201.220458984375)
    store_named_attribute_003.location = (7404.60400390625, 873.4935913085938)
    uv_unwrap.location = (6901.064453125, 668.1045532226562)
    named_attribute_002.location = (6648.99365234375, 678.0661010742188)
    split_edges.location = (6894.9462890625, 775.3009643554688)
    set_position_001.location = (7622.9453125, 782.24609375)
    mix.location = (7401.3662109375, 647.54638671875)
    position_005.location = (7173.380859375, 557.3316040039062)
    store_named_attribute_004.location = (2330.2373046875, -241.455810546875)
    trim_curve_001.location = (36.629638671875, -36.3402099609375)
    group_input_016.location = (7164.40625, 638.0888671875)
    frame_013.location = (3649.0, 1042.0)
    group.location = (2625.246337890625, 865.6160888671875)
    store_named_attribute_005.location = (1622.5205078125, -41.015869140625)
    mesh_to_curve_003.location = (6571.01025390625, 1015.4185791015625)
    named_attribute_003.location = (6289.58154296875, 1138.707275390625)
    fill_curve.location = (6739.294921875, 1034.20751953125)
    join_geometry_001.location = (7191.521484375, 868.9816284179688)
    transform_geometry_001.location = (6930.96240234375, 1106.341552734375)
    combine_xyz_002.location = (6734.5087890625, 1211.9066162109375)
    math_005.location = (6541.2607421875, 1332.480224609375)
    group_input_017.location = (6181.34765625, 1307.7984619140625)
    math_006.location = (6361.33349609375, 1337.4871826171875)
    group_input_018.location = (6179.56884765625, 1220.3131103515625)
    merge_by_distance_003.location = (7837.92138671875, 764.1631469726562)

    #Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    subdivision_surface.width, subdivision_surface.height = 150.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    frame.width, frame.height = 603.0, 291.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    position.width, position.height = 100.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    frame_001.width, frame_001.height = 1509.0, 592.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    position_001.width, position_001.height = 100.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    frame_002.width, frame_002.height = 785.0, 234.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    frame_003.width, frame_003.height = 1048.8994140625, 463.0
    reroute.width, reroute.height = 10.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    named_attribute.width, named_attribute.height = 140.0, 100.0
    named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    sort_elements.width, sort_elements.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    position_003.width, position_003.height = 100.0, 100.0
    frame_005.width, frame_005.height = 600.0, 206.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    integer_math_001.width, integer_math_001.height = 140.0, 100.0
    index_001.width, index_001.height = 140.0, 100.0
    separate_geometry_001.width, separate_geometry_001.height = 140.0, 100.0
    frame_006.width, frame_006.height = 694.0, 215.0
    mesh_to_curve_001.width, mesh_to_curve_001.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
    scale_elements_001.width, scale_elements_001.height = 140.0, 100.0
    merge_by_distance_002.width, merge_by_distance_002.height = 140.0, 100.0
    join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
    extrude_mesh_003.width, extrude_mesh_003.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    mesh_to_curve_002.width, mesh_to_curve_002.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    frame_008.width, frame_008.height = 1842.0, 826.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
    reverse_curve.width, reverse_curve.height = 140.0, 100.0
    set_curve_tilt.width, set_curve_tilt.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    index_002.width, index_002.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    sort_elements_001.width, sort_elements_001.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    position_004.width, position_004.height = 100.0, 100.0
    frame_009.width, frame_009.height = 600.0, 206.0
    reroute_001.width, reroute_001.height = 10.0, 100.0
    reroute_002.width, reroute_002.height = 10.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    set_geometry_name.width, set_geometry_name.height = 140.0, 100.0
    join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
    curve_line.width, curve_line.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
    endpoint_selection.width, endpoint_selection.height = 140.0, 100.0
    capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    resample_curve_001.width, resample_curve_001.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    trim_curve.width, trim_curve.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    delete_geometry_002.width, delete_geometry_002.height = 140.0, 100.0
    geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
    index.width, index.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    menu_switch.width, menu_switch.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    set_geometry_name_001.width, set_geometry_name_001.height = 140.0, 100.0
    frame_004.width, frame_004.height = 2691.0, 550.0
    set_geometry_name_002.width, set_geometry_name_002.height = 140.0, 100.0
    resample_curve_002.width, resample_curve_002.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    resample_curve_003.width, resample_curve_003.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    switch_003.width, switch_003.height = 140.0, 100.0
    frame_010.width, frame_010.height = 1483.0, 548.0
    scale_elements_002.width, scale_elements_002.height = 140.0, 100.0
    endpoint_selection_001.width, endpoint_selection_001.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    face_group_boundaries_001.width, face_group_boundaries_001.height = 150.0, 100.0
    edges_to_face_groups_001.width, edges_to_face_groups_001.height = 140.0, 100.0
    boolean_001.width, boolean_001.height = 140.0, 100.0
    frame_011.width, frame_011.height = 750.0, 167.0
    boolean_math_005.width, boolean_math_005.height = 140.0, 100.0
    store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
    store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
    endpoint_selection_002.width, endpoint_selection_002.height = 140.0, 100.0
    store_named_attribute_003.width, store_named_attribute_003.height = 140.0, 100.0
    uv_unwrap.width, uv_unwrap.height = 140.0, 100.0
    named_attribute_002.width, named_attribute_002.height = 140.0, 100.0
    split_edges.width, split_edges.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    position_005.width, position_005.height = 140.0, 100.0
    store_named_attribute_004.width, store_named_attribute_004.height = 140.0, 100.0
    trim_curve_001.width, trim_curve_001.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    frame_013.width, frame_013.height = 363.0, 328.0
    group.width, group.height = 140.0, 100.0
    store_named_attribute_005.width, store_named_attribute_005.height = 140.0, 100.0
    mesh_to_curve_003.width, mesh_to_curve_003.height = 140.0, 100.0
    named_attribute_003.width, named_attribute_003.height = 140.0, 100.0
    fill_curve.width, fill_curve.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    merge_by_distance_003.width, merge_by_distance_003.height = 140.0, 100.0

    #initialize mesh_hair_base_gen links
    #cube.Mesh -> subdivision_surface.Mesh
    mesh_hair_base_gen.links.new(cube.outputs[0], subdivision_surface.inputs[0])
    #group_input_001.Level -> subdivision_surface.Level
    mesh_hair_base_gen.links.new(group_input_001.outputs[2], subdivision_surface.inputs[1])
    #subdivision_surface.Mesh -> delete_geometry.Geometry
    mesh_hair_base_gen.links.new(subdivision_surface.outputs[0], delete_geometry.inputs[0])
    #separate_xyz.Z -> compare.A
    mesh_hair_base_gen.links.new(separate_xyz.outputs[2], compare.inputs[0])
    #position.Position -> separate_xyz.Vector
    mesh_hair_base_gen.links.new(position.outputs[0], separate_xyz.inputs[0])
    #compare_001.Result -> switch.True
    mesh_hair_base_gen.links.new(compare_001.outputs[0], switch.inputs[2])
    #compare.Result -> boolean_math.Boolean
    mesh_hair_base_gen.links.new(compare.outputs[0], boolean_math.inputs[0])
    #switch.Output -> boolean_math.Boolean
    mesh_hair_base_gen.links.new(switch.outputs[0], boolean_math.inputs[1])
    #boolean_math.Boolean -> delete_geometry.Selection
    mesh_hair_base_gen.links.new(boolean_math.outputs[0], delete_geometry.inputs[1])
    #group_input_002.Quarter Sphere -> switch.Switch
    mesh_hair_base_gen.links.new(group_input_002.outputs[3], switch.inputs[0])
    #separate_xyz.Y -> switch_001.False
    mesh_hair_base_gen.links.new(separate_xyz.outputs[1], switch_001.inputs[1])
    #switch_001.Output -> compare_001.A
    mesh_hair_base_gen.links.new(switch_001.outputs[0], compare_001.inputs[0])
    #group_input_003.Front Quarter -> switch_001.Switch
    mesh_hair_base_gen.links.new(group_input_003.outputs[4], switch_001.inputs[0])
    #separate_xyz.Y -> math.Value
    mesh_hair_base_gen.links.new(separate_xyz.outputs[1], math.inputs[0])
    #math.Value -> switch_001.True
    mesh_hair_base_gen.links.new(math.outputs[0], switch_001.inputs[2])
    #position_001.Position -> separate_xyz_001.Vector
    mesh_hair_base_gen.links.new(position_001.outputs[0], separate_xyz_001.inputs[0])
    #separate_xyz_001.Z -> compare_002.A
    mesh_hair_base_gen.links.new(separate_xyz_001.outputs[2], compare_002.inputs[0])
    #compare_002.Result -> store_named_attribute.Value
    mesh_hair_base_gen.links.new(compare_002.outputs[0], store_named_attribute.inputs[3])
    #delete_geometry.Geometry -> store_named_attribute.Geometry
    mesh_hair_base_gen.links.new(delete_geometry.outputs[0], store_named_attribute.inputs[0])
    #reroute.Output -> extrude_mesh.Mesh
    mesh_hair_base_gen.links.new(reroute.outputs[0], extrude_mesh.inputs[0])
    #extrude_mesh.Mesh -> join_geometry.Geometry
    mesh_hair_base_gen.links.new(extrude_mesh.outputs[0], join_geometry.inputs[0])
    #set_position.Geometry -> merge_by_distance.Geometry
    mesh_hair_base_gen.links.new(set_position.outputs[0], merge_by_distance.inputs[0])
    #store_named_attribute_001.Geometry -> reroute.Input
    mesh_hair_base_gen.links.new(store_named_attribute_001.outputs[0], reroute.inputs[0])
    #join_geometry.Geometry -> set_position.Geometry
    mesh_hair_base_gen.links.new(join_geometry.outputs[0], set_position.inputs[0])
    #vector_math.Vector -> set_position.Position
    mesh_hair_base_gen.links.new(vector_math.outputs[0], set_position.inputs[2])
    #position_002.Position -> vector_math.Vector
    mesh_hair_base_gen.links.new(position_002.outputs[0], vector_math.inputs[0])
    #named_attribute.Attribute -> set_position.Selection
    mesh_hair_base_gen.links.new(named_attribute.outputs[0], set_position.inputs[1])
    #sort_elements.Geometry -> separate_geometry.Geometry
    mesh_hair_base_gen.links.new(sort_elements.outputs[0], separate_geometry.inputs[0])
    #named_attribute_001.Attribute -> separate_geometry.Selection
    mesh_hair_base_gen.links.new(named_attribute_001.outputs[0], separate_geometry.inputs[1])
    #merge_by_distance.Geometry -> sort_elements.Geometry
    mesh_hair_base_gen.links.new(merge_by_distance.outputs[0], sort_elements.inputs[0])
    #position_003.Position -> separate_xyz_002.Vector
    mesh_hair_base_gen.links.new(position_003.outputs[0], separate_xyz_002.inputs[0])
    #separate_xyz_002.X -> sort_elements.Sort Weight
    mesh_hair_base_gen.links.new(separate_xyz_002.outputs[0], sort_elements.inputs[3])
    #integer_math_001.Value -> compare_004.A
    mesh_hair_base_gen.links.new(integer_math_001.outputs[0], compare_004.inputs[2])
    #index_001.Index -> integer_math_001.Value
    mesh_hair_base_gen.links.new(index_001.outputs[0], integer_math_001.inputs[0])
    #compare_004.Result -> separate_geometry_001.Selection
    mesh_hair_base_gen.links.new(compare_004.outputs[0], separate_geometry_001.inputs[1])
    #separate_geometry.Selection -> separate_geometry_001.Geometry
    mesh_hair_base_gen.links.new(separate_geometry.outputs[0], separate_geometry_001.inputs[0])
    #separate_geometry_001.Selection -> mesh_to_curve.Mesh
    mesh_hair_base_gen.links.new(separate_geometry_001.outputs[0], mesh_to_curve.inputs[0])
    #group.Boundary Edge -> mesh_to_curve.Selection
    mesh_hair_base_gen.links.new(group.outputs[0], mesh_to_curve.inputs[1])
    #separate_geometry_001.Inverted -> mesh_to_curve_001.Mesh
    mesh_hair_base_gen.links.new(separate_geometry_001.outputs[1], mesh_to_curve_001.inputs[0])
    #scale_elements.Geometry -> merge_by_distance_001.Geometry
    mesh_hair_base_gen.links.new(scale_elements.outputs[0], merge_by_distance_001.inputs[0])
    #scale_elements_001.Geometry -> merge_by_distance_002.Geometry
    mesh_hair_base_gen.links.new(scale_elements_001.outputs[0], merge_by_distance_002.inputs[0])
    #separate_geometry_001.Inverted -> scale_elements_001.Geometry
    mesh_hair_base_gen.links.new(separate_geometry_001.outputs[1], scale_elements_001.inputs[0])
    #separate_geometry_001.Selection -> scale_elements.Geometry
    mesh_hair_base_gen.links.new(separate_geometry_001.outputs[0], scale_elements.inputs[0])
    #merge_by_distance_002.Geometry -> join_geometry_002.Geometry
    mesh_hair_base_gen.links.new(merge_by_distance_002.outputs[0], join_geometry_002.inputs[0])
    #combine_xyz_001.Vector -> extrude_mesh_003.Offset
    mesh_hair_base_gen.links.new(combine_xyz_001.outputs[0], extrude_mesh_003.inputs[2])
    #math_002.Value -> combine_xyz_001.Z
    mesh_hair_base_gen.links.new(math_002.outputs[0], combine_xyz_001.inputs[2])
    #extrude_mesh_003.Mesh -> mesh_to_curve_002.Mesh
    mesh_hair_base_gen.links.new(extrude_mesh_003.outputs[0], mesh_to_curve_002.inputs[0])
    #mesh_to_curve_002.Curve -> resample_curve.Curve
    mesh_hair_base_gen.links.new(mesh_to_curve_002.outputs[0], resample_curve.inputs[0])
    #group_input_009.Hair Resolution -> resample_curve.Count
    mesh_hair_base_gen.links.new(group_input_009.outputs[7], resample_curve.inputs[2])
    #set_geometry_name.Geometry -> curve_to_mesh.Curve
    mesh_hair_base_gen.links.new(set_geometry_name.outputs[0], curve_to_mesh.inputs[0])
    #group_input_004.Solidify Offset -> extrude_mesh.Offset Scale
    mesh_hair_base_gen.links.new(group_input_004.outputs[5], extrude_mesh.inputs[3])
    #reverse_curve.Curve -> set_curve_tilt.Curve
    mesh_hair_base_gen.links.new(reverse_curve.outputs[0], set_curve_tilt.inputs[0])
    #math_008.Value -> math_001.Value
    mesh_hair_base_gen.links.new(math_008.outputs[0], math_001.inputs[0])
    #index_002.Index -> capture_attribute.Index
    mesh_hair_base_gen.links.new(index_002.outputs[0], capture_attribute.inputs[1])
    #capture_attribute.Index -> math_001.Value
    mesh_hair_base_gen.links.new(capture_attribute.outputs[1], math_001.inputs[1])
    #capture_attribute.Geometry -> extrude_mesh_003.Mesh
    mesh_hair_base_gen.links.new(capture_attribute.outputs[0], extrude_mesh_003.inputs[0])
    #position_004.Position -> separate_xyz_003.Vector
    mesh_hair_base_gen.links.new(position_004.outputs[0], separate_xyz_003.inputs[0])
    #separate_xyz_003.X -> sort_elements_001.Sort Weight
    mesh_hair_base_gen.links.new(separate_xyz_003.outputs[0], sort_elements_001.inputs[3])
    #join_geometry_002.Geometry -> sort_elements_001.Geometry
    mesh_hair_base_gen.links.new(join_geometry_002.outputs[0], sort_elements_001.inputs[0])
    #reroute_002.Output -> reroute_001.Input
    mesh_hair_base_gen.links.new(reroute_002.outputs[0], reroute_001.inputs[0])
    #separate_geometry.Inverted -> reroute_002.Input
    mesh_hair_base_gen.links.new(separate_geometry.outputs[1], reroute_002.inputs[0])
    #math_001.Value -> set_curve_tilt.Tilt
    mesh_hair_base_gen.links.new(math_001.outputs[0], set_curve_tilt.inputs[2])
    #sort_elements_001.Geometry -> capture_attribute.Geometry
    mesh_hair_base_gen.links.new(sort_elements_001.outputs[0], capture_attribute.inputs[0])
    #group_input_007.Hair Length -> math_002.Value
    mesh_hair_base_gen.links.new(group_input_007.outputs[6], math_002.inputs[0])
    #group_input_1.Scale -> transform_geometry.Scale
    mesh_hair_base_gen.links.new(group_input_1.outputs[1], transform_geometry.inputs[3])
    #set_curve_tilt.Curve -> set_geometry_name.Geometry
    mesh_hair_base_gen.links.new(set_curve_tilt.outputs[0], set_geometry_name.inputs[0])
    #mesh_to_curve_001.Curve -> join_geometry_003.Geometry
    mesh_hair_base_gen.links.new(mesh_to_curve_001.outputs[0], join_geometry_003.inputs[0])
    #capture_attribute_001.Geometry -> curve_to_mesh_001.Curve
    mesh_hair_base_gen.links.new(capture_attribute_001.outputs[0], curve_to_mesh_001.inputs[0])
    #endpoint_selection.Selection -> capture_attribute_001.Head
    mesh_hair_base_gen.links.new(endpoint_selection.outputs[0], capture_attribute_001.inputs[1])
    #combine_xyz.Vector -> curve_line.Start
    mesh_hair_base_gen.links.new(combine_xyz.outputs[0], curve_line.inputs[0])
    #math_003.Value -> combine_xyz.Z
    mesh_hair_base_gen.links.new(math_003.outputs[0], combine_xyz.inputs[2])
    #group_input_005.Hair Length -> math_003.Value
    mesh_hair_base_gen.links.new(group_input_005.outputs[6], math_003.inputs[0])
    #trim_curve.Curve -> resample_curve_001.Curve
    mesh_hair_base_gen.links.new(trim_curve.outputs[0], resample_curve_001.inputs[0])
    #group_input_006.Hair Resolution -> resample_curve_001.Count
    mesh_hair_base_gen.links.new(group_input_006.outputs[7], resample_curve_001.inputs[2])
    #curve_line.Curve -> trim_curve.Curve
    mesh_hair_base_gen.links.new(curve_line.outputs[0], trim_curve.inputs[0])
    #math_004.Value -> trim_curve.End
    mesh_hair_base_gen.links.new(math_004.outputs[0], trim_curve.inputs[5])
    #group_input_005.Hair Length -> math_004.Value
    mesh_hair_base_gen.links.new(group_input_005.outputs[6], math_004.inputs[0])
    #group_input_008.Trim Top -> math_004.Value
    mesh_hair_base_gen.links.new(group_input_008.outputs[8], math_004.inputs[1])
    #store_named_attribute_004.Geometry -> set_shade_smooth.Geometry
    mesh_hair_base_gen.links.new(store_named_attribute_004.outputs[0], set_shade_smooth.inputs[0])
    #curve_to_mesh.Mesh -> geometry_to_instance.Geometry
    mesh_hair_base_gen.links.new(curve_to_mesh.outputs[0], geometry_to_instance.inputs[0])
    #geometry_to_instance.Instances -> delete_geometry_002.Geometry
    mesh_hair_base_gen.links.new(geometry_to_instance.outputs[0], delete_geometry_002.inputs[0])
    #delete_geometry_002.Geometry -> transform_geometry.Geometry
    mesh_hair_base_gen.links.new(delete_geometry_002.outputs[0], transform_geometry.inputs[0])
    #compare_003.Result -> delete_geometry_002.Selection
    mesh_hair_base_gen.links.new(compare_003.outputs[0], delete_geometry_002.inputs[1])
    #index.Index -> compare_003.A
    mesh_hair_base_gen.links.new(index.outputs[0], compare_003.inputs[2])
    #menu_switch.Output -> compare_003.B
    mesh_hair_base_gen.links.new(menu_switch.outputs[0], compare_003.inputs[3])
    #group_input_010.Delete -> menu_switch.Menu
    mesh_hair_base_gen.links.new(group_input_010.outputs[9], menu_switch.inputs[0])
    #transform_geometry.Geometry -> realize_instances.Geometry
    mesh_hair_base_gen.links.new(transform_geometry.outputs[0], realize_instances.inputs[0])
    #reroute_001.Output -> set_geometry_name_001.Geometry
    mesh_hair_base_gen.links.new(reroute_001.outputs[0], set_geometry_name_001.inputs[0])
    #set_shade_smooth.Geometry -> set_geometry_name_002.Geometry
    mesh_hair_base_gen.links.new(set_shade_smooth.outputs[0], set_geometry_name_002.inputs[0])
    #group_input_011.Hair Res By Lenght -> resample_curve.Selection
    mesh_hair_base_gen.links.new(group_input_011.outputs[10], resample_curve.inputs[1])
    #group_input_012.Length Res -> resample_curve_002.Length
    mesh_hair_base_gen.links.new(group_input_012.outputs[11], resample_curve_002.inputs[3])
    #group_input_014.Length Res -> resample_curve_003.Length
    mesh_hair_base_gen.links.new(group_input_014.outputs[11], resample_curve_003.inputs[3])
    #resample_curve_001.Curve -> switch_002.False
    mesh_hair_base_gen.links.new(resample_curve_001.outputs[0], switch_002.inputs[1])
    #trim_curve.Curve -> resample_curve_003.Curve
    mesh_hair_base_gen.links.new(trim_curve.outputs[0], resample_curve_003.inputs[0])
    #resample_curve_003.Curve -> switch_002.True
    mesh_hair_base_gen.links.new(resample_curve_003.outputs[0], switch_002.inputs[2])
    #group_input_013.Hair Res By Lenght -> switch_002.Switch
    mesh_hair_base_gen.links.new(group_input_013.outputs[10], switch_002.inputs[0])
    #resample_curve.Curve -> switch_003.False
    mesh_hair_base_gen.links.new(resample_curve.outputs[0], switch_003.inputs[1])
    #mesh_to_curve_002.Curve -> resample_curve_002.Curve
    mesh_hair_base_gen.links.new(mesh_to_curve_002.outputs[0], resample_curve_002.inputs[0])
    #resample_curve_002.Curve -> switch_003.True
    mesh_hair_base_gen.links.new(resample_curve_002.outputs[0], switch_003.inputs[2])
    #switch_003.Output -> reverse_curve.Curve
    mesh_hair_base_gen.links.new(switch_003.outputs[0], reverse_curve.inputs[0])
    #endpoint_selection_001.Selection -> capture_attribute_001.Tail
    mesh_hair_base_gen.links.new(endpoint_selection_001.outputs[0], capture_attribute_001.inputs[2])
    #capture_attribute_001.Tail -> scale_elements_002.Selection
    mesh_hair_base_gen.links.new(capture_attribute_001.outputs[2], scale_elements_002.inputs[1])
    #group_input_015.Tip Scale -> scale_elements_002.Scale
    mesh_hair_base_gen.links.new(group_input_015.outputs[12], scale_elements_002.inputs[2])
    #edges_to_face_groups_001.Face Group ID -> face_group_boundaries_001.Face Group ID
    mesh_hair_base_gen.links.new(edges_to_face_groups_001.outputs[0], face_group_boundaries_001.inputs[0])
    #boolean_001.Boolean -> edges_to_face_groups_001.Boundary Edges
    mesh_hair_base_gen.links.new(boolean_001.outputs[0], edges_to_face_groups_001.inputs[0])
    #face_group_boundaries_001.Boundary Edges -> boolean_math_005.Boolean
    mesh_hair_base_gen.links.new(face_group_boundaries_001.outputs[0], boolean_math_005.inputs[0])
    #store_named_attribute.Geometry -> store_named_attribute_001.Geometry
    mesh_hair_base_gen.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
    #boolean_math_005.Boolean -> store_named_attribute_001.Value
    mesh_hair_base_gen.links.new(boolean_math_005.outputs[0], store_named_attribute_001.inputs[3])
    #uv_unwrap.UV -> store_named_attribute_003.Value
    mesh_hair_base_gen.links.new(uv_unwrap.outputs[0], store_named_attribute_003.inputs[3])
    #named_attribute_002.Attribute -> uv_unwrap.Seam
    mesh_hair_base_gen.links.new(named_attribute_002.outputs[0], uv_unwrap.inputs[1])
    #realize_instances.Geometry -> split_edges.Mesh
    mesh_hair_base_gen.links.new(realize_instances.outputs[0], split_edges.inputs[0])
    #named_attribute_002.Attribute -> split_edges.Selection
    mesh_hair_base_gen.links.new(named_attribute_002.outputs[0], split_edges.inputs[1])
    #store_named_attribute_003.Geometry -> set_position_001.Geometry
    mesh_hair_base_gen.links.new(store_named_attribute_003.outputs[0], set_position_001.inputs[0])
    #mix.Result -> set_position_001.Position
    mesh_hair_base_gen.links.new(mix.outputs[1], set_position_001.inputs[2])
    #uv_unwrap.UV -> mix.B
    mesh_hair_base_gen.links.new(uv_unwrap.outputs[0], mix.inputs[5])
    #position_005.Position -> mix.A
    mesh_hair_base_gen.links.new(position_005.outputs[0], mix.inputs[4])
    #scale_elements_002.Geometry -> store_named_attribute_004.Geometry
    mesh_hair_base_gen.links.new(scale_elements_002.outputs[0], store_named_attribute_004.inputs[0])
    #capture_attribute_001.Tail -> store_named_attribute_004.Value
    mesh_hair_base_gen.links.new(capture_attribute_001.outputs[2], store_named_attribute_004.inputs[3])
    #endpoint_selection_002.Selection -> store_named_attribute_002.Value
    mesh_hair_base_gen.links.new(endpoint_selection_002.outputs[0], store_named_attribute_002.inputs[3])
    #group_input_016.UV Mix -> mix.Factor
    mesh_hair_base_gen.links.new(group_input_016.outputs[13], mix.inputs[0])
    #join_geometry_003.Geometry -> trim_curve_001.Curve
    mesh_hair_base_gen.links.new(join_geometry_003.outputs[0], trim_curve_001.inputs[0])
    #merge_by_distance_003.Geometry -> group_output_1.Geometry
    mesh_hair_base_gen.links.new(merge_by_distance_003.outputs[0], group_output_1.inputs[0])
    #trim_curve_001.Curve -> store_named_attribute_002.Geometry
    mesh_hair_base_gen.links.new(trim_curve_001.outputs[0], store_named_attribute_002.inputs[0])
    #group.Boundary Edge -> mesh_to_curve_001.Selection
    mesh_hair_base_gen.links.new(group.outputs[0], mesh_to_curve_001.inputs[1])
    #store_named_attribute_002.Geometry -> curve_to_mesh_001.Profile Curve
    mesh_hair_base_gen.links.new(store_named_attribute_002.outputs[0], curve_to_mesh_001.inputs[1])
    #curve_to_mesh_001.Mesh -> scale_elements_002.Geometry
    mesh_hair_base_gen.links.new(curve_to_mesh_001.outputs[0], scale_elements_002.inputs[0])
    #switch_002.Output -> store_named_attribute_005.Geometry
    mesh_hair_base_gen.links.new(switch_002.outputs[0], store_named_attribute_005.inputs[0])
    #store_named_attribute_005.Geometry -> capture_attribute_001.Geometry
    mesh_hair_base_gen.links.new(store_named_attribute_005.outputs[0], capture_attribute_001.inputs[0])
    #named_attribute_003.Attribute -> mesh_to_curve_003.Selection
    mesh_hair_base_gen.links.new(named_attribute_003.outputs[0], mesh_to_curve_003.inputs[1])
    #mesh_to_curve_003.Curve -> fill_curve.Curve
    mesh_hair_base_gen.links.new(mesh_to_curve_003.outputs[0], fill_curve.inputs[0])
    #realize_instances.Geometry -> mesh_to_curve_003.Mesh
    mesh_hair_base_gen.links.new(realize_instances.outputs[0], mesh_to_curve_003.inputs[0])
    #endpoint_selection_001.Selection -> store_named_attribute_005.Value
    mesh_hair_base_gen.links.new(endpoint_selection_001.outputs[0], store_named_attribute_005.inputs[3])
    #split_edges.Mesh -> join_geometry_001.Geometry
    mesh_hair_base_gen.links.new(split_edges.outputs[0], join_geometry_001.inputs[0])
    #join_geometry_001.Geometry -> store_named_attribute_003.Geometry
    mesh_hair_base_gen.links.new(join_geometry_001.outputs[0], store_named_attribute_003.inputs[0])
    #fill_curve.Mesh -> transform_geometry_001.Geometry
    mesh_hair_base_gen.links.new(fill_curve.outputs[0], transform_geometry_001.inputs[0])
    #math_005.Value -> combine_xyz_002.Z
    mesh_hair_base_gen.links.new(math_005.outputs[0], combine_xyz_002.inputs[2])
    #math_006.Value -> math_005.Value
    mesh_hair_base_gen.links.new(math_006.outputs[0], math_005.inputs[0])
    #combine_xyz_002.Vector -> transform_geometry_001.Translation
    mesh_hair_base_gen.links.new(combine_xyz_002.outputs[0], transform_geometry_001.inputs[1])
    #group_input_017.Hair Length -> math_006.Value
    mesh_hair_base_gen.links.new(group_input_017.outputs[6], math_006.inputs[0])
    #group_input_018.Scale -> math_006.Value
    mesh_hair_base_gen.links.new(group_input_018.outputs[1], math_006.inputs[1])
    #set_position_001.Geometry -> merge_by_distance_003.Geometry
    mesh_hair_base_gen.links.new(set_position_001.outputs[0], merge_by_distance_003.inputs[0])
    #reroute.Output -> join_geometry.Geometry
    mesh_hair_base_gen.links.new(reroute.outputs[0], join_geometry.inputs[0])
    #merge_by_distance_001.Geometry -> join_geometry_002.Geometry
    mesh_hair_base_gen.links.new(merge_by_distance_001.outputs[0], join_geometry_002.inputs[0])
    #mesh_to_curve.Curve -> join_geometry_003.Geometry
    mesh_hair_base_gen.links.new(mesh_to_curve.outputs[0], join_geometry_003.inputs[0])
    #set_geometry_name_001.Geometry -> geometry_to_instance.Geometry
    mesh_hair_base_gen.links.new(set_geometry_name_001.outputs[0], geometry_to_instance.inputs[0])
    #transform_geometry_001.Geometry -> join_geometry_001.Geometry
    mesh_hair_base_gen.links.new(transform_geometry_001.outputs[0], join_geometry_001.inputs[0])
    #set_geometry_name_002.Geometry -> geometry_to_instance.Geometry
    mesh_hair_base_gen.links.new(set_geometry_name_002.outputs[0], geometry_to_instance.inputs[0])
    delete_socket.default_value = 'Nothing'
    return mesh_hair_base_gen

mesh_hair_base_gen = mesh_hair_base_gen_node_group()

