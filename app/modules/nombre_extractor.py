import re

class NombreExtractor:
    def __init__(self):
        self.patrones_nombre = [
            r"me llamo\s+([a-z]+)",  # "Me llamo Juan"
            r"mi nombre es\s+([a-z]+)",  # "Mi nombre es Juan"
            r"puedes llamarme\s+([a-z]+)",  # "Puedes llamarme Juan"
            r"soy\s+([a-z]+)",  # "Soy Juan"
            r"nombre:\s*([a-z]+)",  # "Nombre: Juan"
            r"me dicen\s+([a-z]+)",  # "Me dicen Juan"
            r"mis amigos me llaman\s+([a-z]+)",  # "Mis amigos me llaman Juan"
            r"(?:llámame|dime|puedes decirme)\s+([a-z]+)",  # "Llámame Juan" o "Dime Juan"
            r"yo soy\s+([a-z]+)",  # "Yo soy Juan"
            r"es\s+([a-z]+)",  # "Es Juan"
            r"soy el/la\s+([a-z]+)",  # "Soy el Juan"
            r"por favor, llámame\s+([a-z]+)",  # "Por favor, llámame Juan"
            r"hola,\s*([a-z]+)"  # "Hola, Juan"
        ]

    # Método que intenta extraer el nombre de un texto dado
    def extraer_nombre(self, texto):
        texto = texto.lower()  # Convertir todo el texto a minúsculas
        for patron in self.patrones_nombre:
            resultado = re.findall(patron, texto)
            if resultado:
                return resultado[0]  # Retorna el primer nombre encontrado
        return None  # Si no encuentra un nombre, retorna None
