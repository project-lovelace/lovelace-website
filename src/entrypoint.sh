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

echo "Populating Django database..."
python manage.py loaddata lovelace_django_dumpdata.json

echo "Collecting static files..."
python manage.py collectstatic

exec "$@"
