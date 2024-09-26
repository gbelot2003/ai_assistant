# app/controllers/chat_controller.py
from flask_socketio import send
from app.services.user_info_service import UserInfoService

class ChatController:
    def __init__(self, user_info_service: UserInfoService):
        self.user_info_service = user_info_service

    def handle_message(self, user_id: str, message: str):
        user_info = self.user_info_service.get_user_info(user_id)
        full_message = f"{user_info['name']} ({user_info['email']}): {message}"
        send(full_message, broadcast=True)