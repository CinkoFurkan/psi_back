#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build process completed successfully."
