from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 30),
    'email': ['takintola98@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'extract_49ers_defensive_stats_2024',
    default_args=default_args,
    description='A simple DAG to extract relevant 49er defensive stats every week',
    schedule=timedelta(weeks=1),
)

run_script = BashOperator(
    task_id='run_extract_script',
    bash_command='python /c:/Users/User/OneDrive/Desktop/Data Engineering/NFLStatsPipeline/nflstatspipeline/extract_49ers_defensive_stats_2024.py',
    dag=dag,
)

run_script