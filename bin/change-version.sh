#!/bin/bash -e

BASEDIR="$(realpath "$(dirname "$0")/..")"

if [ -z "$1" ]; then
    VERSION=$(<"$BASEDIR/VERSION")
else
    VERSION=$1
fi

# MVN version to python version
PY_VERSION=$(python "$BASEDIR"/bin/python_versioning.py "$VERSION")

echo "Replacing package version to $VERSION (mvn) | $PY_VERSION (python)"

echo "=> Changing version in jupyter-ai-magics"
cd "$BASEDIR"/packages/jupyter-ai-magics
hatch version "$PY_VERSION"

echo "=> Changing version in  jupyter-ai"
cd "$BASEDIR"/packages/jupyter-ai
hatch version "$PY_VERSION"







