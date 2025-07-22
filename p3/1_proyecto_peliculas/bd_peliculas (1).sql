-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2025 a las 06:25:34
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_utd_2a_cla`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bd_peliculas`
--

CREATE TABLE `bd_peliculas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `categoria` varchar(100) NOT NULL,
  `Clasificacion` varchar(100) NOT NULL,
  `genero` varchar(100) NOT NULL,
  `idioma` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bd_peliculas`
--

INSERT INTO `bd_peliculas` (`id`, `nombre`, `categoria`, `Clasificacion`, `genero`, `idioma`) VALUES
(1, 'toystory', 'infantil', 'AA', 'Animacion', 'Español'),
(2, '1887', 'accion', 'B', 'Wester', 'español'),
(3, 'F1', 'carreras', 'B', 'Accion', 'español'),
(4, 'Titanic', 'Drama', 'B', 'Romance', 'Ingles'),
(5, 'Cars', 'Carreras', 'A', 'Animacion', 'Español');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bd_peliculas`
--
ALTER TABLE `bd_peliculas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `bd_peliculas`
--
ALTER TABLE `bd_peliculas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
