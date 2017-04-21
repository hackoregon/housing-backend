#!/bin/bash
# Make sure data is only loaded on first start
if [ ! -d /data ]; then
  echo "#################################################################################################################"
  echo "Running start-dev-server.sh... download CSV data, migrate the database, and load"
  echo "#################################################################################################################"
  echo "start-dev-server.sh: Downloading data..."
  mkdir /data
  wget \
    -O /data/SoHAffordabilityDatabyNeighborhoodUpload.csv \
    https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv
  echo "start-dev-server.sh: Migrating database..."
  while ! ./manage.py migrate >> /dev/null 2>&1 ; do
    sleep 1
  done
  echo "start-dev-server.sh: Loading data..."
  ./manage.py shell --command="import housing_backend.loader"
fi
#./manage.py collectstatic --noinput
#gunicorn backend.wsgi:application -b :8000
