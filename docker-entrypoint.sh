#!/bin/sh
set -e

until python manage.py migrate --noinput; do
	echo "Database is not ready; retrying migrations..."
	sleep 2
done
python manage.py collectstatic --noinput

exec "$@"
