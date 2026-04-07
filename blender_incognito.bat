@echo off

REM === Configuración ===
set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender\blender.exe
set TEMP_CONFIG=C:\temp\blender_temp

REM === Crear carpeta temporal si no existe ===
if not exist "%TEMP_CONFIG%" (
    mkdir "%TEMP_CONFIG%"
)

REM === Lanzar Blender en modo incógnito ===
set BLENDER_USER_CONFIG=%TEMP_CONFIG%
"%BLENDER_PATH%" --factory-startup %*

REM === Limpiar variable (opcional) ===
set BLENDER_USER_CONFIG=
