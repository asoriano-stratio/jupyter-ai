#!/bin/bash -e

BASEDIR="$(realpath "$(dirname "$0")/..")"

echo "Cleaning .yarn directory"
rm -rf "$BASEDIR"/.yarn

echo "Cleaning /dist directory"
rm -rf "$BASEDIR"/dist

echo "Cleaning /node_modules directory"
rm -rf "$BASEDIR"/node_modules

echo "Cleaning /playground/config.py"
rm -rf "$BASEDIR"/playground/config.py

echo "Cleaning /packages/jupyter-ai/lib"
rm -rf "$BASEDIR"/packages/jupyter-ai/lib

echo "Cleaning /packages/jupyter-ai/tsconfig.tsbuildinfo"
rm -rf "$BASEDIR"/packages/jupyter-ai/tsconfig.tsbuildinfo

echo "Cleaning /packages/jupyter-ai/jupyter_ai/labextension"
rm -rf "$BASEDIR"/packages/jupyter-ai/jupyter_ai/labextension

echo "Cleaning /packages/jupyter-ai/jupyter_ai/_version.py"
rm -rf "$BASEDIR"/packages/jupyter-ai/jupyter_ai/_version.py

echo "Cleaning /packages/jupyter-ai-magics/jupyter_ai_magics/_version.py"
rm -rf "$BASEDIR"/packages/jupyter-ai-magics/jupyter_ai_magics/_version.py

echo "Cleaning /packages/jupyter-ai/dist"
rm -rf "$BASEDIR"/packages/jupyter-ai/dist

echo "Cleaning /packages/jupyter-ai-magics/dist"
rm -rf "$BASEDIR"/packages/jupyter-ai-magics/dist

echo "Cleaning /packages/intell-genai/dist"
rm -rf "$BASEDIR"/packages/intell-genai/dist

echo "Cleaning /packages/intell-genai/intell_genai.egg-info"
rm -rf "$BASEDIR"/packages/intell-genai/intell_genai.egg-info