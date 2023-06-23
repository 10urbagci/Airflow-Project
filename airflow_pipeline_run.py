from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from extract_data import run_extract_data,interval_map
from load_data import upload_file_to_storage

default_args = {
    'start_date': datetime(2023, 6, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'binance_dag_v4',
    default_args=default_args,
    description='My first Airflow DAG Project',
    schedule = None
)

extract_data = PythonOperator(
    task_id = 'extract_data_from_api',
    python_callable= run_extract_data,
    op_kwargs={'symbol': "BTCUSD", 'interval': interval_map['1h']},
    dag = dag
    
)

load_data = PythonOperator(
    task_id = 'load_data_to_bucket',
    python_callable=upload_file_to_storage,
    dag = dag
)

extract_data >> load_data
