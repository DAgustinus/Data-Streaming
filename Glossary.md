## Glossary of Terms: (same as provided at beginning of lesson)
- Broker (Kafka) - A single member server of the Kafka cluster
- Cluster (Kafka) - A group of one or more Kafka Brokers working together to satisfy Kafka production and consumption
- Node - A single computing instance. May be physical, as in a server in a datacenter, or virtual, as an instance might be in AWS, GCP, or Azure.
- Zookeeper - Used by Kafka Brokers to determine which broker is the leader of a given partition and topic, as well as track cluster membership and configuration for Kafka
- Access Control List (ACL) - Permissions associated with an object. In Kafka, this typically refers to a user’s permissions with respect to production and consumption, and/or the topics themselves.
- JVM - The Java Virtual Machine. Responsible for allowing host computers to execute the byte-code compiled against the JVM.
- Data Partition (Kafka) - Kafka topics consist of one or more partitions. A partition is a log which provides ordering guarantees for all of the data contained within it. Partitions are chosen by hashing key values.
- Data Replication (Kafka) - A mechanism by which data is written to more than one broker to ensure that if a single broker is lost, a replicated copy of the data is available.
- In-Sync Replica (ISR) - A broker which is up to date with the leader for a particular broker for all of the messages in the current topic. This number may be less than the replication factor for a topic.
- Rebalance - A process in which the current set of consumers changes (addition or removal of consumer). When this occurs, assignment of partitions to the various consumers in a consumer group must be changed.
- Data Expiration - A process in which data is removed from a Topic log, determined by data retention policies.
- Data Retention - Policies that determine how long data should be kept. Configured by time or size.
- Batch Size - The number of messages that are sent or received from Kafka
- acks - The number of broker acknowledgements that must be received from Kafka before a producer continues processing
- Synchronous Production - Producers which send a message and wait for a response before performing additional processing
- Asynchronous Production - Producers which send a message and do not wait for a response before performing additional processing
- Avro - A binary message serialization format
- Message Serialization - The process of transforming an applications internal data representation to a format suitable for interprocess communication over a protocol like TCP or HTTP.
- Message Deserialization - The process of transforming an incoming set of data from a form suitable for interprocess communication, into a data representation more suitable for the application receiving the data.
- Retries (Kafka Producer) - The number of times the underlying library will attempt to deliver data before moving on
- Consumer Offset - A value indicating the last seen processed of a given consumer, by ID.
- Consumer Group - A collection of one or more consumers, identified by group.id which collaborate to consume data from Kafka and share a consumer offset.
- Consumer Group Coordinator - The broker in charge of working with the Consumer Group Leader to initiate a rebalance
- Consumer Group Leader - The consumer in charge of working with the Group Coordinator to manage the consumer group
- Topic Subscription - Kafka consumers indicate to the Kafka Cluster that they would like to consume from one or more topics by specifying one or more topics that they wish to subscribe to.
- Consumer Lag - The difference between the offset of a consumer group and the latest message offset in Kafka itself
- CCPA - California Consumer Privacy Act
- GDPR - General Data Protection Regulation
- Kafka Connect - A web server and framework for integrating Kafka with external data sources such as SQL databases, log files, and HTTP endpoints.
- JAR - Java ARchive. Used to distribute Java code reusably in a library format under a single file.
- Connector - A JAR built on the Kafka Connect framework which integrates to an external system to either source or sink data from Kafka
- Source - A Kafka client putting data into Kafka from an external location, such as a data store
- Sink - A Kafka client remove data from Kafka into an external location, such as a data store
- JDBC - Java Database Connectivity. A Java programming abstraction over SQL database interactions.
- Task - Responsible for actually interacting with and moving data within a Kafka connector. One or more tasks make up a connector.
- Kafka REST Proxy - A web server providing APIs for producing and consuming from Kafka, as well as fetching cluster metadata.
- Join (Streams) - The process of combining one or more streams into an output stream, typically on some related key attribute.
- Filtering (Streams) - The process of removing certain events in a data stream based on a condition
- Aggregating (Streams) - The process of summing, reducing, or otherwise grouping data based on a key attribute
- Remapping (Streams) - The process of modifying the input stream data structure into a different output structure. This may include the addition or removal of fields on a given event.
- Windowing (Streams) - Defining a period of time from which data is analyzed. Once data falls outside of that period of time, it is no longer valid for streaming analysis.
- Tumbling Window (Streams) - The tumbling window defines a block of time which rolls over once the duration has elapsed. A tumbling window of one hour, started now, would collect all data for the next 60 minutes. Then, at the 60 minute mark, it would reset all of the data in the topic, and begin collecting a fresh set of data for the next 60 minutes.
- Hopping Window (Streams) - Hopping windows advance in defined increments of time. A hopping window consists of a window length, e.g. 30 minutes, and an increment time, e.g. 5 minutes. Every time the increment time expires, the window is advanced forward by the increment.
- Sliding Window (Streams) - Sliding Windows work identically to Hopping Windows, except the increment period is much smaller -- typically measured in seconds. Sliding windows are constantly updated and always represent the most up-to-date state of a given stream aggregation.
- Stream - Streams contain all events in a topic, immutable, and in order. As new events occur, they are simply appended to the end of the stream.
- Table - Tables are the result of aggregation operations in stream processing applications. They are a roll-up, point-in-time view of data.
- Stateful - Stateful operations must store the intermediate results of combining multiple events to represent the latest point-in-time value for a given key
- DSL - Domain Specific Language. A metaprogramming language for specific tasks, such as building database queries or stream processing applications.
- Dataclass (Python) - A special type of Class in which instances are meant to represent data, but not contain mutating functions
- Changelog - An append-only log of changes made to a particular component. In the case of Faust and other stream processors, this tracks all changes to a given processor.
- Processor (Faust) - Functions that take a value and return a value. Can be added in a pre-defined list of callbacks to stream declarations.
- Operations (Faust) - Actions that can be applied to an incoming stream to create an intermediate stream containing some modification, such as a group-by or filter