# app/services/openai_service.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    def __init__(self):
        self.user_info = {}
        self.greeted = False

    def generate_response(self, prompt):
        if not self.greeted:
            self.greeted = True
            return "¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy?"
        elif not self.user_info.get('name'):
            self.user_info['name'] = prompt
            return "Gracias por proporcionarnos tu nombre. Ahora, por favor, dinos tu correo electrónico."
        elif not self.user_info.get('email'):
            self.user_info['email'] = prompt
            return "Gracias por proporcionarnos tu correo electrónico. Ahora podemos continuar con la conversación."
        else:
            print(f"Tu: {prompt}")
            messages = [{"role": "user", "content": prompt}]

            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1 # type: ignore
            )

            # Accede a la respuesta correcta
            print(f"GPT : {response.choices[0].message.content.strip()}") # type: ignore
            return response.choices[0].message.content.strip() # type: ignore