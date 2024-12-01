bin/kafka-topics.sh --create --topic logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /path/to/your/log/files/*.log

output.kafka:
  hosts: ["localhost:9092"]
  topic: "logs"
  codec.json:
    pretty: false

    