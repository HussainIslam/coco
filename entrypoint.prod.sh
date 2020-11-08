#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! pg_isready -h ${DB_HOST} -p ${DB_PORT} >/dev/null 2>/dev/null; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

exec "$@"