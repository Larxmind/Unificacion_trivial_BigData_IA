from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client['trivia_db']
col = db['preguntas']

col.delete_many({})

preguntas_arte = [
# 1-10: Clásicos y Renacimiento
    {"diff": "Fácil", "es": "¿Quién pintó la 'Mona Lisa'?", "en": "Who painted the 'Mona Lisa'?", "opts": ["Leonardo da Vinci", "Miguel Ángel", "Rafael", "Donatello"], "ans": "Leonardo da Vinci"},
    {"diff": "Fácil", "es": "¿Quién pintó el techo de la Capilla Sixtina?", "en": "Who painted the ceiling of the Sistine Chapel?", "opts": ["Miguel Ángel", "Da Vinci", "Botticelli", "Tiziano"], "ans": "Miguel Ángel"},
    {"diff": "Media", "es": "¿Quién pintó 'El nacimiento de Venus'?", "en": "Who painted 'The Birth of Venus'?", "opts": ["Botticelli", "Rafael", "Donatello", "Fra Angelico"], "ans": "Botticelli"},
    {"diff": "Media", "es": "¿Qué artista es famoso por sus esculturas de mármol como 'El David'?", "en": "Which artist is famous for marble sculptures like 'David'?", "opts": ["Miguel Ángel", "Bernini", "Canova", "Donatello"], "ans": "Miguel Ángel"},
    {"diff": "Experto", "es": "¿Quién pintó 'La escuela de Atenas'?", "en": "Who painted 'The School of Athens'?", "opts": ["Rafael", "Da Vinci", "Miguel Ángel", "Bramante"], "ans": "Rafael"},
    {"diff": "Difícil", "es": "¿En qué siglo vivió el pintor El Greco?", "en": "In which century did the painter El Greco live?", "opts": ["Siglo XVI", "Siglo XVIII", "Siglo XIV", "Siglo XX"], "ans": "Siglo XVI"},
    {"diff": "Media", "es": "¿Quién pintó 'La última cena'?", "en": "Who painted 'The Last Supper'?", "opts": ["Leonardo da Vinci", "Rembrandt", "Caravaggio", "Velázquez"], "ans": "Leonardo da Vinci"},
    {"diff": "Experto", "es": "¿Quién diseñó la cúpula de la Catedral de Florencia?", "en": "Who designed the dome of Florence Cathedral?", "opts": ["Brunelleschi", "Alberti", "Bramante", "Vasari"], "ans": "Brunelleschi"},
    {"diff": "Media", "es": "¿Qué técnica usaba puntitos de color para formar imágenes?", "en": "What technique used small dots of color to form images?", "opts": ["Puntillismo", "Cubismo", "Fovismo", "Óleo"], "ans": "Puntillismo"},
    {"diff": "Media", "es": "¿Quién pintó 'La joven de la perla'?", "en": "Who painted 'Girl with a Pearl Earring'?", "opts": ["Johannes Vermeer", "Rembrandt", "Rubens", "Van Dyck"], "ans": "Johannes Vermeer"},

    # 11-20: Barroco y Siglo de Oro
    {"diff": "Difícil", "es": "¿Quién pintó 'Las Meninas'?", "en": "Who painted 'Las Meninas'?", "opts": ["Diego Velázquez", "Goya", "El Greco", "Murillo"], "ans": "Diego Velázquez"},
    {"diff": "Experto", "es": "¿Qué estilo artístico se caracteriza por el uso dramático del claroscuro?", "en": "What art style is characterized by the dramatic use of chiaroscuro?", "opts": ["Barroco", "Rococó", "Gótico", "Neoclásico"], "ans": "Barroco"},
    {"diff": "Difícil", "es": "¿Quién pintó 'La ronda de noche'?", "en": "Who painted 'The Night Watch'?", "opts": ["Rembrandt", "Vermeer", "Hals", "Rubens"], "ans": "Rembrandt"},
    {"diff": "Media", "es": "¿Quién es el autor de 'El jardín de las delicias'?", "en": "Who is the author of 'The Garden of Earthly Delights'?", "opts": ["El Bosco", "Brueghel", "Durero", "Van Eyck"], "ans": "El Bosco"},
    {"diff": "Experto", "es": "¿Quién esculpió el 'Éxtasis de Santa Teresa'?", "en": "Who sculpted the 'Ecstasy of Saint Teresa'?", "opts": ["Bernini", "Borromini", "Algardi", "Canova"], "ans": "Bernini"},
    {"diff": "Media", "es": "¿En qué ciudad se encuentra el Museo del Prado?", "en": "In which city is the Prado Museum located?", "opts": ["Madrid", "Barcelona", "Sevilla", "Bilbao"], "ans": "Madrid"},
    {"diff": "Fácil", "es": "¿Qué país es la cuna del Renacimiento?", "en": "Which country is the birthplace of the Renaissance?", "opts": ["Italia", "Francia", "España", "Grecia"], "ans": "Italia"},
    {"diff": "Difícil", "es": "¿Quién pintó 'La maja desnuda'?", "en": "Who painted 'The Nude Maja'?", "opts": ["Francisco de Goya", "Velázquez", "Picasso", "Sorolla"], "ans": "Francisco de Goya"},
    {"diff": "Experto", "es": "¿Quién pintó 'El caballero de la mano en el pecho'?", "en": "Who painted 'The Nobleman with his Hand on his Chest'?", "opts": ["El Greco", "Velázquez", "Zurbarán", "Murillo"], "ans": "El Greco"},
    {"diff": "Media", "es": "¿Quién pintó 'La libertad guiando al pueblo'?", "en": "Who painted 'Liberty Leading the People'?", "opts": ["Eugène Delacroix", "Géricault", "Ingres", "David"], "ans": "Eugène Delacroix"},

    # 21-30: Impresionismo y Postimpresionismo
    {"diff": "Fácil", "es": "¿Quién pintó 'La noche estrellada'?", "en": "Who painted 'The Starry Night'?", "opts": ["Vincent van Gogh", "Claude Monet", "Paul Cézanne", "Edvard Munch"], "ans": "Vincent van Gogh"},
    {"diff": "Media", "es": "¿Quién es considerado el padre del Impresionismo?", "en": "Who is considered the father of Impressionism?", "opts": ["Claude Monet", "Edouard Manet", "Renoir", "Degas"], "ans": "Claude Monet"},
    {"diff": "Fácil", "es": "¿Qué artista se cortó una oreja?", "en": "Which artist cut off his own ear?", "opts": ["Van Gogh", "Gauguin", "Toulouse-Lautrec", "Modigliani"], "ans": "Van Gogh"},
    {"diff": "Media", "es": "¿Quién pintó 'El beso'?", "en": "Who painted 'The Kiss'?", "opts": ["Gustav Klimt", "Egon Schiele", "Oskar Kokoschka", "Munch"], "ans": "Gustav Klimt"},
    {"diff": "Difícil", "es": "¿Quién pintó 'Un domingo por la tarde en la isla de la Grande Jatte'?", "en": "Who painted 'A Sunday Afternoon on the Island of La Grande Jatte'?", "opts": ["Georges Seurat", "Paul Signac", "Pissarro", "Sisley"], "ans": "Georges Seurat"},
    {"diff": "Media", "es": "¿En qué ciudad vivió y pintó mucho tiempo Toulouse-Lautrec?", "en": "In which city did Toulouse-Lautrec live and paint for a long time?", "opts": ["París", "Londres", "Viena", "Bruselas"], "ans": "París"},
    {"diff": "Difícil", "es": "¿Quién pintó 'Los comedores de patatas'?", "en": "Who painted 'The Potato Eaters'?", "opts": ["Vincent van Gogh", "Jean-François Millet", "Courbet", "Daumier"], "ans": "Vincent van Gogh"},
    {"diff": "Experto", "es": "¿Quién pintó 'Impresión, sol naciente'?", "en": "Who painted 'Impression, Sunrise'?", "opts": ["Claude Monet", "Pissarro", "Sisley", "Renoir"], "ans": "Claude Monet"},
    {"diff": "Media", "es": "¿Quién esculpió 'El pensador'?", "en": "Who sculpted 'The Thinker'?", "opts": ["Auguste Rodin", "Camille Claudel", "Bourdelle", "Maillol"], "ans": "Auguste Rodin"},
    {"diff": "Fácil", "es": "¿Cuál de estos es un color primario?", "en": "Which of these is a primary color?", "opts": ["Azul", "Verde", "Naranja", "Violeta"], "ans": "Azul"},

    # 31-40: Siglo XX y Modernismo
    {"diff": "Fácil", "es": "¿Quién pintó el 'Guernica'?", "en": "Who painted 'Guernica'?", "opts": ["Pablo Picasso", "Salvador Dalí", "Joan Miró", "Juan Gris"], "ans": "Pablo Picasso"},
    {"diff": "Experto", "es": "¿Quién pintó 'La persistencia de la memoria'?", "en": "Who painted 'The Persistence of Memory'?", "opts": ["Salvador Dalí", "René Magritte", "Max Ernst", "Frida Kahlo"], "ans": "Salvador Dalí"},
    {"diff": "Media", "es": "¿Quién pintó 'Las dos Fridas'?", "en": "Who painted 'The Two Fridas'?", "opts": ["Frida Kahlo", "Diego Rivera", "Remedios Varo", "Leonora Carrington"], "ans": "Frida Kahlo"},
    {"diff": "Fácil", "es": "¿Qué estilo fundó Picasso junto a Georges Braque?", "en": "What style did Picasso found with Georges Braque?", "opts": ["Cubismo", "Surrealismo", "Expresionismo", "Fovismo"], "ans": "Cubismo"},
    {"diff": "Media", "es": "¿Quién pintó 'El hijo del hombre' (el hombre con la manzana en la cara)?", "en": "Who painted 'The Son of Man'?", "opts": ["René Magritte", "Dalí", "Miró", "Chagall"], "ans": "René Magritte"},
    {"diff": "Difícil", "es": "¿Quién es famoso por sus pinturas de gotas y salpicaduras (Action Painting)?", "en": "Who is famous for his drip and splash paintings?", "opts": ["Jackson Pollock", "Mark Rothko", "Willem de Kooning", "Andy Warhol"], "ans": "Jackson Pollock"},
    {"diff": "Media", "es": "¿Quién pintó las famosas latas de sopa Campbell?", "en": "Who painted the famous Campbell's Soup Cans?", "opts": ["Andy Warhol", "Roy Lichtenstein", "Jasper Johns", "Keith Haring"], "ans": "Andy Warhol"},
    {"diff": "Experto", "es": "¿Quién pintó 'Composición en rojo, azul y amarillo'?", "en": "Who painted 'Composition with Red, Blue and Yellow'?", "opts": ["Piet Mondrian", "Kandinsky", "Malevich", "Klee"], "ans": "Piet Mondrian"},
    {"diff": "Media", "es": "¿Quién diseñó la Sagrada Familia en Barcelona?", "en": "Who designed the Sagrada Familia in Barcelona?", "opts": ["Antoni Gaudí", "Le Corbusier", "Mies van der Rohe", "Frank Gehry"], "ans": "Antoni Gaudí"},
    {"diff": "Difícil", "es": "¿Quién pintó 'El grito'?", "en": "Who painted 'The Scream'?", "opts": ["Edvard Munch", "Ensor", "Nolde", "Kandinsky"], "ans": "Edvard Munch"},

    # 41-50: Curiosidades y Museos
    {"diff": "Fácil", "es": "¿En qué ciudad se encuentra el Museo Guggenheim diseñado por Frank Gehry?", "en": "In which city is the Guggenheim Museum designed by Frank Gehry?", "opts": ["Bilbao", "Nueva York", "Venecia", "Berlín"], "ans": "Bilbao"},
    {"diff": "Media", "es": "¿En qué museo se encuentra la 'Mona Lisa'?", "en": "In which museum is the 'Mona Lisa'?", "opts": ["Louvre", "British Museum", "Metropolitan", "Hermitage"], "ans": "Louvre"},
    {"diff": "Fácil", "es": "¿Quién pintó la 'Capilla Sixtina'?", "en": "Who painted the 'Sistine Chapel'?", "opts": ["Miguel Ángel", "Rafael", "Da Vinci", "Perugino"], "ans": "Miguel Ángel"},
    {"diff": "Media", "es": "¿Cómo se llama la Venus de Milo por la isla donde fue encontrada?", "en": "What is the Venus de Milo named after?", "opts": ["La isla de Milo", "Su escultor Milo", "La ciudad de Milo", "El rey Milo"], "ans": "La isla de Milo"},
    {"diff": "Difícil", "es": "¿Quién pintó 'American Gothic'?", "en": "Who painted 'American Gothic'?", "opts": ["Grant Wood", "Edward Hopper", "Norman Rockwell", "Andrew Wyeth"], "ans": "Grant Wood"},
    {"diff": "Experto", "es": "¿Quién pintó 'La traición de las imágenes' ('Esto no es una pipa')?", "en": "Who painted 'The Treachery of Images'?", "opts": ["René Magritte", "Marcel Duchamp", "Francis Picabia", "Man Ray"], "ans": "René Magritte"},
    {"diff": "Media", "es": "¿Quién pintó 'Nighthawks' (Halcones de la noche)?", "en": "Who painted 'Nighthawks'?", "opts": ["Edward Hopper", "Grant Wood", "George Bellows", "Thomas Hart Benton"], "ans": "Edward Hopper"},
    {"diff": "Media", "es": "¿Qué artista es conocido por sus figuras de proporciones exageradamente gruesas?", "en": "Which artist is known for his figures with exaggeratedly thick proportions?", "opts": ["Fernando Botero", "Picasso", "Henry Moore", "Giacometti"], "ans": "Fernando Botero"},
    {"diff": "Fácil", "es": "¿Qué animal aparece en el cuadro 'La dama del armiño'?", "en": "What animal appears in the painting 'Lady with an Ermine'?", "opts": ["Un armiño", "Un perro", "Un gato", "Un conejo"], "ans": "Un armiño"},
    {"diff": "Experto", "es": "¿Quién pintó 'El entierro del Conde de Orgaz'?", "en": "Who painted 'The Burial of the Count of Orgaz'?", "opts": ["El Greco", "Velázquez", "Goya", "Zurbarán"], "ans": "El Greco"}
]
docs_to_insert = []
for p in preguntas_arte:
    doc = {
        "difficulty": p["diff"],
        "createdAt": datetime.now().isoformat(),
        "localizations": [
            {
                "language": "es",
                "text": p["es"],
                "items": p["opts"],
                "ok_item": p["ans"]
            },
            {
                "language": "en",
                "text": p["en"],
                "items": p["opts"],
                "ok_item": p["ans"]
            }
        ]
    }
    docs_to_insert.append(doc)


col.insert_many(docs_to_insert)

print(f"✅ Se han insertado {col.count_documents({})} preguntas de Arte en MongoDB.")