#!/bin/bash

set -e

if [ "$DEBUG" = "False" ]; then
    echo "Collecting static files..."
    if python /app/manage.py collectstatic --no-input; then
        echo "Static files collected successfully."
    else
        echo "Failed to collect static files!" >&2
        exit 1
    fi
else
    echo "DEBUG is True, skipping static file collection."
fi

echo "Starting database migrations..."
if python /app/manage.py migrate --no-input; then
    echo "Database migrations completed successfully."
else
    echo "Database migrations failed!" >&2
    exit 1
fi

echo "Starting the Django server..."

poetry run python /app/manage.py runserver 0.0.0.0:${APP_PORT}
