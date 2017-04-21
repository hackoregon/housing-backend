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
fi

if [ ! -d /data ]; then
  echo "docker-entrypoint.sh: Downloading data..."
  mkdir /data
  wget \
    -O /data/SoHAffordabilityDatabyNeighborhoodUpload.csv \
    https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv
  echo "docker-entrypoint.sh: Migrating database..."
  while ! ./manage.py migrate >> /dev/null 2>&1 ; do
    sleep 1
  done
  echo "docker-entrypoint.sh: Loading data..."
  ./manage.py shell --command="import housing_backend.loader"
fi

python manage.py collectstatic --no-input

echo -e  docker-entrypoint.sh: Running gunicorn...
# Fire up a lightweight frontend to host the Django endpoints - gunicorn was the default choice
# gevent used to address ELB/gunicorn issue here https://github.com/benoitc/gunicorn/issues/1194
#gunicorn backend.wsgi:application -b :8000 --worker-class 'gevent' --workers 3 --keep-alive 60
gunicorn backend.wsgi:application -b :8000 --worker-class 'gevent' --workers 1
