from bd import obtener_conexion

def color_existe(color):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM color_prenda WHERE color = %s", (color,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def color_existe_por_id(color_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM color_prenda WHERE id_color_prenda = %s", (color_id,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def insertar_color_prenda(color):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO color_prenda (color) VALUES (%s)",
                        (color,))
    conexion.commit()
    conexion.close()


def obtener_color_prenda():
    conexion = obtener_conexion()
    color_prenda = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_color_prenda,color FROM color_prenda")
        color_prenda = cursor.fetchall()
    conexion.close()
    return color_prenda


def eliminar_color_prenda(id_color_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE color_prenda SET estado = false WHERE id_color_prenda = %s", (id_color_prenda,))
    conexion.commit()
    conexion.close()


def obtener_color_por_id(id_color_prenda):
    conexion = obtener_conexion()
    producto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_color_prenda, color FROM color_prenda WHERE id_color_prenda = %s", (id_color_prenda,))
        producto = cursor.fetchone()
    conexion.close()
    return producto


def actualizar_color_prenda(color, id_color_prenda):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE color_prenda SET color = %s WHERE id_color_prenda= %s",
                        (color, id_color_prenda,))
    conexion.commit()
    conexion.close()
