import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='crudpython'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
            
            
            
    def llamarUser(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM `user` ORDER BY `fecha_user` DESC") 
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion {0}".format(ex))
    
    
    def registrarUser(self, user):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO `user` (`idUser`, `name_user`, `fecha_user`, `rango_user`) VALUES ('{0}', '{1}', '{2}', '{3}');"
                cursor.execute(sql.format(user[0], user[1], user[2], user[3]))
                self.conexion.commit()
                print("¡Usuario registrado con exito! \n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
        
    
    