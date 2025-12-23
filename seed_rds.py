import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def cargar_rds_flat():
    try:
        conn = psycopg2.connect(
            host=os.getenv('RDS_HOST'),
            database=os.getenv('RDS_DB'),
            user=os.getenv('RDS_USER'),
            password=os.getenv('RDS_PASS'),
            port=5432  # El puerto por defecto de Postgres es 5432
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS trivial_flat (
                id SERIAL PRIMARY KEY,
                datos_pregunta TEXT NOT NULL
            );
        """)
        # Formato: Pregunta|Dificultad|Fecha|R1|R2|R3|R4|Correcta
        preguntas = [
            # GEOGRAFÍA
            "¿Cuál es el país más pequeño del mundo?|fácil|2025-12-23|Mónaco|Vaticano|San Marino|Andorra|Vaticano",
            "¿Qué río pasa por Londres?|fácil|2025-12-23|Sena|Danubio|Támesis|Rin|Támesis",
            "¿Cuál es la capital de Japón?|fácil|2025-12-23|Kioto|Osaka|Tokio|Hiroshima|Tokio",
            "¿En qué país está el Taj Mahal?|fácil|2025-12-23|Pakistán|India|Bangladesh|Nepal|India",
            "¿Qué océano baña las costas de Brasil?|fácil|2025-12-23|Pacífico|Índico|Ártico|Atlántico|Atlántico",
            "¿Cuál es el monte más alto de África?|medio|2025-12-23|Kenia|Kilimanjaro|Atlas|Everest|Kilimanjaro",
            "¿Qué país tiene más fronteras terrestres?|difícil|2025-12-23|Rusia|China|Brasil|India|China",
            "¿Cuál es la capital de Suiza?|medio|2025-12-23|Zúrich|Ginebra|Basilea|Berna|Berna",
            "¿Qué país es el mayor productor de café?|medio|2025-12-23|Colombia|Vietnam|Etiopía|Brasil|Brasil",
            "¿En qué mar desemboca el río Nilo?|medio|2025-12-23|Rojo|Caspio|Mediterráneo|Negro|Mediterráneo",
            "¿Cuál es la isla más grande del mundo?|difícil|2025-12-23|Australia|Groenlandia|Borneo|Madagascar|Groenlandia",
            "¿Cuál es la capital de Noruega?|fácil|2025-12-23|Oslo|Bergen|Estocolmo|Copenhague|Oslo",
            "¿Qué desierto es el más seco del mundo?|difícil|2025-12-23|Sahara|Gobi|Atacama|Kalahari|Atacama",
            "¿A qué país pertenecen las Islas Canarias?|fácil|2025-12-23|Portugal|Marruecos|España|Francia|España",
            "¿Qué estrecho separa Asia de América?|medio|2025-12-23|Gibraltar|Bering|Magallanes|Ormuz|Bering",
            "¿Cuál es la capital de Argentina?|fácil|2025-12-23|Rosario|Córdoba|Buenos Aires|Mendoza|Buenos Aires",
            "¿En qué continente está el Gran Cañón?|fácil|2025-12-23|Asia|Europa|América|África|América",
            "¿Cuál es el país más poblado del mundo?|fácil|2025-12-23|India|China|EEUU|Rusia|India",
            "¿Qué moneda se usa en México?|fácil|2025-12-23|Dólar|Peso|Bolívar|Sol|Peso",
            "¿Cuál es la capital de Egipto?|fácil|2025-12-23|Alejandría|Luxor|El Cairo|Giza|El Cairo",
            "¿Qué país es famoso por sus canales y tulipanes?|fácil|2025-12-23|Bélgica|Dinamarca|Países Bajos|Suecia|Países Bajos",
            "¿En qué país se encuentra la ciudad de Dubái?|medio|2025-12-23|Arabia Saudita|Qatar|EAU|Omán|EAU",
            "¿Cuál es la capital de Portugal?|fácil|2025-12-23|Oporto|Lisboa|Faro|Coímbra|Lisboa",
            "¿Qué línea imaginaria divide la Tierra en Norte y Sur?|fácil|2025-12-23|Ecuador|Meridiano|Trópico|Círculo Polar|Ecuador",
            "¿Cuál es el pico más alto de España?|medio|2025-12-23|Aneto|Mulhacén|Teide|Pico de Europa|Teide",

            # DEPORTES
            "¿Quién ha ganado más mundiales de fútbol?|fácil|2025-12-23|Alemania|Italia|Brasil|Argentina|Brasil",
            "¿Cuántos jugadores hay en un equipo de baloncesto?|fácil|2025-12-23|4|5|6|7|5",
            "¿En qué deporte se usa un 'puck'?|fácil|2025-12-23|Golf|Tenis|Hockey sobre hielo|Béisbol|Hockey sobre hielo",
            "¿Quién es el rey de la tierra batida en tenis?|fácil|2025-12-23|Federer|Djokovic|Nadal|Alcaraz|Nadal",
            "¿Cada cuántos años hay Juegos Olímpicos?|fácil|2025-12-23|2|3|4|5|4",
            "¿Cuál es la distancia de una media maratón?|medio|2025-12-23|10km|21.097km|42.195km|15km|21.097km",
            "¿En qué equipo jugaba Michael Jordan?|fácil|2025-12-23|Lakers|Celtics|Bulls|Knicks|Bulls",
            "¿Qué selección ganó la Eurocopa 2024?|fácil|2025-12-23|Inglaterra|España|Francia|Alemania|España",
            "¿Quién es el máximo goleador de la Champions?|medio|2025-12-23|Messi|Lewandowski|Cristiano Ronaldo|Raúl|Cristiano Ronaldo",
            "¿En qué deporte destaca Tiger Woods?|fácil|2025-12-23|Tenis|Golf|Surf|F1|Golf",
            "¿Cuál es el estilo de natación más rápido?|medio|2025-12-23|Espalda|Braza|Crol|Mariposa|Crol",
            "¿Quién ganó el primer mundial de F1 en 1950?|difícil|2025-12-23|Fangio|Farina|Ascari|Moss|Farina",
            "¿Cómo se llama el estadio del Real Madrid?|fácil|2025-12-23|Camp Nou|Metropolitano|Santiago Bernabéu|Mestalla|Santiago Bernabéu",
            "¿Qué país inventó el judo?|fácil|2025-12-23|China|Corea|Japón|Tailandia|Japón",
            "¿Cuántos puntos vale un touchdown?|medio|2025-12-23|3|6|7|1|6",
            "¿Qué tenista femenina tiene más Grand Slams?|difícil|2025-12-23|Serena Williams|Margaret Court|Steffi Graf|Navratilova|Margaret Court",
            "¿En qué ciudad se celebraron los JJOO de 1992?|fácil|2025-12-23|Madrid|Sevilla|Barcelona|Valencia|Barcelona",
            "¿Quién es 'The G.O.A.T' en gimnasia artística femenina?|medio|2025-12-23|Nadia Comăneci|Simone Biles|Beth Tweddle|Aliya Mustafina|Simone Biles",
            "¿Qué equipo de la NBA tiene más títulos?|medio|2025-12-23|Lakers|Celtics|Warriors|Bulls|Celtics",
            "¿Qué color de jersey lleva el líder del Tour de Francia?|fácil|2025-12-23|Rojo|Verde|Amarillo|Blanco|Amarillo",
            "¿En qué deporte se compite por la America's Cup?|difícil|2025-12-23|Equitación|Vela|Polo|Esgrima|Vela",
            "¿Cuánto dura un combate de boxeo olímpico?|difícil|2025-12-23|3 asaltos|5 asaltos|10 asaltos|12 asaltos|3 asaltos",
            "¿Quién ostenta el récord de 100m lisos?|fácil|2025-12-23|Tyson Gay|Yohan Blake|Usain Bolt|Asafa Powell|Usain Bolt",
            "¿En qué ciudad juegan los Yankees de béisbol?|fácil|2025-12-23|Chicago|Boston|Nueva York|Miami|Nueva York",
            "¿Cuántas piezas tiene un jugador al empezar ajedrez?|medio|2025-12-23|12|16|20|32|16"
        ]

        for p in preguntas:
            cur.execute("INSERT INTO trivial_flat (datos_pregunta) VALUES (%s)", (p,))

        conn.commit()
        print(f"✅ Se han cargado {len(preguntas)} registros planos en RDS Postgres.")
        
        cur.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error conectando a RDS: {e}")

if __name__ == "__main__":
    cargar_rds_flat()