#! /bin/bash
docker-compose -f backend/docker-compose.yml run web py.test
