from bd import obtener_conexion

def insertar_tipo_prenda(tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tipo_prenda (tipo) VALUES (%s)", (tipo,))
    conexion.commit()
    conexion.close()

def obtener_tipo_prenda():
    conexion = obtener_conexion()
    tipo_prenda = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo_prenda,tipo FROM tipo_prenda")
        tipo_prenda = cursor.fetchall()
    conexion.close()
    return tipo_prenda

def eliminar_tipo_prenda(id_tipo_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM tipo_prenda WHERE id_tipo_prenda = %s", (id_tipo_prenda,))
    conexion.commit()
    conexion.close()

def obtener_tipo_por_id(id_tipo_prenda):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_tipo_prenda, tipo FROM tipo_prenda WHERE id_tipo_prenda = %s", (id_tipo_prenda,))
        producto = cursor.fetchone()
    conexion.close()
    return producto

def actualizar_tipo_prenda(tipo, id_tipo_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_prenda SET tipo = %s WHERE id_tipo_prenda= %s",(tipo, id_tipo_prenda,))
    conexion.commit()
    conexion.close()
