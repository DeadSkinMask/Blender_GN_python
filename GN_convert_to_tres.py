import bpy
import os
from mathutils import Matrix

def convert_matrix_to_godot_tres(blender_matrix: Matrix) -> str:
    """
    Convierte una matriz de Blender (Matrix) a una cadena de texto con el formato
    Transform3D de Godot, aplicando la conversión de coordenadas.
    Blender (X, Y, Z) -> Godot (X, Z, -Y)
    """
    # Ejes de la base de la matriz de Blender
    b_x = blender_matrix.col[0].to_3d()
    b_y = blender_matrix.col[1].to_3d()
    b_z = blender_matrix.col[2].to_3d()
    # Origen (posición) de la matriz de Blender
    b_o = blender_matrix.translation

    # Mapeo de ejes de Blender a Godot:
    # Godot X -> Blender X
    # Godot Y -> Blender Z
    # Godot Z -> Blender -Y
    
    # Aplicar la conversión a cada vector de la base y al origen
    g_x = (b_x.x, b_x.z, -b_x.y)
    g_y = (b_z.x, b_z.z, -b_z.y)
    g_z = (-b_y.x, -b_y.z, b_y.y)
    g_o = (b_o.x, b_o.z, -b_o.y)
    
    # Formatear la cadena para el constructor Transform3D(basis.x, basis.y, basis.z, origin)
    # Los números se formatean con varios decimales para mayor precisión.
    return (
        f"Transform3D(Vector3({g_x[0]:.6f}, {g_x[1]:.6f}, {g_x[2]:.6f}), "
        f"Vector3({g_y[0]:.6f}, {g_y[1]:.6f}, {g_y[2]:.6f}), "
        f"Vector3({g_z[0]:.6f}, {g_z[1]:.6f}, {g_z[2]:.6f}), "
        f"Vector3({g_o[0]:.6f}, {g_o[1]:.6f}, {g_o[2]:.6f}))"
    )

# --- INICIO DEL SCRIPT PRINCIPAL ---

# Forzar la actualización del scene graph
bpy.context.view_layer.update()

# Obtén el gráfico de dependencias evaluado
depsgraph = bpy.context.evaluated_depsgraph_get()

# Obtén el objeto activo evaluado (el que tiene la colección de instancias)
active_obj = bpy.context.object
if not active_obj:
    raise Exception("No hay un objeto activo seleccionado.")
eval_obj = active_obj.evaluated_get(depsgraph)

# Almacena las cadenas de texto de las transformaciones
transforms_tres_list = []

# Itera sobre todas las instancias en el scene graph
for inst in depsgraph.object_instances:
    # Filtra las instancias que son instancias reales y pertenecen al objeto activo
    if inst.is_instance and inst.parent and inst.parent.original == active_obj:
        matrix = inst.matrix_world
        
        # Convierte la matriz y la añade a la lista
        godot_transform_str = convert_matrix_to_godot_tres(matrix)
        transforms_tres_list.append(godot_transform_str)

# Define la ruta de salida del archivo .tres
blend_file_path = bpy.data.filepath
if not blend_file_path:
    raise Exception("Guarda tu archivo .blend antes de ejecutar el script.")

blend_dir = os.path.dirname(blend_file_path)
# El nombre del archivo .tres se basará en el nombre del objeto activo
output_filename = f"{active_obj.name}_instancias.tres"
tres_path = os.path.join(blend_dir, output_filename)

# --- Generación del contenido del archivo .tres ---

# Une todas las cadenas de transformación con una coma
transforms_content = ",\n\t".join(transforms_tres_list)

# Plantilla para el archivo .tres
# Asegúrate de que la ruta a "instance_transforms_resource.gd" es correcta en tu proyecto de Godot.
tres_template = f"""[gd_resource type="Resource" script_class="InstanceTransformsResource" load_steps=2 format=3]

[ext_resource type="Script" path="res://instance_transforms_resource.gd" id="1_abcde"]

[resource]
script = ExtResource("1_abcde")
transforms = [
	{transforms_content}
]
"""

# Exporta los datos al archivo .tres
with open(tres_path, 'w') as f:
    f.write(tres_template)

print(f"Datos de {len(transforms_tres_list)} instancias exportados exitosamente a {tres_path}")
