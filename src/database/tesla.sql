-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 12, 2024 at 08:28 PM
-- Server version: 8.0.36
-- PHP Version: 8.1.10

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
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('33febd5569c7');

-- --------------------------------------------------------

--
-- Table structure for table `bateria`
--

CREATE TABLE `bateria` (
  `id_Bateria` int NOT NULL,
  `Marca` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `bateria`
--

INSERT INTO `bateria` (`id_Bateria`, `Marca`) VALUES
(1, 'PylonTech');

-- --------------------------------------------------------

--
-- Table structure for table `clase_de_proyecto`
--

CREATE TABLE `clase_de_proyecto` (
  `ClaseID` int NOT NULL,
  `Clase` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `clase_de_proyecto`
--

INSERT INTO `clase_de_proyecto` (`ClaseID`, `Clase`) VALUES
(1, 'Residencial'),
(2, 'Comercial'),
(3, 'Industrial');

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `ClientesID` int NOT NULL,
  `ClienteNombre` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ClienteCedula` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ClienteTel` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ClienteEmail` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_services` int DEFAULT NULL,
  `ClienteComent` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ClienteLat` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ClienteLon` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ClienteDone` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `diseño`
--

CREATE TABLE `diseño` (
  `DiseñoID` int NOT NULL,
  `SolarID` int DEFAULT NULL,
  `Planos` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inversor`
--

CREATE TABLE `inversor` (
  `id_inversor` int NOT NULL,
  `MarcaID` int DEFAULT NULL,
  `Capacidad` int DEFAULT NULL,
  `Model` varchar(100) DEFAULT NULL,
  `SolarID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inversores`
--

CREATE TABLE `inversores` (
  `id_marca` int NOT NULL,
  `Marca` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `paneles`
--

CREATE TABLE `paneles` (
  `id_Panel` int NOT NULL,
  `Marca` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `propuestas`
--

CREATE TABLE `propuestas` (
  `id_propuesta` int NOT NULL,
  `ProjectID` int DEFAULT NULL,
  `Propuesta` varchar(255) DEFAULT NULL,
  `PropuestaFile` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `proyectos`
--

CREATE TABLE `proyectos` (
  `ProjectID` int NOT NULL,
  `ClientesID` int DEFAULT NULL,
  `ClaseID` int DEFAULT NULL,
  `TipoID` int DEFAULT NULL,
  `ProjectLat` varchar(100) DEFAULT NULL,
  `ProjectLon` varchar(100) DEFAULT NULL,
  `InitDate` date DEFAULT NULL,
  `FinishDate` date DEFAULT NULL,
  `ProjectName` varchar(100) DEFAULT NULL,
  `CompletadoStatus` tinyint(1) DEFAULT NULL,
  `CanceladoStatus` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `proyecto_solar`
--

CREATE TABLE `proyecto_solar` (
  `SolarID` int NOT NULL,
  `SolarName` varchar(255) DEFAULT NULL,
  `ProjectID` int DEFAULT NULL,
  `TechoID` int DEFAULT NULL,
  `TechoInfo` varchar(255) DEFAULT NULL,
  `Aguas` int DEFAULT NULL,
  `AreaM2` float DEFAULT NULL,
  `IpAmp` int DEFAULT NULL,
  `Demanda` int DEFAULT NULL,
  `SistemaID` int DEFAULT NULL,
  `CapacidadInst` float DEFAULT NULL,
  `PanelID` int DEFAULT NULL,
  `PanelWatts` int DEFAULT NULL,
  `PanelUnits` int DEFAULT NULL,
  `BattID` int DEFAULT NULL,
  `BattWatts` int DEFAULT NULL,
  `BattUnits` int DEFAULT NULL,
  `Comentarios` varchar(255) DEFAULT NULL,
  `Medunits` int DEFAULT NULL,
  `Medbrand` varchar(100) DEFAULT NULL,
  `Medtipe` varchar(100) DEFAULT NULL,
  `DataLogger` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `revision`
--

CREATE TABLE `revision` (
  `id_revision` int NOT NULL,
  `SolarID` int DEFAULT NULL,
  `PapNaturgy` tinyint(1) DEFAULT NULL,
  `PapBomberos` tinyint(1) DEFAULT NULL,
  `PapMunicipio` tinyint(1) DEFAULT NULL,
  `InversorConfig` tinyint(1) DEFAULT NULL,
  `InversorLog` tinyint(1) DEFAULT NULL,
  `letrero` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id_rol` int NOT NULL,
  `rol` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id_rol`, `rol`) VALUES
(1, 'Admin'),
(2, 'Ingeniero'),
(4, 'Instalador'),
(3, 'Ventas');

-- --------------------------------------------------------

--
-- Table structure for table `servicios`
--

CREATE TABLE `servicios` (
  `id_services` int NOT NULL,
  `services` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `servicios`
--

INSERT INTO `servicios` (`id_services`, `services`) VALUES
(2, 'Automatización y Domótica'),
(1, 'Diseño e Instalación de Sistema Fotovoltaico'),
(3, 'Energía Eléctrica');

-- --------------------------------------------------------

--
-- Table structure for table `sistema_fotovoltaico`
--

CREATE TABLE `sistema_fotovoltaico` (
  `id_Sistema` int NOT NULL,
  `Sistema` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sistema_fotovoltaico`
--

INSERT INTO `sistema_fotovoltaico` (`id_Sistema`, `Sistema`) VALUES
(1, 'OFF-GRID'),
(2, 'ON-GRID'),
(3, 'Hybrid');

-- --------------------------------------------------------

--
-- Table structure for table `tipo_de_techo`
--

CREATE TABLE `tipo_de_techo` (
  `id_Techo` int NOT NULL,
  `Material` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tipo_de_techo`
--

INSERT INTO `tipo_de_techo` (`id_Techo`, `Material`) VALUES
(1, 'Zinc'),
(2, 'Panel Sandwich'),
(3, 'Tejalit'),
(4, 'Panalit'),
(5, 'Teja (Buena)'),
(6, 'Teja (Mala)');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `correo` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_rol` int DEFAULT NULL,
  `nombre` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `cedula` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `profile_picture` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `correo`, `password`, `id_rol`, `nombre`, `cedula`, `profile_picture`) VALUES
(1, 'levi.sanchez@corptesla.com', '$2b$12$5nT0NDOWNvMeIFDLYKU7he7hEQ.opgfcvbSJZfQT9bGv49Kls3JfS', 1, 'Levi Sánchez', '6-723-1548', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ventas`
--

CREATE TABLE `ventas` (
  `VentasID` int NOT NULL,
  `PropuestaID` int DEFAULT NULL,
  `Pago1` tinyint(1) DEFAULT NULL,
  `Pago2` tinyint(1) DEFAULT NULL,
  `Pago3` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `bateria`
--
ALTER TABLE `bateria`
  ADD PRIMARY KEY (`id_Bateria`);

--
-- Indexes for table `clase_de_proyecto`
--
ALTER TABLE `clase_de_proyecto`
  ADD PRIMARY KEY (`ClaseID`);

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ClientesID`),
  ADD UNIQUE KEY `ix_clientes_ClienteCedula` (`ClienteCedula`),
  ADD UNIQUE KEY `ix_clientes_ClienteEmail` (`ClienteEmail`),
  ADD UNIQUE KEY `ix_clientes_ClienteLat` (`ClienteLat`),
  ADD UNIQUE KEY `ix_clientes_ClienteLon` (`ClienteLon`),
  ADD KEY `id_services` (`id_services`),
  ADD KEY `ix_clientes_ClienteComent` (`ClienteComent`),
  ADD KEY `ix_clientes_ClienteNombre` (`ClienteNombre`),
  ADD KEY `ix_clientes_ClienteTel` (`ClienteTel`);

--
-- Indexes for table `diseño`
--
ALTER TABLE `diseño`
  ADD PRIMARY KEY (`DiseñoID`),
  ADD KEY `SolarID` (`SolarID`);

--
-- Indexes for table `inversor`
--
ALTER TABLE `inversor`
  ADD PRIMARY KEY (`id_inversor`),
  ADD KEY `MarcaID` (`MarcaID`),
  ADD KEY `SolarID` (`SolarID`);

--
-- Indexes for table `inversores`
--
ALTER TABLE `inversores`
  ADD PRIMARY KEY (`id_marca`);

--
-- Indexes for table `paneles`
--
ALTER TABLE `paneles`
  ADD PRIMARY KEY (`id_Panel`);

--
-- Indexes for table `propuestas`
--
ALTER TABLE `propuestas`
  ADD PRIMARY KEY (`id_propuesta`),
  ADD KEY `ProjectID` (`ProjectID`);

--
-- Indexes for table `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`ProjectID`),
  ADD UNIQUE KEY `ix_proyectos_ProjectLat` (`ProjectLat`),
  ADD UNIQUE KEY `ix_proyectos_ProjectLon` (`ProjectLon`),
  ADD KEY `ClaseID` (`ClaseID`),
  ADD KEY `ClientesID` (`ClientesID`),
  ADD KEY `TipoID` (`TipoID`);

--
-- Indexes for table `proyecto_solar`
--
ALTER TABLE `proyecto_solar`
  ADD PRIMARY KEY (`SolarID`),
  ADD KEY `BattID` (`BattID`),
  ADD KEY `PanelID` (`PanelID`),
  ADD KEY `ProjectID` (`ProjectID`),
  ADD KEY `SistemaID` (`SistemaID`),
  ADD KEY `TechoID` (`TechoID`);

--
-- Indexes for table `revision`
--
ALTER TABLE `revision`
  ADD PRIMARY KEY (`id_revision`),
  ADD KEY `SolarID` (`SolarID`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`),
  ADD UNIQUE KEY `rol_2` (`rol`),
  ADD KEY `rol` (`rol`);

--
-- Indexes for table `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id_services`),
  ADD UNIQUE KEY `services` (`services`);

--
-- Indexes for table `sistema_fotovoltaico`
--
ALTER TABLE `sistema_fotovoltaico`
  ADD PRIMARY KEY (`id_Sistema`);

--
-- Indexes for table `tipo_de_techo`
--
ALTER TABLE `tipo_de_techo`
  ADD PRIMARY KEY (`id_Techo`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_usuarios_cedula` (`cedula`),
  ADD UNIQUE KEY `ix_usuarios_correo` (`correo`),
  ADD KEY `id_rol` (`id_rol`),
  ADD KEY `ix_usuarios_nombre` (`nombre`),
  ADD KEY `ix_usuarios_password` (`password`);

--
-- Indexes for table `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`VentasID`),
  ADD KEY `PropuestaID` (`PropuestaID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bateria`
--
ALTER TABLE `bateria`
  MODIFY `id_Bateria` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `clase_de_proyecto`
--
ALTER TABLE `clase_de_proyecto`
  MODIFY `ClaseID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `clientes`
--
ALTER TABLE `clientes`
  MODIFY `ClientesID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diseño`
--
ALTER TABLE `diseño`
  MODIFY `DiseñoID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inversor`
--
ALTER TABLE `inversor`
  MODIFY `id_inversor` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inversores`
--
ALTER TABLE `inversores`
  MODIFY `id_marca` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paneles`
--
ALTER TABLE `paneles`
  MODIFY `id_Panel` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `propuestas`
--
ALTER TABLE `propuestas`
  MODIFY `id_propuesta` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `proyectos`
--
ALTER TABLE `proyectos`
  MODIFY `ProjectID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `proyecto_solar`
--
ALTER TABLE `proyecto_solar`
  MODIFY `SolarID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `revision`
--
ALTER TABLE `revision`
  MODIFY `id_revision` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id_services` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sistema_fotovoltaico`
--
ALTER TABLE `sistema_fotovoltaico`
  MODIFY `id_Sistema` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tipo_de_techo`
--
ALTER TABLE `tipo_de_techo`
  MODIFY `id_Techo` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ventas`
--
ALTER TABLE `ventas`
  MODIFY `VentasID` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`id_services`) REFERENCES `servicios` (`id_services`);

--
-- Constraints for table `diseño`
--
ALTER TABLE `diseño`
  ADD CONSTRAINT `diseño_ibfk_1` FOREIGN KEY (`SolarID`) REFERENCES `proyecto_solar` (`SolarID`);

--
-- Constraints for table `inversor`
--
ALTER TABLE `inversor`
  ADD CONSTRAINT `inversor_ibfk_1` FOREIGN KEY (`MarcaID`) REFERENCES `inversores` (`id_marca`),
  ADD CONSTRAINT `inversor_ibfk_2` FOREIGN KEY (`SolarID`) REFERENCES `proyecto_solar` (`SolarID`);

--
-- Constraints for table `propuestas`
--
ALTER TABLE `propuestas`
  ADD CONSTRAINT `propuestas_ibfk_1` FOREIGN KEY (`ProjectID`) REFERENCES `proyectos` (`ProjectID`);

--
-- Constraints for table `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `proyectos_ibfk_1` FOREIGN KEY (`ClaseID`) REFERENCES `clase_de_proyecto` (`ClaseID`),
  ADD CONSTRAINT `proyectos_ibfk_2` FOREIGN KEY (`ClientesID`) REFERENCES `clientes` (`ClientesID`),
  ADD CONSTRAINT `proyectos_ibfk_3` FOREIGN KEY (`TipoID`) REFERENCES `servicios` (`id_services`);

--
-- Constraints for table `proyecto_solar`
--
ALTER TABLE `proyecto_solar`
  ADD CONSTRAINT `proyecto_solar_ibfk_1` FOREIGN KEY (`BattID`) REFERENCES `bateria` (`id_Bateria`),
  ADD CONSTRAINT `proyecto_solar_ibfk_3` FOREIGN KEY (`PanelID`) REFERENCES `paneles` (`id_Panel`),
  ADD CONSTRAINT `proyecto_solar_ibfk_4` FOREIGN KEY (`ProjectID`) REFERENCES `proyectos` (`ProjectID`),
  ADD CONSTRAINT `proyecto_solar_ibfk_5` FOREIGN KEY (`SistemaID`) REFERENCES `sistema_fotovoltaico` (`id_Sistema`),
  ADD CONSTRAINT `proyecto_solar_ibfk_6` FOREIGN KEY (`TechoID`) REFERENCES `tipo_de_techo` (`id_Techo`);

--
-- Constraints for table `revision`
--
ALTER TABLE `revision`
  ADD CONSTRAINT `revision_ibfk_1` FOREIGN KEY (`SolarID`) REFERENCES `proyecto_solar` (`SolarID`);

--
-- Constraints for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`);

--
-- Constraints for table `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`PropuestaID`) REFERENCES `propuestas` (`id_propuesta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
