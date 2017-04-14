#!/bin/bash

echo  Running docker-entrypoint.sh...
export DEPLOY_TARGET=dev # it's always dev on your local machine
./bin/getconfig.sh # Necessary to pull the config file here because .dockerignore ignores the config file if it's downloaded to the container image

# Disabled the migrate step to bring the container startup time down to acceptable levels
#python manage.py migrate --no-input
python manage.py collectstatic --no-input

# Fire up a lightweight frontend to host the Django endpoints - gunicorn was the default choice
gunicorn backend.wsgi:application -b :8000
