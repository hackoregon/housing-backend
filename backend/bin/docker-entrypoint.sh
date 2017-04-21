#!/bin/bash

# Start up command for the Docker image
echo "#################################################################################################################"
echo "Running docker-entrypoint.sh..."
echo "#################################################################################################################"

# Necessary to pull the config file here because .dockerignore ignores the config file if it's downloaded to the container image
./bin/getconfig.sh

# If running locally apply migrations
if [ "$DEPLOY_TARGET" == "dev" ]; then
    echo -e  docker-entrypoint.sh: Running Django migrations...
    python manage.py makemigrations --no-input
    python manage.py migrate --no-input
    echo -e docker-entrypoint.sh: Download raw CSV and load database...
    ./start-dev-server.sh
fi

python manage.py collectstatic --no-input

echo -e  docker-entrypoint.sh: Running gunicorn...
# Fire up a lightweight frontend to host the Django endpoints - gunicorn was the default choice
# gevent used to address ELB/gunicorn issue here https://github.com/benoitc/gunicorn/issues/1194
gunicorn backend.wsgi:application -b :8000 --worker-class 'gevent' --workers 1
