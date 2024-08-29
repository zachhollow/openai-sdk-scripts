from openai import OpenAI
client = OpenAI()
  
assistant = client.beta.assistants.create(
  name="Digital and Social Media Research Assistant",
  instructions="You are a digital and social media research assistant. Analyze data and write holistic memos when prompted",
  tools=[{"type": "file_search"}],
  model="gpt-4-turbo",
)

print(assistant)

user_input = input("\nYou: ") 

thread = client.beta.threads.create()

message_thread = client.beta.threads.create(
  messages=[
      
    {"role": "system", "content": "You are a helpful assistant run via a console app in Terminal."},
    {"role": "user", "content": user_input}
  ]
)

print(message_thread)


from openai import OpenAI
client = OpenAI()

thread_message = client.beta.threads.messages.create(
  "thread_abc123",
  role="user",
  content="How does AI work? Explain it in simple terms.",
)
print(thread_message)
