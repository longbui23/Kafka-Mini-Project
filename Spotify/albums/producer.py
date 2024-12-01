from kafka import KafkaProducer
import pandas as pd
import json 

producer = KafkaProducer(
        bootstrap_servers='mutual-shrimp-13505-us1-kafka.upstash.io:9092',
        sasl_mechanism='SCRAM-SHA-256',
        security_protocol='SASL_SSL',
        sasl_plain_username = None,
        sasl_plain_password = None,
        api_version_auto_timeout_ms=100000,    
    ) 

albums = pd.read_csv("../data/albums.csv")

for line in albums.to_dict(orient='records'):
    data = json.dumps(line).encode('utf-8')

    try:
        result = producer.send('albums', data).get(timeout = 60)
        print("Message produced:", result)
    except Exception as e:
        print(f"Error producing message:{e}")
    
producer.close()