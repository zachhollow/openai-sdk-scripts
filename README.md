# ChatGPT Console App

For a general-purpose chatbot in Terminal, please see the ```MainConsoleApp``` 

For Assistants intended for data analysis, see the ```CreateAssistants``` folder

For scripts on processing data files and images, please see the ```ProcessFiles``` folder


```
openai-sdk-scripts/
│
├── CreateAssistant/
│   ├── assistant-class.py
│   ├── code-interpreter.py
│   ├── digital-assistant.py
│
├── MainConsoleApp/
│   ├── app.py
│
├── CreateAssistant/
│   ├── assistant-class.py
│   ├── code-interpreter.py
│   ├── digital-assistant.py
│
├── openai-env/
│
├── LICENSE
├── README.md
```


## Installation

- `pip install openai`
- `pip install logging`
  
## Virtual Environment Setup (Optional, but a step I took in this project)

`python -m venv openai-env`

## Activation

- Windows: `openai-env\Scripts\activate`
- MacOS or Unix: `source openai-env/bin/activate`

## API Key Setup

Follow the steps in the Quickstart Guide to set up your API key.

## Documentation

- OpenAI Documentation: https://platform.openai.com/docs/introduction
- OpenAI API Reference: https://platform.openai.com/docs/api-reference

## Running the Console App

Open terminal and run the following:

`python app.py` 
