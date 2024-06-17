# BUILD


```bash
VERSION="0.0.1"
docker build -t robertsilvatech/django-crud-pastelaria-devops:${VERSION} -t robertsilvatech/django-crud-pastelaria-devops:latest -f Dockerfile_sem_entrypoint .

docker push robertsilvatech/django-crud-pastelaria-devops:${VERSION} 
docker push robertsilvatech/django-crud-pastelaria-devops:latest

VERSION="0.0.2"
docker build -t robertsilvatech/django-crud-pastelaria-devops:${VERSION} -t robertsilvatech/django-crud-pastelaria-devops:latest .

```