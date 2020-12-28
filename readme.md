# CoCo - Code Collaboration

## What is CoCo?
This is a code collaboration platform for programmers to create, solve, and collaborate while learning.

## How to run the application?
Following these steps to run the application:

1. clone this repository: `git clone `
2. create .env files from the sample
3. build docker image and run container: `docker-compose up -d --build`
4. If it is the first time running, run the migrations: `docker-compose exec web python manage.py migrate`
5. create a superuser: `docker-compose exec web python manage.py createsuperuser --username <username> --email <email_address>`

## Check whether running
There are multiple ways to check whether the application is running. The most evident way of checking is actually going to the address of the application. Currently, the application is running on the following address:

`http://localhost:8000`

Another way to check if everything is running smoothly is to check the logs of the application. To check the logs, run the following command from the terminal:
```
docker-compose logs
```

You can also check the logs of a particular service. We currently have serviecs like: web, db and redis. The names of the services can be found in the `docker-compose` file. Run the following command to specify a service:
```
docker-compose logs -f <service_name>

# example: 
docker-compose logs -f web
```

## Known problems while running

### `database "coco_db_dev" does not exist`
If the Docker images were built successfully but in the logs, there was an error saying the database 'coco_db_dev' doesn't exist, then possibility is that the Host system is running another instance of postgreSQL. You need to stop that instance and clear the volume data before running the container again. Refer to this problem: https://stackoverflow.com/a/49770668/10031472

To solve the problem, do the following:

1. check the status of local postgres: `sudo service postgresql status`
2. stop the postgres: `sudo service postgresql stop`
3. make sure it is stopped: `sudo service postgresql status`
4. check the docker volumes: `docker volumes ls`
5. remove the particular volume: `docker volume rm coco_postgres_data`
