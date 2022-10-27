from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "9YPkwXkgfc65dmj9+LXC"

# Create the client instance
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="/home/elasticsearch-8.4.1/config/certs/http_ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Successful response!
print(client.info())

consumer = KafkaConsumer('all_words_bolsonaro')


for message in consumer:
    if message != None:
        print (f'{json.loads(message.value.decode("utf-8"))} - {json.loads(message.key.decode("utf-8"))}')
        
        doc = {
            'word': json.loads(message.value.decode("utf-8")),
            'count': json.loads(message.key.decode("utf-8"))
        }
        
        resp = client.index(index="words_bolsonaro", id=json.loads(message.value.decode("utf-8")), document=doc)
        
        print(resp['result'])