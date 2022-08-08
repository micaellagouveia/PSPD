FROM openjdk:8-jdk-buster

RUN wget https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz
RUN tar xvf spark-3.3.0-bin-hadoop3.tgz

RUN mkdir /opt/spark

RUN mv spark-3.3.0-bin-hadoop3/* /opt/spark

RUN chmod -R 111 /opt/spark

WORKDIR /opt/spark

COPY find_log.py find_log.py
COPY command.sh command.sh
COPY src src

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:${SPARK_HOME}/sbin

RUN apt update -y && apt install python3 time -y

## ENV SPARK_MASTER_HOST=0.0.0.0
ENV TIME="%E"

RUN ./sbin/start-master.sh
# RUN python find_log.py | xargs -0 tail -f

CMD ./command.sh