# pip install apache-airflow-providers-apache-spark
# pip install apache-airflow-providers-apach
# import airflow
from airflow.models import DAG
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow import providers_manager
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

from datetime import datetime, timedelta

# -- coding: utf-8 --

from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}
dag = DAG(
    dag_id='my_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    dagrun_timeout=timedelta(minutes=60),
    tags=['spark']
)
templated_bash_command = """
    spark-submit \
    --class my_class \
    --master spark://spark-master:17077 \
    --executor-cores 2 \
    --executor-memory 2g \
    my_first.jar
"""
hook = SSHHook(
    ssh_conn_id='ssh_default',
    remote_host='spark-master',
    username='username',
    key_file='~/.ssh/id_rsa'
)
run_ssh = SSHOperator(
    task_id='spark_submit_task',
    ssh_hook=hook,
    command=templated_bash_command,
    dag=dag
)
run_ssh