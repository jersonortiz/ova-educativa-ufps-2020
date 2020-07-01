-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 01-07-2020 a las 14:41:42
-- Versión del servidor: 10.3.22-MariaDB-1ubuntu1
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ovaeducativa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_docente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grupo`
--

INSERT INTO `grupo` (`id`, `nombre`, `id_docente`) VALUES
(1, 'prueba', 2),
(2, 'otro', 2),
(3, 'asd', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupoestudiante`
--

CREATE TABLE `grupoestudiante` (
  `id` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grupoestudiante`
--

INSERT INTO `grupoestudiante` (`id`, `id_grupo`, `id_estudiante`) VALUES
(1, 1, 1),
(6, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pendiente`
--

CREATE TABLE `pendiente` (
  `id` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `correo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pregunta`
--

CREATE TABLE `pregunta` (
  `id` int(11) NOT NULL,
  `id_tema` int(11) NOT NULL,
  `contenido` text NOT NULL,
  `respuesta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pregunta`
--

INSERT INTO `pregunta` (`id`, `id_tema`, `contenido`, `respuesta`) VALUES
(1, 1, '¿Qué es un objeto virtual de aprendizaje?%d%Es la unidad mínima de aprendizaje, en formato digital que puede ser reusada y secuenciada.%d%Es un entorno virtual%d%Es un objeto interactivo%d%Es un objeto de educación digital', 0),
(2, 1, '¿Cuáles son los beneficios de un objeto virtual de aprendizaje?%d%Accesible, eficaz, eficiente%d%Reusable%d%interoperabilidad, auto contenible%d%Flexibilidad, Administración del contenido, Adaptabilidad', 3),
(3, 1, '¿En qué consiste la granularidad de un objeto virtual de aprendizaje?%d%No es posible definir la cantidad de información o elementos que un OA debe contener, esto dependerá de las necesidades y habilidades del autor para trabajar y conceptuar trozos de contenidos que irán formando un curso.%d%En un recurso educativo%d%Modelo de referencia para un sistema abierto de archivo de información%d%En la estructura general de los metadatos', 0),
(4, 1, '¿Cuáles son las características de un objeto virtual de aprendizaje?%d%reusable, digital%d%interoperable, reusable%d%Formato digital, propósito pedagógico, interactivo, reutilizable%d%dinámico, activo, interactivo', 2),
(5, 1, '¿Cuáles son los pasos que se requieren para la construcción de un objeto de aprendizaje?%d%Conceptuales y actitudinales%d%Procedimentales%d%Conceptuales, procedimentales, actitudinales.%d%Ninguna de las anteriores', 2),
(6, 1, '¿Cual es una ventaja de los educadores a tener un ova de apoyo?%d%Falta de experiencia en producción de e-learning%d%La apariencia de los recursos instruccionales promueve la comodidad y disponibilidad.%d%Evita la necesidad de recrear los recursos existentes diseño y proceso de desarrollo consistentes.%d%Falta de familiaridad con el proceso de instrucción Disponibilidad Limitada', 2),
(7, 1, '¿Cual es una desventaja de los estudiantes a tener un ova de apoyo?%d%Necesita contar con recursos%d%Requiere tecnología de información, incluyendo acceso a Internet de banda ancha y un sistema de gestión del aprender.%d%Sirve para una variedad de estilos de aprendizaje individuales.%d%Falta de familiaridad con el proceso de instrucción Disponibilidad Limitada.', 3),
(8, 2, 'Que significan las siglas LMS%d%Learning management system%d%lightweight mass system%d%ninguna de las anteriores', 0),
(9, 2, '¿LMS cuenta con 7 características?%d%f%d%v', 1),
(10, 2, 'Bajo que licencia esta LMS?%d%QWERTY-7%d%GPL-9%d%GPL-2%d%QWAC-7', 2),
(11, 2, 'Para que se usa LCMS%d%Medicinal%d%Educativo%d%Militar%d%Robotica', 1),
(12, 2, '¿Saba, Bb, LotusLearningSpace son ejemplos de propietario?%d%v%d%f', 0),
(13, 2, '¿Los sistemas propietarios destacan a Blackboard?%d%f%d%v', 1),
(14, 2, '¿LMS de código abierto requiere pago para su uso?%d%f%d%v', 0),
(15, 2, '¿Moodle, dokeos y LRN son ejemplos de código abierto?%d%f%d%v', 1),
(16, 3, '¿ExeLearning es una herramienta de código abierto (open source) que facilita la creación de contenidos educativos sin necesidad de ser experto en HTML o XML. Se trata de una aplicación multiplataforma que nos permite la utilización de árboles de contenido, elementos multimedia, actividades interactivas de autoevaluación… facilitando la exportación del contenido generado a múltiples formatos: HTML, SCORM, IMS, etc.?%d%f%d%v', 1),
(17, 3, '¿Que gobierno financio el proyecto exelearning?%d%Nueva zelanda%d%Peru%d%china%d%iran', 0),
(18, 3, '¿Exelearning es la herramienta de autor más completa del mercado?%d%f%d%v', 0),
(19, 3, 'Al abrir eXeLearning cuantas zonas hay%d%7%d%2%d%4%d%gúgol^gúgol', 2),
(20, 3, 'EXE-learning permite exportar en html%d%f%d%v', 1),
(21, 4, 'Reload cuenta con 4 pasos básicos para su utilización?%d%f%d%v', 1),
(22, 4, '¿Reload tiene como función empaquetar contenidos creados con otras herramientas?%d%f%d%v', 1),
(23, 4, '¿El proyecto de Reload Editor es una aplicación libre la cual puedes descargar y utilizar gratuitamente desde su web?%d%f%d%v', 1),
(24, 4, '¿Reload Editor Permite modificar, editar y construir paquetes SCORM e IMS para manejar tus contenidos?%d%f%d%v', 1),
(25, 5, '¿Las siglas SCORM a que se refiere?%d%hacen alusión a un conjunto de estándares y especificaciones que permiten crear objetos pedagógicos estructurados%d%resuelven un problema que se planteaba antes de su creación%d%distribuyen como un conjunto de ficheros organizados en carpetas%d%son variables que se registran', 0),
(26, 5, '¿En qué año fue creado SCORM?%d%1980%d%1990%d%1999%d%1988', 2),
(27, 5, '¿Que se aloja en el formato zip?%d%fichero imsmanifest.xml%d%fichero ims%d%fichero xml%d%fichero imsmanfest', 0),
(28, 5, '¿Cómo se distribuyen los paquetes SCORM?%d%píldoras de contenido pedagógico que se trate%d%como un conjunto de ficheros organizados en carpetas, habitualmente en formato%d%formatos Tin Can API%d%mobile learning', 1),
(29, 5, '¿Los SCORM incluyen uno o varios?%d%SCE%d%SDO%d%SDE%d%SCO', 3),
(30, 5, '¿Las ventajas de SCORM son?%d%portabilidad, interoperabilidad, adaptabilidad%d%Accesibilidad, Adaptabilidad, Durabilidad, Interoperabilidad, Reusabilidad, Reducción de costes.%d%eficacia y Eficiencia%d%Interactividad, portabilidad', 1),
(31, 5, '¿Los SCORM son realmente personalizables y permiten que una misma formación base pueda adaptarse para un sinfín de organizaciones y estudiantes hace referencia a?%d%Durabilidad%d%Interoperabilidad%d%Reusabilidad%d%Adaptabilidad', 3),
(32, 6, '¿Los metadatos LOM son?%d%específicos para describir recursos educativos e incluyen no solamente los elementos identificatorios como el título o el idioma%d%Crear descripciones bien estructuradas para recursos educativos%d%Adecuación de las descripciones de recursos para cumplir las necesidades especializadas de una comunidad%d%especifica los metadatos para objetos de aprendizaje', 0),
(33, 6, 'Cuantas categorias tiene LOM?%d%4%d%7%d%8%d%9', 3),
(34, 6, '¿Es un objetivo en el cual se diseñó LOM?%d%Podrían ser transcriptos con un esquema de metadatos de índole general%d%Un objeto educativo%d%Crear descripciones bien estructuradas para recursos educativos.%d%ninguna de las anteriores', 2),
(35, 6, '¿Cuales son los tipos de elementos que tiene LOM?%d%obligatorios%d%calificativos%d%calificativos,opcionales%d%obligatorios,opcionales,recomendados', 3),
(36, 6, '¿El estándar de metadatos IEEE LOM contiene un grupo mínimo de elementos para?%d%a administración, ubicación y evaluación de los objetos de aprendizaje%d%Información general que describe el objeto de aprendizaje como un todo%d%Agrupa información sobre los mismos metadatos, no sobre el objeto de aprendizaje que se está describiendo%d%primera y tercera', 0),
(37, 6, '¿Cuales son los metadatos obligatorios para los Objetos de Aprendizaje del Banco Nacional y considera opcionales, los correspondientes al resto de campos de la especificación IEEE LOM?%d%General,técnico,activo%d%Derechos,clasificación,inactivo%d%interactivo,educacional%d%General,ciclo de vida,Técnico,educacional,Derechos,anotación,clasificación', 3),
(38, 6, '¿Que es un registro de metadatos?%d% Sistemas de catalogación%d%Gran cantidad de recursos digitales disponibles en Internet%d%Consiste en un conjunto de atributos o elementos necesarios para describir un recurso determinado, que funciona como identificador de los materiales digitales diseñados.%d%primera y tercera', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuesta`
--

CREATE TABLE `respuesta` (
  `id` int(11) NOT NULL,
  `puntaje` int(11) NOT NULL,
  `correcta` tinyint(1) NOT NULL,
  `opcion_escogida` varchar(8) NOT NULL,
  `id_pregunta` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `respuesta`
--

INSERT INTO `respuesta` (`id`, `puntaje`, `correcta`, `opcion_escogida`, `id_pregunta`, `id_estudiante`) VALUES
(1, 29, 0, '-1', 25, 1),
(2, 29, 0, '-1', 26, 1),
(3, 29, 0, '-1', 27, 1),
(4, 29, 0, '-1', 28, 1),
(5, 29, 0, '-1', 29, 1),
(6, 29, 1, '1', 30, 1),
(7, 29, 1, '3', 31, 1),
(8, 14, 0, '2', 32, 1),
(9, 14, 0, '0', 33, 1),
(10, 14, 0, '1', 34, 1),
(11, 14, 0, '2', 35, 1),
(12, 14, 0, '2', 36, 1),
(13, 14, 1, '3', 37, 1),
(14, 14, 0, '3', 38, 1),
(15, 71, 1, '0', 1, 3),
(16, 71, 0, '0', 2, 3),
(17, 71, 1, '0', 3, 3),
(18, 71, 1, '2', 4, 3),
(19, 71, 1, '2', 5, 3),
(20, 71, 1, '2', 6, 3),
(21, 71, 0, '0', 7, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tema`
--

CREATE TABLE `tema` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tema`
--

INSERT INTO `tema` (`id`, `nombre`) VALUES
(1, 'Concepto de objeto virtual de aprendizaje'),
(2, 'que son los LMS'),
(3, 'EXE learning'),
(4, 'Reload'),
(5, 'SCORM'),
(6, 'LOM');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  `tipo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `correo`, `contraseña`, `tipo`) VALUES
(1, 'pepe', 'algo', 'algo@que.es', '1234', 1),
(2, 'juan', 'ju', 'pri@es.n', '1234', 2),
(3, 'este', 'as', 'seg@n.e', '1234', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `grupoestudiante`
--
ALTER TABLE `grupoestudiante`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_estudiante_usuario` (`id_estudiante`),
  ADD KEY `idgrupo_grupo` (`id_grupo`);

--
-- Indices de la tabla `pendiente`
--
ALTER TABLE `pendiente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo_grupo` (`id_grupo`);

--
-- Indices de la tabla `pregunta`
--
ALTER TABLE `pregunta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tema_id_tema` (`id_tema`);

--
-- Indices de la tabla `respuesta`
--
ALTER TABLE `respuesta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `respuesta_ibfk_1` (`id_estudiante`),
  ADD KEY `respuesta_ibfk_2` (`id_pregunta`);

--
-- Indices de la tabla `tema`
--
ALTER TABLE `tema`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `grupo`
--
ALTER TABLE `grupo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `grupoestudiante`
--
ALTER TABLE `grupoestudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `pendiente`
--
ALTER TABLE `pendiente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pregunta`
--
ALTER TABLE `pregunta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `respuesta`
--
ALTER TABLE `respuesta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `tema`
--
ALTER TABLE `tema`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `grupoestudiante`
--
ALTER TABLE `grupoestudiante`
  ADD CONSTRAINT `id_estudiante_usuario` FOREIGN KEY (`id_estudiante`) REFERENCES `usuario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idgrupo_grupo` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `pendiente`
--
ALTER TABLE `pendiente`
  ADD CONSTRAINT `id_grupo_grupo` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `pregunta`
--
ALTER TABLE `pregunta`
  ADD CONSTRAINT `tema_id_tema` FOREIGN KEY (`id_tema`) REFERENCES `tema` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `respuesta`
--
ALTER TABLE `respuesta`
  ADD CONSTRAINT `respuesta_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `usuario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `respuesta_ibfk_2` FOREIGN KEY (`id_pregunta`) REFERENCES `pregunta` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
