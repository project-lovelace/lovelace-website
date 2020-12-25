#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    while ! nc -z $SQL_HOST $SQL_PORT; do
        echo "Waiting for postgres..."
        sleep 1
    done

    echo "PostgreSQL started"
fi

echo "Flushing Django database..."
python manage.py flush --no-input

echo "Migrating Django changes..."
python manage.py migrate --no-input

echo "Loading Django data..."
python manage.py loaddata lovelace_website.json

exec "$@"
