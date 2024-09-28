from app.models.user import User
from app.extensions import db

class UserService:
    def get_or_create_user(self, nombre, telefono=None, direccion=None, email=None):
        user = User.query.filter_by(telefono=telefono).first()
        if not user:
            user = User(nombre=nombre, telefono=telefono, direccion=direccion, email=email) # type: ignore
            db.session.add(user)
            db.session.commit()
        return user

    def get_user_by_phone_number(self, telefono):
        return User.query.filter_by(telefono=telefono).first()