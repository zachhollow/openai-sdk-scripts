from openai import OpenAI
client = OpenAI()

file = client.files.create(
                file=open("INSERT HERE.csv", "rb"),
                purpose='assistants',
            )
    
