import pymysql

def obtener_conexion():
    return pymysql.connect(host='GrupoWeb1.mysql.pythonanywhere-services.com',
                                user='GrupoWeb1',
                                password='Vale 2502',
                                db='GrupoWeb1$ProyectoFinal')