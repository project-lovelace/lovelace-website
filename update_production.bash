#!/bin/bash

git pull && \
docker pull projectlovelace/lovelace-engine && \
docker-compose -f docker-compose.prod.yml build && \
docker-compose -f docker-compose.prod.yml down && \
docker-compose -f docker-compose.prod.yml up --detach && \
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input
