#!/bin/bash

echo "#################################################################################################################"
echo "Running test-entrypoint.sh..."
echo "#################################################################################################################"

export PATH=$PATH:~/.local/bin

#./bin/getconfig.sh
#python manage.py migrate --noinput
#python manage.py test --no-input

echo "Running database migrations..."
./bin/getconfig.sh
python manage.py makemigrations --no-input
python manage.py migrate --no-input

echo "Download raw CSV and load database tables..."
./start-dev-server.sh

py.test
