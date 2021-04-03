"""Producer base-class providing common utilites and functionality"""
import logging
import time


from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer

logger = logging.getLogger(__name__)


class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema=None,
        num_partitions=1,
        num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        #
        #
        # TODO: Configure the broker properties below. Make sure to reference the project README
        # and use the Host URL for Kafka and Schema Registry!
        #
        #
        self.broker_properties = {
            "bootstrap.servers": ",".join(["PLAINTEXT://localhost:9092"]),
            "schema.registry.url": "http://localhost:8081",
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # TODO: Configure the AvroProducer
        self.producer = AvroProducer(
            self.broker_properties,
            default_key_schema=key_schema,
            default_value_schema=value_schema,
        )

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        #
        #
        # TODO: Write code that creates the topic for this producer if it does not already exist on
        # the Kafka Broker.
        #
        #
        # logger.info("topic creation kafka integration incomplete - skipping")
        
        client = AdminClient({
            "bootstrap.servers": "PLAINTEXT://localhost:9092"
        })
        
        # Get the list of existing topics
        exists_topic_list = client.list_topics()
        
        # if exists_topic_list.topics.get(self.topic_name)
        if self.topic_name in exists_topic_list.topics:
            logger.info(f"Topic Skipped - Exists: {self.topic_name}")
            return
        
        futures = client.create_topics([
            NewTopic(
                topic=self.topic_name,
                num_partitions=5,
                replication_factor=1
            )
        ])
        
        for topic, future in futures.items():
            try:
                future.result()
                logger.info(f"Topic has been created: {topic}")
            except Exception as e:
                logger.warning(f"failed to create topic {topic}: {e}")
                

    def time_millis(self):
        return int(round(time.time() * 1000))

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        if self.producer is not None:
            logger.debug("Flushing producer")
            self.producer.flush()

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
