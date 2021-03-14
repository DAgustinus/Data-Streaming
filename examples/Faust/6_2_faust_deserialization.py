# Read dataclasses in python 3.7++
from dataclasses import asdict, dataclass
import json

import faust


# 1. Define a ClickEvent Record Class with
#       email (str),
#       timestamp (str),
#       uri(str),
#       number (int)
#
# 2. Set the validation to True to make sure that the type of data that we've received is correct
#       Else it would be discarded
#
#   See: https://docs.python.org/3/library/dataclasses.html
#   See: https://faust.readthedocs.io/en/latest/userguide/models.html#model-types
@dataclass
class ClickEvent(faust.Record, validation=True):
    email: str = ""
    timestamp: str = ""
    uri: str = ""
    number: int = 0
    # If we are expecting a new field, we can add it here and set the default value here

# Create the app via faust.App, set the name and location of the broker
app = faust.App("exercise2", broker="kafka://localhost:9092")


# Provide the key (uri) and value type to the clickevent
clickevents_topic = app.topic(
    "com.udacity.streams.clickevents",      # Topic name
    key_type=str,                           # key type
    value_type=ClickEvent,                  # dataclass ClickEvent above in line 18
)

@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for ce in clickevents:
        # PrettyPrint the data
        print(json.dumps(asdict(ce), indent=2))


if __name__ == "__main__":
    app.main()
