CREATE DATABASE  IF NOT EXISTS `boxhapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `boxhapp`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: boxhapp
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_dat_clasificacion_especie`
--

DROP TABLE IF EXISTS `tb_dat_clasificacion_especie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_clasificacion_especie` (
  `id_especie` int NOT NULL AUTO_INCREMENT,
  `nombre_especie` varchar(20) NOT NULL,
  `origen` varchar(20) NOT NULL,
  `rendimiento` int NOT NULL,
  `observacion` varchar(250) NOT NULL,
  PRIMARY KEY (`id_especie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_clasificacion_especie`
--

LOCK TABLES `tb_dat_clasificacion_especie` WRITE;
/*!40000 ALTER TABLE `tb_dat_clasificacion_especie` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_clasificacion_especie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_clasificacion_inventario`
--

DROP TABLE IF EXISTS `tb_dat_clasificacion_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_clasificacion_inventario` (
  `id_inventario` int NOT NULL AUTO_INCREMENT,
  `id_lote` int NOT NULL,
  `cantidad_kg` float NOT NULL,
  `clasificacion_calidad` varchar(20) NOT NULL,
  `id_usuario_clasifica` int NOT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_usuario_aprueba` int NOT NULL,
  `lugar_almacenamiento` varchar(50) NOT NULL,
  `observacion` varchar(250) NOT NULL,
  PRIMARY KEY (`id_inventario`),
  KEY `id_lote` (`id_lote`),
  KEY `id_usuario_clasifica` (`id_usuario_clasifica`),
  KEY `id_usuario_aprueba` (`id_usuario_aprueba`),
  CONSTRAINT `tb_dat_clasificacion_inventario_ibfk_1` FOREIGN KEY (`id_lote`) REFERENCES `tb_dat_lote` (`id_lote`),
  CONSTRAINT `tb_dat_clasificacion_inventario_ibfk_2` FOREIGN KEY (`id_usuario_clasifica`) REFERENCES `tb_dat_usuarios` (`id_usuario`),
  CONSTRAINT `tb_dat_clasificacion_inventario_ibfk_3` FOREIGN KEY (`id_usuario_aprueba`) REFERENCES `tb_dat_usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_clasificacion_inventario`
--

LOCK TABLES `tb_dat_clasificacion_inventario` WRITE;
/*!40000 ALTER TABLE `tb_dat_clasificacion_inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_clasificacion_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_costos_produccion`
--

DROP TABLE IF EXISTS `tb_dat_costos_produccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_costos_produccion` (
  `id_costo` int NOT NULL AUTO_INCREMENT,
  `id_lote` int NOT NULL,
  `fecha` date NOT NULL,
  `id_usuario` int NOT NULL,
  `salarios` float NOT NULL,
  `insumos_agricolas` float NOT NULL,
  `equipos` float NOT NULL,
  `servicios_publicos` float NOT NULL,
  `transporte` float NOT NULL,
  `gastos_admin` float NOT NULL,
  `gastos_financieros` float NOT NULL,
  `otros_costos` float NOT NULL,
  `observaciones` varchar(250) NOT NULL,
  `id_usuario_aprueba` int NOT NULL,
  PRIMARY KEY (`id_costo`),
  KEY `id_lote` (`id_lote`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_usuario_aprueba` (`id_usuario_aprueba`),
  CONSTRAINT `tb_dat_costos_produccion_ibfk_1` FOREIGN KEY (`id_lote`) REFERENCES `tb_dat_lote` (`id_lote`),
  CONSTRAINT `tb_dat_costos_produccion_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `tb_dat_usuarios` (`id_usuario`),
  CONSTRAINT `tb_dat_costos_produccion_ibfk_3` FOREIGN KEY (`id_usuario_aprueba`) REFERENCES `tb_dat_usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_costos_produccion`
--

LOCK TABLES `tb_dat_costos_produccion` WRITE;
/*!40000 ALTER TABLE `tb_dat_costos_produccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_costos_produccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_lote`
--

DROP TABLE IF EXISTS `tb_dat_lote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_lote` (
  `id_lote` int NOT NULL AUTO_INCREMENT,
  `nombre_lote` varchar(50) NOT NULL,
  `ubicacion` varchar(100) NOT NULL,
  `area_m2` int NOT NULL,
  `observacion` varchar(250) NOT NULL,
  PRIMARY KEY (`id_lote`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_lote`
--

LOCK TABLES `tb_dat_lote` WRITE;
/*!40000 ALTER TABLE `tb_dat_lote` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_lote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_proyeccion`
--

DROP TABLE IF EXISTS `tb_dat_proyeccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_proyeccion` (
  `id_proyeccion` int NOT NULL AUTO_INCREMENT,
  `id_especie` int NOT NULL,
  `topografia_terreno` varchar(10) NOT NULL,
  `temperatura_celsius` float NOT NULL,
  `altura_metros` int NOT NULL,
  `area_terreno_m2` int NOT NULL,
  `pais` varchar(50) NOT NULL,
  `departamento` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `nombre_finca` varchar(50) NOT NULL,
  `observacion` varchar(250) NOT NULL,
  PRIMARY KEY (`id_proyeccion`),
  KEY `id_especie` (`id_especie`),
  CONSTRAINT `tb_dat_proyeccion_ibfk_1` FOREIGN KEY (`id_especie`) REFERENCES `tb_dat_clasificacion_especie` (`id_especie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_proyeccion`
--

LOCK TABLES `tb_dat_proyeccion` WRITE;
/*!40000 ALTER TABLE `tb_dat_proyeccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_proyeccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_recoleccion`
--

DROP TABLE IF EXISTS `tb_dat_recoleccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_recoleccion` (
  `id_recoleccion` int NOT NULL AUTO_INCREMENT,
  `id_lote` int NOT NULL,
  `id_proyeccion_resultado` int NOT NULL,
  `cantidad_recogida_kg` float NOT NULL,
  `usuario_recolecta` varchar(10) NOT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `usuario_registra` varchar(10) NOT NULL,
  `observacion` varchar(250) NOT NULL,
  PRIMARY KEY (`id_recoleccion`),
  KEY `id_lote` (`id_lote`),
  KEY `id_proyeccion_resultado` (`id_proyeccion_resultado`),
  CONSTRAINT `tb_dat_recoleccion_ibfk_1` FOREIGN KEY (`id_lote`) REFERENCES `tb_dat_lote` (`id_lote`),
  CONSTRAINT `tb_dat_recoleccion_ibfk_2` FOREIGN KEY (`id_proyeccion_resultado`) REFERENCES `tb_dat_resultado_proyeccion` (`id_proyeccion_resultado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_recoleccion`
--

LOCK TABLES `tb_dat_recoleccion` WRITE;
/*!40000 ALTER TABLE `tb_dat_recoleccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_recoleccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_resultado_proyeccion`
--

DROP TABLE IF EXISTS `tb_dat_resultado_proyeccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_resultado_proyeccion` (
  `id_proyeccion_resultado` int NOT NULL AUTO_INCREMENT,
  `id_proyeccion` int NOT NULL,
  `distancia_surco_m2` float NOT NULL,
  `cantidad_producida_kg` float NOT NULL,
  `cantidad_semillas` int NOT NULL,
  PRIMARY KEY (`id_proyeccion_resultado`),
  KEY `id_proyeccion` (`id_proyeccion`),
  CONSTRAINT `tb_dat_resultado_proyeccion_ibfk_1` FOREIGN KEY (`id_proyeccion`) REFERENCES `tb_dat_proyeccion` (`id_proyeccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_resultado_proyeccion`
--

LOCK TABLES `tb_dat_resultado_proyeccion` WRITE;
/*!40000 ALTER TABLE `tb_dat_resultado_proyeccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dat_resultado_proyeccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_roles`
--

DROP TABLE IF EXISTS `tb_dat_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(200) DEFAULT NULL,
  `Descripcion` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id_rol`),
  UNIQUE KEY `nombre_rol` (`nombre_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_roles`
--

LOCK TABLES `tb_dat_roles` WRITE;
/*!40000 ALTER TABLE `tb_dat_roles` DISABLE KEYS */;
INSERT INTO `tb_dat_roles` VALUES (1,'Prueba','Prueba crear en tabla base de datos'),(3,'Prueba3','Modificacion de descripcion correcta'),(4,'Prueba5','Prueba mas datos'),(5,'ingreso nombre largo de rol','revisar descro´pociopm ára eñ rol largo'),(7,'Administrador','Rol administrador para la aplicacion Boxhapp');
/*!40000 ALTER TABLE `tb_dat_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dat_usuarios`
--

DROP TABLE IF EXISTS `tb_dat_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dat_usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(10) NOT NULL,
  `id_rol` int NOT NULL,
  `id_identificacion` int NOT NULL,
  `primer_nombre` varchar(15) NOT NULL,
  `segundo_nombre` varchar(15) DEFAULT NULL,
  `primer_apellido` varchar(15) NOT NULL,
  `segundo_apellido` varchar(15) DEFAULT NULL,
  `cargo` varchar(50) NOT NULL,
  `celular` bigint NOT NULL,
  `contrasena` varchar(50) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `tipo_documento` varchar(500) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `tb_dat_usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `tb_dat_roles` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dat_usuarios`
--

LOCK TABLES `tb_dat_usuarios` WRITE;
/*!40000 ALTER TABLE `tb_dat_usuarios` DISABLE KEYS */;
INSERT INTO `tb_dat_usuarios` VALUES (3,'Prueba3',3,800,'gina','carolina','suarez','','aux',800000,'12','arrow@prueba.com','122','1990-01-01'),(4,'ad',3,6565,'dsgf','sdgf','asdg','adfg','adsf',1000,'6565','dfg','656','2000-01-01'),(5,'ax',3,9840,'andrea','','echeverry','','ss',335,'12345','sdafgads','5656','2000-01-01'),(6,'other',3,1022900618,'asdfg','adgf','adfg','adfg','sdc',1234567890,'656','hfdtghjsgf','vv','2020-01-01');
/*!40000 ALTER TABLE `tb_dat_usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-17 22:44:34
