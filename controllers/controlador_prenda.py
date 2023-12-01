from bd import obtener_conexion

def insertar_prenda(codigo, nombre, descripcion, id_tipo, id_color, id_material, id_temporada, imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (codigo, nombre, descripcion, id_tipo, id_color, id_material, id_temporada, imagen,))
    conexion.commit()
    conexion.close()

def prenda_existe(codigo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM prenda WHERE codigo = %s", (codigo,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def prenda_existe_por_id(prenda_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM prenda WHERE id_prenda = %s", (prenda_id,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def obtener_prenda():
    conexion = obtener_conexion()
    prenda = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda, codigo, nomPrenda, descripcion, tp.tipo, c.color, m.material, t.temporada, imagen FROM prenda AS p "
                                + "INNER JOIN tipo_prenda AS tp ON p.id_tipo_prenda = tp.id_tipo_prenda "
                                + "INNER JOIN color_prenda AS c ON p.id_color_prenda = c.id_color_prenda "
                                + "INNER JOIN tipo_material AS m ON p.id_tipo_material = m.id_tipo_material "
                                + "INNER JOIN prenda_temporada AS t ON p.id_prenda_temporada = t.id_prenda_temporada")
        prenda = cursor.fetchall()
    conexion.close()
    return prenda

def obtener_nombre_prenda(nom_prenda):
    conexion = obtener_conexion()
    prenda = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda FROM prenda WHERE nomPrenda = %s", (nom_prenda,))
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
        cursor.execute("SELECT id_prenda, nomPrenda, descripcion, imagen, tp.tipo, m.material, t.temporada, (SELECT precio FROM disponibilidad_prenda WHERE id_prenda = p.id_prenda LIMIT 1) as precio, codigo FROM prenda AS p "
                        + "INNER JOIN tipo_prenda AS tp ON p.id_tipo_prenda = tp.id_tipo_prenda "
                        + "INNER JOIN tipo_material AS m ON p.id_tipo_material = m.id_tipo_material "
                        + "INNER JOIN prenda_temporada AS t ON p.id_prenda_temporada = t.id_prenda_temporada "
                        + " WHERE id_prenda = %s", (id_prenda,))
        prenda = cursor.fetchone()
    conexion.close()
    return prenda

def actualizar_prenda(nombre, descripcion, id_tipo, id_color, id_material, id_temporada, imagen,id_prenda ):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE prenda SET nomPrenda = %s, descripcion = %s, id_tipo_prenda = %s, id_color_prenda = %s, id_tipo_material = %s, id_prenda_temporada = %s, imagen = %s WHERE id_prenda = %s", (nombre, descripcion, id_tipo, id_color, id_material, id_temporada, imagen, id_prenda,))
    conexion.commit()
    conexion.close() 

def obtener_total_registros():
    conexion = obtener_conexion()
    contador = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM prenda AS p")
        contador = cursor.fetchone()[0]
    conexion.close()
    return contador

def prendas_paginacion(cant_elementos, inicio_index):
    conexion = obtener_conexion()
    prendas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda, codigo, nomPrenda, imagen, (SELECT precio FROM disponibilidad_prenda WHERE id_prenda = P.id_prenda LIMIT 1) as precio FROM prenda AS P "
                       "WHERE id_prenda >= 1 and codigo LIKE %s "
                       "ORDER BY id_prenda DESC LIMIT %s OFFSET %s", ('P%',cant_elementos, inicio_index - 1,))
        prendas = cursor.fetchall()
    conexion.close()
    return prendas

def prendas_paginacion_nov(cant_elementos, inicio_index):
    conexion = obtener_conexion()
    prendas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda, codigo, nomPrenda, imagen, (SELECT precio FROM disponibilidad_prenda WHERE id_prenda = P.id_prenda LIMIT 1) as precio FROM prenda AS P "
                       "WHERE id_prenda >= 1 and codigo LIKE %s "
                       "ORDER BY id_prenda DESC LIMIT %s OFFSET %s", ('M%',cant_elementos, inicio_index - 1,))
        prendas = cursor.fetchall()
    conexion.close()
    return prendas
