-- Crear la tabla de preguntas
CREATE TABLE IF NOT EXISTS preguntas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(500) NOT NULL,
    nivel ENUM('fácil', 'medio', 'difícil') NOT NULL,
    fecha_registro DATE NOT NULL,
    categoria VARCHAR(50)
);

-- Crear la tabla de opciones (Respuestas)
CREATE TABLE IF NOT EXISTS opciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta_id INT,
    texto_opcion VARCHAR(255) NOT NULL,
    es_correcta BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id) ON DELETE CASCADE
);

-- Inserción de datos de prueba (Geografía y Deportes)
-- =============================================
-- SECCIÓN: GEOGRAFÍA (25 PREGUNTAS)
-- =============================================

-- 1
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el océano más grande del mundo?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Atlántico', 0), (@last_id, 'Índico', 0), (@last_id, 'Pacífico', 1), (@last_id, 'Ártico', 0);

-- 2
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país tiene forma de bota?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Grecia', 0), (@last_id, 'España', 0), (@last_id, 'Italia', 1), (@last_id, 'Portugal', 0);

-- 3
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es la capital de Islandia?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Oslo', 0), (@last_id, 'Reikiavik', 1), (@last_id, 'Helsinki', 0), (@last_id, 'Estocolmo', 0);

-- 4
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué país se encuentra el Monte Kilimanjaro?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Kenia', 0), (@last_id, 'Etiopía', 0), (@last_id, 'Tanzania', 1), (@last_id, 'Uganda', 0);

-- 5
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el país más poblado de África?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Egipto', 0), (@last_id, 'Nigeria', 1), (@last_id, 'Sudáfrica', 0), (@last_id, 'Argelia', 0);

-- 6
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué estrecho separa España de Marruecos?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Magallanes', 0), (@last_id, 'Gibraltar', 1), (@last_id, 'Bósforo', 0), (@last_id, 'Bering', 0);

-- 7
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el pico más alto de los Pirineos?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Mulhacén', 0), (@last_id, 'Teide', 0), (@last_id, 'Aneto', 1), (@last_id, 'Pico Posets', 0);

-- 8
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué país se encuentra la ciudad de Petra?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Egipto', 0), (@last_id, 'Jordania', 1), (@last_id, 'Siria', 0), (@last_id, 'Irak', 0);

-- 9
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué río es el más largo de Europa?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Danubio', 0), (@last_id, 'Rin', 0), (@last_id, 'Volga', 1), (@last_id, 'Sena', 0);

-- 10
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es la capital de Canadá?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Toronto', 0), (@last_id, 'Vancouver', 0), (@last_id, 'Ottawa', 1), (@last_id, 'Montreal', 0);

-- 11
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el desierto más cálido del mundo?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Gobi', 0), (@last_id, 'Atacama', 0), (@last_id, 'Sahara', 1), (@last_id, 'Kalahari', 0);

-- 12
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿A qué país pertenecen las Islas Galápagos?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Colombia', 0), (@last_id, 'Perú', 0), (@last_id, 'Ecuador', 1), (@last_id, 'Chile', 0);

-- 13
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país tiene más islas en el mundo?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Filipinas', 0), (@last_id, 'Indonesia', 0), (@last_id, 'Suecia', 1), (@last_id, 'Grecia', 0);

-- 14
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es la capital de Turquía?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Estambul', 0), (@last_id, 'Ankara', 1), (@last_id, 'Esmirna', 0), (@last_id, 'Antalya', 0);

-- 15
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué continente está Surinam?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'África', 0), (@last_id, 'Asia', 0), (@last_id, 'América del Sur', 1), (@last_id, 'Oceanía', 0);

-- 16
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país es conocido como el país del sol naciente?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'China', 0), (@last_id, 'Corea del Sur', 0), (@last_id, 'Japón', 1), (@last_id, 'Tailandia', 0);

-- 17
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el lago más profundo del mundo?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Victoria', 0), (@last_id, 'Superior', 0), (@last_id, 'Baikal', 1), (@last_id, 'Titicaca', 0);

-- 18
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué ciudad es la capital de Suiza?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Zúrich', 0), (@last_id, 'Ginebra', 0), (@last_id, 'Berna', 1), (@last_id, 'Basilea', 0);

-- 19
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el punto más bajo de la Tierra (en tierra firme)?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Valle de la Muerte', 0), (@last_id, 'Mar Muerto', 1), (@last_id, 'Fosa de las Marianas', 0), (@last_id, 'Depresión de Afar', 0);

-- 20
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país tiene la mayor superficie de selva amazónica?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Colombia', 0), (@last_id, 'Perú', 0), (@last_id, 'Brasil', 1), (@last_id, 'Venezuela', 0);

-- 21
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es la capital de Marruecos?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Casablanca', 0), (@last_id, 'Marrakech', 0), (@last_id, 'Rabat', 1), (@last_id, 'Fez', 0);

-- 22
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué país se encuentra el Salto del Ángel?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Brasil', 0), (@last_id, 'Guyana', 0), (@last_id, 'Venezuela', 1), (@last_id, 'Ecuador', 0);

-- 23
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país europeo tiene más volcanes activos?', 'difícil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Italia', 0), (@last_id, 'Grecia', 0), (@last_id, 'Islandia', 1), (@last_id, 'España', 0);

-- 24
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es la capital de Portugal?', 'fácil', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Oporto', 0), (@last_id, 'Coímbra', 0), (@last_id, 'Lisboa', 1), (@last_id, 'Faro', 0);

-- 25
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué cordillera separa Europa de Asia?', 'medio', '2025-12-23', 'Geografía');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Alpes', 0), (@last_id, 'Cáucaso', 0), (@last_id, 'Montes Urales', 1), (@last_id, 'Himalaya', 0);


-- =============================================
-- SECCIÓN: DEPORTES (25 PREGUNTAS)
-- =============================================

-- 26
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuántos minutos dura un partido de fútbol oficial (sin descuento)?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '80', 0), (@last_id, '90', 1), (@last_id, '100', 0), (@last_id, '45', 0);

-- 27
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué tenista ha ganado más torneos de Roland Garros?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Roger Federer', 0), (@last_id, 'Novak Djokovic', 0), (@last_id, 'Rafael Nadal', 1), (@last_id, 'Björn Borg', 0);

-- 28
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué ciudad juegan los Lakers de la NBA?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Chicago', 0), (@last_id, 'Miami', 0), (@last_id, 'Los Ángeles', 1), (@last_id, 'Nueva York', 0);

-- 29
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país ganó el primer Mundial de Fútbol en 1930?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Brasil', 0), (@last_id, 'Argentina', 0), (@last_id, 'Uruguay', 1), (@last_id, 'Italia', 0);

-- 30
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿A qué distancia se encuentra el punto de penalti en fútbol?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '9 metros', 0), (@last_id, '10 metros', 0), (@last_id, '11 metros', 1), (@last_id, '12 metros', 0);

-- 31
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Quién es el máximo goleador histórico de los Mundiales?', 'difícil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Pelé', 0), (@last_id, 'Ronaldo Nazário', 0), (@last_id, 'Miroslav Klose', 1), (@last_id, 'Lionel Messi', 0);

-- 32
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuántos anillos de la NBA ganó Michael Jordan?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '4', 0), (@last_id, '5', 0), (@last_id, '6', 1), (@last_id, '7', 0);

-- 33
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué año se celebraron los Juegos Olímpicos de Barcelona?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '1988', 0), (@last_id, '1992', 1), (@last_id, '1996', 0), (@last_id, '2000', 0);

-- 34
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué selección de fútbol es conocida como "La Naranja Mecánica"?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Alemania', 0), (@last_id, 'Bélgica', 0), (@last_id, 'Países Bajos', 1), (@last_id, 'España', 0);

-- 35
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cómo se llama el estilo de natación más lento?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Crol', 0), (@last_id, 'Mariposa', 0), (@last_id, 'Braza (Pecho)', 1), (@last_id, 'Espalda', 0);

-- 36
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Quién ostenta el récord mundial de 100 metros lisos?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Carl Lewis', 0), (@last_id, 'Tyson Gay', 0), (@last_id, 'Usain Bolt', 1), (@last_id, 'Yohan Blake', 0);

-- 37
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el equipo con más Champions League?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'AC Milan', 0), (@last_id, 'Liverpool', 0), (@last_id, 'Real Madrid', 1), (@last_id, 'Bayern Munich', 0);

-- 38
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuánto dura un asalto en el boxeo profesional masculino?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '2 minutos', 0), (@last_id, '3 minutos', 1), (@last_id, '4 minutos', 0), (@last_id, '5 minutos', 0);

-- 39
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿En qué ciudad se encuentra el circuito de Interlagos de F1?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Madrid', 0), (@last_id, 'Ciudad de México', 0), (@last_id, 'São Paulo', 1), (@last_id, 'Mónaco', 0);

-- 40
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Quién fue el primer ciclista en ganar 5 Tours de Francia?', 'difícil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Eddy Merckx', 0), (@last_id, 'Jacques Anquetil', 1), (@last_id, 'Miguel Induráin', 0), (@last_id, 'Bernard Hinault', 0);

-- 41
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué deporte practica Tiger Woods?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Tenis', 0), (@last_id, 'Baloncesto', 0), (@last_id, 'Golf', 1), (@last_id, 'Rugby', 0);

-- 42
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuántos puntos vale un tiro libre en baloncesto?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '1', 1), (@last_id, '2', 0), (@last_id, '3', 0), (@last_id, '0', 0);

-- 43
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es el Grand Slam que se juega sobre hierba?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'US Open', 0), (@last_id, 'Open de Australia', 0), (@last_id, 'Wimbledon', 1), (@last_id, 'Roland Garros', 0);

-- 44
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué país ha ganado más mundiales de fútbol masculino?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Alemania', 0), (@last_id, 'Italia', 0), (@last_id, 'Brasil', 1), (@last_id, 'Argentina', 0);

-- 45
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cómo se llama el jugador de fútbol americano que lanza el balón?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Linebacker', 0), (@last_id, 'Quarterback', 1), (@last_id, 'Wide Receiver', 0), (@last_id, 'Fullback', 0);

-- 46
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿De qué país es el piloto Max Verstappen?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Alemania', 0), (@last_id, 'Bélgica', 0), (@last_id, 'Países Bajos', 1), (@last_id, 'Austria', 0);

-- 47
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué ciudad albergará los JJOO de 2024 (o los últimos celebrados)?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Londres', 0), (@last_id, 'Tokio', 0), (@last_id, 'París', 1), (@last_id, 'Los Ángeles', 0);

-- 48
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Cuál es la distancia de una maratón?', 'difícil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '40 km', 0), (@last_id, '42,195 km', 1), (@last_id, '45 km', 0), (@last_id, '21 km', 0);

-- 49
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Quién ganó el Mundial de Fútbol de 2010?', 'fácil', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, 'Holanda', 0), (@last_id, 'Alemania', 0), (@last_id, 'España', 1), (@last_id, 'Brasil', 0);

-- 50
INSERT INTO preguntas (texto, nivel, fecha_registro, categoria) VALUES ('¿Qué número llevaba Kobe Bryant en sus inicios en los Lakers?', 'medio', '2025-12-23', 'Deportes');
SET @last_id = LAST_INSERT_ID();
INSERT INTO opciones (pregunta_id, texto_opcion, es_correcta) VALUES (@last_id, '24', 0), (@last_id, '23', 0), (@last_id, '8', 1), (@last_id, '10', 0);