#!/bin/bash -e

BASEDIR="$(realpath "$(dirname "$0")/..")"

VERSION=$(<"$BASEDIR/VERSION")
PY_VERSION=$(python "$BASEDIR"/bin/python_versioning.py "$VERSION")

echo -e "\n\n=> Installing jupyter-ai-magics in development mode"
cd "$BASEDIR"/packages/jupyter-ai-magics || exit
pip install dist/jupyter_ai_magics-"$PY_VERSION".tar.gz

echo -e "\n\n=> Installing jupyter-ai in development mode"
cd "$BASEDIR"/packages/jupyter-ai || exit
pip install dist/jupyter_ai-"$PY_VERSION".tar.gz

echo -e "\n\n=> Installing intell-genai in development mode"
cd "$BASEDIR"/packages/intell-genai || exit
pip install dist/intell_genai-"$PY_VERSION".tar.gz

echo -e "\n\n=> Launching JupyterLab"
python  "$BASEDIR"/playground/jupyterlab_launcher.py