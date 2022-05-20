FROM nvidia/cuda:11.4.0-cudnn8-runtime-ubuntu18.04

RUN apt update
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*
RUN apt install -y vim 
RUN apt install -y wget
RUN apt install -y tar
RUN apt install -y mlocate
RUN apt install -y net-tools iputils-ping
RUN apt install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y libkrb5-dev
RUN apt-get install openjdk-8-jdk -y

RUN wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
RUN tar -xvf spark-3.1.2-bin-hadoop3.2.tgz
RUN mv spark-3.1.2-bin-hadoop3.2/ /opt/spark


RUN apt-get remove --purge python3.6

RUN apt-get install python3.8 -y
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 10

RUN apt install python3.8-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3.8 get-pip.py

COPY assets/spark_test/requirements.txt .

RUN pip install --upgrade && \
    pip install --upgrade setuptools && \
    pip install --no-cache-dir -r requirements.txt

# download jars
# org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2
RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.1.2/spark-sql-kafka-0-10_2.12-3.1.2.jar && \
    mv spark-sql-kafka-0-10_2.12-3.1.2.jar /opt/spark/jars

# org.apache.kafka:kafka-clients:3.1.0
RUN wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.1.0/kafka-clients-3.1.0.jar && \
    mv kafka-clients-3.1.0.jar /opt/spark/jars

# org.apache.spark:spark-token-provider-kafka-0-10_2.12:3.1.2
RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.1.2/spark-token-provider-kafka-0-10_2.12-3.1.2.jar && \
    mv spark-token-provider-kafka-0-10_2.12-3.1.2.jar /opt/spark/jars

RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.12/3.1.2/spark-streaming-kafka-0-10_2.12-3.1.2.jar && \
    mv spark-streaming-kafka-0-10_2.12-3.1.2.jar /opt/spark/jars

RUN wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.12/3.2.1/spark-streaming-kafka-0-10_2.12-3.2.1.jar && \
    mv spark-streaming-kafka-0-10_2.12-3.2.1.jar /opt/spark/jars

RUN wget https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar && \
    mv commons-pool2-2.11.1.jar /opt/spark/jars

RUN wget https://repo1.maven.org/maven2/com/pygmalios/reactiveinflux-spark_2.11/1.4.0.10.0.4.1/reactiveinflux-spark_2.11-1.4.0.10.0.4.1.jar && \
    mv reactiveinflux-spark_2.11-1.4.0.10.0.4.1.jar /opt/spark/jars

RUN mkdir /root/.pip && \
    set -x \
    && { \
    echo '[global]'; \
    echo 'timeout = 60'; \
    echo '[freeze]'; \
    echo 'timeout = 10'; \
    echo '[list]'; \
    echo 'format = columns'; \
    } > /root/.pip/pip.conf


ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/usr/local/cuda/include:/usr/local/cuda/lib64

COPY assets/spark_test/entrypoint.sh /usr/local/bin/entrypoint.sh

ENV SPARK_NO_DAEMONIZE=1
ENV SPARK_MODE=master
ENV SPARK_MASTER_HOST=spark-master_test
ENV SPARK_MASTER_PORT=17077
ENV SPARK_MASTER=spark://spark-master_test:17077
ENV SPARK_MASTER_WEBUI_PORT=18083
ENV SPARK_WORKER_INSTANCES=1
ENV SPARK_WORKER_CORES=1
ENV SPARK_WORKER_MEMORY=1g

ENV USE_HADOOP=false

WORKDIR /opt/spark

RUN ["chmod", "+x", "/entrypoint.sh"]

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
