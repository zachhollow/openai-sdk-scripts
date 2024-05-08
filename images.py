# Code is complete, needs integration

from openai import OpenAI
client = OpenAI()

user_input = input("\nEnter prompt for DALL-E-3: ") 

response = client.images.generate(
  model="dall-e-3",
  prompt=user_input,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)