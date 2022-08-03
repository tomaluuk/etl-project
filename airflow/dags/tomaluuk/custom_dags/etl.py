import os
from datetime import datetime, timedelta
from tomaluuk.extract import extract_source_data

from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    'demo-etl',
    default_args={
        'depends_on_past': False,
        'email': ['luukkane@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='A demo ETL DAG',
    template_searchpath='/opt/airflow/dags/tomaluuk',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    extract_source_data_task = PythonOperator(
        task_id='extract-source-data',
        python_callable=extract_source_data.main
    )

    create_tables_task = PostgresOperator(
        task_id="create-tables",
        postgres_conn_id='postgres_airflow_worker',
        sql="sql/create_tables.sql"
    )

    insert_data_task = PostgresOperator(
        task_id="insert-data",
        postgres_conn_id='postgres_airflow_worker',
        sql="sql/insert_data.sql"
    )

    extract_source_data_task >> create_tables_task
    create_tables_task >> insert_data_task
