#!/bin/bash

# Notes:
# 1. This script populates the production environment with Project Lovelace data.
#    This is done by entrypoint.sh for the development environment.
# 2. This script should only be run when initially spinning up `docker-compose.prod.yml`.
# 3. This script should be run after `docker-compose.prod.yml` is up and running.
# 4. `lovelace_website.json` is the output of `django-admin dumpdata` from production.
# 5. Don't forget that production needs the `media` folder for user uploads!

echo "Migrating Django changes..."
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --no-input

echo "Populating Django database..."
docker-compose -f docker-compose.prod.yml exec django python manage.py loaddata lovelace_website.json

echo "Collecting static files..."
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic
