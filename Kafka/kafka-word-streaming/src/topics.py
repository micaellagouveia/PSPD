import contextlib
from json import dumps
import json
import random
from time import sleep
from faker import Faker
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import os

KAFKA_SERVERS = os.getenv(
    'KAFKA_SERVERS',
    'localhost:9091,localhost:9092,localhost:9093',
).split(',')

print('KAFKA_SERVERS', KAFKA_SERVERS)

def create_kafka_topic(topic_name):
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_SERVERS,
    )

    topic_list = [
        NewTopic(
            name=topic_name,
            num_partitions=10,
            replication_factor=2,
            topic_configs={"retention.ms": "-1"},
        ),
    ]

    with contextlib.suppress(Exception):
        admin_client.create_topics(
            new_topics=topic_list,
            validate_only=False,
        )

if __name__ == '__main__':

    create_kafka_topic('all_words')
    create_kafka_topic('topic_SPR')
    create_kafka_topic('word_count')
    create_kafka_topic('chars')

