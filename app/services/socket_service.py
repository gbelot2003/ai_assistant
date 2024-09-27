# app/services/socket_service.py
from flask_socketio import SocketIO, send
from app.services.openai_service import OpenAIService

socketio = SocketIO()
openai_service = OpenAIService()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('message')
    def handle_message(message):
        response = openai_service.generate_response(message)
        send(response, broadcast=True)

    return socketio