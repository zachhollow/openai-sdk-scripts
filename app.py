#ChatGPT Console App

# pip install openai
# OR 'pip install --upgrade openai'
from openai import OpenAI

# Set up a virtual environment (optional):
# python -m venv openai-env

# Activation 
# Windows: openai-env\Scripts\activate
# MacOS or Unix: source openai-env/bin/activate

# See quickstart for how to set up your API key by editing your bash profile (MacOS) or by editing your advanced system settings (Windows):
# https://platform.openai.com/docs/quickstart

# For all else, see the OpenAI Documentation: https://platform.openai.com/docs/introduction 
# And OpenAI API Reference: https://platform.openai.com/docs/api-reference

# pip install logging
# OR 'pip install --upgrade logging'
import logging 
# More logging code to be implemented

client = OpenAI()

print("\nMessage ChatGPT...")  

class ExitChatGPTAI(Exception):
   pass

conversation = [
    {
        "role": "assistant",
        "content": "You are a console app run via terminal.",
    },
]

def chatgpt(): 
    try:
        user_input = input("\nYou: ") 
        if user_input == "EXIT":
            raise ExitChatGPTAI
        else:
            conversation.append({"role": "user", "content": user_input})     
            stream = client.chat.completions.create(
                model="gpt-4",
                messages=conversation,
                temperature=1,
                max_tokens=256,
                stream=True,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            print()
            # See OpenAI API Reference on Streaming: https://platform.openai.com/docs/api-reference/streaming
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    chatgpt_response = chunk.choices[0].delta.content
                    conversation.append({"role":"assistant", "content": chatgpt_response})
                    print(chatgpt_response, end="")
            print()
    except ExitChatGPTAI:
        logging.info("Exiting ChatGPT.")
        exit()
    except KeyboardInterrupt:
        print("\nExiting ChatGPT...")
while True:
    chatgpt()