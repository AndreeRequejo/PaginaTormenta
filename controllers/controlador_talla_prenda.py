from bd import obtener_conexion


def insertar_talla_prenda(talla):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO talla_prenda (tipo_talla) VALUES (%s)",
                        (talla,))
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
            "DELETE FROM talla_prenda WHERE id_talla_prenda = %s", (id_talla_prenda,))
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


def actualizar_talla_prenda(talla, id_talla_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE talla_prenda SET tipo_talla = %s WHERE id_talla_prenda= %s",
                        (talla, id_talla_prenda,))
    conexion.commit()
    conexion.close()
