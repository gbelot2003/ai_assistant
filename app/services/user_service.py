from app.models.user import User
from app.extensions import db

class UserService:
    def get_or_create_user(self, phone_number, name=None):
        user = User.query.filter_by(phone_number=phone_number).first()
        if not user:
            user = User(phone_number=phone_number, name=name)
            db.session.add(user)
            db.session.commit()
        return user

    def get_user_by_phone_number(self, phone_number):
        return User.query.filter_by(phone_number=phone_number).first()