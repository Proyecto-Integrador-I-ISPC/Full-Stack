# 📘 Documentación técnica: Diagramas y modelo de datos

Este documento describe la estructura y relación entre las entidades `Usuario`, `Rol` y `Servicio` mediante tres enfoques complementarios: **diagrama de clases**, **diagrama entidad-relación (ER)** y **modelo relacional**.  
Se incluye también la tabla intermedia `usuarioxservicio`, que implementa la relación **muchos a muchos (N:N)** entre `Usuario` y `Servicio`.

---

## 🧩 Diagrama de clases (UML)

El diagrama de clases representa la estructura lógica del sistema desde una perspectiva orientada a objetos.  
Define las clases, sus atributos, métodos y relaciones.

### Clases involucradas

#### Clase: `Usuario`
- **Atributos**:
  - `- id: int` → Identificador único del usuario (privado)
  - `- nombre: string` → Nombre del usuario
  - `- correo: string` → Correo electrónico
  - `- contrasenia: string` → Contraseña encriptada
  - `- id_rol: int` → Identificador del rol asignado (clave foránea)
- **Métodos**:
  - `+ registrar()`
  - `+ login()`
  - `+ verDatosPersonales()`
  - `+ editarDatosPersonales()`
  - `+ listarUsuarios()`
  - `+ cambiarRol()`
  - `+ eliminarUsuario()`

#### Clase: `Rol`
- **Atributos**:
  - `- id: int` → Identificador único del rol
  - `- nombre: string` → Nombre del rol (ej. administrador, cliente)

#### Clase: `Servicio`
- **Atributos**:
  - `- idservicio: int` → Identificador único del servicio
  - `- nombre: string` → Nombre del servicio
  - `- descripcion: string` → Descripción breve del servicio
  - `- precio: float` → Precio del servicio

#### Clase: `UsuarioxServicio`
- **Atributos**:
  - `- idusuarioxservicio: int` → Identificador único del registro
  - `- id_usuario: int` → Clave foránea que referencia a `Usuario`
  - `- id_servicio: int` → Clave foránea que referencia a `Servicio`
  - `- fecha: datetime` → Fecha de contratación o asignación
- **Rol**: Esta clase **no representa una entidad lógica del negocio**, sino una **asociación** que implementa la relación muchos a muchos entre `Usuario` y `Servicio`.

### Relaciones

- Un **Rol** puede estar asignado a **muchos Usuarios** → relación **1:N**
- Un **Usuario** puede tener **muchos Servicios**, y un **Servicio** puede pertenecer a **muchos Usuarios** → relación **N:N** implementada por la clase asociativa `UsuarioxServicio`.

---

## 🗃️ Diagrama entidad-relación (ER)

El diagrama ER representa las entidades del sistema y sus relaciones desde una perspectiva de base de datos.

### Entidades principales

#### Entidad: `Usuario`
- `id` (PK, INT)
- `nombre` (VARCHAR)
- `correo` (VARCHAR)
- `contrasenia` (VARCHAR)
- `id_rol` (FK, INT) → Referencia a `Rol.id`

#### Entidad: `Rol`
- `id` (PK, INT)
- `nombre` (VARCHAR)

#### Entidad: `Servicio`
- `idservicio` (PK, INT)
- `nombre` (VARCHAR)
- `descripcion` (VARCHAR)
- `precio` (DECIMAL)

#### Entidad intermedia: `usuarioxservicio`
- `idusuarioxservicio` (PK, INT)
- `id_usuario` (FK, INT) → Referencia a `Usuario.id`
- `id_servicio` (FK, INT) → Referencia a `Servicio.idservicio`
- `fecha` (DATETIME)

### Relaciones

- **Usuario – Rol** → Relación **1:N**
  - Un rol puede estar asignado a varios usuarios.
- **Usuario – Servicio** → Relación **N:N**, implementada mediante la entidad intermedia `usuarioxservicio`.

### Simbología

- En `Rol` → `1`
- En `Usuario` → `N`
- En `UsuarioxServicio` → se conecta con **dos relaciones 1:N**:
  - `Usuario 1 ─── N UsuarioxServicio N ─── 1 Servicio`

---

## 🧱 Modelo relacional

El modelo relacional define cómo se implementan las entidades y relaciones en la base de datos.

### Tabla: `Rol`

CREATE TABLE Rol (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);

### Tabla: `Usuario`

CREATE TABLE Usuario (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  correo VARCHAR(150),
  contrasenia VARCHAR(255),
  id_rol INT,
  FOREIGN KEY (id_rol) REFERENCES Rol(id)
);

### Tabla: `Servicio`

CREATE TABLE Servicio (
  idservicio INT PRIMARY KEY,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(10,2)
);

### Tabla: `usuarioxservicio`

CREATE TABLE usuarioxservicio (
  idusuarioxservicio INT NOT NULL AUTO_INCREMENT,
  id_usuario INT DEFAULT NULL,
  id_servicio INT DEFAULT NULL,
  fecha DATETIME DEFAULT NULL,
  PRIMARY KEY (idusuarioxservicio),
  KEY fk_usuario_idx (id_usuario),
  KEY fk_servicio_idx (id_servicio),
  CONSTRAINT fk_servicio FOREIGN KEY (id_servicio) REFERENCES servicio (idservicio),
  CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES usuario (id)
);

Explicación

1) La tabla usuarioxservicio implementa la relación N:N entre Usuario y Servicio.
2) Cada registro representa una asociación única entre un usuario y un servicio determinado.
3) Se pueden almacenar atributos adicionales de la relación, como fecha.