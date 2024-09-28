# app/router/twilio_routes.py

from flask import request, jsonify
from app.services.openai_service import OpenAIService
from app.services.chromadb_service import search_in_chromadb
from app.modules.embedding_processing import get_embedding_for_chunk
from app.models.conversation import Conversation
from app.extensions import db

def configure_twilio_routes(app):
    openai_service = OpenAIService()

    @app.route('/api/twilio', methods=['POST'])
    def twilio_webhook():

        print(f"API: {request}")
        
        # Obtener el mensaje de Twilio
        message_body = request.form.get('Body')
        from_number = request.form.get('From')

       
        # Buscar en ChromaDB los fragmentos más relevantes
        query_embedding = get_embedding_for_chunk(message_body)
        relevant_chunks = search_in_chromadb(query_embedding)
        
        # Generar respuesta utilizando los fragmentos relevantes
        response = openai_service.generate_response(message_body, relevant_chunks)

        # Guardar la conversación en la base de datos
        conversation = Conversation(user_message=message_body, bot_response=response, user_id=from_number) # type: ignore
        db.session.add(conversation)
        db.session.commit()

        # Devolver la respuesta a Twilio
        return jsonify({"message": response})