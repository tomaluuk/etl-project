import os
from datetime import datetime, timedelta
from tomaluuk.extract import extract_municipality_popular_names_data

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.decorators import task

# Operators; we need this to operate!
#from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
#from airflow.providers.postgres.operators.postgres import PostgresOperator

#DATA_FILES_PATH = "./data/"
#DATA_FILES = os.listdir(DATA_FILES_PATH)

with DAG(
    'demo-etl',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['luukkane@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='A demo ETL DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # @task.virtualenv(task_id='test', requirements=["fastparquet", "pandas"])
    extract_municipality_popular_names_data_task = PythonVirtualenvOperator(
        python_callable=extract_municipality_popular_names_data
    )
    # @task.virtualenv(
    #    # "./requirements.txt"
    #    task_id='test2', requirements=["colorama==0.4.0"]
    # )
    # def callable_virtualenv():  # extract_municipality_popular_names_data_task():
    #    """
    #     Example function that will be performed in a virtual environment.
#
    #     Importing at the module level ensures that it will not attempt to import the
    #     library before it is installed.
    #     """
    #    from time import sleep
#
    #    from colorama import Back, Fore, Style
#
    #    print(Fore.RED + 'some red text')
    #    print(Back.GREEN + 'and with a green background')
    #    print(Style.DIM + 'and in dim text')
    #    print(Style.RESET_ALL)
    #    for _ in range(10):
    #        print(Style.DIM + 'Please wait...', flush=True)
    #        sleep(2)
    #    print('Finished')
#
    #virtualenv_task = callable_virtualenv()

    # create_tables_task = PostgresOperator(
    #    task_id="create_municipality_table",
    #    postgres_conn_id="sql_qlchemy_conn",
    #    sql="sql/employees_schema.sql"
    # )
