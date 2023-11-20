from bd import obtener_conexion

def insertar_tipo_prenda(id_tipo_prenda,tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tipo_prenda (id_tipo_prenda,tipo) VALUES (%s,%s)", (id_tipo_prenda,tipo,))
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

def obtener_tipo_prenda_por_id(id_tipo_prenda):
    conexion = obtener_conexion()
    tipo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_tipo_prenda, tipo FROM tipo_prenda WHERE id_tipo_prenda = %s", (id_tipo_prenda,))
        tipo = cursor.fetchone()
    conexion.close()
    return tipo

def eliminar_tipo_prenda(id_tipo_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE tipo_prenda SET estado = false WHERE id_tipo_prenda = %s", (id_tipo_prenda,))
    conexion.commit()
    conexion.close()


def actualizar_tipo_prenda(tipo, id_tipo_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tipo_prenda SET tipo = %s WHERE id_tipo_prenda= %s",(tipo, id_tipo_prenda,))
    conexion.commit()
    conexion.close()

def tipo_prenda_existe_por_id(id_tipo_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM tipo_prenda WHERE id_tipo_prenda = %s", (id_tipo_prenda,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def tipo_prenda_existe(tipo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM tipo_prenda WHERE tipo = %s", (tipo,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe