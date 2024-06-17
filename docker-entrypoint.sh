#!/usr/bin/env bash

if [ ! -z ${DEPLOY_DB} ] && $DEPLOY_DB; then
    echo "Create superuser and loaddata"
    python manage.py makemigrations && \
    python manage.py migrate && \
    export DJANGO_SUPERUSER_PASSWORD=djangoadmin;python manage.py createsuperuser --noinput --username admin --email contato@robertsilva.com.br && \
    python manage.py runserver 0.0.0.0:8000      
else
    echo "Environment not defined at $DEPLOY_DB or is False";
    echo "Do makemigrations and migrate"
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
fi