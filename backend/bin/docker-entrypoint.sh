#!/bin/bash

# Start up command for the Docker image
echo "##############################"
echo  Running docker-entrypoint.sh...

# Necessary to pull the config file here because .dockerignore ignores the config file if it's downloaded to the container image
./bin/getconfig.sh

# If running locally apply migrations
if [ "$DEPLOY_TARGET" == "dev" ]; then
    echo -e "#####################################################"
    echo -e  RUNNING MIGRATIONS
    python manage.py makemigrations --no-input
    python manage.py migrate --no-input
fi
python manage.py collectstatic --no-input

# Fire up a lightweight frontend to host the Django endpoints - gunicorn was the default choice
# gevent used to address ELB/gunicorn issue here https://github.com/benoitc/gunicorn/issues/1194
#gunicorn backend.wsgi:application -b :8000 --worker-class 'gevent' --workers 3 --keep-alive 60
gunicorn backend.wsgi:application -b :8000 --worker-class 'gevent' --workers 1
