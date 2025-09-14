from clases.usuario import Usuario

def menu_admin(usuario):
    while True:
        print(f"\n--- Menú Administrador ({usuario.nombre}) ---")
        print("1. Ver mis datos personales")
        print("2. Editar mis datos personales")
        print("3. Visualizar usuarios registrados")
        print("4. Cambiar rol de un usuario")
        print("5. Eliminar un usuario")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            usuario.ver_datos()

        elif opcion == "2":
            usuario.editar_datos()

        elif opcion == "3":
            # Lista todos los usuarios solo si es admin
            Usuario.listar_usuarios(usuario)


        elif opcion == "4":
            try:
                user_id = int(input("Ingrese ID del usuario: ").strip())
                nuevo_rol = int(input("Ingrese nuevo rol (1=Admin, 2=Cliente, 3=Empleado): ").strip())
                Usuario.cambiar_rol(usuario, user_id, nuevo_rol)  # usuario = admin actual
            except ValueError:
                print("❌ Debe ingresar un número válido para ID y rol.")


        elif opcion == "5":
            try:
                user_id = int(input("Ingrese ID del usuario a eliminar: ").strip())
                confirm = input(f"¿Está seguro que desea eliminar al usuario {user_id}? (s/n): ").strip().lower()
                if confirm == "s":
                    Usuario.eliminar_usuario(usuario, user_id)
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("❌ Debe ingresar un número válido para el ID.")

        elif opcion == "6":
            print("Sesión cerrada.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
