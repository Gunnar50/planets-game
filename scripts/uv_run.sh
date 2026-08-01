#!/bin/bash
#
# Execute a command using uv (after checking that the env has been setup)

# Set some failure conditions
set -o errexit   # Fail on any error
set -o pipefail  # Trace ERR through pipes
set -o errtrace  # Trace ERR through sub-shell commands

if type uv  > /dev/null 2>&1; then
  uv run --locked $@
else
  $@
fi
