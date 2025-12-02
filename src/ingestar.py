
# --- INGESTA DE ARCHIVOS TXT Y PDF ---
import os
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

def get_redis_client():
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )

def read_txt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def read_pdf_file(filepath):
    try:
        import PyPDF2
    except ImportError:
        raise ImportError("PyPDF2 no está instalado. Instala con 'uv pip install PyPDF2'")
    text = ""
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

if __name__ == "__main__":
    client = get_redis_client()
    # Ejemplo de uso: ingesta de archivos en la carpeta '../data'
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if filename.lower().endswith('.txt'):
            content = read_txt_file(filepath)
        elif filename.lower().endswith('.pdf'):
            content = read_pdf_file(filepath)
        else:
            continue
        # Guarda el contenido en Redis con la clave igual al nombre del archivo
        client.set(filename, content)
        # Validar que el contenido se guardó correctamente
        saved = client.get(filename)
        if saved == content:
            print(f"✅ Archivo '{filename}' guardado y verificado en Redis.")
        else:
            print(f"❌ Error al guardar el archivo '{filename}' en Redis.")