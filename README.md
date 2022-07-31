# Docker Airflow ETL project 

Hi! This is my first ETL project to learn more about Docker and Airflow. I made an effort to try to make this possible to run on someone else's machine as well. I haven't yet tested this works as intended, but I'll be updating the code accordingly. 
<br/>
Prerequisites are, that you have already installed Docker Desktop on your computer.

To get this code working on your machine you'll need to follow these steps. ("configuration" refers to the `docker-compose.yaml` file unless specified otherwise).

## Set up the Docker containers

1. Build an extended Airflow Docker image with the `Dockerfile`, and install additional packages listed in `requirements.txt`
```
docker build . --tag airflow-extended:latest
```

2. Initialize Airflow by running `airflow-init` script fount in the configuration (This step takes a little while to finish)
```
docker-compose up airflow-init
```

3. Start up the environment in detached mode (runs containers on the background and allows same terminal to be used)
```
docker-compose up -d 
```

<br/>

## Set up pgAdmin
1. In your browser, go to the address `localhost:5050` as configured under the `pgadmin` service

2. Log in with credentials set up in service `pgadmin`:
```
email: pgadmin4@pgadmin.org
password: admin
```

<br/>

3. Note, that before we can set up the database server, we need to find out first what is the IP address of our Postgres database service. In your terminal/command prompt window, input the following command:

```
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' local_pgdb
```

The output varies, but it looks like this: 
``` 
172.20.0.3
```

4. In pgAdmin UI Right-click on `Servers` in pgAdmin UI and choose `Register>Server...` <br/>
and input the following server information (square-brackets `[]` indicate the tab name under which the field is found)

```
[General]
Name: localhost

[Connection]
Host name / address: <Put IP from previous step here>
Port: 5432
Maintenance database: airflow
Username: airflow
Password: airflow
``` 

## Set up Airflow 

1. Go to `http://localhost:8080` as configured under `airflow-webserver` service

2. Log in with `AIRFLOW_WWW_USER` credentials configured in the environment variables of the `airflow-init` service:

```
Username: airflow
Password: airflow
```

3. Create a new connection in Airflow UI `Admin` dropdown menu with following parameters 

```
Connection id: postgres_airflow_worker
Connection Type: Postgres
Host: postgres
Schema: postgres
Login: airflow
Port: 5432
```

## Running the ETL tasks
We have now set up everything that is needed to run the Airflow tasks.

1. First, go to `DAGs` tab in Airflow UI and choose the `demo-etl` DAG (ignore the extra tutorial DAGs created by the Airflow image, I'll figure out later, how to get rid of them)

2. Click the DAG on if it's not already

3. Choose the `Graph` view on the view selection ribbon 

4. Click the play button on the right edge of the screen (it's on the same vertical level as the view selection ribbon you just clicked)

The tasks should now run and turn green, if successful.

<br/>

*Et Voilà*

<br/>

## Cleaning the environment

Clean the environment with the command (you'll need to start the instructions from the beginning after running this command)
```
docker-compose down --volumes --rmi all
``` 