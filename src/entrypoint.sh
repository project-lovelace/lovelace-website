#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    while ! nc -z $SQL_HOST $SQL_PORT; do
        echo "Waiting for postgres..."
        sleep 1
    done

    echo "PostgreSQL started"
fi

# We want to do this manually via
# $ docker-compose exec web python manage.py flush --no-input
# $ docker-compose exec web python manage.py migrate
echo "Flushing Django database..."
python manage.py flush --no-input

echo "Migrating Django changes..."
python manage.py migrate

echo "Loading Django data..."
python manage.py loaddata lovelace_website.json

exec "$@"

