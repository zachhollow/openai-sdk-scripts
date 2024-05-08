from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler

client = OpenAI()

file = client.files.retrieve("file-x6YV6lMHUF44eC03mKiVVR56")

assistant = client.beta.assistants.create(
    instructions="You are a data analyst. Summarize data and provide data visualizations.",
    name="Data Analyst",
    tools=[{"type": "code_interpreter"}, {"type": "file_search"}], 
    model="gpt-4-turbo",\
    tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content=input("\nYou: ") 
)

# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
 
class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nAssistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nAssistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\nOutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 
# Then, we use the `stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.
 
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Zach. The user has a background in data analytics and machine learning using Python.",
  event_handler=EventHandler(),
) as stream:
  stream.until_done()


image_data = client.files.content("file-x6YV6lMHUF44eC03mKiVVR56")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)