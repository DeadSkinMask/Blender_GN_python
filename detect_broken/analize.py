import bpy
import sys
import json
import os

argv = sys.argv
argv = argv[argv.index("--") + 1:]
filepath = argv[0]

data = {
    "file": filepath,
    "blender_version": bpy.app.version_string,
    "images": [],
    "libraries": [],
    "missing": []
}

# imágenes
for img in bpy.data.images:
    if img.filepath:
        path = bpy.path.abspath(img.filepath)
        data["images"].append(path)
        if not os.path.exists(path):
            data["missing"].append(path)

# librerías linkeadas
for lib in bpy.data.libraries:
    path = bpy.path.abspath(lib.filepath)
    data["libraries"].append(path)
    if not os.path.exists(path):
        data["missing"].append(path)

print(json.dumps(data))
