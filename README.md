<a href="https://www.arkondata.com/">
    <img src="./img/logo.jpg" align="right" height="80">
</a>

# Arkon's Python Training

## Description
Python hands on training project. Looking to introduce new team members or anyone interested to the python 
programming language and the way it's used within the ArkonData team. 

You'll implement a web server exposing a GraphQL API to expose business retrieved from the INEGI's API and 
query them based on their location.

# https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/geolibs/#gdalbuild
# https://docs.djangoproject.com/en/3.2/ref/contrib/gis/model-api/

* [Concepts](https://github.com/Grupo-Abraxas/arkon-scalatraining#concepts)
* [Tools](https://github.com/Grupo-Abraxas/arkon-scalatraining#tools)
* [Libraries](https://github.com/Grupo-Abraxas/arkon-scalatraining#libraries)
* [Exercises](https://github.com/Grupo-Abraxas/arkon-scalatraining#exercises)
* [Basic commands](https://github.com/Grupo-Abraxas/arkon-scalatraining#basic-commands)
* [Requirements](https://github.com/Grupo-Abraxas/arkon-scalatraining#requirements)

## Concepts
- FP
    - [Functional Programming HOWTO](https://docs.python.org/es/3/howto/functional.html#functional-programming-howto)

## Books
- Coming soon

## Videos
- Coming soon

## Tools
- [Python]https://www.python.org/)
- [Code](https://code.visualstudio.com/)

## Libraries
- [Django](https://docs.djangoproject.com).
- [Geospatial libraries](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/geolibs/)
- [GeoDjango Model API](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/model-api/)
- [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
    - [GeoDjango](https://github.com/EverWinter23/graphene-gis)
    - [Testing API](https://docs.graphene-python.org/projects/django/en/latest/testing/)
- [Testing in Django](https://docs.djangoproject.com/en/3.2/topics/testing/): Python testing library.

## Exercises

## How to execute services and tests with docker-compose and docker
```
 docker-compose up -d

 // docker-compose
 docker-compose exec denue-api python denue/manage.py migrate 
 docker-compose exec denue-api python denue/manage.py test api.tests.tests_model_comercial_activity

 // docker
 docker exec -it arkon-scalatraining_denue-api_1 python denue/manage.py migrate
 docker exec -it arkon-scalatraining_denue-api_1 python denue/manage.py test api.tests.tests_model_comercial_activity
```

## Basic commands (Docker)

```
// create network
docker network create denue-net

// runing database
docker run -d --name denue-db -p 5432:5432 --env-file .env --net denue-net postgis/postgis

// build develop image 
docker build -t denue-dev .

// running container (Linux)
docker run -it -d --name denue-app --rm --volume $(pwd):/app --net denue-net denue-dev:latest

// running container (Windows PS)
docker run -it -d --name denue-app --rm --volume ${pwd}:/app --net denue-net denue-dev:latest

// python makemigrations
docker exec -it denue-app python denue/manage.py makemigrations api

// python all makemigrations
docker exec -it denue-app python denue/manage.py makemigrations

// python database migrate 
docker exec -it denue-app python denue/manage.py migrate api

// apply all migrates
docker exec -it denue-app python denue/manage.py migrate

// runing server Django
docker exec -it denue-app python denue/manage.py runserver

// runing test
docker exec -it denue-app python denue/manage.py test api.tests.tests_model_comercial_activity


// on bash...

// running container (bash Linux)
docker run -it --name denue-app --rm --volume $(pwd):/app --net denue-net denue-dev:latest bash

// running container (bash Windows PS)
docker run -it --name denue-app --rm --volume ${pwd}:/app --net denue-net denue-dev:latest bash

// python makemigrations
python denue/manage.py makemigrations api

// python database migrate 
python denue/manage.py migrate api

// runing server Django
python denue/manage.py runserver

// runing test
python denue/manage.py test api.tests.tests_model_comercial_activity

```

## Enviroment File
if the .env file is created in the app directory denue the python commands should be removed denue/
example:
```
python manage.py test api.tests.tests_model_comercial_activity
```
.env example
```
SECRET_KEY=your-secret-key
RENUE_API_KEY=your-denue-api=key
POSTGRES_ENGINE=django.contrib.gis.db.backends.postgis
POSTGRES_HOST=localhost
POSTGRES_NAME=postgres
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=your-db-password
POSTGRES_PORT=5432
DJANGO_DEBUG=True
```

## Requirements 
Implement a GraphQL API based on the given [schema](./schema.graphql) to expose the saved business and 
query them based on their location. The database to be used should be [PostgreSQL](www.postgresql.org) with the 
[PostGIS](http://postgis.net/) extension to power the georeferenced queries. To fill the database you'll have 
to implement a web scrapper to retrieve data from the INEGI's DENUE [API](https://www.inegi.org.mx/servicios/api_denue.html) 
and execute the `createShop` mutation defined on the implemented API.

The implemented API should comply the following rules: 
- On the `createShop` mutation 
    - The `activity`, `stratum` and `shopType` fields should search for existing records on the `Activity`, 
      `Stratum` and `ShopType` tables and insert only if there is no previous record.
