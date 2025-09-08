import bpy, mathutils

mat = bpy.data.materials.new(name = "Tornasol")
mat.use_nodes = True
#initialize Tornasol node group
def tornasol_node_group():

    tornasol = mat.node_tree
    #start with a clean node tree
    for node in tornasol.nodes:
        tornasol.nodes.remove(node)
    tornasol.color_tag = 'NONE'
    tornasol.description = ""
    tornasol.default_group_node_width = 140
    

    #tornasol interface

    #initialize tornasol nodes
    #node Principled BSDF
    principled_bsdf = tornasol.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #Metallic
    principled_bsdf.inputs[1].default_value = 1.0
    #Roughness
    principled_bsdf.inputs[2].default_value = 0.25
    #IOR
    principled_bsdf.inputs[3].default_value = 1.5
    #Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    #Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    #Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    #Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    #Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    #Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    #Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    #Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    #Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    #Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    #Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    #Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    #Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Color
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    #Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    #node Material Output
    material_output = tornasol.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Vector Math
    vector_math = tornasol.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'DOT_PRODUCT'

    #node Math
    math = tornasol.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 1.0471975803375244

    #node Math.001
    math_001 = tornasol.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'SINE'
    math_001.use_clamp = False

    #node Combine Color
    combine_color = tornasol.nodes.new("ShaderNodeCombineColor")
    combine_color.name = "Combine Color"
    combine_color.mode = 'RGB'

    #node Math.002
    math_002 = tornasol.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'ADD'
    math_002.use_clamp = False
    #Value_001
    math_002.inputs[1].default_value = 2.094399929046631

    #node Math.003
    math_003 = tornasol.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'SINE'
    math_003.use_clamp = False

    #node Math.004
    math_004 = tornasol.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'SINE'
    math_004.use_clamp = False

    #node Math.005
    math_005 = tornasol.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'ADD'
    math_005.use_clamp = False
    #Value_001
    math_005.inputs[1].default_value = 3.1415927410125732

    #node Math.006
    math_006 = tornasol.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY_ADD'
    math_006.use_clamp = False
    #Value_001
    math_006.inputs[1].default_value = 10.0
    #Value_002
    math_006.inputs[2].default_value = 2.0

    #node Mix
    mix = tornasol.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'ADD'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    #Factor_Float
    mix.inputs[0].default_value = 0.44999998807907104
    #A_Color
    mix.inputs[6].default_value = (0.0, 0.10000014305114746, 1.0, 1.0)

    #node Math.007
    math_007 = tornasol.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False

    #node Math.008
    math_008 = tornasol.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'SUBTRACT'
    math_008.use_clamp = False

    #node Math.009
    math_009 = tornasol.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'SUBTRACT'
    math_009.use_clamp = False

    #node Value
    value = tornasol.nodes.new("ShaderNodeValue")
    value.name = "Value"

    value.outputs[0].default_value = 1.0
    #node Mix.001
    mix_001 = tornasol.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    #Factor_Float
    mix_001.inputs[0].default_value = 0.5
    #B_Color
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    #node Texture Coordinate
    texture_coordinate = tornasol.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Mix.002
    mix_002 = tornasol.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    #Factor_Float
    mix_002.inputs[0].default_value = 0.30000001192092896
    #B_Color
    mix_002.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)


    #Set locations
    principled_bsdf.location = (572.0496826171875, 235.56309509277344)
    material_output.location = (847.5894165039062, 146.10543823242188)
    vector_math.location = (-1210.57666015625, 44.99153137207031)
    math.location = (-781.8076782226562, 72.44114685058594)
    math_001.location = (-609.6983032226562, 52.0239372253418)
    combine_color.location = (-107.03788757324219, 156.70545959472656)
    math_002.location = (-782.1834106445312, -116.27770233154297)
    math_003.location = (-622.542236328125, -120.7584457397461)
    math_004.location = (-631.6710815429688, 234.3430938720703)
    math_005.location = (-793.920166015625, 245.81866455078125)
    math_006.location = (-1022.0941772460938, 68.60192108154297)
    mix.location = (239.5755157470703, 171.23512268066406)
    math_007.location = (-332.7503662109375, 255.39454650878906)
    math_008.location = (-324.3370056152344, 62.503692626953125)
    math_009.location = (-357.87274169921875, -106.56410217285156)
    value.location = (-623.69775390625, -263.9009704589844)
    mix_001.location = (68.2916030883789, 178.3257293701172)
    texture_coordinate.location = (-1382.2071533203125, 91.03739929199219)
    mix_002.location = (409.43994140625, 167.4630126953125)

    #Set dimensions
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    material_output.width, material_output.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_color.width, combine_color.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    value.width, value.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    mix_002.width, mix_002.height = 140.0, 100.0

    #initialize tornasol links
    #math.Value -> math_001.Value
    tornasol.links.new(math.outputs[0], math_001.inputs[0])
    #math_002.Value -> math_003.Value
    tornasol.links.new(math_002.outputs[0], math_003.inputs[0])
    #math_005.Value -> math_004.Value
    tornasol.links.new(math_005.outputs[0], math_004.inputs[0])
    #vector_math.Value -> math_006.Value
    tornasol.links.new(vector_math.outputs[1], math_006.inputs[0])
    #math_006.Value -> math_005.Value
    tornasol.links.new(math_006.outputs[0], math_005.inputs[0])
    #math_006.Value -> math.Value
    tornasol.links.new(math_006.outputs[0], math.inputs[0])
    #math_006.Value -> math_002.Value
    tornasol.links.new(math_006.outputs[0], math_002.inputs[0])
    #math_004.Value -> math_007.Value
    tornasol.links.new(math_004.outputs[0], math_007.inputs[1])
    #math_003.Value -> math_009.Value
    tornasol.links.new(math_003.outputs[0], math_009.inputs[1])
    #math_001.Value -> math_008.Value
    tornasol.links.new(math_001.outputs[0], math_008.inputs[1])
    #math_008.Value -> combine_color.Green
    tornasol.links.new(math_008.outputs[0], combine_color.inputs[1])
    #math_009.Value -> combine_color.Blue
    tornasol.links.new(math_009.outputs[0], combine_color.inputs[2])
    #math_007.Value -> combine_color.Red
    tornasol.links.new(math_007.outputs[0], combine_color.inputs[0])
    #value.Value -> math_007.Value
    tornasol.links.new(value.outputs[0], math_007.inputs[0])
    #value.Value -> math_008.Value
    tornasol.links.new(value.outputs[0], math_008.inputs[0])
    #value.Value -> math_009.Value
    tornasol.links.new(value.outputs[0], math_009.inputs[0])
    #mix_001.Result -> mix.B
    tornasol.links.new(mix_001.outputs[2], mix.inputs[7])
    #combine_color.Color -> mix_001.A
    tornasol.links.new(combine_color.outputs[0], mix_001.inputs[6])
    #principled_bsdf.BSDF -> material_output.Surface
    tornasol.links.new(principled_bsdf.outputs[0], material_output.inputs[0])
    #texture_coordinate.Reflection -> vector_math.Vector
    tornasol.links.new(texture_coordinate.outputs[6], vector_math.inputs[1])
    #texture_coordinate.Normal -> vector_math.Vector
    tornasol.links.new(texture_coordinate.outputs[1], vector_math.inputs[0])
    #mix.Result -> mix_002.A
    tornasol.links.new(mix.outputs[2], mix_002.inputs[6])
    #mix_002.Result -> principled_bsdf.Base Color
    tornasol.links.new(mix_002.outputs[2], principled_bsdf.inputs[0])
    return tornasol

tornasol = tornasol_node_group()

