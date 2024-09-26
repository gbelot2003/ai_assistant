# app/services/openai_service.py
from app.modules.nombre_extractor import NombreExtractor
from openai import OpenAI
from dotenv import load_dotenv
import os

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    def __init__(self):
        self.user_info = {}
        # El extractor de nombres es inyectado como una dependencia
        nombre_extractor = NombreExtractor()
        self.nombre_extractor = nombre_extractor
        self.nombre_usuario = None  # Inicialmente no conocemos el nombre del usuario
        

    def generate_response(self, prompt):

        return self.handle_request(prompt)

    def handle_request(self, prompt):
        print(f"Tu: {prompt}")

         # Utilizamos el método inyectado para extraer el nombre
        self.nombre_usuario = self.nombre_extractor.extraer_nombre(prompt)
        
        if not self.nombre_usuario:
            messages = [
                {"role": "system", "content": "Saluda cortezmente y pregunta el nombre del usuario y en que se le puede servir"},
                {"role": "user", "content": prompt}
            ]
        else:
            messages = [
                {"role": "user", "content": prompt}
            ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1 # type: ignore
        )
        

        # Accede a la respuesta correcta
        print(f"GPT : {response.choices[0].message.content.strip()}") # type: ignore
        return response.choices[0].message.content.strip() # type: ignore