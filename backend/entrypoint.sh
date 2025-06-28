#!/bin/bash

echo "Running migrations..."
pipenv run flask db upgrade

echo "Seeding DB..."
pipenv run flask seed all

echo "Starting Flask dev server..."
pipenv run gunicorn -b 0.0.0.0:5000 application:application
