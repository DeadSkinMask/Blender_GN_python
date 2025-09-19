import bpy

# --- CONFIGURACIÓN ---
# Armature seleccionado
armature = bpy.context.object
if armature is None or armature.type != 'ARMATURE':
    raise Exception("Selecciona un Armature con animaciones")

# Factor de escala que deseas aplicar a las animaciones
# Por ejemplo, si tu armature está en escala 0.01, pon 0.01
scale_factor = 0.01

print(f"Escalando animaciones del armature '{armature.name}' por factor {scale_factor}")

# --- Función que reescala animaciones ---
def rescale_animation(action, scale_factor):
    for fcurve in action.fcurves:
        # Solo localización
        if fcurve.data_path.endswith("location"):
            for keyframe in fcurve.keyframe_points:
                keyframe.co[1] *= scale_factor
                keyframe.handle_left[1] *= scale_factor
                keyframe.handle_right[1] *= scale_factor

# --- Detectar acciones vinculadas al armature ---
actions_to_fix = set()

# Acción activa
if armature.animation_data and armature.animation_data.action:
    actions_to_fix.add(armature.animation_data.action)

# Actions en NLA tracks
if armature.animation_data and armature.animation_data.nla_tracks:
    for track in armature.animation_data.nla_tracks:
        for strip in track.strips:
            if strip.action:
                actions_to_fix.add(strip.action)

# --- Escalar animaciones ---
for action in actions_to_fix:
    rescale_animation(action, scale_factor)

print(f"{len(actions_to_fix)} acción(es) reescalada(s) con factor {scale_factor}")
