import logging
from kafka import KafkaProducer
import json
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def produce_logs():
    while True:
        log_entry = {
            "timestamp": time.time(),
            "level": "INFO",
            "message": "This is a sample log message"
        }
        producer.send('logs', log_entry)
        logger.info(f"Sent log: {log_entry}")
        time.sleep(1)

if __name__ == "__main__":
    produce_logs()