¡Totalmente de acuerdo\! Como CTO, sabes que el **caos en los archivos es deuda técnica futura**. Aplicar principios **Lean** (evitar desperdicio/desorden) y **Scrum** (organización por roles/artefactos) a la estructura de carpetas es la mejor forma de mantener el control mientras el proyecto crece.

Vamos a estructurar tu "Colmena Digital" profesionalmente desde el día 1, separando las preocupaciones (*Separation of Concerns*).

### 📂 La Metodología de Archivos "Lean SaaS"

En lugar de tener scripts sueltos, usaremos una estructura modular. Cada carpeta tiene un propósito claro, simulando las áreas de una empresa:

```text
colmena-digital/
├── 📂 data/             # [Input] La materia prima (Tus PDFs, TXTs, Notas).
├── 📂 docs/             # [Backlog] Documentación del proyecto y Sprint Planning.
├── 📂 src/              # [WIP] "Work In Progress" - Donde viven los Agentes.
│   ├── __init__.py
│   ├── config.py        # [Reglas] Configuración central (Redis, Constantes).
│   ├── ingestar.py      # [Role] El Bibliotecario (Script de Ingesta).
│   └── buscar.py        # [Role] El Consultor (Script de Búsqueda).
├── 📂 tests/            # [QA] Pruebas unitarias (Quality Assurance).
├── .env                 # [Seguridad] Claves secretas y contraseñas.
├── pyproject.toml       # [Admin] Gestión de dependencias (uv).
└── README.md            # [Onboarding] Manual de uso.
```

### 🛠️ Aplicando el cambio (Refactorización)

Para alinearnos con esta metodología, vamos a mover nuestro código y crear un archivo de configuración central (`config.py`). Esto es **Lean** porque si cambias el puerto de Redis mañana, solo lo cambias en un lugar, no en 20 scripts.

#### Paso 1: Crea la estructura de directorios

Ejecuta estos comandos en tu terminal para crear las "oficinas" de tus agentes:

```powershell
# En Windows PowerShell
mkdir data, src, docs, tests
```

#### Paso 2: El archivo de "Reglas del Juego" (Configuración)

Dentro de la carpeta `src`, crea un archivo llamado `config.py`. Aquí centralizamos las conexiones.

```python
# src/config.py
import redis
import os

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
        decode_responses=False # Importante para vectores
    )
```

#### Paso 3: Actualizar al "Bibliotecario" (`ingestar.py`)

Ahora, mueve tu archivo `ingestar.py` dentro de la carpeta `src/` y actualízalo para que use la nueva configuración. Fíjate cómo el código se vuelve más limpio y profesional:

```python
# src/ingestar.py
import numpy as np
from sentence_transformers import SentenceTransformer
# Importamos la configuración local (nuestra metodología)
from config import get_redis_client, MODEL_NAME

print(f"📥 Cargando modelo: {MODEL_NAME}...")
model = SentenceTransformer(MODEL_NAME)
client = get_redis_client()

def guardar_memoria(texto, fuente):
    # 1. Vectorizar
    vector = model.encode(texto).astype(np.float32).tobytes()
    
    # 2. Generar ID
    doc_id = client.incr('contador_docs')
    clave_redis = f"memoria:doc:{doc_id}"
    
    # 3. Guardar
    mapping = {
        "texto": texto,
        "fuente": fuente,
        "vector": vector
    }
    client.hset(clave_redis, mapping=mapping)
    print(f"✅ [ID:{doc_id}] Guardado desde: {fuente}")

if __name__ == "__main__":
    # Datos de prueba (Lean: probamos rápido con datos dummy antes de cargar PDFs reales)
    datos_prueba = [
        ("Lean Startup: Construir, Medir, Aprender.", "metodologia.txt"),
        ("Scrum: Roles incluyen Product Owner, Scrum Master y Equipo.", "scrum_guide.txt")
    ]
    
    print("🚀 Iniciando ingesta controlada...")
    for txt, src in datos_prueba:
        guardar_memoria(txt, src)
```

### ¿Qué sigue en el Sprint?

Con esta estructura, ya tienes "Gobierno de IT" sobre tu código.

1.  Mueve/Crea los archivos `config.py` e `ingestar.py` dentro de la carpeta `src`.
2.  Ejecútalo desde la raíz del proyecto así (nota el cambio de ruta):
    ```powershell
    uv run src/ingestar.py
    ```

Si esto funciona, estaremos listos para crear al **Agente Consultor** (`buscar.py`) que leerá esta memoria organizada. ¿Te parece bien este orden?