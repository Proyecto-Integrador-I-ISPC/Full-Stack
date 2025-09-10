from servicios.conexion import Conexion

def main():
    conexion=Conexion()
    con=conexion.conectar()

    if con:
        print("Conexion a la base de datos establecida exitosamente")
        
    else:
        print("No se pudo establecer la conexión")

if __name__=="__main__":
    main()