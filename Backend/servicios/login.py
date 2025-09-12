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
            select * from usuario where correo = %s and contrasenia = %s
            """
                        
            cursor.execute(query, (email, contrasenia,))
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()

            if not resultado:
                print("Usuario no encontrado.")
                return None
            
            id_usuario, nombre, email_db, password_db, id_rol = resultado[0]

            if contrasenia != password_db:
                print("Contraseña incorrecta.")
                return None

            usuario = Usuario(id_usuario, nombre, email_db, id_rol)

            print(f"Bienvenido, {usuario.nombre}")
            return usuario

        except mysql.connector.Error as err:
            print(f"Error al autenticar: {err}")
            return None