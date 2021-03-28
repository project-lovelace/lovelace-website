#!/bin/bash

git pull
docker pull projectlovelace/lovelace-engine
docker-compose build
docker-compose down
docker-compose up --detach
docker-compose exec django python manage.py collectstatic --no-input
