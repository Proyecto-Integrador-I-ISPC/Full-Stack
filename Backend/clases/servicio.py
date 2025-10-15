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
      print(f"\nID:{servicio[0]}. \nNombre del servicio: {servicio[1]}. \nDescripción: {servicio[2]}. \nPrecio: {servicio[3]}\n")