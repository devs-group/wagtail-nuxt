#!/bin/bash

function waitForPostgres() {
    echo "Waiting for postgres ..."
    python wait_for_postgres.py
}

function migrateTables() {
    echo "Migrating tables..."
    python manage.py makemigrations && python manage.py migrate --noinput
}

function loadStatics() {
    echo "Loading static files..."
    python manage.py collectstatic --noinput
}

function loadFixtures() {
  echo "Loading fixtures..."
  if [ -f fixtures.json ]; then
    python manage.py loaddata fixtures.json
  fi
}

function createSuperuser () {
    echo "Creating superuser..."
    local username="$1"
    local password="$2"
    python manage.py create_superuser $username $password
}


waitForPostgres
migrateTables
loadStatics
if [[ ${ENVIRONMENT} != "production" ]]; then
    createSuperuser "admin" "admin123"
    loadFixtures
    gunicorn --bind 0.0.0.0:8000 --reload --workers 3 --worker-class gevent --access-logfile - cms.wsgi:application
else
    gunicorn --bind 0.0.0.0:8000 --workers 3 --worker-class gevent --access-logfile - cms.wsgi:application
fi
