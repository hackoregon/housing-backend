#! /bin/bash

export PROJ_SETTINGS_DIR=backend # This sets up access for other scripts to the app's subdirectory
# ??? Troy, what's the right value here for DOCKER_IMAGE?
export DOCKER_IMAGE=housing-service  # This is used to identify the service being run by test-proj.sh

echo "##############################"
echo  LOCAL CONFIG SETTINGS
echo "##############################"
echo  DOCKER_IMAGE $DOCKER_IMAGE
echo  PROJ_SETTINGS_DIR $PROJ_SETTINGS_DIR
