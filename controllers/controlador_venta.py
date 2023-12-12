from bd import obtener_conexion

def insertar_venta(id_venta,monto_total,descuento,id_usuario,id_tipo_comprobante):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta (id_venta,fecha,estado,monto_total,descuento,id_usuario,id_tipo_comprobante) VALUES (%s, CURRENT_DATE, true, %s, %s, %s, %s)",
                        (id_venta,monto_total,descuento,id_usuario,id_tipo_comprobante,))
    conexion.commit()
    conexion.close()

def insertar_detalle_venta(id_venta,id_prenda,id_talla_prenda,precio,cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_venta (id_venta,id_prenda,id_talla_prenda,precio,cantidad) VALUES (%s, %s, %s, %s, %s)",
                        (id_venta,id_prenda,id_talla_prenda,precio,cantidad,))
    conexion.commit()
    conexion.close()

def insertar_venta_y_detalles(venta, monto_total, descuento, id_usuario, id_tipo_comprobante, detalles_venta):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            # Verificar que venta tiene un valor
            if venta is None:
                raise ValueError("Error: el valor de venta es None.")

            # Insertar en la tabla venta
            print(f"Insertando en venta con id_venta: {venta}")
            cursor.execute("INSERT INTO venta (id_venta, fecha, estado, monto_total, descuento, id_usuario, id_tipo_comprobante) VALUES (%s,CURRENT_DATE, true, %s, %s, %s, %s)",
                           (venta, monto_total, descuento, id_usuario, id_tipo_comprobante,))

            # Insertar en la tabla detalle_venta y actualizar stock en disponibilidad_prenda
            for detalle in detalles_venta:
                # Verificar que detalle['id_prenda'] es un entero
                if not isinstance(detalle['id_prenda'], int):
                    raise ValueError("Error: detalle['id_prenda'] no es un entero.")

                # Verificar que detalle['id_talla_prenda'] es un entero
                if not isinstance(detalle['id_talla_prenda'], int):
                    raise ValueError("Error: detalle['id_talla_prenda'] no es un entero.")

                # Insertar en la tabla detalle_venta
                cursor.execute("INSERT INTO detalle_venta (id_venta, id_prenda, id_talla_prenda, precio, cantidad) VALUES (%s, %s, %s, %s, %s)",
                               (venta, detalle['id_prenda'], detalle['id_talla_prenda'], detalle['precio'], detalle['cantidad'],))

                # Actualizar stock en disponibilidad_prenda
                cursor.execute("UPDATE disponibilidad_prenda SET stock = stock - %s WHERE id_prenda = %s AND id_talla_prenda = %s",
                               (detalle['cantidad'], detalle['id_prenda'], detalle['id_talla_prenda'],))

        conexion.commit()
        print("Venta y detalles insertados correctamente.")
    except Exception as e:
        # Manejar excepciones (puedes imprimir el error o realizar alguna acción específica)
        print(f"Error al insertar en la base de datos: {e}")
        conexion.rollback()
    finally:
        conexion.close()


def venta_existe(id_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM venta WHERE id_venta = %s", (id_venta,))
        resultado = cursor.fetchone()
        existe = resultado[0] > 0
    conexion.close()
    return existe

def obtener_venta():
    conexion = obtener_conexion()
    venta = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM venta")
        venta = cursor.fetchall()
    conexion.close()
    return venta

def obtener_total_registros():
    conexion = obtener_conexion()
    contador = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS total FROM detalle_venta AS v ")
        contador = cursor.fetchone()[0]
    conexion.close()
    return contador

def obtener_venta_id(id_venta):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM venta " + "WHERE id_venta = %s", (id_venta,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def obtener_detalle_venta_id(id_venta):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT p.nomPrenda,tp.tipo_talla,v.precio,v.cantidad FROM detalle_venta v inner join disponibilidad_prenda dp on v.id_talla_prenda= dp.id_talla_prenda and v.id_prenda=dp.id_prenda inner join prenda p on p.id_prenda=dp.id_prenda inner join talla_prenda tp on tp.id_talla_prenda=dp.id_talla_prenda WHERE v.id_venta = %s", (id_venta,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def ventas_paginacion(cant_elementos, inicio_index, usuario):
    conexion = obtener_conexion()
    prendas = []
    with conexion.cursor() as cursor:
        cursor.execute("select v.id_venta,p.nomPrenda,tp.tipo_talla,v.precio,v.cantidad,p.imagen,ven.fecha FROM detalle_venta v inner join disponibilidad_prenda dp on v.id_talla_prenda= dp.id_talla_prenda and v.id_prenda=dp.id_prenda inner join prenda p on p.id_prenda=dp.id_prenda inner join talla_prenda tp on tp.id_talla_prenda=dp.id_talla_prenda inner join venta ven on ven.id_venta=v.id_venta inner join usuarios u on u.id=ven.id_usuario "
                        + "WHERE v.id_venta >= 1 and u.id = %s "
                        + "ORDER BY v.id_venta DESC LIMIT %s OFFSET %s", (usuario,cant_elementos,inicio_index - 1,))
        prendas = cursor.fetchall()
    conexion.close()
    return prendas

def actualizar_venta(id_venta,fecha,estado,monto_total,descuento,id_usuario,id_tipo_comprobante):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE venta SET fecha = %s, estado = %s, monto_total = %s, descuento = %s, id_usuario = %s, id_tipo_comprobante = %s WHERE id_venta = %s", (fecha, estado, monto_total, descuento, id_usuario, id_tipo_comprobante, id_venta,))
    conexion.commit()
    conexion.close()

def eliminar_venta(id_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE venta SET estado = false WHERE id_venta = %s", (id_venta,))
    conexion.commit()
    conexion.close()

def obtener_comprobante(tipo_comprobante):
    conexion = obtener_conexion()
    comprobante = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_tipo_comprobante_venta FROM tipo_comprobante_venta WHERE tipo_comprobante = %s", (tipo_comprobante,))
        comprobante = cursor.fetchone()
    conexion.close()
    return comprobante

def generar_venta():
    conexion = obtener_conexion()
    venta = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COALESCE(MAX(id_venta), 0) + 1 AS codigo FROM venta")
            result = cursor.fetchone()
            if result:
                venta = result[0]
                print(f"Venta generada: {venta}")
            else:
                raise ValueError("Error: no se pudo obtener el valor de venta.")
    except Exception as e:
        print(f"Error al generar venta: {e}")
    finally:
        conexion.close()
    return venta

def clavesForaneas_existen(id_usuario, id_tipo_comprobante):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT 1 FROM usuarios WHERE id = %s", (id_usuario,))
        usuario_existe = cursor.fetchone() is not None

        cursor.execute("SELECT 1 FROM tipo_comprobante_venta WHERE id_tipo_comprobante_venta = %s", (id_tipo_comprobante,))
        tipoComprobante_existe = cursor.fetchone() is not None

    conexion.close()
    return usuario_existe and tipoComprobante_existe