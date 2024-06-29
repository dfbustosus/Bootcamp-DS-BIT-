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

# 4. Crear asistente  
assistant = client.beta.assistants.create(
  name="Programming Tutor",
  instructions="You are a expert programmer in Golang. Write and run code to answer programming questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-3.5-turbo",
)
# 5. Crear un thread
thread = client.beta.threads.create()
# 6. Añadir mensaje al thread
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I need to create a simple class to implement a derivate given x and y values"
)
# 7. Crear el run
run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please answer all the user questions as you were an expert."
)
# 8. Resultados
if run.status == 'completed': 
  messages = client.beta.threads.messages.list(
    thread_id=thread.id
  )
  print(messages)
else:
  print(run.status)