#!/bin/bash
#
# Update uv dependencies for a service.

# Set some failure conditions
set -o errexit   # Fail on any error
set -o pipefail  # Trace ERR through pipes
set -o errtrace  # Trace ERR through sub-shell commands

echo "Updating dependencies..."
uv lock --upgrade

echo "Generating requirements.txt file..."
uv export --no-dev > requirements.txt
uv export > requirements-dev.txt
