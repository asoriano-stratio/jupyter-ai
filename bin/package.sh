#!/bin/bash -e

BASEDIR="$(realpath "$(dirname "$0")/..")"

#echo "=> Activating stratio-jupyter-ai conda environment"
#conda activate stratio-jupyter-ai

echo "=> Packaging jupyter-ai-magics"
cd "$BASEDIR"/packages/jupyter-ai-magics
python -m build

echo "=> Packaging jupyter-ai"
cd "$BASEDIR"/packages/jupyter-ai
python -m build

echo "=> Packaging intell-genai"
cd "$BASEDIR"/packages/intell-genai
python -m build