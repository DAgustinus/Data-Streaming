from dataclasses import asdict, dataclass
import json
import random

import faust


@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int
    score: int = 0


# We're adding a function that would process the stream data
# For this one, we take the whole entire data (event) and set the event.score as a random int
# Then we return the data back
def add_score(event):
    event.score = random.randint(0, 10)
    return event

# As usual, create the app, set the consumer and producer topic
app = faust.App("exercise5", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)
scored_topic = app.topic(
    "com.udacity.streams.clickevents.scored",
    key_type=str,
    value_type=ClickEvent,
)


@app.agent(clickevents_topic)
async def clickevent(clickevents):
    # We add the clickevents.add_processor(add_score) which is the function from line 9
    # See: https://faust.readthedocs.io/en/latest/reference/faust.streams.html?highlight=add_processor#faust.streams.Stream.add_processor
    clickevents.add_processor(add_score)

    async for ce in clickevents:
        await scored_topic.send(key=ce.uri, value=ce)


if __name__ == "__main__":
    app.main()
