class UserInfoService:
    def __init__(self):
        self.nombre = None
        # self.email = None
        # Otros datos que podrías querer manejar

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def tiene_nombre(self):
        return self.nombre is not None