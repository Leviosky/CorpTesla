-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Apr 14, 2024 at 06:54 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tesla`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `ClientesID` int(11) NOT NULL,
  `ClienteNombre` varchar(50) NOT NULL,
  `ClienteCedula` varchar(15) NOT NULL,
  `ClienteTel` varchar(15) NOT NULL,
  `ClienteEmail` varchar(50) NOT NULL,
  `id_services` int(5) NOT NULL,
  `ClienteComent` varchar(200) NOT NULL,
  `ClienteLat` varchar(100) NOT NULL,
  `ClienteLon` varchar(100) NOT NULL,
  `ClienteDone` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`ClientesID`, `ClienteNombre`, `ClienteCedula`, `ClienteTel`, `ClienteEmail`, `id_services`, `ClienteComent`, `ClienteLat`, `ClienteLon`, `ClienteDone`) VALUES
(1, 'levi sanchez', '6-723-1548', '68312443', 'lsanchez@corptesla.com', 5, 'asdasdasdasd', '7.974275921465744', '-80.43153047561646', 0),
(2, 'yelenis Gallardo', '7-712-1569', '62027840', 'ygallardo@corptesla.com', 4, 'Automatizacion de aires, luces y puertas con alexa', '7.935122740865674', '-80.42071580886842', 0),
(3, 'fadul', '6-721-2401', '123123123', 'fadul12323@gmail.com', 3, 'xD', '7.974034781586858', '-80.42837083339693', 0);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `rol` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id_rol`, `rol`) VALUES
(1, 'Admin'),
(2, 'Ingeniero'),
(3, 'Ventas'),
(4, 'Instalador');

-- --------------------------------------------------------

--
-- Table structure for table `servicios`
--

CREATE TABLE `servicios` (
  `id_services` int(11) NOT NULL,
  `services` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `servicios`
--

INSERT INTO `servicios` (`id_services`, `services`) VALUES
(1, 'Diseño e Instalación de Sistema Fotovoltaico'),
(2, 'Diseño e Instalación de Sistema Eléctrico'),
(3, 'Energía Eléctrica'),
(4, 'Automatización Residencial'),
(5, 'Automatización Industrial'),
(6, 'Otro');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_rol` int(10) NOT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `correo`, `password`, `id_rol`, `nombre`) VALUES
(1, 'levi.sanchez@corptesla.com', '$2b$12$5nT0NDOWNvMeIFDLYKU7he7hEQ.opgfcvbSJZfQT9bGv49Kls3JfS', 1, 'Levi Sanchez');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ClientesID`),
  ADD KEY `id_services` (`id_services`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indexes for table `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id_services`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ClientesID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id_services` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`id_services`) REFERENCES `servicios` (`id_services`);

--
-- Constraints for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_roles` FOREIGN KEY (`id`) REFERENCES `usuarios` (`id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
