## Iniciar o Kafka e ZooKeeper - Verificar onde o Kafka está instalado
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

## Iniciar o Elastic e o Kibana - Verificar onde essas ferramentas estão instaladas 
./bin/elasticsearch
./bin/kibana

## Iniciar o produtor e o worker - Pasta TwitterKafka
python3 producer.py
python3 worker.py

## Iniciar o consumidor - Pasta Elastic
python3 consumer.py

## Para executar o Spark - Verificar onde o Spark está instalado
opt/spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 home/renan/PSPD/ElasticLula/Spark/spark_kafka.py
