from bd import obtener_conexion

def insertar_prenda(codigo, nombre, descripcion, id_tipo, id_color, id_material, id_temporada):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada) VALUES (%s, %s, %s, %s, %s, %s, %s)", (codigo, nombre, descripcion, id_tipo, id_color, id_material, id_temporada,))
    conexion.commit()
    conexion.close()

def obtener_prenda():
    conexion = obtener_conexion()
    prenda = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda, codigo, nomPrenda, descripcion, tp.tipo, c.color, m.material, t.temporada FROM prenda AS p "
                                + "INNER JOIN tipo_prenda AS tp ON p.id_tipo_prenda = tp.id_tipo_prenda "
                                + "INNER JOIN color_prenda AS c ON p.id_color_prenda = c.id_color_prenda "
                                + "INNER JOIN tipo_material AS m ON p.id_tipo_material = m.id_tipo_material "
                                + "INNER JOIN prenda_temporada AS t ON p.id_prenda_temporada = t.id_prenda_temporada")
        prenda = cursor.fetchall()
    conexion.close()
    return prenda

def eliminar_prenda(id_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM prenda WHERE id_prenda = %s", (id_prenda,))
    conexion.commit()
    conexion.close()

def obtener_prenda_id(id_prenda):
    conexion = obtener_conexion()
    prenda = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda, codigo, nomPrenda, descripcion, tp.tipo, c.color, m.material, t.temporada FROM prenda AS p "
                        + "INNER JOIN tipo_prenda AS tp ON p.id_tipo_prenda = tp.id_tipo_prenda "
                        + "INNER JOIN color_prenda AS c ON p.id_color_prenda = c.id_color_prenda "
                        + "INNER JOIN tipo_material AS m ON p.id_tipo_material = m.id_tipo_material "
                        + "INNER JOIN prenda_temporada AS t ON p.id_prenda_temporada = t.id_prenda_temporada "
                        + " WHERE id_prenda = %s", (id_prenda,))
        prenda = cursor.fetchone()
    conexion.close()
    return prenda

def actualizar_prenda(codigo, nombre, descripcion, id_tipo, id_color, id_material, id_temporada, id_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE prenda SET codigo = %s, nomPrenda = %s, descripcion = %s, id_tipo_prenda = %s, id_color_prenda = %s, id_tipo_material = %s, id_prenda_temporada = %s WHERE id_prenda = %s", (codigo, nombre, descripcion, id_tipo, id_color, id_material, id_temporada, id_prenda,))
    conexion.commit()
    conexion.close() 