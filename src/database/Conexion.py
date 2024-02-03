import mysql.connector


class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',password='',
                                               host='127.0.0.1',
                                               database='tesla',
                                               port='3307')
            print("Conexion Correcta")
            
            return conexion
            
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de Datos{}".format(error))
            return None
            


    ConexionBaseDeDatos()