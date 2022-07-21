# 연습 DAG
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
# DAG - dag를 정의하기 위함
# operators - 실제 연산(실행)을 하기 위해 필요한 operators들을 불러오기 위함

# args = 정해지지 않은 수의 (일반)파라미터 
# default_args = default로 제공하는 파라미터의 집합
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 18),
    'retries': 0
}

dag = DAG(
    dag_id = 'Test_DAG_1',
    description = 'DAG_1_description',
    default_args= default_args,
    catchup = False,
    schedule_interval= '*/1 * * * *') #1분마다 interval

start = DummyOperator(
    task_id = 'DAG_1_start',
    dag = dag
)

end = DummyOperator(
    task_id = 'DAG_1_end',
    dag = dag
)

start >> end

