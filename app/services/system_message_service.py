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
        
        # Aquí podrías agregar otros checks, como si falta el correo electrónico u otra información
        # if not self.user_info_service.tiene_email():
        #     messages.append(
        #         {"role": "system", "content": "Solicita el correo electrónico del usuario de manera educada."}
        #     )

        return messages

    def generar_mensaje_continuacion(self, prompt):
        """
        Genera el mensaje de continuación basado en la entrada del usuario.
        """
        return [
            {"role": "user", "content": prompt}
        ]
