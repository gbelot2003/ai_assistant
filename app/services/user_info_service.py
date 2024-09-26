# app/services/user_info_service.py
from abc import ABC, abstractmethod

class UserInfoService(ABC):
    @abstractmethod
    def get_user_info(self, user_id: str) -> dict:
        """Retorna un diccionario con el nombre y el correo electrónico del usuario."""
        pass