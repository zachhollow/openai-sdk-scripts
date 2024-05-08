# TO-DO: Effectively need to add CRUD
from openai import OpenAI
client = OpenAI()

file = client.files.create(
                file=open("INSERT HERE.csv", "rb"),
                purpose='assistants',
            )
    
