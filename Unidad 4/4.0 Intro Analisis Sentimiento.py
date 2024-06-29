import os
import requests
import json
from dotenv import load_dotenv

# Var. entorno
load_dotenv()

# URL de API
api_url = os.getenv('API_URL')

# Data a mandar
data = {
    "text": "Hi how are you",
}

# POST
response = requests.post(api_url, json=data)

# Resultado
try:
    response_json = response.json()
    print(json.dumps(response_json, indent=4))
except json.JSONDecodeError:
    print("Error")
    print(response.text)
