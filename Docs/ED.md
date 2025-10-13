# 📘 Documentación técnica: Diagramas y modelo de datos

Este documento describe la estructura y relación entre las entidades `Usuario` y `Rol` a través de tres enfoques complementarios: **diagrama de clases**, **diagrama entidad-relación (ER)** y **modelo relacional**. Cada uno cumple una función específica en el diseño y documentación del sistema.

---

## 🧩 Diagrama de clases (UML)

El diagrama de clases representa la estructura lógica del sistema desde una perspectiva orientada a objetos. Define las clases, sus atributos, métodos y relaciones.

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

### Relación entre clases

- Un **rol** puede estar asignado a **muchos usuarios** → relación **1:N**
- Se representa con una **línea recta** entre las clases, con multiplicidades: Usuario * ──────────────── 1 Rol

---

## 🗃️ Diagrama entidad-relación (ER)

El diagrama ER representa las entidades del sistema y sus relaciones desde una perspectiva de base de datos. Es útil para visualizar cómo se estructuran los datos y cómo se vinculan.

### Entidades

#### Entidad: `Usuario`
- `id` (PK, INT)
- `nombre` (VARCHAR)
- `correo` (VARCHAR)
- `contrasenia` (VARCHAR)
- `id_rol` (FK, INT) → Referencia a `Rol.id`

#### Entidad: `Rol`
- `id` (PK, INT)
- `nombre` (VARCHAR)

### Relación

- **Nombre**: "tiene"
- **Tipo**: 1:N (uno a muchos)
- **Dirección**: Un rol puede estar asignado a varios usuarios

### Simbología

- Se utiliza una **línea recta** entre las entidades
- En el extremo de `Rol`: `1`
- En el extremo de `Usuario`: `N` o `∞`

Ejemplo visual: Usuario ∞ ──────────────── 1 Rol

---

## 🧱 Modelo relacional

El modelo relacional define cómo se implementan las entidades y relaciones en una base de datos relacional. Es la base para generar scripts SQL y estructurar tablas.

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

Relación
- id_rol en la tabla Usuario actúa como clave foránea que referencia a Rol.id
- Esto establece una relación uno a muchos: varios usuarios pueden compartir el mismo rol