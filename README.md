# shopping
1.Create a frist web on Docker.
```console
docker compose run web django-admin startproject shopping .
```
2.Down u Docker containers
```console
docker-compose down
```
3.Up u Docker containers
```console
docker-compose up -d
```
4.Into u Docker containers makemigrations & migrate
```console
python manage.py makemigrations
python manage.py migrate
```
