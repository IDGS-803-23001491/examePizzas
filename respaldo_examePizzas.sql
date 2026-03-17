/*
MySQL Backup
Database: examepizzas
Backup Time: 2026-03-17 14:14:40
*/

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `examepizzas`.`alembic_version`;
DROP TABLE IF EXISTS `examepizzas`.`clientes`;
DROP TABLE IF EXISTS `examepizzas`.`detalle_pedido`;
DROP TABLE IF EXISTS `examepizzas`.`detalle_temporal`;
DROP TABLE IF EXISTS `examepizzas`.`pedidos`;
DROP TABLE IF EXISTS `examepizzas`.`pizzas`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE `detalle_pedido` (
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `id_pedido` int NOT NULL,
  `id_pizza` int NOT NULL,
  `cantidad` int DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `id_pizza` (`id_pizza`),
  KEY `id_pedido` (`id_pedido`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE `detalle_temporal` (
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `tamano` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ingredientes` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `precio` decimal(8,2) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE `pedidos` (
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `fecha` date DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `id_cliente` (`id_cliente`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE TABLE `pizzas` (
  `id_pizza` int NOT NULL AUTO_INCREMENT,
  `tamano` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ingredientes` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `precio` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`id_pizza`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
BEGIN;
LOCK TABLES `examepizzas`.`alembic_version` WRITE;
DELETE FROM `examepizzas`.`alembic_version`;
INSERT INTO `examepizzas`.`alembic_version` (`version_num`) VALUES ('89f45ecbbacd')
;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `examepizzas`.`clientes` WRITE;
DELETE FROM `examepizzas`.`clientes`;
INSERT INTO `examepizzas`.`clientes` (`id_cliente`,`nombre`,`direccion`,`telefono`) VALUES (1, 'Juan', 'Su casa', '4770298317'),(2, 'Carlos', 'El parque', '4778942763'),(3, 'Pedro', 'La playa', '4778942768'),(4, 'Pablo', 'El trabajo', '4776890263'),(5, 'Juan', 'El parque', '4778942768')
;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `examepizzas`.`detalle_pedido` WRITE;
DELETE FROM `examepizzas`.`detalle_pedido`;
INSERT INTO `examepizzas`.`detalle_pedido` (`id_detalle`,`id_pedido`,`id_pizza`,`cantidad`,`subtotal`) VALUES (1, 1, 1, 3, 270.00),(2, 1, 2, 1, 60.00),(3, 2, 3, 6, 660.00),(4, 2, 1, 3, 270.00),(5, 3, 1, 7, 630.00),(6, 3, 4, 2, 260.00),(7, 3, 5, 4, 160.00),(8, 4, 5, 6, 240.00),(9, 5, 6, 5, 300.00)
;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `examepizzas`.`detalle_temporal` WRITE;
DELETE FROM `examepizzas`.`detalle_temporal`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `examepizzas`.`pedidos` WRITE;
DELETE FROM `examepizzas`.`pedidos`;
INSERT INTO `examepizzas`.`pedidos` (`id_pedido`,`id_cliente`,`fecha`,`precio`) VALUES (1, 1, '2026-03-17', 330.00),(2, 2, '2026-03-17', 930.00),(3, 3, '2026-03-15', 260.00),(4, 4, '2026-02-15', 40.00),(5, 5, '2026-03-16', 60.00)
;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `examepizzas`.`pizzas` WRITE;
DELETE FROM `examepizzas`.`pizzas`;
INSERT INTO `examepizzas`.`pizzas` (`id_pizza`,`tamano`,`ingredientes`,`precio`) VALUES (1, 'Mediana', 'Jamón', 90.00),(2, 'Chica', 'Champiñones,Piña', 60.00),(3, 'Mediana', 'Champiñones,Jamón,Piña', 110.00),(4, 'Grande', 'Champiñones', 130.00),(5, 'Chica', '', 40.00),(6, 'Chica', 'Jamón,Piña', 60.00)
;
UNLOCK TABLES;
COMMIT;
