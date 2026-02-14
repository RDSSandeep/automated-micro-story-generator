#!/bin/bash
# Create source code zip for Configuration Management Report submission.
# Excludes .env (secrets), .venv, .git, __pycache__, etc.
# Run from project root: ./create_submission_zip.sh

set -e
cd "$(dirname "$0")"
ZIP_NAME="automated-micro-story-generator-source.zip"
zip -r "$ZIP_NAME" . \
  -x "*.git*" \
  -x "*.venv*" \
  -x "*.env" \
  -x "*__pycache__*" \
  -x "*.pyc" \
  -x "*.pytest_cache*" \
  -x "*.cursor*" \
  -x "*.DS_Store" \
  -x "test_results.txt"
echo "Created $ZIP_NAME"
echo "Submit this file along with the Configuration Management Report."
