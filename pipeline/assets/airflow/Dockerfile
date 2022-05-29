
FROM apache/airflow:2.2.4

USER root
WORKDIR /opt/airflow

ARG AIRFLOW_VERSION=2.2.4
ARG HADOOP_VERSION="3.2"
ARG SPARK_VERSION="3.1.2"


RUN apt-get update
RUN apt update
# RUN apt-get install openjdk-8-jdk -y
RUN apt-get install -y vim
RUN apt-get install -y wget
RUN apt-get install -y tar
RUN apt-get install -y python3-pip

# WORKDIR /src

# COPY src/requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ .


RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get install -y gnupg2 && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB9B1D8886F44E2A && \
    add-apt-repository "deb http://security.debian.org/debian-security stretch/updates main" && \ 
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    pip freeze && \
    java -version $$ \
    javac -version

# Setup JAVA_HOME 
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
RUN export JAVA_HOME


# RUN cd "/tmp" && \
#         wget --no-verbose "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
#         tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
#         mkdir -p "${SPARK_HOME}/bin" && \
#         mkdir -p "${SPARK_HOME}/assembly/target/scala-2.12/jars" && \
#         cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin/." "${SPARK_HOME}/bin/" && \
#         cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/." "${SPARK_HOME}/assembly/target/scala-2.12/jars/" && \
#         rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

RUN wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz && \
    tar -xvf spark-3.1.2-bin-hadoop3.2.tgz && \
    # mv spark-3.1.2-bin-hadoop3.2/ /opt/airflow && \
    rm -rf spark-3.1.2-bin-hadoop3.2.tgz

# # download jars
# # org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2
WORKDIR /opt/airflow/jars

RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.1.2/spark-sql-kafka-0-10_2.12-3.1.2.jar
    # mv spark-sql-kafka-0-10_2.12-3.1.2.jar /opt/airflow/jars

# # org.apache.kafka:kafka-clients:3.1.0
RUN wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.1.0/kafka-clients-3.1.0.jar
    # mv kafka-clients-3.1.0.jar /opt/airflow/jars

# # org.apache.spark:spark-token-provider-kafka-0-10_2.12:3.1.2
RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.1.2/spark-token-provider-kafka-0-10_2.12-3.1.2.jar
    # mv spark-token-provider-kafka-0-10_2.12-3.1.2.jar /opt/airflow/jars

RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.12/3.1.2/spark-streaming-kafka-0-10_2.12-3.1.2.jar
    # mv spark-streaming-kafka-0-10_2.12-3.1.2.jar /opt/airflow/jars

RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.12/3.2.1/spark-streaming-kafka-0-10_2.12-3.2.1.jar
    # mv spark-streaming-kafka-0-10_2.12-3.2.1.jar /opt/airflow/jars

RUN wget https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar
    # mv commons-pool2-2.11.1.jar /opt/airflow/jars

RUN wget https://repo1.maven.org/maven2/com/pygmalios/reactiveinflux-spark_2.11/1.4.0.10.0.4.1/reactiveinflux-spark_2.11-1.4.0.10.0.4.1.jar
    # mv reactiveinflux-spark_2.11-1.4.0.10.0.4.1.jar /opt/airflow/jars


RUN chown root:root -R /opt/airflow

# WORKDIR /opt/airflow





# COPY requirements.txt requirements.txt
# COPY ./requirements.txt .

COPY requirements.txt /tmp
WORKDIR /tmp
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir apache-airflow-providers-docker
RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN apt install -r requirements.txt
RUN pip install apache-airflow-providers-docker
FROM python:3.8-slim-buster



# ###### GIT 에서 퍼온 코드 #######

# ### 여기 ###
# COPY entrypoint.sh /entrypoint.sh
# COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow/airflow.cfg
# #### ! ###


# ###############################
# ## SPARK files and variables
# ###############################
# ENV SPARK_HOME /usr/local/spark

# # Spark submit binaries and jars (Spark binaries must be the same version of spark cluster)
# # RUN cd "/tmp" && \
#         wget --no-verbose "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
#         tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
#         mkdir -p "${SPARK_HOME}/bin" && \
#         mkdir -p "${SPARK_HOME}/assembly/target/scala-2.12/jars" && \
#         cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin/." "${SPARK_HOME}/bin/" && \
#         cp -a "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/." "${SPARK_HOME}/assembly/target/scala-2.12/jars/" && \
#         rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

# # Create SPARK_HOME env var
# RUN export SPARK_HOME
# ENV PATH $PATH:/usr/local/spark/bin
# ###############################
# ## Finish SPARK files and variables
# ###############################

# RUN chown -R airflow: ${AIRFLOW_HOME}
# RUN chmod +x entrypoint.sh

# #### 여기 #####
# USER airflow
# WORKDIR ${AIRFLOW_HOME}
# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["webserver"] # set default arg for entrypoint