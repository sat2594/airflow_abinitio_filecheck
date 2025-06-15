from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='abinitio_file_check',
    default_args=default_args,
    description='Check if file exists and run Ab Initio graph every hour',
    schedule_interval='@hourly',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['abinitio', 'file_check']
) as dag:

    check_file = BashOperator(
        task_id='check_file_exists',
        bash_command='[ -f /path/to/watch/file.csv ] && echo "File exists." || echo "File not found."'
    )

    run_abinitio = BashOperator(
        task_id='run_abinitio_graph',
        bash_command='bash /opt/airflow/scripts/run_abinitio_graph.sh',
        trigger_rule='all_success'
    )

    check_file >> run_abinitio
