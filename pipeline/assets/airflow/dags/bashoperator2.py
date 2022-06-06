from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
        'owner': 'gahee', 
        'catchup': False,
        'execution_자timeout': timedelta(hours=6),
        'depends_on_past': False,
    }

dag = DAG(
    'sparkspark',
    default_args = default_args,
    description = "spark submit 테스트 중",
    schedule_interval = "@once",
    start_date = days_ago(3),
    tags = ['daily'],
    max_active_runs=3,
    concurrency=1
)

a = BashOperator(
    task_id='AAAAA',
    bash_command='echo hello I am A',
    dag=dag)

b = BashOperator(
    task_id='BBBBB',
    bash_command='echo hello I am B',
    dag=dag)
    
c = BashOperator(
    task_id='CCCCC',
    bash_command = '/opt/airflow/dags/spark.sh '
    #, bash_command='echo "테스트입니다~!" >> /opt/airflow/dags/spark-sh-text.txt'
    #, dag=dag
)

c << b << a
# a << b << c