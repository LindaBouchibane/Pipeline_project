from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('credit_etl_dag', start_date=datetime(2024, 1, 1), schedule_interval=None, catchup=False) as dag:

    extract = BashOperator(
        task_id='extract_data',
        bash_command='python /app/extract/download_data.py'
    )

    transform = BashOperator(
        task_id='transform_data',
        bash_command='python /app/transform/clean_transform.py'
    )

    test = BashOperator(
        task_id='test_data',
        bash_command='pytest /app/tests/test_pipeline.py'
    )

    load_pg = BashOperator(
        task_id='load_postgres',
        bash_command='python /app/load/load_to_postgres.py'
    )

    load_mysql = BashOperator(
        task_id='load_mysql',
        bash_command='python /app/load/load_to_mysql.py'
    )

    extract >> transform >> test >> [load_pg, load_mysql]