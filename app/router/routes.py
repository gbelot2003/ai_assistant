# app/router/routes.py
from flask import render_template
from app.services.socket_service import init_socketio

def configure_routes(app, socketio):
    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")

    # Inicializar socketio con los servicios
    init_socketio(app)