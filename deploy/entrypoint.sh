#!/bin/sh
set -e

# pindah ke folder yang berisi manage.py
cd /app

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 2
