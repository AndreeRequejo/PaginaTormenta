from bd import obtener_conexion

def insertar_disponibilidad_prenda(id_prenda, id_talla, precio, stock):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (%s, %s, %s, %s)", (id_prenda, id_talla, precio, stock,))
    conexion.commit()
    conexion.close()

def obtener_disponibilidad_prenda():
    conexion = obtener_conexion()
    disponibilidad = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT P.nomPrenda, T.tipo_talla, precio, stock, DP.id_prenda, DP.id_talla_prenda FROM disponibilidad_prenda AS DP "
                                + "INNER JOIN prenda AS P ON DP.id_prenda = P.id_prenda "
                                + "INNER JOIN talla_prenda AS T ON DP.id_talla_prenda = T.id_talla_prenda")
        disponibilidad = cursor.fetchall()
    conexion.close()
    return disponibilidad

def eliminar_disponibilidad_prenda(id_prenda, id_talla_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM disponibilidad_prenda WHERE id_prenda = %s and id_talla_prenda = %s", (id_prenda,id_talla_prenda,))
    conexion.commit()
    conexion.close()

def obtener_disponibilidad_id(id_prenda, id_talla_prenda):
    conexion = obtener_conexion()
    prenda = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT P.nomPrenda, T.tipo_talla, DP.precio, DP.stock, DP.id_prenda, DP.id_talla_prenda FROM disponibilidad_prenda AS DP "
                        + "INNER JOIN prenda AS P ON DP.id_prenda = P.id_prenda "
                        + "INNER JOIN talla_prenda AS T ON DP.id_talla_prenda = T.id_talla_prenda "
                        + "WHERE DP.id_prenda = %s and DP.id_talla_prenda = %s", (id_prenda,id_talla_prenda,))
        prenda = cursor.fetchone()
    conexion.close()
    return prenda


def obtener_tallas_prenda(id_prenda):
    conexion = obtener_conexion()
    prenda = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT T.tipo_talla FROM disponibilidad_prenda AS DP "
                        + "INNER JOIN talla_prenda AS T ON DP.id_talla_prenda = T.id_talla_prenda "
                        + "WHERE DP.id_prenda = %s ", (id_prenda,))
        prenda = cursor.fetchall()
    conexion.close()
    return prenda

def actualizar_disponibilidad_prenda(precio, stock, id_prenda, id_talla):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE disponibilidad_prenda SET precio = %s, stock = %s WHERE id_prenda = %s and id_talla_prenda = %s", (precio, stock, id_prenda, id_talla,))
    conexion.commit()
    conexion.close()