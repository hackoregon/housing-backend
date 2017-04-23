#! /bin/bash
#docker-compose -f backend/docker-compose.yml run housing-service py.test

echo "#################################################################################################################"
echo "Running test-proj.sh... run all configured unit tests inside Docker container"
echo "#################################################################################################################"

usage() { echo "Usage: $0 [-l] for a local test or [-t] for a Travis CI test " 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

while getopts ":lt" opt; do
    case "$opt" in
        l)
          echo  "Running local test..."
          docker-compose -f backend/local-docker-compose.yml build
          docker-compose -f backend/local-docker-compose.yml run \
          --entrypoint /code/bin/test-entrypoint.sh housing-service
          ;;
        t)
          echo  "Running Travis CI test..."
          # docker-compose -f $PROJ_SETTINGS_DIR/travis-docker-compose.yml build
          # docker-compose -f $PROJ_SETTINGS_DIR/travis-docker-compose.yml run \
          docker-compose -f backend/travis-docker-compose.yml build
          docker-compose -f backend/travis-docker-compose.yml run \
          --entrypoint /code/bin/test-entrypoint.sh housing-service
          ;;
        *)
          usage
          ;;
    esac
done
