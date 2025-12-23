# 📚 Proyecto de Unificación Trivial Big Data IA

Este proyecto implementa un pipeline de datos híbrido para recolectar, normalizar y limpiar preguntas de trivia desde 5 fuentes de datos distintas, enriqueciendo el resultado mediante Inteligencia Artificial.

## 🚀 Arquitectura del Sistema
El script actúa como un puente (bridge) que conecta con:
* **MySQL (Docker):** Datos locales relacionales.
* **Redis (Docker):** Caché de preguntas de Ciencias.
* **MongoDB (Docker):** Documentos de Arte en formato internacionalizado.
* **AWS DynamoDB:** Base de datos NoSQL Cloud (Espectáculo).
* **AWS RDS (PostgreSQL):** Base de datos relacional Cloud (Historia).

## 🛠️ Requisitos Técnicos Cumplidos
1.  **Normalización:** Clase `PreguntasUnificadas` que estandariza esquemas heterogéneos.
2.  **Limpieza:** Eliminación de espacios en blanco y conversión de respuestas a **MAYÚSCULAS**.
3.  **Resiliencia:** Gestión de errores independiente (si una DB cae, el resto continúa).
4.  **Salida Estándar:** Generación de un set unificado en formato **JSON**.
5.  **IA:** Clasificación automática de categorías usando `BART Large MNLI`.

## 📦 Instalación y Uso
1. Instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

2. Configurar el archivo .env con tus credenciales de AWS y bases de datos locales.
3. Ejecutar el pipeline:
```bash
python main.py
```
## 📊  Formato de salida (JSON)
Cada pregunta procesada sigue este esquema:
```json
{
    "fuente_origen": "Nombre de la Fuente",
    "pregunta": "Texto de la pregunta",
    "opciones": ["A", "B", "C", "D"],
    "respuesta_correcta": "RESPUESTA MAYÚSCULAS",
    "dificultad": "Baja/Media/Alta",
    "fecha_creacion": "YYYY-MM-DD"
}
```