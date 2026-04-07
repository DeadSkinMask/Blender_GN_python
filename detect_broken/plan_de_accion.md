# PLAN DE ACCIÓN — Auditoría de archivos <mark>.blend</mark>
🎯 Objetivo
Detectar dependencias externas

Verificar rutas rotas

Identificar versiones

Preparar migración entre PCs sin perder referencias
---

## 1. 📁 Estructura base
```
project/
│
├── files.json          # tu inventario actual
├── results.json        # salida consolidada
├── scan.sh             # controlador bash
├── analyze.py          # script interno de Blender
├── detect_version.py   # scanner rápido (opcional)
```
---
## 2. 🔍 Fase 1 — Scanner rápido (opcional pero recomendado)

**Script:** <mark>detect_version.py</mark>

✔ No usa Blender

✔ Extrae versión real del archivo

Uso:

Filtrar archivos problemáticos antes de abrirlos

Detectar incompatibilidades
---

## 3. 🧠 Fase 2 — Análisis real con Blender
**Script:** <mark>analyze.py</mark>

---
## 4. 🖥️ Fase 3 — Controlador Bash
**Script:** <mark>scan.sh</mark>

---
## 5. ⚡ Buenas prácticas (crítico)
**✔ Siempre usar:**
```
-b --factory-startup

```

**✔ Procesar en serie**

NO paralelizar (evita saturación de RAM)

**✔ Agregar timeout (opcional)**

```
timeout 60s blender ...
```

**✔ Filtrar por cambios (recomendado)**


Solo reanalizar si cambió <mark>mtime</mark>

---

## 6. 🔄 Fase futura — Migración de rutas

Extensión del <mark>analyze.py</mark>:
```
bpy.ops.file.make_paths_relative()
# o
bpy.ops.file.make_paths_absolute()
```

Opcional:
```
bpy.ops.file.pack_all()
```

---

## 7. 🧩 Flujo completo
1.- Leer <mark>files.json</mark>

2.- (Opcional) detectar versión sin Blender

3.- Ejecutar <mark>scan.sh</mark>

4.- Generar <mark>results.json</mark>

5.- Revisar:

* archivos con <mark>missing</mark>
* rutas rotas

6.- Corregir / migrar

---
## 8. 🧠 Resultado esperado

Por cada <mark>.blend:</mark>

```
{
  "file": "model.blend",
  "blender_version": "4.1.0",
  "images": [...],
  "libraries": [...],
  "missing": [...]
}
```
---

## 9. 📌 Estado del sistema

✔ No depende de addons

✔ Escalable

✔ Compatible con pipeline GLB / assets

✔ Seguro (no modifica archivos si no lo indicas)