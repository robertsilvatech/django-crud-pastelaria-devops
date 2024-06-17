# Este dockerfile sem utilizar o entrypoint é proposital para explicar na prática o funcionamento do entrypoint.
# No caso desta aplicação o entrypoint irá fazer o makemigrations e migrate do Django.

FROM python:3.12-slim

COPY requirements.txt /
RUN pip install -U pip && pip install -r requirements.txt
COPY manage.py /app/
COPY ./pastelaria_devops /app/pastelaria_devops
COPY --chmod=777 docker-entrypoint.sh /app/docker-entrypoint.sh

WORKDIR /app

EXPOSE 8000

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]