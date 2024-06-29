#!python -m pip install -q openai dotenv
# 1. Librerias
from pprint import pprint
import json
from openai import OpenAI
import time
from dotenv import load_dotenv
import os
import numpy as np
import base64
#from Funciones import gather_user_data, gather_reservation_data, not_talk
import requests
from pathlib import Path
import warnings 
warnings.filterwarnings("ignore")
###################################################
# 2. Cargar variables entorno
load_dotenv();
openai_key= os.getenv("OPENAI_KEY");
#print(openai_key)
###################################################
# 3. Crear el cliente (permite la conexión con OPENAI)
client=OpenAI(api_key= openai_key);

# 4. Function calling
messages = [
    #{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}
    {"role": "user", "content": "Hi how are you"},
    {"role":"assistant", "content": "I'm just a computer program, so I don't have feelings, but I'm here and ready to help you with whatever you need! How can I assist you today?"},
    {"role": "user", "content":"Como es el clima en Bogota hoy"}
    ]
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    tool_choice="auto",  # auto is default, but we'll be explicit
)
response_message = response.choices[0].message
tool_calls = response_message.tool_calls
print(response_message)
print(tool_calls)