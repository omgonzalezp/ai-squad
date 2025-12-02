

# NOMBRE CODIGO: YELLOW JACKET

## Scope del Proyecto

El objetivo de "ai-squad" es crear una plataforma donde un equipo de agentes de IA pueda desarrollar soluciones de software de forma automatizada, sin necesidad de contratar personas. El sistema debe:

1. Levantar la infraestructura básica con Docker, Redis y PostgreSQL.
2. Permitir la ingesta de información (archivos TXT/PDF) y almacenarla en Redis.
3. Implementar un agente de búsqueda que recupere información relevante desde Redis según una consulta.
4. (Opcional) Integrar una API de IA (como OpenAI/Copilot) para generar respuestas automáticas basadas en la información almacenada.

El objetivo es facilitar el desarrollo y consulta de soluciones, usando agentes automatizados y almacenamiento eficiente, para crear productos que puedan venderse o usarse en otros proyectos.

---

# Sprint Backlog

## Fase 1: Infraestructura (Cimientos)
- [x] Instalar Docker y levantar contenedores.
- [x] Desplegar Redis y PostgreSQL con configuración segura.
- [x] Preparar entorno Python e instalar librerías clave (redis, numpy, drivers de IA).

## Fase 2: Ingesta de Información
- [x] Conexión: `ingestar.py` conecta correctamente con Redis.
- [ ] Lectura: Agregar funciones para leer archivos TXT y PDF locales.
- [ ] Almacenamiento: Guardar el contenido leído en Redis con una clave identificadora.
- [ ] Validación: Verificar que los datos se guardaron correctamente y mostrar mensajes de éxito/error.

## Fase 3: Búsqueda y Consulta
- [ ] Script de búsqueda (`buscar.py`): Permitir buscar texto relevante en Redis según una consulta.

## Fase 4: Integración IA (Opcional)
- [ ] Conexión con API de IA (OpenAI/Copilot) para generar respuestas automáticas basadas en la información almacenada.

- [ ] Paso 2 (La Búsqueda): Un script (`buscar.py`) que, cuando escribas una pregunta, encuentre el texto correcto en Redis. (**Pendiente**)

## Fase 3: Integración IA

- [ ] Paso 3 (La Conexión): Solo si el paso 2 funciona, conectar la API de OpenAI/Copilot para que redacte la respuesta final. (**Pendiente**)

