from app.services.nombre_service import NombreService
from app.services.user_info_service import UserInfoService
from app.services.system_message_service import SystemMessageService
from openai import OpenAI
from dotenv import load_dotenv
import os

# Inicializa la API de OpenAI
load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIService:
    def __init__(self):
        self.user_info_service = UserInfoService()  # Servicio que centraliza la info del usuario
        self.nombre_service = NombreService(self.user_info_service)  # Servicio especializado en manejar nombres
        self.system_message_service = SystemMessageService(self.user_info_service)  # Servicio de mensajes de 'system'
        self.respuesta_nombre = None

    def generate_response(self, prompt):
        return self.handle_request(prompt)

    def handle_request(self, prompt):
        print(f"Usuario: {prompt}")

        # Primero verificamos si hay que obtener información adicional (nombre, correo, etc.)
        messages = self.system_message_service.generar_mensaje_inicial(prompt)

        # Si ya tenemos la información necesaria, solo mandamos el prompt
        if not messages:
            messages = self.system_message_service.generar_mensaje_continuacion(prompt)

        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1  # type: ignore
        )

        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

        print(f"GPT: {respuesta_modelo}")

        # Detectar si el modelo ha identificado un nombre en la respuesta
        self.respuesta_nombre = self.detectarNombre(respuesta_modelo)

        return respuesta_modelo

    def detectarNombre(self, prompt):
        self.nombre_service.detectar_y_almacenar_nombre(prompt)
        print(self.user_info_service.tiene_nombre())
        return self.user_info_service.get_nombre()
        