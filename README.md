# **AQUAMOVIL**

---

## **Introducción**  
AquaMóvil es un sistema de gestión de servicios de lavado de autos a domicilio on demand. Permite a los clientes solicitar el lavado de su vehículo, elegir ubicación y horario de manera sencilla. Los empleados reciben y gestionan los pedidos de forma organizada. El sistema contempla distintos roles de usuario, estados de pedidos, formas de pago y registro de operarios, garantizando una experiencia óptima para clientes, empleados y administradores.  
El administrador tiene el mayor nivel de acceso y supervisa el sistema, gestionando usuarios, operarios y pedidos para asegurar su correcto funcionamiento.

---

## **Tecnologías y Herramientas Utilizadas**  
AquaMóvil se desarrolló en Python por su claridad y versatilidad, utilizando Programación Orientada a Objetos (POO) para organizar el código en módulos, facilitar su mantenimiento y ampliar funcionalidades. La información se gestiona con MySQL siguiendo un modelo relacional.  
El desarrollo se realizó en Visual Studio Code y se gestionó con Git y GitHub para un control de versiones eficiente y trabajo en equipo. Se aplicó la metodología Scrum para organizar tareas y avances. La documentación incluye diagramas de clases, entidad-relación, código Python comentado y documentos según IEEE 830\.

---

## **Fundamentación Técnica**  
Python con POO permitió modelar de manera natural usuarios, pedidos y servicios, reflejando el funcionamiento real del negocio. La estructura modular con clases bien definidas mantiene el código ordenado, facilita la incorporación de nuevas funcionalidades y permite corregir errores sin afectar el sistema. Esto convierte a AquaMóvil en un sistema robusto, flexible y eficiente.

---

## **Roles de Usuario en AquaMóvil**

**Administrador:** gestionar usuarios, pedidos y asignaciones.

**Cliente:** solicitar servicios, realizar pagos y consultar el estado de sus pedidos.

**Empleado (lavacoches):** visualiza pedidos asignados y actualiza su estado.

---

## **Objetivos del Proyecto**

* Ofrecer un servicio de lavado a domicilio rápido, sencillo y eficiente, optimizando el tiempo de los clientes.  
* Gestionar de forma dinámica usuarios, pedidos y roles, adaptándose a las necesidades de cada tipo de usuario.  
* Generar información organizada y accesible para la administración del negocio, facilitando la toma de decisiones.  
* Sentar las bases para futuras ampliaciones, como apps móviles, franquicias o integración con pagos online.

---

# **INSTRUCCIONES TÉCNICAS**

**Backend (Python \+ MySQL)**

Este proyecto implementa un sistema básico de usuarios con roles, utilizando Python y MySQL.


## **Requisitos previos**

\- \[Python 3.10+\](https://www.python.org/downloads/)  

\- \[MySQL Server\](https://dev.mysql.com/downloads/mysql/)  

\- \[MySQL Workbench\](https://dev.mysql.com/downloads/workbench/) (opcional, recomendado)  

\- Librería *mysql-connector-python:*  (bash) *pip install mysql-connector-python*

---

## **Instalación de MySQL**

1. Descarga e instala **MySQL Server** desde la página oficial.  
2. Durante la instalación, define un **usuario y contraseña** (ejemplo: usuario root, contraseña 1234).  
3. Verifica que MySQL esté corriendo: *mysql \-u root \-p*

---

## **Importar la base de datos**

1. Abre MySQL Workbench o la terminal de MySQL.  
2. Crea la base de datos:

   *CREATE DATABASE aquamovil;*  
   *USE aquamovil;*  
3. Importa el script *aquamovil.sql* que viene en este repositorio (contiene las tablas usuarios y roles).

   * En Workbench: **Server → Data Import → Import from Self-Contained File → Seleccionar *aquamovil.sql* → Start Import**.  
   * En terminal: *mysql \-u root \-p aquamovil \< aquamovil.sql*

---

## **Cómo correr los archivos Python**

Todos los archivos están en la carpeta /backend.

 1. **conexion.py**

   Prueba la conexión con MySQL: *python backend/conexion.py*

   Deberías ver: *Conexión exitosa*


 2. **registrarse.py**

   Registra un nuevo usuario en la base de datos: *python backend/registrarse.py*


 3. **inicio\_sesion.py**

   Permite que un usuario inicie sesión con correo y contraseña: *python backend/inicio\_sesion.py*


 4. **administrador.py**

   Funciones de administrador: *python backend/administrador.py*

- Ver lista de usuarios
- Cambiar rol de un usuario
- Eliminar usuario

---