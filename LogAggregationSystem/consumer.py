from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

# Configure Kafka consumer
consumer = KafkaConsumer('logs',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Configure Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])

def consume_logs():
    for message in consumer:
        log_entry = message.value
        es.index(index='logs', body=log_entry)
        print(f"Stored log: {log_entry}")

if __name__ == "__main__":
    consume_logs()