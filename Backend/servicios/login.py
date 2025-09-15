from clases.usuario import Usuario
from clases.rol import Rol
import mysql.connector

class Login:

    def __init__(self, conexion):
        self.conexion = conexion

    def autenticar(self, email, contrasenia):

        try:

            conn = self.conexion.conectar()
            if not conn:
                return None

            cursor = conn.cursor()
            query = """
            SELECT * FROM usuario WHERE correo = %s AND contrasenia = %s
            """

            cursor.execute(query, (email, contrasenia,))
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()

            if not resultado:
                print("Usuario no encontrado.")
                return None
            
            id_usuario, nombre, email_db, password_db, id_rol, deleted = resultado[0]

            if contrasenia != password_db:
                print("Contraseña incorrecta.")
                return None

            usuario = Usuario(id_usuario, nombre, email_db, password_db, deleted, id_rol)

            print(f"\nBienvenido, {usuario.nombre}")
            return usuario

        except mysql.connector.Error as err:
            print(f"Error al autenticar: {err}")
            return None