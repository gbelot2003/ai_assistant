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
        self.waiting_for_email = False
        self.initial_request = None

    def generate_response(self, prompt):
        if not self.greeted:
            self.greeted = True
            return "¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy?"
        elif not self.user_info.get('email'):
            self.user_info['email'] = prompt
            self.waiting_for_email = True
            return "Gracias por proporcionarnos tu correo electrónico. Ahora puedes hacer tu petición."
        elif self.waiting_for_email:
            self.initial_request = prompt
            self.waiting_for_email = False
            return self.handle_request(prompt)
        else:
            return self.handle_request(prompt)

    def handle_request(self, prompt):
        print(f"Tu: {prompt}")
        messages = [
            {"role": "system", "content": f"El usuario necesita ayuda con: {self.initial_request}"},
            {"role": "user", "content": prompt}
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1 # type: ignore
        )

        # Accede a la respuesta correcta
        print(f"GPT : {response.choices[0].message.content.strip()}") # type: ignore
        return response.choices[0].message.content.strip() # type: ignore