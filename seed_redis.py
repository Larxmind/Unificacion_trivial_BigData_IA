import redis
import json
import os
from dotenv import load_dotenv

# Cargar configuración desde .env
load_dotenv()

# Uso de variables de entorno (requisito técnico)
r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'localhost'), 
    port=int(os.getenv('REDIS_PORT', 6379)), 
    decode_responses=True
)

# Lista de 50 preguntas de Ciencias
preguntas_ciencia = [
    # --- NIVEL FÁCIL ---
    {"key": "trivia:sci:1", "val": {"txt": "¿Cuál es el planeta rojo?", "opts": ["Júpiter", "Marte", "Saturno", "Venus"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T10:00:00Z"}},
    {"key": "trivia:sci:2", "val": {"txt": "¿Cuál es el órgano más grande del cuerpo humano?", "opts": ["Corazón", "Hígado", "Piel", "Pulmones"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T10:05:00Z"}},
    {"key": "trivia:sci:3", "val": {"txt": "¿Qué gas necesitan los humanos para respirar?", "opts": ["Nitrógeno", "Dióxido de carbono", "Oxígeno", "Argón"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T10:10:00Z"}},
    {"key": "trivia:sci:4", "val": {"txt": "¿Cuántos planetas hay en el sistema solar?", "opts": ["7", "8", "9", "10"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T10:15:00Z"}},
    {"key": "trivia:sci:5", "val": {"txt": "¿Cuál es el símbolo químico del oro?", "opts": ["Ag", "Au", "Fe", "Pb"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T10:20:00Z"}},
    {"key": "trivia:sci:6", "val": {"txt": "¿Cómo se llama el centro de un átomo?", "opts": ["Corteza", "Núcleo", "Protón", "Electrón"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T10:25:00Z"}},
    {"key": "trivia:sci:7", "val": {"txt": "¿Cuál es el animal terrestre más rápido?", "opts": ["León", "Guepardo", "Tigre", "Caballo"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T10:30:00Z"}},
    {"key": "trivia:sci:8", "val": {"txt": "¿Qué parte de la célula contiene el ADN?", "opts": ["Citoplasma", "Membrana", "Núcleo", "Mitocondria"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T10:35:00Z"}},
    {"key": "trivia:sci:9", "val": {"txt": "¿En qué estado se encuentra el agua a 0°C?", "opts": ["Líquido", "Gaseoso", "Sólido", "Plasma"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T10:40:00Z"}},
    {"key": "trivia:sci:10", "val": {"txt": "¿Quién formuló la teoría de la relatividad?", "opts": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Marie Curie"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T10:45:00Z"}},

    # --- NIVEL MEDIO ---
    {"key": "trivia:sci:11", "val": {"txt": "¿Cuál es el pH neutro?", "opts": ["0", "7", "14", "5"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:00:00Z"}},
    {"key": "trivia:sci:12", "val": {"txt": "¿Qué tipo de sangre es conocida como el donante universal?", "opts": ["A+", "B-", "O-", "AB+"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T11:05:00Z"}},
    {"key": "trivia:sci:13", "val": {"txt": "¿Cuál es la principal fuente de energía de la Tierra?", "opts": ["El Sol", "La Luna", "El viento", "El núcleo terrestre"], "ans_idx": 0, "diff": "medio", "tstamp": "2025-12-23T11:10:00Z"}},
    {"key": "trivia:sci:14", "val": {"txt": "¿Cómo se llama el proceso por el cual las plantas fabrican su alimento?", "opts": ["Respiración", "Combustión", "Fotosíntesis", "Ósmosis"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T11:15:00Z"}},
    {"key": "trivia:sci:15", "val": {"txt": "¿Qué vitamina produce el cuerpo al exponerse al sol?", "opts": ["Vitamina A", "Vitamina C", "Vitamina D", "Vitamina B12"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T11:20:00Z"}},
    {"key": "trivia:sci:16", "val": {"txt": "¿Cuál es el metal más abundante en la corteza terrestre?", "opts": ["Hierro", "Aluminio", "Cobre", "Zinc"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:25:00Z"}},
    {"key": "trivia:sci:17", "val": {"txt": "¿Qué rama de la ciencia estudia los fósiles?", "opts": ["Arqueología", "Paleontología", "Geología", "Biología"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:30:00Z"}},
    {"key": "trivia:sci:18", "val": {"txt": "¿Cuál es la velocidad del sonido aproximadamente?", "opts": ["343 m/s", "1200 m/s", "300,000 km/s", "50 m/s"], "ans_idx": 0, "diff": "medio", "tstamp": "2025-12-23T11:35:00Z"}},
    {"key": "trivia:sci:19", "val": {"txt": "¿Cuál es la galaxia más cercana a la Vía Láctea?", "opts": ["Sagitario", "Andrómeda", "Magallanes", "Sombrero"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:40:00Z"}},
    {"key": "trivia:sci:20", "val": {"txt": "¿Cuántos huesos tiene el cuerpo humano adulto?", "opts": ["150", "206", "300", "250"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:45:00Z"}},
    {"key": "trivia:sci:21", "val": {"txt": "¿Qué gas es el responsable del efecto invernadero en mayor medida?", "opts": ["Oxígeno", "CO2", "Metano", "Ozono"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:50:00Z"}},
    {"key": "trivia:sci:22", "val": {"txt": "¿Quién descubrió la penicilina?", "opts": ["Louis Pasteur", "Alexander Fleming", "Gregor Mendel", "Charles Darwin"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T11:55:00Z"}},
    {"key": "trivia:sci:23", "val": {"txt": "¿Cuál es el único mamífero capaz de volar?", "opts": ["Avestruz", "Pingüino", "Murciélago", "Ardilla voladora"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T12:00:00Z"}},
    {"key": "trivia:sci:24", "val": {"txt": "¿Qué mide la escala de Richter?", "opts": ["Presión", "Humedad", "Sismos", "Temperatura"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T12:05:00Z"}},
    {"key": "trivia:sci:25", "val": {"txt": "¿Cuál es el planeta más grande de nuestro sistema?", "opts": ["Saturno", "Neptuno", "Júpiter", "Urano"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T12:10:00Z"}},

    # --- NIVEL DIFÍCIL ---
    {"key": "trivia:sci:26", "val": {"txt": "¿Cuál es el único metal líquido a temperatura ambiente?", "opts": ["Plomo", "Mercurio", "Bario", "Cesio"], "ans_idx": 1, "diff": "difícil", "tstamp": "2025-12-23T12:15:00Z"}},
    {"key": "trivia:sci:27", "val": {"txt": "¿Qué partícula subatómica tiene carga negativa?", "opts": ["Protón", "Neutrón", "Electrón", "Quark"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T12:20:00Z"}},
    {"key": "trivia:sci:28", "val": {"txt": "¿Cuál es la unidad de medida de la resistencia eléctrica?", "opts": ["Voltio", "Amperio", "Ohmio", "Vatio"], "ans_idx": 2, "diff": "difícil", "tstamp": "2025-12-23T12:25:00Z"}},
    {"key": "trivia:sci:29", "val": {"txt": "¿A qué temperatura el agua alcanza su máxima densidad?", "opts": ["0°C", "4°C", "100°C", "-4°C"], "ans_idx": 1, "diff": "difícil", "tstamp": "2025-12-23T12:30:00Z"}},
    {"key": "trivia:sci:30", "val": {"txt": "¿Cuántos corazones tiene un pulpo?", "opts": ["1", "2", "3", "8"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T12:35:00Z"}},
    {"key": "trivia:sci:31", "val": {"txt": "¿Cuál es el elemento químico con el número atómico 1?", "opts": ["Helio", "Oxígeno", "Hidrógeno", "Carbono"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T12:40:00Z"}},
    {"key": "trivia:sci:32", "val": {"txt": "¿Qué hueso es el más pequeño del cuerpo humano?", "opts": ["Fémur", "Estribo", "Radio", "Falange"], "ans_idx": 1, "diff": "difícil", "tstamp": "2025-12-23T12:45:00Z"}},
    {"key": "trivia:sci:33", "val": {"txt": "¿Qué gas compone el 78% de la atmósfera terrestre?", "opts": ["Oxígeno", "Argón", "Nitrógeno", "Metano"], "ans_idx": 2, "diff": "difícil", "tstamp": "2025-12-23T12:50:00Z"}},
    {"key": "trivia:sci:34", "val": {"txt": "¿Cuál es la velocidad de escape de la Tierra?", "opts": ["11.2 km/s", "5.5 km/s", "30 km/s", "100 km/s"], "ans_idx": 0, "diff": "difícil", "tstamp": "2025-12-23T12:55:00Z"}},
    {"key": "trivia:sci:35", "val": {"txt": "¿En qué parte del Sol se produce la fusión nuclear?", "opts": ["Corona", "Fotosfera", "Núcleo", "Zona convectiva"], "ans_idx": 2, "diff": "difícil", "tstamp": "2025-12-23T13:00:00Z"}},
    {"key": "trivia:sci:36", "val": {"txt": "¿Qué ley establece que la energía no se crea ni se destruye?", "opts": ["Leyes de Newton", "Termodinámica", "Ley de Ohm", "Ley de Hooke"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T13:05:00Z"}},
    {"key": "trivia:sci:37", "val": {"txt": "¿Quién propuso el modelo atómico de niveles de energía?", "opts": ["Dalton", "Bohr", "Rutherford", "Thomson"], "ans_idx": 1, "diff": "difícil", "tstamp": "2025-12-23T13:10:00Z"}},
    {"key": "trivia:sci:38", "val": {"txt": "¿Cuál es el principal componente de las estrellas?", "opts": ["Helio", "Hierro", "Hidrógeno", "Silicio"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T13:15:00Z"}},
    {"key": "trivia:sci:39", "val": {"txt": "¿Qué tipo de lente se usa para corregir la miopía?", "opts": ["Convexa", "Divergente", "Plana", "Bifocal"], "ans_idx": 1, "diff": "difícil", "tstamp": "2025-12-23T13:20:00Z"}},
    {"key": "trivia:sci:40", "val": {"txt": "¿Cuántos cromosomas tiene el ser humano?", "opts": ["24", "48", "46", "23"], "ans_idx": 2, "diff": "medio", "tstamp": "2025-12-23T13:25:00Z"}},
    {"key": "trivia:sci:41", "val": {"txt": "¿Cuál es la unidad de fuerza en el SI?", "opts": ["Julio", "Vatio", "Newton", "Pascal"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T13:30:00Z"}},
    {"key": "trivia:sci:42", "val": {"txt": "¿Cuál es el metal con el punto de fusión más alto?", "opts": ["Hierro", "Oro", "Wolframio", "Platino"], "ans_idx": 2, "diff": "difícil", "tstamp": "2025-12-23T13:35:00Z"}},
    {"key": "trivia:sci:43", "val": {"txt": "¿Qué tipo de roca es el mármol?", "opts": ["Ígnea", "Metamórfica", "Sedimentaria", "Volcánica"], "ans_idx": 1, "diff": "medio", "tstamp": "2025-12-23T13:40:00Z"}},
    {"key": "trivia:sci:44", "val": {"txt": "¿Qué orgánulo celular se encarga de la síntesis de proteínas?", "opts": ["Lisosoma", "Vacuola", "Ribosoma", "Aparato de Golgi"], "ans_idx": 2, "diff": "difícil", "tstamp": "2025-12-23T13:45:00Z"}},
    {"key": "trivia:sci:45", "val": {"txt": "¿Cómo se llama el miedo a las arañas?", "opts": ["Acrofobia", "Aracnofobia", "Claustrofobia", "Agorafobia"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T13:50:00Z"}},
    {"key": "trivia:sci:46", "val": {"txt": "¿Cuál es la velocidad de la luz?", "opts": ["300,000 km/s", "150,000 km/s", "1,000 km/h", "343 m/s"], "ans_idx": 0, "diff": "fácil", "tstamp": "2025-12-23T13:55:00Z"}},
    {"key": "trivia:sci:47", "val": {"txt": "¿Quién descubrió la radioactividad?", "opts": ["Marie Curie", "Henri Becquerel", "Rutherford", "Fermi"], "ans_idx": 1, "diff": "difícil", "tstamp": "2025-12-23T14:00:00Z"}},
    {"key": "trivia:sci:48", "val": {"txt": "¿Qué planeta tiene los anillos más visibles?", "opts": ["Urano", "Saturno", "Neptuno", "Júpiter"], "ans_idx": 1, "diff": "fácil", "tstamp": "2025-12-23T14:05:00Z"}},
    {"key": "trivia:sci:49", "val": {"txt": "¿Cuál es el mineral más duro de la Tierra?", "opts": ["Cuarzo", "Rubí", "Diamante", "Grafito"], "ans_idx": 2, "diff": "fácil", "tstamp": "2025-12-23T14:10:00Z"}},
    {"key": "trivia:sci:50", "val": {"txt": "¿Cómo se llama la primera capa de la atmósfera?", "opts": ["Estratosfera", "Mesosfera", "Troposfera", "Exosfera"], "ans_idx": 2, "diff": "difícil", "tstamp": "2025-12-23T14:15:00Z"}}
]
for p in preguntas_ciencia:
    r.set(p["key"], json.dumps(p["val"]))

print(f"✅ Se han sembrado {len(preguntas_ciencia)} preguntas de Ciencias en Redis.")