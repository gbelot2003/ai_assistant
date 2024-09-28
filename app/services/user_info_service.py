from app.models.user import User
from app.extensions import db

class UserInfoService:
    def __init__(self):
        self.nombre = None
        self.telefono = None

    def get_nombre(self):
        return self.nombre

    def get_telefono(self):
        return self.telefono

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_telefono(self, telefono):
        self.telefono = telefono

    def tiene_nombre(self):
        return self.nombre is not None

    def almacenar_nombre(self, nombre, telefono):
        user = User.query.filter_by(telefono=telefono).first()
        if not user:
            user = User(nombre=nombre, telefono=telefono) # type: ignore
            db.session.add(user)
        else:
            user.nombre = nombre
        db.session.commit()