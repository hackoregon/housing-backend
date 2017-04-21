#! /bin/bash

echo "#################################################################################################################"
echo "Running scrub-proj.sh... remove all Docker containers and images"
echo "#################################################################################################################"

docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
