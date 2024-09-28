from flask_socketio import SocketIO, send
from app.services.openai_service import OpenAIService
from app.services.chromadb_service import search_in_chromadb
from app.modules.embedding_processing import get_embedding_for_chunk
from app.models.conversation import Conversation
from app.extensions import db

socketio = SocketIO()
openai_service = OpenAIService()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('message')
    def handle_message(message):
        # Buscar en ChromaDB los fragmentos más relevantes
        query_embedding = get_embedding_for_chunk(message)
        relevant_chunks = search_in_chromadb(query_embedding)
        
        # Generar respuesta utilizando los fragmentos relevantes
        response = openai_service.generate_response(message, relevant_chunks)
        send(response, broadcast=True)

        # Guardar la conversación en la base de datos
        conversation = Conversation(user_message=message, bot_response=response)
        db.session.add(conversation)
        db.session.commit()

    return socketio