#! /bin/bash

echo "#################################################################################################################"
echo "Running start-proj.sh... start the Docker containers for services"
echo "#################################################################################################################"

usage() { echo "Usage: $0 [-l] for a local build or [-t] for a travis build " 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

# PURPOSE: used to launch the Django app inside the Docker container
# Can be used on local developer machine; if used in Travis build, will fail the build after 10min timeout

# Builds and launches the Docker container to be run in daemon mode - requires [CTRL]-C to stop the container
while getopts ":lt" opt; do
    case "$opt" in
        l)
          # This is an unfortunate workaround to the subdirectory that is used to contain all app code
          echo -e "Running with local-docker-compose.yml..."
          docker-compose -f backend/local-docker-compose.yml up --build
          ;;
        t)
        echo -e "Running with travis-docker-compose.yml..."
          docker-compose -f backend/travis-docker-compose.yml up
          ;;
        *)
          usage
          ;;
    esac
done
