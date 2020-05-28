#!/bin/bash -ex
service nginx start
python manage.py migrate --noinput --settings=aclabs.settings
python manage.py collectstatic --noinput --settings=aclabs.settings

gunicorn aclabs.wsgi:application --config configuration/gunicorn.conf.py
