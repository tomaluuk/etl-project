import os
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.decorators import task


with DAG(
    'demo-etl',
    default_args={
        'depends_on_past': False,
        'email': ['luukkane@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
    },
    description='A demo ETL DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    @task.virtualenv(
        # "./requirements.txt"
        task_id='test2', requirements=["colorama==0.4.0"]
    )
    def callable_virtualenv():  # extract_municipality_popular_names_data_task():
        """
         Example function that will be performed in a virtual environment.

         Importing at the module level ensures that it will not attempt to import the
         library before it is installed.
         """
        from time import sleep

        from colorama import Back, Fore, Style

        print(Fore.RED + 'some red text')
        print(Back.GREEN + 'and with a green background')
        print(Style.DIM + 'and in dim text')
        print(Style.RESET_ALL)
        for _ in range(10):
            print(Style.DIM + 'Please wait...', flush=True)
            sleep(2)
        print('Finished')

    virtualenv_task = callable_virtualenv()
