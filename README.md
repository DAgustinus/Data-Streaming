# Data-Streaming

Commands:
- list all topics
    - `kafka-topics --list --zookeeper http://localhost:8082`
- check if topic is receiving data:
    - `kafka-console-consumer --bootstrap-server http://localhost:9092 --topic "lesson4.exercise6.click_events" --from-beginning`