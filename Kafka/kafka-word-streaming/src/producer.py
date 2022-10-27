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

admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_SERVERS,
)

Faker.seed(random.randint(0, 1000000))

faker = Faker(['bg_BG',   'cs_CZ', 'da_DK', 'de_DE', 'en_US',
              'es_ES', 'fi_FI', 'fr_FR',  'it_IT',
              'nl_NL', 'pl_PL', 'pt_BR'])

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


def kafka_is_running():
    topics = admin_client.list_topics()
    return bool(topics)


if __name__ == '__main__':

    create_kafka_topic('all_words')
    create_kafka_topic('start_S')
    create_kafka_topic('start_P')
    create_kafka_topic('start_R')
    create_kafka_topic('word_count')
    create_kafka_topic('char6')
    create_kafka_topic('char8')
    create_kafka_topic('char11')

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries=3,
        request_timeout_ms=1000
    )

    j = 0

    while True:
        i = random.randint(0, 8)
        if i == 0:
            data = f'{faker.name()} {faker.address()}'

        elif i == 1:
            data = faker.name()

        elif i == 2:
            data = faker.text()

        elif i == 3:
            data = faker.paragraph()

        elif i == 4:
            data = faker.email()

        elif i == 5:
            data = faker.bairro()

        elif i == 6:
            data = faker.city()

        elif i == 7:
            data = faker.country()

        elif i == 8:
            data = faker.company()


        for word in data.split():
            print(f"({j}) Sending := {word}", flush=True)
            j += 1

            if kafka_is_running():
                producer.send(topic='all_words', value=word, key=word)

                if word.startswith('S') | word.startswith('s'):
                    producer.send(topic='start_S', value=word, key=word)
                elif word.startswith('P') | word.startswith('p'):
                    producer.send(topic='start_P', value=word, key=word)
                elif word.startswith('R') | word.startswith('r'):
                    producer.send(topic='start_R', value=word, key=word)
                elif len(word)== 6:
                    producer.send(topic='char6', value=word, key=word)
                elif len(word)== 8:
                    producer.send(topic='char8', value=word, key=word)
                elif len(word)== 11:
                    producer.send(topic='char11', value=word, key=word)

            
            sleep(0.5)
                
                    
                # producer.send(topic='send_words', value=word, key=word)
                # producer.send(topic='all_words_count', value=word, key=word)
                