# Assistant App

Esta aplicación es un asistente basado en Flask y Flask-SocketIO que utiliza OpenAI para generar respuestas basadas en la entrada del usuario. Además, procesa y consulta información de archivos PDF almacenados en ChromaDB para proporcionar respuestas más precisas y contextualizadas.

## Características

- Comunicación en tiempo real utilizando Flask-SocketIO.
- Generación de respuestas utilizando la API de OpenAI.
- Procesamiento de archivos PDF para extraer y vectorizar fragmentos de texto.
- Almacenamiento y consulta de fragmentos de texto en ChromaDB.
- Gestión de información del usuario, como nombre y correo electrónico.

## Requisitos

- Python 3.7 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/assistant-app.git
   cd assistant-app
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:

   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```env
   OPENAI_API_KEY=tu_clave_de_api_de_openai
   ```

## Configuración

1. **Archivos PDF**: Coloca los archivos PDF que deseas procesar en la carpeta `files/`.

2. **Lista de Rutas de Archivos PDF**: Edita la lista `pdf_paths` en `app.py` para incluir las rutas de los archivos PDF que deseas procesar:

   ```python
   pdf_paths = [
       "files/encomiendas.pdf",
       # Agrega más rutas de archivos PDF aquí
   ]
   ```

## Ejecución

1. Inicia la aplicación:

   ```bash
   python app.py
   ```

2. Abre tu navegador y ve a `http://localhost:5000` para interactuar con el asistente.

## Uso

1. **Interacción con el Asistente**: Escribe mensajes en la interfaz web para interactuar con el asistente. El asistente utilizará la API de OpenAI para generar respuestas y consultar información relevante de los archivos PDF procesados.

2. **Gestión de Información del Usuario**: El asistente puede solicitar y almacenar información del usuario, como su nombre y correo electrónico, para proporcionar respuestas más personalizadas.

## Estructura del Proyecto

```
assistant-app/
│
├── app/
│   ├── modules/
│   │   ├── embedding_processing.py
│   │   ├── nombre_extractor.py
│   │   └── pdf_processing.py
│   ├── router/
│   │   └── routes.py
│   ├── services/
│   │   ├── chromadb_service.py
│   │   ├── openai_service.py
│   │   ├── socket_service.py
│   │   ├── system_message_service.py
│   │   └── user_info_service.py
│   └── templates/
│       └── index.html
│
├── app.py
├── requirements.txt
└── .env
```

## TODOS
- Agregar registro de usuarios
- Buscar información de usuarios ya contactados
- ~~Grabar las conversaciones~~
- revisar las conversaciones por usuario para contexto
- Agregar acciones para RESTApi

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias para mejorar la aplicación, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por usar Assistant App! Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarnos.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de [gerardo.belot@gmail.com](mailto:gerardo.belot@gmail.com).

---

¡Gracias por visitar este repositorio! Espero que encuentres útil este servicio de chatbot basado en OpenAI.