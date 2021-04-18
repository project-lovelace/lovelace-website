#!/bin/bash

# This might be dangerous... I once accidently flushed production lol.
# echo "Flushing Django database..."
# docker-compose exec django python manage.py flush --no-input

echo "Migrating Django changes..."
docker-compose exec django python manage.py migrate --no-input

echo "Populating Django database with problems..."
docker-compose exec django python manage.py loaddata lovelace_problems.json

echo "Collecting static files..."
docker-compose exec django python manage.py collectstatic --no-input
