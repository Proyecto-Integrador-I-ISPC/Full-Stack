
import mysql.connector
class Servicio: 
    def __init__(self,conexion=None):
      self.conexion=conexion 

       
    def listar_servicios(self):
        cursor =  self.conexion.cursor()
        cursor.execute("SELECT * FROM servicio")
        lista_servicios=cursor.fetchall()
        cursor.close()

        for servicio in lista_servicios:
            print(f"id:{servicio[0]}, nombre del servicio {servicio[1]}, descripción: {servicio[2]}, precio: {servicio[3]}")


