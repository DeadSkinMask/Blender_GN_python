import bpy
import json
import os

# Forzar la actualización del scene graph
bpy.context.view_layer.update()

# Obtén el gráfico de dependencias evaluado
depsgraph = bpy.context.evaluated_depsgraph_get()

# Obtén el objeto evaluado
evalA = bpy.context.object.evaluated_get(depsgraph)

# Almacena los datos de las instancias
instances_data = []

# Itera sobre todas las instancias en el scene graph
for inst in depsgraph.object_instances:
    # Filtra las instancias que pertenecen al objeto evaluado
    if inst.is_instance and inst.parent == evalA:
        # Obtén la matriz de transformación de la instancia
        matrix = inst.matrix_world

        # Extrae la posición, rotación y escala de la matriz
        position = tuple(matrix.translation)
        rotation = tuple(matrix.to_euler())
        scale = tuple(matrix.to_scale())

        # Guarda los datos en un diccionario
        instance_data = {
            'position': position,
            'rotation': rotation,
            'scale': scale
        }
        instances_data.append(instance_data)

# Obtén la ruta del archivo de Blender actual
blend_file_path = bpy.data.filepath
if blend_file_path:
    # Extrae el directorio donde se encuentra el archivo de Blender
    blend_dir = os.path.dirname(blend_file_path)
    # Define la ruta completa para el archivo JSON
    json_path = os.path.join(blend_dir, "instancias.json")
else:
    # Si el archivo de Blender no está guardado, usa la ruta temporal de Blender
    temp_dir = bpy.context.preferences.filepaths.temporary_directory
    if temp_dir:
        json_path = os.path.join(temp_dir, "instancias.json")
    else:
        # Si no hay ruta temporal configurada, usa una ruta por defecto
        json_path = "/ruta/por/defecto/instancias.json"

# Exporta los datos a un archivo JSON
with open(json_path, 'w') as f:
    json.dump(instances_data, f, indent=4)

print(f"Datos exportados exitosamente a {json_path}")
