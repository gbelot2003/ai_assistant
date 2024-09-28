from flask import render_template, jsonify, request
from app.services.socket_service import init_socketio
from app.services.conversation_service import ConversationService
from app.services.user_service import UserService
from app.router.wsi_routes import configure_wsi_routes
from app.router.twilio_routes import configure_twilio_routes

def configure_routes(app, socketio):
    # Configurar las rutas de WSI y send_message
    configure_wsi_routes(app)

    # Configurar las rutas de Twilio
    configure_twilio_routes(app)

    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")

    # Ruta para obtener todas las conversaciones
    @app.route("/conversations")
    def get_conversations():
        user_id = request.args.get('user_id')  # Obtener el identificador del usuario o sesión
        conversations = ConversationService().get_conversations(user_id)
        return jsonify([{
            'id': conv.id,
            'user_message': conv.user_message,
            'bot_response': conv.bot_response,
            'user_id': conv.user_id,
            'timestamp': conv.timestamp
        } for conv in conversations])

    # Ruta para verificar si un usuario existe
    @app.route("/check_user", methods=['GET'])
    def check_user():
        phone_number = request.args.get('phone_number')
        user = UserService().get_user_by_phone_number(phone_number)
        if user:
            return jsonify({"name": user.name})
        return jsonify({"name": None})

    # Ruta para registrar un usuario por webchat
    @app.route("/register_user", methods=['POST'])
    def register_user():
        data = request.json
        phone_number = data.get('phone_number') # type: ignore
        name = data.get('name') # type: ignore

        if not phone_number or not name:
            return jsonify({"status": "error", "message": "Phone number and name are required"}), 400

        user = UserService().get_or_create_user(phone_number, name)
        return jsonify({"status": "success", "user_id": user.id})

    # Inicializar socketio con los servicios
    init_socketio(app)