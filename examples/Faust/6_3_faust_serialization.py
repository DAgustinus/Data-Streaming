from dataclasses import asdict, dataclass
import json

import faust

# This data class is the expected data class that we will receive
@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int

# This is the expected outgoing
@dataclass
class ClickEventSanitized(faust.Record):
    timestamp: str
    uri: str
    number: int

# Start by creating the app as usual
app = faust.App("exercise3", broker="kafka://localhost:9092")

# Create the faust topic by using the topic name and specifying how the data will be received as (Line 8)
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)

# Define an output topic for sanitized click events, without the user email (This also creates the topic as well!)
sanitized_topic = app.topic("com.udacity.streams.clickevents.sanitized")


@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for clickevent in clickevents:
        # We modify the incoming click event to remove the user email.
        #       Create and send a ClickEventSanitized object.
        ces = ClickEventSanitized(
            timestamp=clickevent.timestamp,
            uri=clickevent.uri,
            number=clickevent.number
        )

        # Send the data to the topic you created above.
        #       Make sure to set a key and value
        await sanitized_topic.send(key=ces.uri, value=ces)


if __name__ == "__main__":
    app.main()
