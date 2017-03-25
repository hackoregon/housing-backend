#! /bin/bash
#docker-compose -f backend/docker-compose.yml run web py.test

usage() { echo "Usage: $0 [-l] for a local test or [-t] for a travis test " 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

echo  Running test_proj.sh...

# Run all configured unit tests inside the Docker container
while getopts ":lt" opt; do
    case "$opt" in
        l)
          docker-compose -f $PROJ_SETTINGS_DIR/local-docker-compose.yml build
          docker-compose -f $PROJ_SETTINGS_DIR/local-docker-compose.yml run \
          --entrypoint /code/bin/test-entrypoint.sh $DOCKER_IMAGE
          ;;
        t)
          # docker-compose -f $PROJ_SETTINGS_DIR/travis-docker-compose.yml build
          # docker-compose -f $PROJ_SETTINGS_DIR/travis-docker-compose.yml run \
          docker-compose -f backend/travis-docker-compose.yml build
          docker-compose -f backend/travis-docker-compose.yml run \
          --entrypoint /code/bin/test-entrypoint.sh $DOCKER_IMAGE
          ;;
        *)
          usage
          ;;
    esac
done