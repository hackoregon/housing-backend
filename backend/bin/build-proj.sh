#! /bin/bash

usage() { echo "Usage: $0 [-l] for a local build or [-t] for a travis build " 1>&2; exit 1; }

if [ $# == 0 ]; then usage; fi

echo  Running build-proj.sh...

while getopts ":lt" opt; do
    case "$opt" in
        l)
          echo  Running docker-compose build with local-docker-compose...
          docker-compose -f backend/local-docker-compose.yml build
          ;;
        t)
        echo  Running docker-compose build with travis-docker-compose...
          docker-compose -f backend/travis-docker-compose.yml build
          ;;
        *)
          usage
          ;;
    esac
done
