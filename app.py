# app.py
import os
from flask import Flask
from flask_socketio import SocketIO
from app.router.routes import configure_routes  # Importamos las rutas

template_dir = os.path.abspath('app/templates')
app = Flask(__name__, template_folder=template_dir)
app.config["SECRET_KEY"] = "supersecretkey!"

socketio = SocketIO(app)

# Configurar las rutas
configure_routes(app, socketio)

if __name__ == "__main__":
    socketio.run(app, debug=True)