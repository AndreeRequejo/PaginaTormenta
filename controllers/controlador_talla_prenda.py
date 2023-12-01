from bd import obtener_conexion


def insertar_talla_prenda(id_talla_prenda,tipo_talla):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO talla_prenda (id_talla_prenda,tipo_talla) VALUES (%s, %s)",
                        (id_talla_prenda,tipo_talla,))
    conexion.commit()
    conexion.close()


def obtener_talla_prenda():
    conexion = obtener_conexion()
    talla_prenda = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_talla_prenda,tipo_talla FROM talla_prenda")
        talla_prenda = cursor.fetchall()
    conexion.close()
    return talla_prenda


def eliminar_talla_prenda(id_talla_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE talla_prenda SET estado = false WHERE id_talla_prenda = %s", (id_talla_prenda,))
    conexion.commit()
    conexion.close()


def obtener_talla_por_id(id_talla_prenda):
    conexion = obtener_conexion()
    talla = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_talla_prenda, tipo_talla FROM talla_prenda WHERE id_talla_prenda = %s", (id_talla_prenda,))
        talla = cursor.fetchone()
    conexion.close()
    return talla

def obtener_talla_por_talla(talla_prenda):
    conexion = obtener_conexion()
    talla = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_talla_prenda FROM talla_prenda WHERE tipo_talla = %s", (talla_prenda,))
        talla = cursor.fetchone()
    conexion.close()
    return talla


def actualizar_talla_prenda(tipo_talla, id_talla_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE talla_prenda SET tipo_talla = %s WHERE id_talla_prenda= %s",
                        (tipo_talla, id_talla_prenda,))
    conexion.commit()
    conexion.close()

def talla_existe_por_id(talla_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM talla_prenda WHERE id_talla_prenda = %s", (talla_id,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def talla_existe(tipo_talla):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM talla_prenda WHERE tipo_talla = %s", (tipo_talla,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe