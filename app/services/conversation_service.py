from app.models.conversation import Conversation
from app.extensions import db

class ConversationService:
    def add_conversation(self, user_id, message, response):
        conversation = Conversation(user_id=user_id, user_message=message, bot_response=response)
        db.session.add(conversation)
        db.session.commit()

    def get_conversations(self, user_id):
        return Conversation.query.filter_by(user_id=user_id).all()