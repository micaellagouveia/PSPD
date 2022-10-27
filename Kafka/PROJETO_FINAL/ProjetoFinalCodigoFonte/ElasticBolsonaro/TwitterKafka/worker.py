import contextlib
from json import dumps
import json
from time import sleep
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import os
import json
import re

KAFKA_SERVERS = ["localhost:9092"]

print('KAFKA_SERVERS', KAFKA_SERVERS)

admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_SERVERS,
)

def create_kafka_topic(topic_name):
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

RAW_TOPICS = [
    'twitter_bolsonaro',
]

print('RAW_TOPICS', RAW_TOPICS)

def get_consumer(
    group_id='consumer-id-3',
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
    exclude_words = ["de", "em", "a", "per", "por", "o", "do", "no", "ao", "pelo", "os", "dos", 
        "nos", "aos", "pelos", "a", "da", "na", "à", "pela", "as", "das", "nas", "às", "pelas", "um", "dum", 
        "num", "uns", "duns", "nuns", "uma", "duma", "numa", "umas", "dumas", "numas"]

    consumer = get_consumer()

    producer_bolsonaro = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries=3,
        request_timeout_ms=1000
    )

    while True:
        try:
            for event in consumer:
                print(f"{event.topic}: {event.value}" )
                message = json.loads(event.value)['data']['text']

                words = message.split()

                for word in words:
                    word = word.lower()
                    word = re.sub(r'[^\w\s]', '', word)

                    if not word.startswith("@") and word not in exclude_words and len(word) > 2:
                        producer_bolsonaro.send(
                            topic='bolsonaro_treated_messages', 
                            value=word, 
                            key=word,
                        )

        
        except Exception as exc:
            print(exc)



