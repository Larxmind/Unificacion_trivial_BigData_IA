import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def sembrar_dynamo_corregido():
    try:
        session = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_REGION')
        )
        dynamodb = session.resource('dynamodb')
        table = dynamodb.Table('TriviaEspectaculo')

        preguntas = [
        {"id": "hist_01", "cat": "Historia", "q": "¿En qué año comenzó la Segunda Guerra Mundial?", "ans": "1939", "opts": ["1914", "1939", "1945", "1936"], "diff": "Fácil"},
        {"id": "hist_02", "cat": "Historia", "q": "¿Quién fue el primer presidente de los Estados Unidos?", "ans": "George Washington", "opts": ["Thomas Jefferson", "Lincoln", "Washington", "Adams"], "diff": "Fácil"},
        {"id": "hist_03", "cat": "Historia", "q": "¿Qué civilización construyó las pirámides de Giza?", "ans": "Egipcia", "opts": ["Maya", "Azteca", "Egipcia", "Inca"], "diff": "Fácil"},
        {"id": "hist_04", "cat": "Historia", "q": "¿En qué año llegó el hombre a la Luna?", "ans": "1969", "opts": ["1965", "1969", "1972", "1959"], "diff": "Media"},
        {"id": "hist_05", "cat": "Historia", "q": "¿Qué reina gobernó Inglaterra durante 63 años en el siglo XIX?", "ans": "Victoria", "opts": ["Isabel I", "Victoria", "Ana", "Isabel II"], "diff": "Media"},
        {"id": "hist_06", "cat": "Historia", "q": "¿Cuál era la capital del Imperio Bizantino?", "ans": "Constantinopla", "opts": ["Roma", "Atenas", "Constantinopla", "Viena"], "diff": "Media"},
        {"id": "hist_07", "cat": "Historia", "q": "¿Quién lideró la Revolución Rusa de 1917?", "ans": "Lenin", "opts": ["Stalin", "Trotsky", "Lenin", "Nicolás II"], "diff": "Media"},
        {"id": "hist_08", "cat": "Historia", "q": "¿Qué ciudad fue destruida por el Vesubio en el 79 d.C.?", "ans": "Pompeya", "opts": ["Herculano", "Pompeya", "Roma", "Nápoles"], "diff": "Fácil"},
        {"id": "hist_09", "cat": "Historia", "q": "¿Quién escribió el 'Manifiesto Comunista' con Engels?", "ans": "Karl Marx", "opts": ["Adam Smith", "Karl Marx", "Lenin", "Bakunin"], "diff": "Media"},
        {"id": "hist_10", "cat": "Historia", "q": "¿Qué tratado puso fin a la Primera Guerra Mundial?", "ans": "Tratado de Versalles", "opts": ["Tordesillas", "Utrecht", "Versalles", "Varsovia"], "diff": "Media"},
        {"id": "hist_11", "cat": "Historia", "q": "¿En qué año cayó el Imperio Romano de Occidente?", "ans": "476", "opts": ["395", "476", "1453", "1000"], "diff": "Difícil"},
        {"id": "hist_12", "cat": "Historia", "q": "¿Quién fue la última reina de la dinastía ptolemaica?", "ans": "Cleopatra VII", "opts": ["Nefertiti", "Cleopatra VII", "Hatshepsut", "Isis"], "diff": "Fácil"},
        {"id": "hist_13", "cat": "Historia", "q": "¿Qué ruta comercial unía China con Europa?", "ans": "Ruta de la Seda", "opts": ["Ruta Especias", "Ruta de la Seda", "Camino Real", "Senda"], "diff": "Fácil"},
        {"id": "hist_14", "cat": "Historia", "q": "¿Quién lideró la independencia pacífica de la India?", "ans": "Mahatma Gandhi", "opts": ["Nehru", "Indira Gandhi", "Mahatma Gandhi", "Ambedkar"], "diff": "Fácil"},
        {"id": "hist_15", "cat": "Historia", "q": "¿Cómo se llamaba el barco de Charles Darwin?", "ans": "HMS Beagle", "opts": ["HMS Victory", "HMS Beagle", "Santa María", "Endeavour"], "diff": "Difícil"},
        {"id": "hist_16", "cat": "Historia", "q": "¿Qué emperador fue derrotado en Waterloo?", "ans": "Napoleón Bonaparte", "opts": ["Luis XIV", "Napoleón", "Carlos X", "Luis XVI"], "diff": "Fácil"},
        {"id": "hist_17", "cat": "Historia", "q": "¿Qué muro dividió Berlín de 1961 a 1989?", "ans": "Muro de Berlín", "opts": ["Muro Paz", "Muro de Berlín", "Muro Hierro", "Malla"], "diff": "Fácil"},
        {"id": "hist_18", "cat": "Historia", "q": "¿Qué conquistador macedonio llegó hasta la India?", "ans": "Alejandro Magno", "opts": ["Julio César", "Alejandro Magno", "Ciro", "Darío I"], "diff": "Fácil"},
        {"id": "hist_19", "cat": "Historia", "q": "¿Qué cultura inventó la escritura cuneiforme?", "ans": "Sumeria", "opts": ["Egipcia", "Sumeria", "Fenicia", "Griega"], "diff": "Difícil"},
        {"id": "hist_20", "cat": "Historia", "q": "¿Quién llegó a América en 1492?", "ans": "Cristóbal Colón", "opts": ["Vespucio", "Colón", "Magallanes", "Vasco de Gama"], "diff": "Fácil"},
        {"id": "hist_21", "cat": "Historia", "q": "¿Cómo se llama el renacer cultural tras la Edad Media?", "ans": "Renacimiento", "opts": ["Ilustración", "Barroco", "Renacimiento", "Gótico"], "diff": "Fácil"},
        {"id": "hist_22", "cat": "Historia", "q": "¿Quién era el rey durante la Revolución Francesa?", "ans": "Luis XVI", "opts": ["Luis XIV", "Luis XV", "Luis XVI", "Napoleón"], "diff": "Media"},
        {"id": "hist_23", "cat": "Historia", "q": "¿En qué país comenzó la Revolución Industrial?", "ans": "Gran Bretaña", "opts": ["Francia", "Alemania", "EEUU", "Gran Bretaña"], "diff": "Media"},
        {"id": "hist_24", "cat": "Historia", "q": "¿Qué filósofo fue maestro de Alejandro Magno?", "ans": "Aristóteles", "opts": ["Platón", "Sócrates", "Aristóteles", "Epicuro"], "diff": "Difícil"},
        {"id": "hist_25", "cat": "Historia", "q": "¿Cuál fue el imperio liderado por Gengis Kan?", "ans": "Imperio Mongol", "opts": ["Imperio Chino", "Imperio Otomano", "Imperio Mongol", "Persa"], "diff": "Fácil"},

        # --- CINE (25 Preguntas) ---
        {"id": "cine_01", "cat": "Cine", "q": "¿Quién dirigió 'Pulp Fiction'?", "ans": "Quentin Tarantino", "opts": ["Spielberg", "Tarantino", "Scorsese", "Nolan"], "diff": "Fácil"},
        {"id": "cine_02", "cat": "Cine", "q": "¿Qué película ganó el primer Oscar en 1929?", "ans": "Wings", "opts": ["Wings", "Metropolis", "The Jazz Singer", "Sunrise"], "diff": "Difícil"},
        {"id": "cine_03", "cat": "Cine", "q": "¿Cuál es la película más taquillera (sin inflación)?", "ans": "Avatar", "opts": ["Titanic", "Endgame", "Avatar", "Star Wars VII"], "diff": "Fácil"},
        {"id": "cine_04", "cat": "Cine", "q": "¿Dónde vive Simba en 'El Rey León'?", "ans": "Tierras del Orgullo", "opts": ["Selva Negra", "Tierras del Orgullo", "Roca", "Sabana"], "diff": "Fácil"},
        {"id": "cine_05", "cat": "Cine", "q": "¿Quién interpretó a Jack Sparrow?", "ans": "Johnny Depp", "opts": ["Brad Pitt", "Johnny Depp", "Orlando Bloom", "Tom Cruise"], "diff": "Fácil"},
        {"id": "cine_06", "cat": "Cine", "q": "¿Qué película presenta al payaso Pennywise?", "ans": "It", "opts": ["Saw", "It", "The Conjuring", "Poltergeist"], "diff": "Fácil"},
        {"id": "cine_07", "cat": "Cine", "q": "¿Cuál fue el primer largometraje de Pixar?", "ans": "Toy Story", "opts": ["Bugs Life", "Toy Story", "Monsters Inc", "Nemo"], "diff": "Fácil"},
        {"id": "cine_08", "cat": "Cine", "q": "¿Quién dirigió 'El Padrino'?", "ans": "Francis Ford Coppola", "opts": ["Scorsese", "Coppola", "De Palma", "Spielberg"], "diff": "Media"},
        {"id": "cine_09", "cat": "Cine", "q": "¿Qué actor protagoniza la saga 'Misión Imposible'?", "ans": "Tom Cruise", "opts": ["Will Smith", "Keanu Reeves", "Tom Cruise", "Willis"], "diff": "Fácil"},
        {"id": "cine_10", "cat": "Cine", "q": "¿Cómo se llama el hobbit protagonista de ESDLA?", "ans": "Frodo Bolsón", "opts": ["Sam", "Frodo Bolsón", "Bilbo", "Pippin"], "diff": "Fácil"},
        {"id": "cine_11", "cat": "Cine", "q": "¿En qué película se dice 'Yo soy tu padre'?", "ans": "El Imperio Contraataca", "opts": ["Star Wars IV", "El Imperio Contraataca", "Star Wars VI", "Star Wars III"], "diff": "Fácil"},
        {"id": "cine_12", "cat": "Cine", "q": "¿Quién dio voz al Genio en Aladdín (1992)?", "ans": "Robin Williams", "opts": ["Tom Hanks", "Robin Williams", "Murphy", "Danny DeVito"], "diff": "Media"},
        {"id": "cine_13", "cat": "Cine", "q": "¿Qué película de 1975 dirigió Spielberg sobre un gran pez?", "ans": "Tiburón", "opts": ["Piraña", "Tiburón", "Orca", "The Deep"], "diff": "Fácil"},
        {"id": "cine_14", "cat": "Cine", "q": "¿Qué actor fue el Joker en 'The Dark Knight'?", "ans": "Heath Ledger", "opts": ["Nicholson", "Jared Leto", "Heath Ledger", "Phoenix"], "diff": "Fácil"},
        {"id": "cine_15", "cat": "Cine", "q": "¿Cómo se llama el hotel de 'El Resplandor'?", "ans": "Overlook", "opts": ["Overlook", "Bates Motel", "Grand Budapest", "Stanley"], "diff": "Media"},
        {"id": "cine_16", "cat": "Cine", "q": "¿Cuál es la ciudad que protege Batman?", "ans": "Gotham City", "opts": ["Metropolis", "Central City", "Gotham City", "Star City"], "diff": "Fácil"},
        {"id": "cine_17", "cat": "Cine", "q": "¿En qué año se estrenó 'Titanic' de James Cameron?", "ans": "1997", "opts": ["1994", "1997", "2000", "1991"], "diff": "Media"},
        {"id": "cine_18", "cat": "Cine", "q": "¿Quién dirigió la premiada película 'Parásitos'?", "ans": "Bong Joon-ho", "opts": ["Kurosawa", "Bong Joon-ho", "Park Chan-wook", "Ang Lee"], "diff": "Media"},
        {"id": "cine_19", "cat": "Cine", "q": "¿Qué película de Disney trata de la familia Madrigal?", "ans": "Encanto", "opts": ["Coco", "Encanto", "Moana", "Raya"], "diff": "Fácil"},
        {"id": "cine_20", "cat": "Cine", "q": "¿Cuál es el nombre del robot en Wall-E?", "ans": "Wall-E", "opts": ["EVE", "Wall-E", "R2-D2", "Bender"], "diff": "Fácil"},
        {"id": "cine_21", "cat": "Cine", "q": "¿Qué actriz dio vida a Hermione Granger?", "ans": "Emma Watson", "opts": ["Emma Roberts", "Emma Stone", "Emma Watson", "Bonnie Wright"], "diff": "Fácil"},
        {"id": "cine_22", "cat": "Cine", "q": "¿En qué película sale Bubba y una fábrica de gambas?", "ans": "Forrest Gump", "opts": ["Big", "Forrest Gump", "Náufrago", "Apollo 13"], "diff": "Fácil"},
        {"id": "cine_23", "cat": "Cine", "q": "¿Cómo se llama el elegido en 'The Matrix'?", "ans": "Neo", "opts": ["Morpheus", "Neo", "Trinity", "Smith"], "diff": "Fácil"},
        {"id": "cine_24", "cat": "Cine", "q": "¿Quién dirigió 'Jurassic Park'?", "ans": "Steven Spielberg", "opts": ["Lucas", "Spielberg", "Scott", "Cameron"], "diff": "Fácil"},
        {"id": "cine_25", "cat": "Cine", "q": "¿Qué película trata sobre Miguel y la Tierra de los Muertos?", "ans": "Coco", "opts": ["Libro de la vida", "Coco", "Encanto", "Up"], "diff": "Fácil"}
        ]

        print("🚀 Iniciando carga en DynamoDB con estructura de Payload...")
        
        with table.batch_writer() as batch:
            for p in preguntas:
                batch.put_item(
                    Item={
                        'id': p['id'],            # Clave primaria
                        'question': p['q'],       # Campo plano
                        'options': p['opts'],     # Campo plano
                        'answer': p['ans'],       # Campo plano
                        'difficulty': p['diff'],  # Campo plano
                        'timestamp': datetime.now().isoformat()
                    }
                )
        print(f"✅ Éxito: {len(preguntas)} preguntas insertadas.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    sembrar_dynamo_corregido()