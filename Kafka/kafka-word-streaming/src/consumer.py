import contextlib
from json import dumps
import json
import random
from time import sleep
from faker import Faker
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import os

KAFKA_SERVERS = os.getenv(
    'KAFKA_SERVERS',
    'localhost:9091,localhost:9092,localhost:9093',
).split(',')

print('KAFKA_SERVERS', KAFKA_SERVERS)

RAW_TOPICS = [
    'all_words',
    'start_S',
    'start_P',
    'start_R',
    'word_count',
    'char6',
    'char8',
    'char11'
]

print('RAW_TOPICS', RAW_TOPICS)

def get_consumer(
    group_id='consumer-id-2',
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    key_deserializer=lambda x: json.loads(x.decode("utf-8")),
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    consumer_timeout_ms=1000,
):
    consumer = KafkaConsumer(
        group_id=group_id,
        auto_offset_reset=auto_offset_reset,
        bootstrap_servers=KAFKA_SERVERS,
        enable_auto_commit=enable_auto_commit,
        key_deserializer=key_deserializer,
        value_deserializer=value_deserializer,
        consumer_timeout_ms=consumer_timeout_ms,
    )

    consumer.subscribe(RAW_TOPICS)
    return consumer


def process(event):
    event_data = event.value
    print(event_data)
    

if __name__ == '__main__':

    consumer = get_consumer()

    while True:
        try:
            for event in consumer:
                print(f"{event.topic}: {event.value}" )
        
        except Exception as exc:
            print(exc)
