@echo off
cd /d "%~dp0"

"C:\Program Files\GIMP 3\bin\gimp-console-3.exe" ^
    --no-interface ^
    --quit ^
    --batch-interpreter=python-fu-eval ^
    -b "exec(open('generator.py').read()); main()"