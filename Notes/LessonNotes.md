# Lesson 5: Streaming Strategy
- Stream Processing Strategies (CARF)
    - Combining
        - Joined streams always share some common attribute across the data in all of the streams. For example, we might use a user_id to merge user streams.
        - State must be kept as events flow through the join calculation, until all of the related data has arrived. Once this happens, the new event can be emitted, and the state can be flushed
            - If the related data never fully arrives, at some point the data in memory should be cleared
    - Aggregating
        - Aggregate Functions: Max, Min, Sum, TopN, HIstograms, Sets, Lists, and more
        - Aggregates in streaming applications almost always involve a __timeframe__, unless the source topic is compacted
    - Remapping
        - Remapping streams is the process of transforming an input event and outputting it in a different form to a new stream
        - Sometimes paired up with filter and joining
        - Scenario Example:
            - Converting JSON to AVRO (vice versa)
            - Removing columns
            - Updating data structure to be able to be process by older legacy system
    - Filtering
        - Filtering a stream is the process of removing unwanted or unneeded data from an input stream, and outputting the desired data into a new stream
        - Filtering may be a step in joining or combining two or more streams
        - Filtering is often desirable when data clients don’t need access to all data for throughput or security reasons
        - Applying filters earlier, rather than later, in the processing pipeline, can allow stream processing calculations to scale better and analyze less data.

- Windowing:
    - Period of time start-end for which data is aggregated for analysis
    - Type of Windows:
        - Tumbling:
            - A fixed period of time that rolls over after the fixed window has ended
            - Each events does not overlap/roll or have any gaps between them
        - Hopping:
            - A fixed period of time (similar to tumbling) but some data may overlap
        - Sliding:
            - Window slides at each second

- Streams VS Tables:
    - Streams is the process when we process each data orderly 
    - Tables is when we aggregate the information into things such as count/max/min/etc 

- Storage for Streaming:
    - Use rocksDB as your local state store
    - Fast speed reboot/recovery time in any case of failure on high usage amount of data