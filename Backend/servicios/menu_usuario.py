from servicios.conexion import Conexion
from clases.usuario import Usuario

def menu_user(usuario):
    while True:
        print(f"\n--- Menú Usuario ({usuario.nombre}) ---")
        print("1. Ver mis datos")
        print("2. Editar mis datos")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            usuario.ver_datos()

        elif opcion == "2":
            usuario.editar_datos()

        elif opcion == "3":
            print("Sesión cerrada.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")