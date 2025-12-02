# src/config.py
import redis
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# --- CONFIGURACIÓN DE INFRAESTRUCTURA ---
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# --- CONFIGURACIÓN DE MODELOS ---
MODEL_NAME = 'all-MiniLM-L6-v2'

# --- SINGLETON DE CONEXIÓN (Patrón de diseño) ---
# Creamos una única función para conectarnos, usada por todos los agentes.
def get_redis_client():
    return redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=os.getenv("REDIS_PASSWORD"),
        decode_responses=False # Importante para vectores
    )