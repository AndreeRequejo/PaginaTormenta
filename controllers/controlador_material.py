from bd import obtener_conexion


def material_existe(material):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT COUNT(*) FROM tipo_material WHERE material = %s", (material,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe


def material_existe_por_id(material_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT COUNT(*) FROM tipo_material WHERE id_tipo_material = %s", (material_id,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe


def insertar_material(material):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO tipo_material (material) VALUES (%s)", (material,))
    conexion.commit()
    conexion.close()


def obtener_material():
    conexion = obtener_conexion()
    material = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_tipo_material,material FROM tipo_material")
        material = cursor.fetchall()
    conexion.close()
    return material


def eliminar_material(id_mat):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM tipo_material WHERE id_tipo_material = %s", (id_mat,))
    conexion.commit()
    conexion.close()


def obtener_material_id(id_mat):
    conexion = obtener_conexion()
    material = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_tipo_material, material FROM tipo_material WHERE id_tipo_material = %s", (id_mat,))
        material = cursor.fetchone()
    conexion.close()
    return material


def actualizar_material(material, id_mat):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE tipo_material SET material = %s WHERE id_tipo_material= %s", (material, id_mat,))
    conexion.commit()
    conexion.close()
