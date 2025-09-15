--- Crear BD y utilizarla (codificación UTF-8)
CREATE DATABASE IF NOT EXISTS aquamovilbd
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE aquamovilbd;

--- Creación tabla ROL
CREATE TABLE IF NOT EXISTS rol (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--- Inserciones mínimas (roles)
INSERT INTO rol (nombre) VALUES ('Administrador'), ('Usuario Estándar');

--- Creación tabla USUARIO
CREATE TABLE IF NOT EXISTS usuario (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  correo VARCHAR(45) NOT NULL,
  contrasenia VARCHAR(45) NOT NULL,
  id_rol INT NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--- IMPORTANTE: Edición posterior
ALTER TABLE usuario ADD COLUMN deleted BOOLEAN NOT NULL DEFAULT FALSE;

--- Inserción mínima (Administrador)
INSERT INTO usuario (nombre, correo, contrasenia, id_rol) VALUES ('Rafael Cáceres', 'rafaelcaceres@gmail.com', 'RAfael11??', 1);