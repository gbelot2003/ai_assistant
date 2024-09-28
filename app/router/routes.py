# app/router/routes.py
from flask import render_template
from app.services.socket_service import init_socketio
from app.models.conversation import Conversation
from app.extensions import db

def configure_routes(app, socketio):
    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")

    # Ruta para obtener todas las conversaciones
    @app.route("/conversations")
    def get_conversations():
        conversations = Conversation.query.all()
        return jsonify([{
            'id': conv.id,
            'user_message': conv.user_message,
            'bot_response': conv.bot_response,
            'timestamp': conv.timestamp
        } for conv in conversations])

    # Inicializar socketio con los servicios
    init_socketio(app)