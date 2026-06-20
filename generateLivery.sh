#!/bin/bash
if [[ "$(uname -s)" == "Darwin" || "$(uname -s)" == "Linux" ]]; then
    /Applications/GIMP.app/Contents/MacOS/gimp-console-3  --quit --batch-interpreter python-fu-eval -b - << EOF
$(cat ./generator.py)
main()
EOF
else    
    /c/Program\ Files/GIMP\ 3/bin/gimp-console-3 --quit --batch-interpreter python-fu-eval -b - << EOF
$(cat ./generator.py)
main()
EOF
fi
