from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import python_operator
from airflow.utils.dates import days_ago

default_args = {
    "owner":"airflow",
    "depends_on_past": False,
    "start_date": datetime(2020,11,8),
    "email":["ibrahim@gmail.com"],
    "email_on_failure":False,
    "email_on_retry":False,
    "retries":2
}

dag = DAG(
    "my_test_dag",
    default_args=default_args,
    description="",
    schedule_interval=timetable(day=1),
)

def tryIt():
    print("hhhhh")
    
run_etl = python_operator(
    task_id="testing...?",
    python_callable= tryIt,
    dag=dag
)

run_etl