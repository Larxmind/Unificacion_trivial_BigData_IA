import json
import mysql.connector
import psycopg2
import redis
import boto3 
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from transformers import pipeline
import random

load_dotenv()

db_user = os.getenv('MYSQL_USER')
db_pass = os.getenv('MYSQL_PASS')
db_host = os.getenv('MYSQL_HOST')

# 2. Clase de Unificación
class PreguntasUnificadas:
    def __init__(self, fuente, pregunta, opciones, respuesta, dificultad, fecha):
        self.fuente_origen = fuente
        self.pregunta = self.limpiar(pregunta)
        self.opciones = [self.limpiar(opt) for opt in opciones]
        self.respuesta_correcta = self.limpiar(respuesta, forzar_mayusculas=True)
        self.dificultad = self.normalizar_dificultad(dificultad)
        self.fecha_creacion = str(fecha)[:10]

    @staticmethod
    def limpiar(texto, forzar_mayusculas=False):
        if not texto: return ""
        limpio = str(texto).strip()
        return limpio.upper() if forzar_mayusculas else limpio

    @staticmethod
    def normalizar_dificultad(dif):
        dif = str(dif).lower()
        if dif in ['1', 'baja', 'fácil', 'easy']: return 'Baja'
        if dif in ['2', 'medio', 'media', 'normal']: return 'Media'
        if dif in ['3', 'alta', 'difícil', 'hard', 'experto']: return 'Alta'
        return 'Media'

    def to_dict(self):
        return {
            "fuente_origen": self.fuente_origen,
            "pregunta": self.pregunta,
            "opciones": self.opciones,
            "respuesta_correcta": self.respuesta_correcta,
            "dificultad": self.dificultad,
            "fecha_creacion": self.fecha_creacion
        }
    
# 3. Funciones de Carga (MySQL, Redis, Mongo, Dynamo, RDS)
def cargar_preguntas_mysql(): 
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASS'),
            database=os.getenv('MYSQL_DB')
        )
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT p.id, p.texto, p.nivel, p.fecha_registro, o.texto_opcion, o.es_correcta
            FROM preguntas p
            JOIN opciones o ON p.id = o.pregunta_id
            ORDER BY p.id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows: return []
        temporal_dict = {}
        for row in rows:
            p_id = row['id']
            if p_id not in temporal_dict:
                temporal_dict[p_id] = {"texto": row['texto'], "nivel": row['nivel'], "fecha": row['fecha_registro'], "opciones": [], "correcta": ""}
            temporal_dict[p_id]["opciones"].append(row['texto_opcion'])
            if row['es_correcta']: temporal_dict[p_id]["correcta"] = row['texto_opcion']
        
        return [PreguntasUnificadas("MySQL", info['texto'], info['opciones'], info['correcta'], info['nivel'], str(info['fecha'])).to_dict() for info in temporal_dict.values()]
    except Exception as e:
        print(f"❌ Error en MySQL: {e}"); return []
    finally:
        if 'conn' in locals() and conn.is_connected(): conn.close()

def cargar_preguntas_redis():
    try:
        r = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), decode_responses=True)
        keys = r.keys("trivia:game:*")
        preguntas_redis = []
        for key in keys:
            data = json.loads(r.get(key))
            preguntas_redis.append(PreguntasUnificadas("Redis (Ciencias)", data['txt'], data['opts'], data['opts'][data['ans_idx']], data['diff'], data['tstamp'].split('T')[0]).to_dict())
        return preguntas_redis
    except Exception as e:
        print(f"❌ Error en Redis: {e}"); return []

def cargar_preguntas_mongo():
    try:
        client = MongoClient(os.getenv('MONGO_URI'))
        db = client['trivia_db']
        cursor = db['preguntas'].find({"localizations.language": "es"})
        preguntas_mongo = []
        for doc in cursor:
            traduccion_es = next(l for l in doc['localizations'] if l['language'] == 'es')
            preguntas_mongo.append(PreguntasUnificadas("MongoDB (Arte)", traduccion_es['text'], traduccion_es['items'], traduccion_es['ok_item'], doc['difficulty'], doc['createdAt'].split('T')[0]).to_dict())
        return preguntas_mongo
    except Exception as e:
        print(f"❌ Error en MongoDB: {e}"); return []

def cargar_preguntas_dynamo():
    try:
        session = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_REGION')
        )
        table = session.resource('dynamodb').Table('TriviaEspectaculo')
        items = table.scan().get('Items', [])
        
        preguntas_dynamo = []
        for item in items:
            pregunta_obj = PreguntasUnificadas(
                fuente="DynamoDB (Espectáculo)",
                pregunta=item.get('question'),
                opciones=item.get('options', []),
                respuesta=item.get('answer'),
                dificultad=item.get('difficulty', 'Media'),
                fecha=item.get('timestamp', '2025-12-23')[:10] # Tomamos solo YYYY-MM-DD
            )
            preguntas_dynamo.append(pregunta_obj.to_dict())
            
        return preguntas_dynamo
    except Exception as e:
        print(f"❌ Error en DynamoDB: {e}")
        return []

def cargar_preguntas_rds():
    try:
        conn = psycopg2.connect(host=os.getenv('RDS_HOST'), user=os.getenv('RDS_USER'), password=os.getenv('RDS_PASS'), database=os.getenv('RDS_DB'))
        cursor = conn.cursor()
        cursor.execute("SELECT datos_pregunta FROM trivial_flat;")
        preguntas_rds = []
        for row in cursor.fetchall():
            partes = row[0].split('|')
            if len(partes) < 8: continue
            preguntas_rds.append(PreguntasUnificadas("AWS RDS (Historia)", partes[0], partes[3:7], partes[7], partes[1], partes[2]).to_dict())
        return preguntas_rds
    except Exception as e:
        print(f"❌ Error en RDS: {e}"); return []
    finally:
        if 'conn' in locals(): conn.close()

# 4. Función de Inteligencia Artificial
def pregunta_del_dia_ia(pool):
    pool_valido = [p for p in pool if p.get('pregunta') and p['pregunta'].strip()]
    
    if not pool_valido:
        print("⚠️ No hay preguntas válidas para la IA."); return

    print("\n🤖 Consultando con la IA de Hugging Face (Zero-Shot)...")
    
    pregunta_data = random.choice(pool_valido)
    texto = pregunta_data['pregunta']
    
    # Limpieza de caracteres extraños (encoding)
    try:
        texto_limpio = texto.encode('latin-1').decode('utf-8')
    except:
        texto_limpio = texto

    clasificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)
    categorias = ["Geografía", "Deportes", "Ciencias", "Historia", "Espectáculo", "Arte"]
    
    try:
        res = clasificador(texto_limpio, categorias)
        
        print(f"\n🌟 --- PREGUNTA DEL DÍA --- 🌟")
        print(f"Pregunta: {texto_limpio}")
        print(f"Fuente de origen: {pregunta_data['fuente_origen']}")
        print(f"🏷️ Categoría detectada: {res['labels'][0]} ({res['scores'][0]:.2%} de confianza)")
        print(f"✅ Respuesta correcta: {pregunta_data['respuesta_correcta']}")
        
    except Exception as e:
        print(f"❌ Error en la IA: {e}")

# --- BLOQUE EJECUCIÓN ---
if __name__ == "__main__":
    print(f"Conectando a {db_host}...")
    print("🚀 Iniciando recolección masiva de datos...")
    
    total_pool = []
    
    total_pool.extend(cargar_preguntas_mysql())
    total_pool.extend(cargar_preguntas_redis())
    total_pool.extend(cargar_preguntas_mongo())
    total_pool.extend(cargar_preguntas_dynamo())
    total_pool.extend(cargar_preguntas_rds())

    if total_pool:
        print("\n" + "="*25)
        print("SET UNIFICADO DE PREGUNTAS (JSON)")
        print("="*25)
        
        salida_json = json.dumps(total_pool, indent=4, ensure_ascii=False)
        print(salida_json)
        
        with open("unificado.json", "w", encoding="utf-8") as f:
            f.write(salida_json)
            
        print("\n" + "="*50)
        print(f"✅ ÉXITO: {len(total_pool)} preguntas normalizadas y exportadas.")
        print("="*50)
        

        print("\n--- BONUS: PROCESANDO PREGUNTA DEL DÍA CON IA ---")
        pregunta_del_dia_ia(total_pool)
    else:
        print("❌ Error: No se pudieron recuperar datos de ninguna fuente.")