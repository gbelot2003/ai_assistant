from flask import render_template, jsonify, request
from app.services.socket_service import init_socketio
from app.models.conversation import Conversation
from app.extensions import db
from app.router.wsi_routes import configure_wsi_routes
from app.router.twilio_routes import configure_twilio_routes

def configure_routes(app, socketio):
    # Configurar las rutas de WSI y send_message
    configure_wsi_routes(app)

    # Configurar las rutas de Twilio
    configure_twilio_routes(app)

    # Inicializar socketio con los servicios
    init_socketio(app)

    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")

    # Ruta para obtener todas las conversaciones
    @app.route("/conversations")
    def get_conversations():
        user_id = request.args.get('user_id')  # Obtener el identificador del usuario o sesión
        if user_id:
            conversations = Conversation.query.filter_by(user_id=user_id).all()
        else:
            conversations = Conversation.query.all()
        return jsonify([{
            'id': conv.id,
            'user_message': conv.user_message,
            'bot_response': conv.bot_response,
            'user_id': conv.user_id,
            'timestamp': conv.timestamp
        } for conv in conversations])

