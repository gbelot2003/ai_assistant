from flask import render_template, jsonify, request
import requests
from flask_socketio import emit
from app.services.conversation_service import ConversationService
from app.services.user_service import UserService

def configure_wsi_routes(app):
    @app.route('/wsi', methods=['GET'])
    def wsi():
        return render_template("wsi.html")
    
    # Endpoint para recibir la URL y el mensaje simulado desde la interfaz
    @app.route('/api/send_message', methods=['POST'])
    def send_message():
        data = request.json
        target_url = data.get('url')
        message_body = data.get('message', 'Este es un mensaje simulado desde Twilio')
        from_number = data.get('from_number', '+14155551234')  # Número simulado del remitente por defecto

        # Obtener o crear el usuario
        user = UserService().get_or_create_user(from_number)

        # Simulando el POST de Twilio
        simulated_twilio_post = {
            "SmsMessageSid": "SM12345678901234567890123456789012",
            "NumMedia": "0",
            "SmsSid": "SM12345678901234567890123456789012",
            "SmsStatus": "received",
            "Body": message_body,  # Utiliza la variable message_body definida previamente o asigna un mensaje manualmente
            "To": "+14155552671",  # Número de tu cuenta Twilio para pruebas
            "NumSegments": "1",
            "MessageSid": "SM12345678901234567890123456789012",
            "AccountSid": "AC12345678901234567890123456789012",  # SID de cuenta simulado
            "From": from_number,  # Número simulado del remitente, configurable desde la interfaz
            "ApiVersion": "2010-04-01",
            "ProfileName": "Twilio Simulator",  # Nombre del perfil simulado
            "WaId": from_number.replace('+', ''),  # ID simulado del usuario en WhatsApp
            "ChannelPrefix": "whatsapp",  # Canal desde el cual proviene el mensaje
            "Type": "TextMessage"  # Tipo de mensaje
        }

        # Envío del POST a la URL proporcionada
        try:
            response = requests.post(target_url, data=simulated_twilio_post)
            response_data = response.json()  # Asegurarse de que la respuesta sea un JSON

            # Guardar la conversación
            ConversationService().add_conversation(user.id, message_body, response_data.get('message'))

            return jsonify({"status": "success", "response": response_data})
        except Exception as e:
            return jsonify({"status": "error", "response": str(e)})