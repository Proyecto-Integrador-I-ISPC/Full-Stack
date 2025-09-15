from servicios.conexion import Conexion
    
def registrarse(conexion):

    if not conexion.conectar():
        print("No se pudo conectar a la base de datos.")
        return
    else:
        print('\n--- REGISTRO DE NUEVO USUARIO ---')

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:

        nombre = input("Nombre: ").strip()
        correo = input("Correo electrónico: ").strip()
        contrasenia = input("Clave (mínimo 8 caracteres): ").strip()

        if not all([nombre, correo, contrasenia]):
            print("¡Error! No se permiten campos vacíos.")
            intentos += 1
            continue

        if len(contrasenia) < 8:
            print("¡Error! Clave demasiado corta.")
            intentos += 1
            continue

        db = Conexion()
        conn = conexion.conectar()

        if conn is None:
            print("No se pudo conectar a la base de datos")
            return

        try:
            cursor = conn.cursor()
            sql = "INSERT INTO usuario (nombre, correo, contrasenia, id_rol) VALUES (%s, %s, %s, 2)"
            valores = (nombre, correo, contrasenia)
            cursor.execute(sql, valores)
            conn.commit()
            print("\nEl registro fue exitoso.")
            return  

        except Exception as err:
            print(f"Error al registrar usuario: {err}")
            intentos += 1

        finally:
            cursor.close()
            conn.close()

    print("Has alcanzado el límite de intentos.")


if __name__=="__main__":
    registrarse()