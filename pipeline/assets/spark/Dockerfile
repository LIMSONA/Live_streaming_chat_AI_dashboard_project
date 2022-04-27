FROM ubuntu:18.04

RUN apt update

RUN apt install -y vim 
RUN apt install -y wget
RUN apt install -y tar
RUN apt install -y mlocate
RUN apt install -y net-tools iputils-ping

RUN apt-get install openjdk-8-jdk -y

RUN wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
RUN tar -xvf spark-3.1.2-bin-hadoop3.2.tgz
RUN mv spark-3.1.2-bin-hadoop3.2/ /opt/spark


RUN wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz && \
    tar -zxf zeppelin-0.10.1-bin-all.tgz && \
    mv zeppelin-0.10.1-bin-all /opt/zeppelin && \
    rm -rf zeppelin-0.10.1-bin-all.tgz

RUN apt-get install python3.8 -y && \
    ln -s /usr/bin/python3.8 /usr/bin/python3 && \
    ln -s /usr/bin/python3.8 /usr/bin/python

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

ENV ZEPPELIN_HOME=/opt/zeppelin
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$ZEPPELIN_HOME/bin

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

ENV SPARK_NO_DAEMONIZE=1
ENV SPARK_MODE=master
ENV SPARK_MASTER_HOST=spark-master
ENV SPARK_MASTER_PORT=7077
ENV SPARK_MASTER_WEBUI_PORT=8080
ENV SPARK_WORKER_INSTANCES=1
ENV SPARK_WORKER_CORES=1
ENV SPARK_WORKER_MEMORY=1g
ENV SPARK_WORKER_WEBUI_PORT=8082

EXPOSE ${SPARK_MASTER_PORT}
EXPOSE ${SPARK_MASTER_WEBUI_PORT}
EXPOSE ${SPARK_WORKER_WEBUI_PORT}

WORKDIR /opt/spark

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
