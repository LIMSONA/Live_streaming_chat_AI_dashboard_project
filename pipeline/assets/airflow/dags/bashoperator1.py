# 연습 DAG
from datetime import datetime
from importlib import import_module
import os
from airflow import DAG
from airflow.operators.bash import BashOperator

# default_args = {
#     'owner': 'gahee',
#     'depends_on_past': False,
#     'start_date': datetime(2022, 5, 25)
#     # ,'retries': 0
# } 
 

args = {
    'owner': 'gahee',
    'start_date': datetime(2022, 5, 20)
} 

dag = DAG(
    'SUBMIT-TEST1',  # DAG id
    default_args = args,  # 언제부터 DAG이 시작되는가
    schedule_interval='*/3 * * * *',  # 3초마다 실행
    catchup=False)

# shell 경로 
create_command = "../../spark/spark.sh"
create_command2 = "sh /spark/spark.sh"



#### 1번
run_this = BashOperator(
    task_id='TEST1',
    bash_command=create_command,
    dag=dag,
)
# [END howto_operator_bash]

# if __name__ == "__main__":
#     dag.cli()


#### 2번
run_this2 = BashOperator(
    task_id="TEST2",
    # "scripts" folder is under "/usr/local/airflow/dags"
    bash_command=create_command2,
    dag=dag,
)


### 3번
create_command3 = """
echo 'ttttteeeeeesssssttttt';
echo 'Welcome';"""


run_this3 = BashOperator(
    task_id='TEST3',
    bash_command=create_command3,
    dag=dag,
)


