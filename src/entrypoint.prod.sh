#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    while ! nc -z $SQL_HOST $SQL_PORT; do
        echo "Waiting for postgres..."
        sleep 1
    done

    echo "PostgreSQL started"
fi

exec "$@"
