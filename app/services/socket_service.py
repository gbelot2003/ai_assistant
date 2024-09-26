# services/socket_service.py
from flask_socketio import SocketIO, send
from app.services.openai_service import Actions

socketio = SocketIO()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('message')
    def handle_message(message):
        
        print(f"Tu: {message}")

        respuesta = Actions().generar_respuesta(message)

        print(f"GPT : {respuesta}")
        send(respuesta, broadcast=True)

    return socketio
