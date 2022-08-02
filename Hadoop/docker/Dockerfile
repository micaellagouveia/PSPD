FROM openjdk:8-jdk-buster

RUN mkdir /hadoop && cd /hadoop

WORKDIR /hadoop

RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.3/hadoop-3.3.3.tar.gz

RUN tar -xzvf hadoop-3.3.3.tar.gz

RUN mv hadoop-3.3.3 /usr/local/hadoop

WORKDIR /usr/local/hadoop

ENV HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar

COPY src/WordCount.java .

RUN mkdir io
COPY src/io io

RUN bin/hadoop com.sun.tools.javac.Main WordCount.java
RUN jar cf wc.jar WordCount*.class
# RUN bin/hadoop jar wc.jar WordCount io/input io/output