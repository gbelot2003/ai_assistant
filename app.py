import os
from flask import Flask
from flask_socketio import SocketIO
from app.router.routes import configure_routes
from app.services.chromadb_service import store_chunks_in_chromadb
from app.modules.pdf_processing import extract_text_from_pdf, split_text_into_chunks
from app.modules.embedding_processing import get_embedding_for_chunk
from dotenv import load_dotenv
from app.config import Config
from app.extensions import db

load_dotenv()

template_dir = os.path.abspath('app/templates')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)

db.init_app(app)
socketio = SocketIO(app)

# Lista de rutas de archivos PDF
pdf_paths = [
    "files/encomiendas.pdf",
    # Agrega más rutas de archivos PDF aquí
]

# Procesar cada PDF al iniciar la aplicación
for pdf_path in pdf_paths:
    try:
        text = extract_text_from_pdf(pdf_path)
        chunks = split_text_into_chunks(text)
        chunks_with_embeddings = [(chunk, get_embedding_for_chunk(chunk)) for chunk in chunks]
        store_chunks_in_chromadb(chunks_with_embeddings, pdf_path)
    except Exception as e:
        print(f"Error procesando el PDF {pdf_path}: {e}")

# Configurar las rutas
configure_routes(app, socketio)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)