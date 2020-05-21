#!/bin/bash -ex
service nginx start
gunicorn aclabs.wsgi:application --config configuration/gunicorn.conf.py
