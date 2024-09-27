from app.modules.nombre_extractor import NombreExtractor

class NombreService:
    def __init__(self, user_info_service):
        self.nombre_extractor = NombreExtractor()
        self.user_info_service = user_info_service

    def detectar_y_almacenar_nombre(self, prompt):
        # Intentamos extraer el nombre del prompt
        nombre_detectado = self.nombre_extractor.extraer_nombre(prompt)
        
        if nombre_detectado:
            self.user_info_service.set_nombre(nombre_detectado)
            return f"¡Gracias, {nombre_detectado}! Encantado de conocerte."
        return None

    def preguntar_nombre_si_necesario(self):
        if not self.user_info_service.tiene_nombre():
            return "Hola, ¿cómo te llamas?"
        return None
