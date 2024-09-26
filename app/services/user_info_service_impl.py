# app/services/user_info_service_impl.py
from app.services.user_info_service import UserInfoService

class UserInfoServiceImpl(UserInfoService):
    def get_user_info(self, user_id: str) -> dict:
        # Aquí podrías implementar la lógica para obtener la información del usuario
        # Por ejemplo, consultar una base de datos o un servicio externo
        # En este ejemplo, devolvemos información estática
        return {
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }