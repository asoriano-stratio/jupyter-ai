#!/bin/bash -e

BASEDIR="$(realpath "$(dirname "$0")/..")"
MODULES_FILE_NAME="release-modules"

if [ ! -f "$MODULES_FILE_NAME" ]; then
    echo "Error: $MODULES_FILE_NAME file not found"
    exit 1
fi

while IFS= read -r module; do
    cd "$BASEDIR"/"$module"
    python_module=$(echo "$module" | tr '-' '_')
    echo "Installing test dependencies for module $module ..."
    poetry install
    echo "Checking code format for module $module ..."
    poetry run black --check ./
    echo "Running pylint for module $module ..."
    poetry run pylint "$python_module" --exit-zero --msg-template="$module/{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint-report.txt
    echo "Running unit tests for module $module ..."
    poetry run pytest "--cov=$python_module" --cov-report "xml:pytest-coverage.xml"
done < $MODULES_FILE_NAME
