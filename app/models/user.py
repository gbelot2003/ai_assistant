from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), unique=True, nullable=True)
    direccion = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return f'<User {self.nombre} - {self.telefono}>'