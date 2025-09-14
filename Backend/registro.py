from servicios.conexion import Conexion

def registrarse():
    
    print('\n--- REGISTRO DE NUEVO CLIENTE ---')

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:

        nombre = input("Nombre: ").strip()
        correo = input("Correo electrónico: ").strip()
        contrasenia = input("Clave (mínimo 8 caracteres): ").strip()
        id_rol = input("Ingrese su id rol: ").strip()

        if not all([nombre, correo, contrasenia,id_rol]):
            print("¡Error! No se permiten campos vacíos.")
            intentos += 1
            continue

        if len(contrasenia) < 8:
            print("¡Error! Clave demasiado corta.")
            intentos += 1
            continue

        # Insertar cliente
        db = Conexion()
        conn = db.conectar()
        if conn is None:
            print("No se pudo conectar a la base de datos")
            return

        try:
            cursor = conn.cursor()
            sql = "INSERT INTO usuario (nombre, correo, contrasenia, id_rol) VALUES (%s, %s, %s, %s)"
            valores = (nombre, correo, contrasenia, id_rol)
            cursor.execute(sql, valores)
            conn.commit()
            print("El registro fue exitoso.")
            return  

        except Exception as err:
            print("Error al registrar cliente: {err}")
            intentos += 1

        finally:
            cursor.close()
            conn.close()

    print("Has alcanzado el límite de intentos.")


if __name__=="__main__":
    registrarse()
