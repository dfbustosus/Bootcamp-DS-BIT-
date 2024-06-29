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
# 4. ChatCompletions
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Eres un asistente util"},
    {"role": "user", "content": "Quien gano la serie mundial de 2020?"},
    {"role": "assistant", "content": "Los Angeles Dodgers"},
    {"role": "user", "content": "When was played?"},
  ],
  temperature=0,
  max_tokens=20
)
print(response.choices[0].message.content)

print('------------------------------------------------------------------')
# 4.1 JSON mode
response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "Eres un asistente util diseñado para responder en formato JSON. Toma lo que el usuario te diga y deberas devolver solo dos categorias con base en el texto: Bueno o Malo"},
    {"role": "user", "content": "Eres una mala persona"},
    #{"role": "assistant", "content": "Los Angeles Dodgers"},
    #{"role": "user", "content": "Cuando se jugo?"}
  ]
)
print(response.choices[0].message.content)