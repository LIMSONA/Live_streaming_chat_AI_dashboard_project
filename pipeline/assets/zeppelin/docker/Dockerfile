FROM apache/zeppelin:0.10.1

USER root

WORKDIR /opt
RUN wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz && \
    tar -xvf spark-3.2.1-bin-hadoop3.2.tgz && \
    mv spark-3.2.1-bin-hadoop3.2 /opt/spark && \
    rm -rf spark-3.2.1-bin-hadoop3.2.tgz
RUN chown root:root -R /opt/spark

ENV SPARK_HOME=/opt/spark

WORKDIR /opt/zeppelin
