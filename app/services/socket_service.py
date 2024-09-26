# services/socket_service.py
from flask_socketio import SocketIO, send

socketio = SocketIO()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('message')
    def handle_message(message):
        print(message)
        send(message, broadcast=True)

    return socketio
