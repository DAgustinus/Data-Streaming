import faust

# Create the faust app with a name and broker
# See: https://faust.readthedocs.io/en/latest/userguide/application.html#application-parameters
app = faust.App("My-first-faust", broker="localhost:9092")

# Connect Faust to com.udacity.streams.clickevents
# See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-topic-create-a-topic-description
topic = app.topic("com.udacity.streams.clickevents")

# Provide an app agent to execute this function on topic event retrieval
# See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-agent-define-a-new-stream-processor
# See: https://faust.readthedocs.io/en/latest/userguide/agents.html#the-stream
@app.agent(topic)
async def clickevent(clickevents):
    # Define the async for loop that iterates over clickevents
    # Basically, as events occured in the topic above (line 11), the iterrator (clickevents in for loop)
    #  will be evoked and will generate the event so we can print it out in this case.
    async for event in clickevents:
        print(event)

if __name__ == "__main__":
    app.main()