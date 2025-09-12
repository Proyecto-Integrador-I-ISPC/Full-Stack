import mysql.connector

class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "12345678"
        self.database = "aquamovilbd"

    def conectar(self):
       
        try:
            conexion = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            return conexion
        except mysql.connector.Error as err:
            print(f"Error al conectar la base de datos: {err}")
            return None