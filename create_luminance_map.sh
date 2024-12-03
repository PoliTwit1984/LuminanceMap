#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$SCRIPT_DIR/venv312/bin/activate"

# Run the Python script with all arguments passed to this script
python3 "$SCRIPT_DIR/lumap2.py" "$@"

# Deactivate the virtual environment
deactivate
