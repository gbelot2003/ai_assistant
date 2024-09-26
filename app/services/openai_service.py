from openai import OpenAI
from dotenv import load_dotenv
import os

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Actions:
    def __init__(self):
        self.usuario = {"nombre": "", "email": ""}

    def generar_respuesta(self, prompt):
        messages = [{"role": "user", "content": prompt}]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1 # type: ignore
        )

        # Accede a la respuesta correcta
        return response.choices[0].message.content.strip() # type: ignore


# Crear una instancia de Actions
actions = Actions()
