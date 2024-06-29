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
# 4. Embeddings
response = client.embeddings.create(
    input="Hola como estás",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)