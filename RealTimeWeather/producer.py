import requests
from kafka import KafkaProducer
import json
import time

import os


producer = KafkaProducer(
    bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

LOCATION = "San Leandro, US"
API_KEY = None

def fetch_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    return data

while True:
    weather_data = fetch_weather_data()
    producer.send('weather', value=weather_data)
    print(f'Send data to Kafka: {weather_data}')
    time.sleep(300)