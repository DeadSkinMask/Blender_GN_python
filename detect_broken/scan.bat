@echo off
setlocal enabledelayedexpansion

REM === CONFIGURACIÓN ===
set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender\blender.exe
set TEMP_CONFIG=C:\temp\blender_temp
set SCRIPT=analyze.py
set INPUT=files.json
set OUTPUT=results.json

REM === Validaciones ===
if not exist "%BLENDER_PATH%" (
    echo ERROR: Blender no encontrado
    exit /b 1
)

if not exist "%SCRIPT%" (
    echo ERROR: analyze.py no encontrado
    exit /b 1
)

if not exist "%INPUT%" (
    echo ERROR: files.json no encontrado
    exit /b 1
)

REM === Crear entorno aislado ===
if not exist "%TEMP_CONFIG%" (
    mkdir "%TEMP_CONFIG%"
)

REM === Inicializar salida JSON ===
echo [ > "%OUTPUT%"
set FIRST=1

REM === Iterar archivos desde JSON usando PowerShell ===
for /f "usebackq delims=" %%F in (`powershell -NoProfile -Command "(Get-Content '%INPUT%' | ConvertFrom-Json).files | ForEach-Object { $_.path }"`) do (

    set FILE=%%F
    echo Procesando: !FILE!

    REM === Ejecutar Blender en modo incógnito ===
    set BLENDER_USER_CONFIG=%TEMP_CONFIG%

    for /f "usebackq delims=" %%R in (`"%BLENDER_PATH%" -b --factory-startup "!FILE!" --python "%SCRIPT%" -- "!FILE!" 2^>nul`) do (
        
        if "!FIRST!"=="1" (
            echo %%R >> "%OUTPUT%"
            set FIRST=0
        ) else (
            echo ,%%R >> "%OUTPUT%"
        )
    )

    REM === Pequeña pausa para estabilidad ===
    timeout /t 1 >nul
)

REM === Cerrar JSON ===
echo ] >> "%OUTPUT%"

echo.
echo === ANALISIS COMPLETADO ===
echo Resultado: %OUTPUT%

endlocal
