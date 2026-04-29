#!/bin/bash

# 1. Define the absolute path to the project root
PROJECT_ROOT=$(pwd)

# 2. Add the source directory to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$PROJECT_ROOT/src/project_01"

# 3. Run pytest using the module flag
python3 -m pytest "$@"