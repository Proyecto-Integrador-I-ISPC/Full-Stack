from servicios.conexion import Conexion
from servicios.login import Login
import registro
from servicios.menu_administrador import menu_admin
from servicios.menu_usuario import menu_user

def iniciar_sesion(conexion):
    email = input("Correo: ").strip()
    contrasenia = input("Contraseña: ").strip()
    login = Login(conexion)
    usuario = login.autenticar(email, contrasenia)
    return usuario

def mostrar_menu_principal():
    print("\n--- Bienvenido a Aquamovil---")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    return input("Seleccione una opción: ").strip()

def main():
    conexion = Conexion()
    if not conexion.conectar():
        print("No se pudo establecer la conexión")
        return

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            usuario = iniciar_sesion(conexion)
            if usuario:
                if usuario.idrol == 1:  # Suponiendo 1 = Admin
                    menu_admin(usuario)
                else:
                    menu_user(usuario)
        elif opcion == "2":
            registro.registrarse(conexion)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()