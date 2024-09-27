# OpenAI Chatbot Service

Este repositorio contiene un servicio de chatbot basado en OpenAI que interactúa con usuarios para obtener información personal como nombres y correos electrónicos, y responde a consultas específicas como información, horarios y cotizaciones.

## Descripción

El servicio de chatbot utiliza la API de OpenAI para generar respuestas basadas en las entradas del usuario. El sistema está diseñado para:

1. **Obtener Información Personal**: El chatbot puede solicitar y almacenar el nombre y el correo electrónico del usuario.
2. **Responder a Consultas Específicas**: El chatbot solo solicita el correo electrónico cuando el usuario pregunta por información, horarios o cotizaciones.
3. **Manejar Múltiples Interacciones**: El sistema puede manejar múltiples interacciones con el usuario, almacenando la información obtenida para futuras consultas.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
openai-chatbot-service/
│
├── app/
│   ├── services/
│   │   ├── nombre_service.py
│   │   ├── user_info_service.py
│   │   ├── system_message_service.py
│   │   └── openai_service.py
│   ├── modules/
│   │   ├── nombre_extractor.py
│   │   └── ...
│   └── ...
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

### Directorios Principales

- **app/services/**: Contiene los servicios principales del chatbot, incluyendo la lógica para manejar nombres, información del usuario, mensajes del sistema y la interacción con OpenAI.
- **app/modules/**: Contiene módulos auxiliares, como el extractor de nombres.

### Archivos Principales

- **openai_service.py**: El servicio principal que maneja las interacciones con OpenAI.
- **user_info_service.py**: Servicio que centraliza la información del usuario (nombre, correo electrónico, etc.).
- **system_message_service.py**: Servicio que genera mensajes del sistema basados en la entrada del usuario.
- **nombre_service.py**: Servicio especializado en manejar nombres.
- **nombre_extractor.py**: Módulo que extrae nombres de texto utilizando expresiones regulares.

## Configuración

### Requisitos

- Python 3.7 o superior
- API Key de OpenAI

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/openai-chatbot-service.git
   cd openai-chatbot-service
   ```

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno en un archivo `.env`:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Ejecución

Para ejecutar el servicio, puedes crear un script de Python que utilice `OpenAIService`:

```python
from app.services.openai_service import OpenAIService

openai_service = OpenAIService()
prompt = "Necesito información sobre los horarios de la tienda."
response = openai_service.generate_response(prompt)
print(response)
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de [gerardo.belot@gmail.com](mailto:gerardo.belot@gmail.com).

---

¡Gracias por visitar este repositorio! Espero que encuentres útil este servicio de chatbot basado en OpenAI.