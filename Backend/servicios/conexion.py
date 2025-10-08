import mysql.connector
from dotenv import load_dotenv
import os


class Conexion:

    load_dotenv()

    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

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