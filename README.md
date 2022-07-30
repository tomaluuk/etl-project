# Docker Airflow ETL project 

Hi! This is my first ETL project to learn more about Docker and Airflow. To get this code working on your machine you'll need to do a few commands.

1. Build an extended Airflow Docker image with additional packages (listed in `requirements.txt`)
```
docker build . --tag airflow-extended:latest
```

2. Initialize Airflow by running `airflow-init` script found in `docker-compose.yml`
```
docker-compose up airflow-init
```

3. Start up the environment in detached mode (runs containers on the background and allows same terminal to be used)
```
docker-compose up -d 
```

<br/>

## Cleaning the environment

Clean the environment with the command
```
docker-compose down --volumes --rmi all
``` 