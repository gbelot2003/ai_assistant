# app/modules/email_extractor.py
import re

class EmailExtractor:
    def __init__(self):
        # Expresión regular para detectar correos electrónicos
        self.patron_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Método que intenta extraer el email de un texto dado
    def extraer_email(self, texto):
        # Buscar coincidencias en el texto con el patrón de email
        resultado = re.findall(self.patron_email, texto)
        
        # Retornar el primer email encontrado, o None si no se encuentra
        if resultado:
            return resultado[0]
        return None
