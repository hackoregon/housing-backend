#! /bin/bash

# Declare config file for de-duplication
export CONFIG_FILE='project_config.py' # with some work, env.sh could alternatively be used

# Get Configuration
echo "#################################################################################################################"
echo "Running getconfig.sh..."
echo "#################################################################################################################"
echo  "getconfig.sh: PROJ_SETTINGS_DIR=" $PROJ_SETTINGS_DIR
echo  "getconfig.sh: DEPLOY_TARGET=" $DEPLOY_TARGET
echo  "getconfig.sh: CONFIG_BUCKET=" $CONFIG_BUCKET

if [ "$DEPLOY_TARGET" == "dev" ]; then
    echo -e  USING LOCAL CONFIG - MAKE SURE YOU HAVE A LOCAL CONFIG FILE: $CONFIG_FILE
else
    echo  getconfig.sh: CONFIG_BUCKET= $CONFIG_BUCKET
    echo  getconfig.sh: DEPLOY_TARGET= $DEPLOY_TARGET

    export PATH=$PATH:~/.local/bin # necessary to help locate the awscli binaries which are pip installed --user
    aws s3 cp \
          s3://$CONFIG_BUCKET/$DEPLOY_TARGET/$CONFIG_FILE \
          ./backend/backend/$CONFIG_FILE;
    ls -l ./backend/backend

fi
