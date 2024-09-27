# app/services/system_message_service.py
import re

class SystemMessageService:
    def __init__(self, user_info_service):
        self.user_info_service = user_info_service

    def generar_mensaje_inicial(self, prompt):
        """
        Genera el mensaje inicial dependiendo de la información que falta (nombre, email, etc.).
        """
        messages = []

        # Verificar si falta el nombre
        if not self.user_info_service.tiene_nombre():
            messages.append(
                {"role": "system", "content": "Saluda cortesmente al usuario y obtén su nombre de manera natural."}
            )
        
            messages.append(
                 {"role": "user", "content": prompt}
            )
        
        return messages

    def generar_mensaje_continuacion(self, prompt):
        """
        Genera el mensaje de continuación basado en la entrada del usuario.
        """
        messages = []

        # Verificar si el usuario pregunta por información, horarios o cotizaciones
        if self.es_consulta_especifica(prompt) and not self.user_info_service.tiene_email():
            messages.append(
                {"role": "system", "content": "Por favor, proporciona tu correo electrónico para enviarte la información solicitada, Habla en español salvo que el usuario indique otra cosa."}
            )

        messages.append(
            {"role": "user", "content": f"{prompt}"}
        )

        return messages

    def es_consulta_especifica(self, prompt):
        """
        Determina si el prompt es una consulta sobre información, horarios o cotizaciones.
        """
        consultas_especificas = [
            r"(información|horarios|cotizaciones|precios|costos|tarifas)",
            r"(cuándo|dónde|cómo|qué|quién)",
            r"(necesito|quiero|deseo|solicito|busco)",
            r"(información|horario|cotización|precio|costo|tarifa)"
        ]

        for consulta in consultas_especificas:
            if re.search(consulta, prompt, re.IGNORECASE):
                return True
        return False