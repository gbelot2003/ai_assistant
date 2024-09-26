# services/socket_service.py
from flask_socketio import SocketIO, send
from app.services.openai_service import Actions
from app.controllers.chat_controller import ChatController
from app.services.user_info_service_impl import UserInfoServiceImpl

socketio = SocketIO()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('message')
    def handle_message(message):
        user_id = 'some_user_id'  # Ejemplo de user_id
        
        chat_controller.handle_message(user_id, message)
        
        respuesta = Actions().generar_respuesta(message)
        
        send(respuesta, broadcast=True)

    return socketio
