from servicios.conexion import Conexion
    
def registrarse(conexion):
    # usar conexion en vez de crear una nueva conexión dentro
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

        print("\nSeleccione su rol:")
        print("1. Cliente")
        print("2. Empleado")
        print("⚠️  Nota: Para ser Administrador, debe contactar a un administrador existente.")
        
        opcion = input("Opción: ").strip()

        if opcion == "1":
            id_rol = 2  # Cliente
        elif opcion == "2":
            id_rol = 3  # Empleado
        else:
            print("¡Error! Opción inválida. Solo puede elegir 1 o 2.")
            intentos += 1
            continue

        # Validar campos
        if not all([nombre, correo, contrasenia]):
            print("¡Error! No se permiten campos vacíos.")
            intentos += 1
            continue

        if len(contrasenia) < 8:
            print("¡Error! Clave demasiado corta.")
            intentos += 1
            continue

        # Insertar cliente/empleado
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
            print(f"Error al registrar usuario: {err}")
            intentos += 1

        finally:
            cursor.close()
            conn.close()

    print("Has alcanzado el límite de intentos.")


if __name__=="__main__":
    registrarse()
