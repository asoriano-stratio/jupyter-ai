#!/bin/bash -e

BASEDIR="$(realpath "$(dirname "$0")/..")"

echo -e "=> Un-installing jupyter-ai-magics in development mode"
cd "$BASEDIR"/packages/jupyter-ai-magics || exit
pip uninstall -y jupyter_ai_magics

echo -e "\n\n=> Un-installing jupyter-ai in development mode"
cd "$BASEDIR"/packages/jupyter-ai || exit
pip uninstall -y jupyter_ai

echo -e "\n\n=> Un-installing intell-genai in development mode"
cd "$BASEDIR"/packages/intell-genai || exit
pip uninstall -y intell_genai