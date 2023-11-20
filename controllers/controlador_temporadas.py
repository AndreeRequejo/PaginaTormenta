from bd import obtener_conexion

def temporada_existe(temporada):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM prenda_temporada WHERE temporada = %s", (temporada,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def temporada_existe_por_id(temp_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM prenda_temporada WHERE id_prenda_temporada = %s", (temp_id,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def insertar_temporada(temporada):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO prenda_temporada (temporada) VALUES (%s)", (temporada,))
    conexion.commit()
    conexion.close()

def obtener_temporada():
    conexion = obtener_conexion()
    temporada = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_prenda_temporada,temporada FROM prenda_temporada")
        temporada = cursor.fetchall()
    conexion.close()
    return temporada

def eliminar_temporada(id_temp):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM prenda_temporada WHERE id_prenda_temporada = %s", (id_temp,))
    conexion.commit()
    conexion.close()

def obtener_temporada_id(id_temp):
    conexion = obtener_conexion()
    temporada = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_prenda_temporada, temporada FROM prenda_temporada WHERE id_prenda_temporada = %s", (id_temp,))
        temporada = cursor.fetchone()
    conexion.close()
    return temporada


def actualizar_temporada(temporada, id_temp):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE prenda_temporada SET temporada = %s WHERE id_prenda_temporada= %s", (temporada, id_temp,))
    conexion.commit()
    conexion.close()
