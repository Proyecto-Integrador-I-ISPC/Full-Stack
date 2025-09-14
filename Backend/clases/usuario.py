from servicios.conexion import Conexion

class Usuario:
    def __init__(self, id, nombre, correo, contrasenia, idrol):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia
        self.idrol = idrol

    # ----------- Métodos en común ----------- #
    def ver_datos(self):
        print("\n--- Mis datos personales ---")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Rol ID: {self.idrol}") #Solo visualización

    def editar_datos(self):
        print("\n--- Editar mis datos (vacío para no editar) ---")
        nuevo_nombre = input(f"Nuevo nombre {self.nombre}): ").strip() or self.nombre
        nuevo_correo = input(f"Nuevo correo {self.correo}): ").strip() or self.correo
        nueva_contrasenia = input("Nueva contraseña: ").strip() or self.contrasenia

        db = Conexion()
        conn = db.conectar()

        if not conn:
            print("No se pudo conectar a la base de datos.")
            return

        try:
            cursor = conn.cursor()
            sql = """
                UPDATE usuario 
                SET nombre = %s, correo = %s, contrasenia = %s
                WHERE id = %s
            """
            valores = (nuevo_nombre, nuevo_correo, nueva_contrasenia, self.id)
            cursor.execute(sql, valores)
            conn.commit()

            # Actualizar
            self.nombre = nuevo_nombre
            self.correo = nuevo_correo
            self.contrasenia = nueva_contrasenia

            print("✅ Datos actualizados correctamente.")

        except Exception as err:
            print(f"Error al actualizar datos: {err}")

        finally:
            cursor.close()
            conn.close()

    # ----------- Métodos solo para administrador ----------- #
    @staticmethod
    def listar_usuarios(usuario_actual):
        print("\n--- Lista de usuarios registrados ---")
        db = Conexion()
        conn = db.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, correo, idrol FROM usuario")
            usuarios = cursor.fetchall()
            for u in usuarios:
                print(f"ID: {u[0]} | Nombre: {u[1]} | Correo: {u[2]} | Rol: {u[3]}")
        except Exception as err:
            print(f"Error al obtener usuarios.")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def cambiar_rol(usuario_actual, user_id, nuevo_rol):
        db = Conexion()
        conn = db.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            sql = "UPDATE usuario SET id_rol = %s WHERE id = %s"
            cursor.execute(sql, (nuevo_rol, user_id))
            conn.commit()
            print("✅ Rol actualizado correctamente.")
        except Exception as err:
            print(f"Error al actualizar rol: {err}")
        finally:
            cursor.close()
            conn.close()

        @staticmethod
        def eliminar_usuario(usuario_actual, user_id):
                db = Conexion()
                conn = db.conectar()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM usuario WHERE id = %s"
            cursor.execute(sql, (user_id,))
            conn.commit()
            print(f"✅ Usuario con ID {user_id} eliminado correctamente.")
        except Exception as err:
            print(f"Error al eliminar usuario: {err}")
        finally:
            cursor.close()
            conn.close()