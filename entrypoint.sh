#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! pg_isready -h ${DB_HOST} -p ${DB_PORT} >/dev/null 2>/dev/null; do
      sleep 10
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"