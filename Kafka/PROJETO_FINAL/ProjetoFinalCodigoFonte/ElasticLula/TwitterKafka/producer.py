import contextlib
from json import dumps
import json
from time import sleep
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import os
import requests

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

    try:        
        admin_client.create_topics(
            new_topics=topic_list,
            validate_only=False,
        )
        print("topico criado", topic_name)
    except Exception:
        print("topico jah existe", topic_name)


if __name__ == '__main__':

    create_kafka_topic('twitter_lula')
    create_kafka_topic('lula_treated_messages')

    producer_lula = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries=3,
        request_timeout_ms=1000
    )

    url = "https://api.twitter.com/2/tweets/search/stream"

    payload={}
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAALrCgwEAAAAA25tE8cT%2F8TiYO%2F2tsXv4IRNf75g%3DWUC48cxiYLBulUWxNINUeNQyXPITAb6jYOKw7sA4qXAl3N56IE',
        'Cookie': 'guest_id=v1%3A166326771971876805; guest_id_ads=v1%3A166326771971876805; guest_id_marketing=v1%3A166326771971876805; personalization_id="v1_WTAhX6LQhkR/TgjwnobnZw=="'
    }


    def get_stream(url):
        s = requests.Session()

        with s.get(url, headers=headers, stream=True) as resp:
            for line in resp.iter_lines():
                if line:
                    yield line.decode("utf-8")
                    print(type(line.decode("utf-8")))
                    producer_lula.send(topic='twitter_lula', value=str(line.decode("utf-8")), key=str(line.decode("utf-8")))



    for a in get_stream(url):
        print(a)