

from airflow import DAG
from airflow.models import dag
from airflow.operators import SparkSubmitOperator
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperdockator
# from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

from airflow.operators.bash import BashOperator
from airflow.operators import python_operator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta





# file_path = "/opt/airflow/airflow.cfg"
# spark_app_name = "spark_submit_test1"


# spark_master = "spark://spark-master:17077"



default_args = {
    'owner': 'gahee',
    'depends_on_past': False,
    'start_date': datetime(2022, 5, 25)
    # ,'retries': 0
}


dag = DAG(
    dag_id = "spark-test1",
    description = "spark-test1_description",
    default_args = default_args,
    catchup = False,
    schedule_interval = '*/1 * * * *'
)


start = DummyOperator(
    task_id = 'spark-test1_start',
    dag = dag
)


#####
submit_job = SparkSubmitOperator(
    application="/spark/streamingspark.py", #실행하고자 하는 streamingspark path
    conf= "/spark/conf/metrics.properties",
    task_id="submit_job",
	conn_id= 'spark_default',
    name= "gahee_submit_job",
    jars =  "spark-sql-kafka-0-10_2.12-3.2.1.jar" ,
    spark_binary=None
)
#####

# (application='', conf=None, conn_id='spark_default', files=None, 
#  py_files=None, archives=None, driver_class_path=None, jars=None, java_class=None,
#  packages=None, exclude_packages=None, repositories=None, total_executor_cores=None,
#  executor_cores=None, proxy_user=None, name='airflow-spark', num_executors=None, status_poll_interval=1,
#  application_args=None, env_vars=None, verbose=False, spark_binary=None, *args, **kwargs)


end = DummyOperator(
    task_id = 'spark-test1_end',
    dag = dag
)

# start >> submit_job >> end
start >> end