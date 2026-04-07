#!/bin/bash

BLENDER="/ruta/a/blender"
SCRIPT="analyze.py"
INPUT="files.json"
OUTPUT="results.json"

echo "[" > $OUTPUT

FIRST=1

jq -r '.files[].path' "$INPUT" | while read file; do
    echo "Procesando: $file"

    RESULT=$($BLENDER -b --factory-startup "$file" \
        --python "$SCRIPT" \
        -- "$file" 2>/dev/null)

    if [ -n "$RESULT" ]; then
        if [ $FIRST -eq 0 ]; then
            echo "," >> $OUTPUT
        fi
        echo "$RESULT" >> $OUTPUT
        FIRST=0
    fi

    # evitar saturación
    sleep 0.3
done

echo "]" >> $OUTPUT
