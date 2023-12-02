from flask import Flask, render_template, request, redirect, flash, jsonify
from flask import make_response
import controllers.controlador_tipo_prenda as controlador_tipo_prenda
import controllers.controlador_color_prenda as controlador_color_prenda
import controllers.controlador_temporadas as controlador_temporadas
import controllers.controlador_material as controlador_material
import controllers.controlador_usuarios as controlador_usuarios
import controllers.controlador_talla_prenda as controlador_talla_prenda
import controllers.controlador_prenda as controlador_prenda
import controllers.controlador_disponibilidad as controlador_disponibilidad
import controllers.controlador_venta as controlador_venta
import clases.clase_color as clase_color
import clases.clase_disponibilidad as clase_disponibilidad
import clases.clase_material as clase_material
import clases.clase_prenda as clase_prenda
import clases.clase_talla_prenda as clase_talla_prenda
import clases.clase_temporada as clase_temporada
import clases.clase_tipoPrenda as clase_tipoPrenda
import clases.clase_usuario as clase_usuario
import clases.clase_venta as clase_venta
import hashlib
import random
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest
from flask_jwt import JWT, jwt_required, current_identity
from flask_paginate import Pagination


###### SEGURIDAD - INICIO ######################################################

def authenticate(username, password):
    usuario = controlador_usuarios.obtener_usuario(username)
    user = clase_usuario.Usuario(usuario[0], usuario[1], usuario[2])
    if user and (user.password == password):
        return user


def identity(payload):
    user_id = payload['identity']
    usuario = controlador_usuarios.obtener_usuario_por_id(user_id)
    user = clase_usuario.Usuario(usuario[0], usuario[1], usuario[2])
    return user


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

###### SEGURIDAD - FIN #########################################################

#! Lógica Token y Principal


def validar_token():
    token = request.cookies.get('token')
    username = request.cookies.get('username')
    usuario = controlador_usuarios.obtener_usuario(username)
    if usuario is not None:
        if token == usuario[3]:
            return True
        return False
    return False

def validar_admin():
    username = request.cookies.get('username')
    if username == 'admin':
        return True
    return False

@app.route("/vista_admin")
def vista_admin():
    if validar_token() and validar_admin():
        tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
        return render_template("vista_admin.html", tipo_prendas=tipo_prendas, esSesionIniciada=True)
    return redirect("/login")


@app.route("/")
def principal():
    return redirect("/index")


@app.route("/login")
def login():
    if validar_token():
        username = request.cookies.get('username')
        if username == 'admin':
            return redirect("vista_admin")
        else:
            return redirect("/mi_cuenta")
    return render_template("client/login.html")


#! Redireccion entre vistaUsuario

#! Redireccion entre vistaUsuario
@app.route("/mi_cuenta")
def mi_cuenta():
    valor_cookie = request.cookies.get('username')
    usuario = controlador_usuarios.obtener_usuario(valor_cookie)
    return render_template("/client/mi_cuenta.html", usuario=usuario)

@app.route("/misCompras")
def misCompras():
    valor_cookie = request.cookies.get('username')
    usuario = controlador_usuarios.obtener_usuario(valor_cookie)
        #! Contar el número total de registros
    registros = controlador_venta.obtener_total_registros()

    #! Obtener el número de página actual y la cantidad de resultados por página
    page_num = request.args.get('page', 1, type=int)
    per_page = 2

    #! Calcular el índice del primer registro y limitar la consulta a un rango de registros
    start_index = (page_num - 1) * per_page + 1

    ventas = controlador_venta.ventas_paginacion(per_page, start_index, usuario[0])

    #! Calcular el índice del último registro
    end_index = min(start_index + per_page, registros)
    # end_index = start_index + per_page - 1
    if end_index > registros:
        end_index = registros

    #! Crear objeto paginable
    pagination = Pagination(page=page_num, total=registros,
                            per_page=per_page, css_framework='bootstrap')
    return render_template("client/misCompras.html", usuario=usuario, ventas=ventas,pagination=pagination)


@app.route("/quienes_somos")
def quienes_somos():
    return render_template("client/quienes_somos.html")


@app.route("/contactanos")
def contactanos():
    return render_template("client/contactanos.html")


@app.route("/terminos_condiciones")
def terminos_condiciones():
    return render_template("client/terminos_condiciones.html")


@app.route("/preguntas_frecuentes")
def preguntas_frecuentes():
    return render_template("client/preguntas_frecuentes.html")


@app.route("/libro_reclamaciones")
def libro_reclamaciones():
    return render_template("client/libro_reclamaciones.html")


@app.route("/politicas_privacidad")
def politicas_privacidad():
    return render_template("client/politicas_privacidad.html")


@app.route("/catalogo-novedades")
def catalogoNovedades():
    #! Contar el número total de registros
    registros = controlador_prenda.obtener_total_registros()

    #! Obtener el número de página actual y la cantidad de resultados por página
    page_num = request.args.get('page', 1, type=int)
    per_page = 8

    #! Calcular el índice del primer registro y limitar la consulta a un rango de registros
    start_index = (page_num - 1) * per_page + 1

    prendas = controlador_prenda.prendas_paginacion_nov(per_page, start_index)

    #! Calcular el índice del último registro
    end_index = min(start_index + per_page, registros)
    # end_index = start_index + per_page - 1
    if end_index > registros:
        end_index = registros

    #! Crear objeto paginable
    pagination = Pagination(page=page_num, total=registros,
                            per_page=per_page, css_framework='bootstrap')

    return render_template("client/catalogo_novedades.html", prendas=prendas, pagination=pagination)


@app.route("/catalogo-prendas")
def catalogoPrendas():
    #! Contar el número total de registros
    registros = controlador_prenda.obtener_total_registros()

    #! Obtener el número de página actual y la cantidad de resultados por página
    page_num = request.args.get('page', 1, type=int)
    per_page = 8

    #! Calcular el índice del primer registro y limitar la consulta a un rango de registros
    start_index = (page_num - 1) * per_page + 1

    prendas = controlador_prenda.prendas_paginacion(per_page, start_index)

    #! Calcular el índice del último registro
    end_index = min(start_index + per_page, registros)
    # end_index = start_index + per_page - 1
    if end_index > registros:
        end_index = registros

    #! Crear objeto paginable
    pagination = Pagination(page=page_num, total=registros,
                            per_page=per_page, css_framework='bootstrap')

    return render_template("client/catalogo_prendas.html", prendas=prendas, pagination=pagination)

@app.route("/detalle-prenda/<int:id>")
def detallePrenda(id):
    prenda = controlador_prenda.obtener_prenda_id(id)
    tallas = controlador_disponibilidad.obtener_tallas_prenda(id)
    return render_template("client/detalle_prenda.html", prenda=prenda, tallas=tallas)

@app.route("/detalle-compra/<int:id>")
def detalleCompra(id):
    detalle_venta = controlador_venta.obtener_detalle_venta_id(id)
    return render_template("client/misCompras.html", detalle_venta=detalle_venta)

'''
@app.route("/datos-usuario")
def datosUsuario():
    valor_cookie = request.cookies.get('username')
    usuario = controlador_usuarios.obtener_usuario(valor_cookie)
    return render_template("/mi_cuenta", usuario=usuario)
    '''

@app.route('/obtener_ultimo_id_venta', methods=['GET'])
def obtener_ultimo_id_venta():
    ultimo_id_venta = controlador_venta.generar_venta()
    return jsonify({'ultimoIdVenta': ultimo_id_venta})

@app.route("/carrito-compras")
def carritoCompras():
    return render_template("client/carrito.html")

@app.route("/entrega-compras")
def entregaCompras():
    return render_template("client/entrega.html")

@app.route("/pago-compras")
def pagoCompras():
    return render_template("client/pago.html")

@app.route("/index")
def indexUsuario():
    return render_template("client/pagPrincipal.html")

#! Lógica Login/Logout Usuario

@app.route("/signup")
def signup():
    return render_template("admin/agregar_usuario.html")

@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    username = request.form["username"]
    password = request.form["password"]
    usuario = controlador_usuarios.obtener_usuario(username)
    h = hashlib.new('sha256')
    h.update(bytes(password, encoding="utf-8"))
    encpass = h.hexdigest()
    if usuario is not None and encpass == usuario[2]:
        numale = random.randint(1, 1024)
        a = hashlib.new('sha256')
        a.update(bytes(str(numale), encoding="utf-8"))
        encnumale = a.hexdigest()
        if username == 'admin':
            resp = make_response(redirect("/vista_admin"))
        else:
            resp = make_response(redirect("/login"))
        resp.set_cookie('token', encnumale)
        resp.set_cookie('username', username)
        controlador_usuarios.actualizar_token_usuario(username, encnumale)
        return resp
    else:
        flash('Ingrese los campos de acceso nuevamente.', 'danger')
        return redirect("/login")

@app.route("/procesar_cambio_con", methods=["POST"])
def procesar_cambio_con():
    contraseña_actual = request.form["contraseña_actual"]
    nueva_contraseña = request.form["nueva_contraseña"]

    usuario = controlador_usuarios.obtener_usuario(request.cookies.get("username"))

    if usuario is not None:
        contraseña_hash_actual = hashlib.sha256(contraseña_actual.encode("utf-8")).hexdigest()

        if contraseña_hash_actual == usuario[2]:
            if nueva_contraseña != contraseña_actual:
                contraseña_hash_nueva = hashlib.sha256(nueva_contraseña.encode("utf-8")).hexdigest()
                controlador_usuarios.actualizar_contrasena_usuario(request.cookies.get("username"), contraseña_hash_nueva)
                return redirect("/procesar_logout")
            else:
                flash('La nueva contraseña es idéntica a la contraseña anterior', 'warning')
                return redirect("/mi_cuenta")
        else:
            flash('La contraseña actual ingresada es incorrecta', 'danger')
            return redirect("/mi_cuenta")
    else:
        return redirect("/login")

@app.route("/procesar_logout")
def procesar_logout():
    valor_cookie = request.cookies.get('username')
    controlador_usuarios.quitar_token_usuario(valor_cookie)
    resp = make_response(redirect("/login"))
    resp.set_cookie('token', '', 0)
    resp.set_cookie('username', '', 0)
    return resp


#! Lógica Usuario

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        nombre_completo = request.form["nombre_completo"]
        apellido_paterno = request.form["apellido_paterno"]
        apellido_materno = request.form["apellido_materno"]
        telefono = request.form["telefono"]
        docid = request.form["docid"]
        # Realiza una consulta en la base de datos para verificar si el username y el email ya existen
        username_existente = controlador_usuarios.username_existente(username)
        email_existente = controlador_usuarios.email_existente(email)

        if username_existente:
            return jsonify({"error": "El nombre de usuario ya está en uso. Por favor, elija otro."})
        elif email_existente:
            return jsonify({"error": "La dirección de correo electrónico ya está en uso. Por favor, elija otra."})
        else:
            # Si el username y el email son válidos y disponibles, procede con el registro
            controlador_usuarios.insertar_usuario(username, email, password, nombre_completo, apellido_paterno, apellido_materno,telefono,docid)
            return redirect("/login")


#! Lógica Tipo de Prenda

@app.route("/tipo_prenda")
def tipo_prenda():
    if validar_token() and validar_admin():
        tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
        return render_template("admin/tipo_prenda.html", tipo_prendas=tipo_prendas)
    return redirect("/login")


@app.route("/agregar_tipo_prenda")
def agregar_tipo_prenda():
    if validar_token() and validar_admin():
        return render_template("admin/tipo_agregar.html")
    return redirect("/login")


@app.route("/guardar_tipo_prenda", methods=["POST"])
def guardar_tipo_prenda():
    nombre_tipo = request.form["nombre_tipo"]
    controlador_tipo_prenda.insertar_tipo_prenda(nombre_tipo)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/tipo_prenda")


@app.route("/editar_tipo_prenda/<int:id>")
def editar_tipo_prenda(id):
    tipo_prendas = controlador_tipo_prenda.obtener_tipo_por_id(id)
    return render_template("admin/tipo_editar.html", tipo_prendas=tipo_prendas)


@app.route("/actualizar_tipo_prenda", methods=["POST"])
def actualizar_tipo_prenda():
    id = request.form["id"]
    nombre_tipo = request.form["nombre_tipo"]
    controlador_tipo_prenda.actualizar_tipo_prenda(nombre_tipo, id)
    return redirect("/tipo_prenda")


@app.route("/eliminar_tipo_prenda", methods=["POST"])
def eliminar_tipo_prenda():
    controlador_tipo_prenda.eliminar_tipo_prenda(request.form["id"])
    return redirect("/tipo_prenda")


#! Lógica de Color de Prenda

@app.route("/color_prenda")
def color_prenda():
    if validar_token() and validar_admin():
        color_prendas = controlador_color_prenda.obtener_color_prenda()
        return render_template("admin/color_prenda.html", color_prendas=color_prendas)
    return redirect("/login")


@app.route("/agregar_color_prenda")
def agregar_color_prenda():
    if validar_token() and validar_admin():
        return render_template("admin/color_agregar.html")
    return redirect("/login")


@app.route("/guardar_color_prenda", methods=["POST"])
def guardar_color_prenda():
    nombre_color = request.form["nombre_color"]
    controlador_color_prenda.insertar_color_prenda(nombre_color)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/color_prenda")


@app.route("/editar_color_prenda/<int:id>")
def editar_color_prenda(id):
    color_prendas = controlador_color_prenda.obtener_color_por_id(id)
    return render_template("admin/color_editar.html", color_prendas=color_prendas)


@app.route("/actualizar_color_prenda", methods=["POST"])
def actualizar_color_prenda():
    id = request.form["id"]
    nombre_color = request.form["nombre_color"]
    controlador_color_prenda.actualizar_color_prenda(nombre_color, id)
    return redirect("/color_prenda")


@app.route("/eliminar_color_prenda", methods=["POST"])
def eliminar_color_prenda():
    controlador_color_prenda.eliminar_color_prenda(request.form["id"])
    return redirect("/color_prenda")


#! Lógica de Temporada de Prenda

@app.route("/temporada_prenda")
def temporada_prenda():
    if validar_token() and validar_admin():
        temporada_prendas = controlador_temporadas.obtener_temporada()
        return render_template("admin/temporada.html", temporada_prendas=temporada_prendas)
    return redirect("/login")


@app.route("/agregar_temporada")
def agregar_temporada():
    if validar_token() and validar_admin():
        return render_template("admin/temporada_agregar.html")
    return redirect("/login")


@app.route("/guardar_temporada", methods=["POST"])
def guardar_temporada():
    nomTemp = request.form["nombre_temporada"]
    controlador_temporadas.insertar_temporada(nomTemp)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/temporada_prenda")


@app.route("/editar_temporada/<int:id>")
def editar_temporada(id):
    temporada_prendas = controlador_temporadas.obtener_temporada_id(id)
    return render_template("admin/temporada_editar.html", temporada_prendas=temporada_prendas)


@app.route("/actualizar_temporada", methods=["POST"])
def actualizar_temporada():
    id = request.form["id"]
    nomTemporada = request.form["nombre_temporada"]
    controlador_temporadas.actualizar_temporada(nomTemporada, id)
    return redirect("/temporada_prenda")


@app.route("/eliminar_temporada", methods=["POST"])
def eliminar_temporada():
    controlador_temporadas.eliminar_temporada(request.form["id"])
    return redirect("/temporada_prenda")


#! Lógica de Material de Prenda

@app.route("/material_prenda")
def material_prenda():
    if validar_token() and validar_admin():
        material_prendas = controlador_material.obtener_material()
        return render_template("admin/material.html", material_prendas=material_prendas)
    return redirect("/login")


@app.route("/agregar_material")
def agregar_material():
    if validar_token() and validar_admin():
        return render_template("admin/material_agregar.html")
    return redirect("/login")


@app.route("/guardar_material", methods=["POST"])
def guardar_material():
    nomMat = request.form["nombre_material"]
    controlador_material.insertar_material(nomMat)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/material_prenda")


@app.route("/editar_material/<int:id>")
def editar_material(id):
    material_prendas = controlador_material.obtener_material_id(id)
    return render_template("admin/material_editar.html", material_prendas=material_prendas)


@app.route("/actualizar_material", methods=["POST"])
def actualizar_material():
    id = request.form["id"]
    nomMaterial = request.form["nombre_material"]
    controlador_material.actualizar_material(nomMaterial, id)
    return redirect("/material_prenda")


@app.route("/eliminar_material", methods=["POST"])
def eliminar_material():
    controlador_material.eliminar_material(request.form["id"])
    return redirect("/material_prenda")

#! Lógica de Talla de Prenda


@app.route("/talla_prenda")
def talla_prenda():
    if validar_token() and validar_admin():
        talla_prendas = controlador_talla_prenda.obtener_talla_prenda()
        return render_template("admin/talla.html", talla_prendas=talla_prendas)
    return redirect("/login")


@app.route("/agregar_talla")
def agregar_talla():
    if validar_token() and validar_admin():
        return render_template("admin/talla_agregar.html")
    return redirect("/login")


@app.route("/guardar_talla", methods=["POST"])
def guardar_talla():
    nomTalla = request.form["nombre_talla"]
    controlador_talla_prenda.insertar_talla_prenda(nomTalla)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/talla_prenda")


@app.route("/editar_talla/<int:id>")
def editar_talla(id):
    talla_prendas = controlador_talla_prenda.obtener_talla_por_id(id)
    return render_template("admin/talla_editar.html", talla_prendas=talla_prendas)


@app.route("/actualizar_talla", methods=["POST"])
def actualizar_talla():
    id = request.form["id"]
    nomTalla = request.form["nombre_talla"]
    controlador_talla_prenda.actualizar_talla_prenda(nomTalla, id)
    return redirect("/talla_prenda")


@app.route("/eliminar_talla", methods=["POST"])
def eliminar_talla():
    controlador_talla_prenda.eliminar_talla_prenda(request.form["id"])
    return redirect("/talla_prenda")

#! Lógica de Prenda


@app.route("/prenda")
def prenda():
    if validar_token() and validar_admin():
        prendas = controlador_prenda.obtener_prenda()
        return render_template("admin/prenda.html", prendas=prendas)
    return redirect("/login")


@app.route("/agregar_prenda")
def agregar_prenda():
    if validar_token() and validar_admin():
        tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
        color_prendas = controlador_color_prenda.obtener_color_prenda()
        temporada_prendas = controlador_temporadas.obtener_temporada()
        material_prendas = controlador_material.obtener_material()
        return render_template("admin/prenda_agregar.html", tipo_prendas=tipo_prendas, color_prendas=color_prendas, temporada_prendas=temporada_prendas, material_prendas=material_prendas)
    return redirect("/login")


@app.route("/guardar_prenda", methods=["POST"])
def guardar_prenda():
    codigo = request.form["cod_prenda"]
    nomPrenda = request.form["nom_prenda"]
    descripcion = request.form["desc_prenda"]
    tipo_prenda = int(request.form["tipo_prenda"])
    color_prenda = int(request.form["color_prenda"])
    temporada_prenda = int(request.form["temporada_prenda"])
    material_prenda = int(request.form["material_prenda"])
    file = request.files["imagen"]
    imagen = recibeFoto(file, codigo)
    controlador_prenda.insertar_prenda(
        codigo, nomPrenda, descripcion, tipo_prenda, color_prenda, material_prenda, temporada_prenda, imagen)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/prenda")

@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():
    try:
        total = float(request.form["monto_total"])
        descuento = int(request.form["descuento"])
        valor_cookie = request.cookies.get('username')
        id_usuario_c = controlador_usuarios.obtener_usuario(valor_cookie)

        if not id_usuario_c:
            raise BadRequest("Usuario no válido")

        comprobante = request.form["valor_comprobante_dinamico"]
        comp = controlador_venta.obtener_comprobante(comprobante)

        detalles_venta = []

        cantidad_productos = int(request.form["cantidad_productos"])
        id_venta = controlador_venta.generar_venta()
        for i in range(cantidad_productos):
            nomPrenda = request.form.get(f"producto_{i}_nomPrenda")
            id_prenda = controlador_prenda.obtener_nombre_prenda(nomPrenda)

            if id_prenda:
                id_prenda = id_prenda[0][0]  # Extraer el valor correcto de la tupla
            else:
                raise BadRequest(f"No se encontró id_prenda para {nomPrenda}")

            talla = request.form.get(f"producto_{i}_talla")
            id_talla = controlador_talla_prenda.obtener_talla_por_talla(talla)

            if id_talla:
                id_talla = id_talla[0]  # Extraer el valor correcto de la tupla
            else:
                raise BadRequest(f"No se encontró id_talla para {talla}")

            cantidad = int(request.form.get(f"producto_{i}_cantidad"))
            precio = float(request.form.get(f"producto_{i}_precio"))

            detalle = {'id_prenda': id_prenda, 'id_talla_prenda': id_talla, 'precio': precio, 'cantidad': cantidad}
            detalles_venta.append(detalle)

        # Imprimir detalles_venta para debug
        print("Detalles de venta:", detalles_venta)

        # Insertar en la base de datos
        controlador_venta.insertar_venta_y_detalles(id_venta,total, descuento, id_usuario_c[0], comp, detalles_venta)
        # O algún mensaje de éxito

        # Devolver una respuesta JSON indicando éxito
                # Activar la ventana modal en el lado del cliente antes de la redirección
        return redirect("/index")

    except Exception as e:
        # Manejar excepciones (puedes imprimir el error o realizar alguna acción específica)
        print(f"Error al procesar la venta: {e}")
        return str(e), 400  # Devolver mensaje de error al cliente.




@app.route("/editar_prenda/<int:id>")
def editar_prenda(id):
    prendas = controlador_prenda.obtener_prenda_id(id)
    tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
    color_prendas = controlador_color_prenda.obtener_color_prenda()
    temporada_prendas = controlador_temporadas.obtener_temporada()
    material_prendas = controlador_material.obtener_material()
    return render_template("admin/prenda_editar.html", prendas=prendas, tipo_prendas=tipo_prendas, color_prendas=color_prendas, temporada_prendas=temporada_prendas, material_prendas=material_prendas)


@app.route("/actualizar_prenda", methods=["POST"])
def actualizar_prenda():
    id = request.form["id"]
    codigo = request.form["codigo"]
    nomPrenda = request.form["nom_prenda"]
    descripcion = request.form["desc_prenda"]
    tipo_prenda = int(request.form["tipo_prenda"])
    color_prenda = int(request.form["color_prenda"])
    temporada_prenda = int(request.form["temporada_prenda"])
    material_prenda = int(request.form["material_prenda"])
    file = request.files["imagen"]
    imagen = recibeFoto(file, codigo)
    controlador_prenda.actualizar_prenda(
        nomPrenda, descripcion, tipo_prenda, color_prenda, material_prenda, temporada_prenda, imagen, id)
    return redirect("/prenda")


@app.route("/eliminar_prenda", methods=["POST"])
def eliminar_prenda():
    controlador_prenda.eliminar_prenda(request.form["id"])
    return redirect("/prenda")

#! Lógica de Disponibilidad Prenda


@app.route("/disponibilidad_prenda")
def disponibilidad_prenda():
    if validar_token() and validar_admin():
        disponibilidad_prendas = controlador_disponibilidad.obtener_disponibilidad_prenda()
        return render_template("admin/disponibilidad_prenda.html", disponibilidad_prendas=disponibilidad_prendas)
    return redirect("/login")


@app.route("/agregar_disponibilidad")
def agregar_disponibilidad():
    if validar_token() and validar_admin():
        prendas = controlador_prenda.obtener_prenda()
        talla_prendas = controlador_talla_prenda.obtener_talla_prenda()
        return render_template("admin/disponibilidad_agregar.html", prendas=prendas, talla_prendas=talla_prendas)
    return redirect("/login")


@app.route("/guardar_disponibilidad", methods=["POST"])
def guardar_disponibilidad():
    id_prenda = request.form["id_prenda"]
    id_talla = request.form["id_talla"]
    precio = request.form["precio"]
    stock = int(request.form["stock"])
    controlador_disponibilidad.insertar_disponibilidad_prenda(
        id_prenda, id_talla, precio, stock)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/disponibilidad_prenda")


@app.route("/editar_disponibilidad/<int:id_prenda>/<int:id_talla>")
def editar_disponibilidad(id_prenda, id_talla):
    disponibilidad_prendas = controlador_disponibilidad.obtener_disponibilidad_id(
        id_prenda, id_talla)
    prendas = controlador_prenda.obtener_prenda()
    talla_prendas = controlador_talla_prenda.obtener_talla_prenda()
    return render_template("admin/disponibilidad_editar.html", disponibilidad_prendas=disponibilidad_prendas, prendas=prendas, talla_prendas=talla_prendas)


@app.route("/actualizar_disponibilidad", methods=["POST"])
def actualizar_disponibilidad():
    id_prenda = request.form["id_prenda"]
    id_talla = request.form["id_talla"]
    precio = request.form["precio"]
    stock = int(request.form["stock"])
    controlador_disponibilidad.actualizar_disponibilidad_prenda(
        precio, stock, id_prenda, id_talla)
    return redirect("/disponibilidad_prenda")


@app.route("/eliminar_disponibilidad", methods=["POST"])
def eliminar_disponibilidad():
    id_prenda = request.form["prenda_id"]
    id_talla = request.form["talla_id"]
    controlador_disponibilidad.eliminar_disponibilidad_prenda(
        id_prenda, id_talla)
    return redirect("/disponibilidad_prenda")

#! Guardar imágenes


def recibeFoto(file, codProd):
    print(file)
    # La ruta donde se encuentra el archivo actual
    basepath = os.path.dirname(__file__)
    filename = secure_filename(file.filename)  # Nombre original del archivo

    # capturando extensión del archivo ejemplo: (.png, .jpg)
    extension = os.path.splitext(filename)[1]
    nuevoNombreFile = codProd + extension
    upload_path = os.path.join(basepath, 'static/products', nuevoNombreFile)
    file.save(upload_path)

    return nuevoNombreFile

# -------------------------------------------- APIS -------------------------------------------- #

# ? APIS Color de Prenda


@app.route("/api_obtener_color_prenda")
@jwt_required()
def api_obtener_color_prenda():
    response = dict()
    datos = []
    try:
        color_prendas = controlador_color_prenda.obtener_color_prenda()
        for color in color_prendas:
            objColor = clase_color.Color(color[0], color[1])
            datos.append(objColor.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Colores listados correctamente"
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_obtener_color_por_id", methods=["POST"])
@jwt_required()
def api_obtener_color_por_id():
    response = dict()
    datos = []
    try:
        id = request.json["id_color_prenda"]
        if not controlador_color_prenda.color_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            color_prendas = controlador_color_prenda.obtener_color_por_id(id)
            objColor = clase_color.Color(color_prendas[0], color_prendas[1])
            datos.append(objColor.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Color encontrado correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_color_prenda", methods=["POST"])
@jwt_required()
def api_guardar_color_prenda():
    response = dict()
    datos = []
    try:
        nombre_color = request.json["color"]
        if not controlador_color_prenda.color_existe(nombre_color):
            controlador_color_prenda.insertar_color_prenda(nombre_color)
            response["code"] = 0
            response["message"] = "Color guardado correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: El color ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_color_prenda", methods=["POST"])
@jwt_required()
def api_actualizar_color_prenda():
    response = dict()
    datos = []
    try:
        id = request.json["id_color_prenda"]
        nombre_color = request.json["color"]
        if not controlador_color_prenda.color_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if not controlador_color_prenda.color_existe(nombre_color):
                controlador_color_prenda.actualizar_color_prenda(
                    nombre_color, id)
                response["code"] = 0
                response["message"] = "Color actualizado correctamente."
            else:
                response["code"] = 4
                response["message"] = "Error: El color ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_color_prenda", methods=["POST"])
@jwt_required()
def api_eliminar_color_prenda():
    response = dict()
    datos = []
    try:
        id = request.json["id_color_prenda"]
        if controlador_color_prenda.color_existe_por_id(id):
            controlador_color_prenda.eliminar_color_prenda(id)
            response["code"] = 0
            response["message"] = "Color eliminado correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


# ? APIS Disponibilidad de Prenda


@app.route("/api_obtener_disponibilidad")
@jwt_required()
def api_obtener_disponibilidad():
    response = dict()
    datos = []
    try:
        disponibilidad_prendas = controlador_disponibilidad.obtener_disponibilidad_prenda()
        for disponibilidad in disponibilidad_prendas:
            objDisp = clase_disponibilidad.Disponibilidad(
                disponibilidad[0], disponibilidad[1], disponibilidad[2], disponibilidad[3], disponibilidad[4], disponibilidad[5])
            datos.append(objDisp.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Disponibilidad listada correctamente"
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_obtener_disponibilidad_por_ids", methods=["POST"])
@jwt_required()
def api_obtener_disponibilidad_por_ids():
    response = dict()
    datos = []
    try:
        id_prenda = request.json["id_prenda"]
        id_talla = request.json["id_talla_prenda"]
        if not controlador_disponibilidad.disponibilidad_existe(id_prenda, id_talla):
            response["code"] = 3
            response["message"] = "Error: Los ID's proporcionados no fueron encontrados."
        else:
            disponibilidad = controlador_disponibilidad.obtener_disponibilidad_id(
                id_prenda, id_talla)
            objDisp = clase_disponibilidad.Disponibilidad(
                disponibilidad[0], disponibilidad[1], disponibilidad[2], disponibilidad[3], disponibilidad[4], disponibilidad[5])
            datos.append(objDisp.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Disponibilidad encontrada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_disponibilidad", methods=["POST"])
@jwt_required()
def api_guardar_disponibilidad():
    response = dict()
    datos = []
    try:
        id_prenda = request.json["id_prenda"]
        id_talla = request.json["id_talla_prenda"]
        precio = request.json["precio"]
        stock = request.json["stock"]
        if controlador_disponibilidad.disponibilidad_existe(id_prenda, id_talla):
            response["code"] = 4
            response["message"] = "Error: La disponibilidad ya existe."
        else:
            if not controlador_disponibilidad.prenda_talla_existen(id_prenda, id_talla):
                response["code"] = 3
                response["message"] = "Error: Los ID's proporcionados no fueron encontrados."
            else:
                controlador_disponibilidad.insertar_disponibilidad_prenda(
                    id_prenda, id_talla, precio, stock)
                response["code"] = 0
                response["message"] = "Disponibilidad guardada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_disponibilidad", methods=["POST"])
@jwt_required()
def api_actualizar_disponibilidad():
    response = dict()
    datos = []
    try:
        id_prenda = request.json["id_prenda"]
        id_talla = request.json["id_talla_prenda"]
        precio = request.json["precio"]
        stock = request.json["stock"]
        if not controlador_disponibilidad.obtener_disponibilidad_id(id_prenda, id_talla):
            response["code"] = 3
            response["message"] = "Error: Los ID's proporcionados no fueron encontrados."
        else:
            controlador_disponibilidad.actualizar_disponibilidad_prenda(
                precio, stock, id_prenda, id_talla)
            response["code"] = 0
            response["message"] = "Disponibilidad actualizada exitosamente"
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_disponibilidad", methods=["POST"])
@jwt_required()
def api_eliminar_disponibilidad_():
    response = dict()
    datos = []
    try:
        id_prenda = request.json["id_prenda"]
        id_talla = request.json["id_talla_prenda"]
        if controlador_disponibilidad.disponibilidad_existe(id_prenda, id_talla):
            controlador_disponibilidad.eliminar_disponibilidad_prenda(
                id_prenda, id_talla)
            response["code"] = 0
            response["message"] = "Disponibilidad eliminada exitosamente."
        else:
            response["code"] = 3
            response["message"] = "Error: Los ID's proporcionados no fueron encontrados."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)

# ? APIS Material de Prenda


@app.route("/api_obtener_material_prenda")
@jwt_required()
def api_obtener_material_prenda():
    response = dict()
    datos = []
    try:
        material_prendas = controlador_material.obtener_material()
        for material in material_prendas:
            objMaterial = clase_material.Material(material[0], material[1])
            datos.append(objMaterial.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Materiales listados correctamente."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_material_prenda_por_id", methods=["POST"])
@jwt_required()
def api_material_prenda_por_id():
    response = dict()
    datos = []
    try:
        id = request.json["id_tipo_material"]
        if not controlador_material.material_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            material = controlador_material.obtener_material_id(id)
            objMaterial = clase_material.Material(material[0], material[1])
            datos.append(objMaterial.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Material encontrado correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_material", methods=["POST"])
@jwt_required()
def api_guardar_material():
    response = dict()
    datos = []
    try:
        nomMat = request.json["material"]
        if not controlador_material.material_existe(nomMat):
            controlador_material.insertar_material(nomMat)
            response["code"] = 0
            response["message"] = "Material guardado correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: El material ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_material", methods=["POST"])
@jwt_required()
def api_actualizar_material():
    response = dict()
    datos = []
    try:
        id = request.json["id_tipo_material"]
        nomMaterial = request.json["material"]
        if not controlador_material.material_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if not controlador_material.material_existe(nomMaterial):
                controlador_material.actualizar_material(nomMaterial, id)
                response["code"] = 0
                response["message"] = "Material actualizado correctamente."
            else:
                response["code"] = 4
                response["message"] = "Error: El material ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_material", methods=["POST"])
@jwt_required()
def api_eliminar_material():
    response = dict()
    datos = []
    try:
        id = request.json["id_tipo_material"]
        if controlador_material.material_existe_por_id(id):
            controlador_material.eliminar_material(id)
            response["code"] = 0
            response["message"] = "Material eliminado correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


# ? APIS Prenda

@app.route("/api_obtener_prenda")
@jwt_required()
def api_obtener_prenda():
    response = dict()
    datos = []
    try:
        prendas = controlador_prenda.obtener_prenda()
        for prenda in prendas:
            objPrenda = clase_prenda.Prenda(
                prenda[0], prenda[1], prenda[2], prenda[3], prenda[4], prenda[5], prenda[6], prenda[7], prenda[8])
            datos.append(objPrenda.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Prendas listadas correctamente."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_prenda_por_id", methods=["POST"])
@jwt_required()
def api_prenda_por_id():
    response = dict()
    datos = []
    try:
        id = request.json["id_prenda"]
        if not controlador_prenda.prenda_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            prenda = controlador_prenda.obtener_prenda_id_2(id)
            objPrenda = clase_prenda.Prenda(
                prenda[0], prenda[1], prenda[2], prenda[3], prenda[4], prenda[5], prenda[6], prenda[7], prenda[8])
            datos.append(objPrenda.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Prenda encontrada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_prenda", methods=["POST"])
@jwt_required()
def api_guardar_prenda():
    response = dict()
    datos = []
    try:
        codigo = request.json["codigo"]
        nomPrenda = request.json["nomPrenda"]
        descripcion = request.json["descripcion"]
        tipo_prenda = int(request.json["id_tipo_prenda"])
        color_prenda = int(request.json["id_color_prenda"])
        material_prenda = int(request.json["id_tipo_material"])
        temporada_prenda = int(request.json["id_prenda_temporada"])
        imagen = request.json["imagen"]
        if not controlador_prenda.prenda_existe(codigo):
            controlador_prenda.insertar_prenda(
                codigo, nomPrenda, descripcion, tipo_prenda, color_prenda, material_prenda, temporada_prenda, imagen)
            response["code"] = 0
            response["message"] = "Prenda guardada correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: La prenda ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_prenda", methods=["POST"])
@jwt_required()
def api_actualizar_prenda():
    response = dict()
    datos = []
    try:
        id = request.json["id_prenda"]
        codigo = request.json["codigo"]
        nomPrenda = request.json["nomPrenda"]
        descripcion = request.json["descripcion"]
        tipo_prenda = int(request.json["id_tipo_prenda"])
        color_prenda = int(request.json["id_color_prenda"])
        material_prenda = int(request.json["id_tipo_material"])
        temporada_prenda = int(request.json["id_prenda_temporada"])
        imagen = request.json["imagen"]
        if not controlador_prenda.prenda_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if controlador_prenda.prenda_existe(codigo):
                controlador_prenda.actualizar_prenda(
                    nomPrenda, descripcion, tipo_prenda, color_prenda, material_prenda, temporada_prenda, imagen, id)
                response["code"] = 0
                response["message"] = "Prenda actualizada correctamente"
            else:
                response["code"] = 4
                response["message"] = "Error: La prenda ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_prenda", methods=["POST"])
@jwt_required()
def api_eliminar_prenda():
    response = dict()
    datos = []
    try:
        id = request.json["id_prenda"]
        if controlador_prenda.prenda_existe_por_id(id):
            controlador_prenda.eliminar_prenda(id)
            response["code"] = 0
            response["message"] = "Prenda eliminada correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


# ? APIS Talla de Prenda


@app.route("/api_obtener_talla_prenda")
@jwt_required()
def api_obtener_talla_prenda():
    response = dict()
    datos = []
    try:
        talla_prendas = controlador_talla_prenda.obtener_talla_prenda()
        for talla in talla_prendas:
            objTalla = clase_talla_prenda.Talla(talla[0], talla[1])
            datos.append(objTalla.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Tallas listadas correctamente."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_obtener_talla_prenda_por_id", methods=["POST"])
@jwt_required()
def api_obtener_talla_prenda_por_id():
    response = dict()
    datos = []
    try:
        id_talla_prenda = request.json["id_talla_prenda"]
        if not controlador_talla_prenda.talla_existe_por_id(id_talla_prenda):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            talla = controlador_talla_prenda.obtener_talla_por_id(
                id_talla_prenda)
            objTalla = clase_talla_prenda.Talla(talla[0], talla[1])
            datos.append(objTalla.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Talla encontrada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_talla_prenda", methods=["POST"])
@jwt_required()
def api_guardar_talla_prenda():
    response = dict()
    datos = []
    try:
        tipo_talla = request.json["tipo_talla"]
        if not controlador_talla_prenda.talla_existe(tipo_talla):
            controlador_talla_prenda.insertar_talla_prenda(tipo_talla)
            response["code"] = 0
            response["message"] = "Talla guardada correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: La talla ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_talla_prenda", methods=["POST"])
@jwt_required()
def api_actualizar_talla_prenda():
    response = dict()
    datos = []
    try:
        id_talla_prenda = request.json["id_talla_prenda"]
        tipo_talla = request.json["tipo_talla"]
        if not controlador_talla_prenda.talla_existe_por_id(id_talla_prenda):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if not controlador_talla_prenda.talla_existe(tipo_talla):
                controlador_talla_prenda.actualizar_talla_prenda(
                    tipo_talla, id_talla_prenda)
                response["code"] = 0
                response["message"] = "Talla actualizada correctamente"
            else:
                response["code"] = 4
                response["message"] = "Error: La talla ya existe"
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_talla_prenda", methods=["POST"])
@jwt_required()
def api_eliminar_talla_prenda():
    response = dict()
    datos = []
    try:
        id_talla_prenda = request.json["id_talla_prenda"]
        if controlador_talla_prenda.talla_existe_por_id(id_talla_prenda):
            controlador_talla_prenda.eliminar_talla_prenda(id_talla_prenda)
            response["code"] = 0
            response["message"] = "Talla eliminada correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


# ? APIS Temporada

@app.route("/api_obtener_temporada_prenda")
@jwt_required()
def api_obtener_temporada_prenda():
    response = dict()
    datos = []
    try:
        temporada_prendas = controlador_temporadas.obtener_temporada()
        for temporada in temporada_prendas:
            objTemporada = clase_temporada.Temporada(
                temporada[0], temporada[1])
            datos.append(objTemporada.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Temporadas listadas correctamente."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_obtener_temporada_por_id", methods=["POST"])
@jwt_required()
def api_obtener_temporada_por_id():
    response = dict()
    datos = []
    try:
        id = request.json["id_prenda_temporada"]
        if not controlador_temporadas.temporada_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            temporadas_prendas = controlador_temporadas.obtener_temporada_id(
                id)
            objTemporada = clase_temporada.Temporada(
                temporadas_prendas[0], temporadas_prendas[1])
            datos.append(objTemporada.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Temporada encontrada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_temporada", methods=["POST"])
@jwt_required()
def api_guardar_temporada():
    response = dict()
    datos = []
    try:
        nomTemp = request.json["temporada"]
        if not controlador_temporadas.temporada_existe(nomTemp):
            controlador_temporadas.insertar_temporada(nomTemp)
            response["code"] = 0
            response["message"] = "Temporada guardada correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: La temporada ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_temporada", methods=["POST"])
@jwt_required()
def api_actualizar_temporada():
    response = dict()
    datos = []
    try:
        id = request.json["id_prenda_temporada"]
        nomTemporada = request.json["temporada"]
        if not controlador_temporadas.temporada_existe_por_id(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if not controlador_temporadas.temporada_existe(nomTemporada):
                controlador_temporadas.actualizar_temporada(nomTemporada, id)
                response["code"] = 0
                response["message"] = "Temporada actualizada correctamente."
            else:
                response["code"] = 4
                response["message"] = "Error: La temporada ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_temporada", methods=["POST"])
@jwt_required()
def api_eliminar_temporada():
    response = dict()
    datos = []
    try:
        temporada_id = request.json["id_prenda_temporada"]
        if controlador_temporadas.temporada_existe_por_id(temporada_id):
            controlador_temporadas.eliminar_temporada(temporada_id)
            response["code"] = 0
            response["message"] = "Temporada eliminada correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


# ? APIS Tipo de Prenda


@app.route("/api_obtener_tipo_prenda")
@jwt_required()
def api_obtener_tipo_prenda():
    response = dict()
    datos = []
    try:
        tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
        for tipo in tipo_prendas:
            objTemporada = clase_tipoPrenda.TipoPrenda(tipo[0], tipo[1])
            datos.append(objTemporada.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Tipos de prendas listadas correctamente."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_obtener_tipo_prenda_por_id", methods=["POST"])
@jwt_required()
def api_obtener_tipo_prenda_por_id():
    response = dict()
    datos = []
    try:
        id_tipo_prenda = request.json["id_tipo_prenda"]
        if not controlador_tipo_prenda.tipo_prenda_existe_por_id(id_tipo_prenda):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            tipo = controlador_tipo_prenda.obtener_tipo_prenda_por_id(
                id_tipo_prenda)
            objTemporada = clase_tipoPrenda.TipoPrenda(tipo[0], tipo[1])
            datos.append(objTemporada.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Tipo de prenda encontrada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_tipo_prenda", methods=["POST"])
@jwt_required()
def api_guardar_tipo_prenda():
    response = dict()
    datos = []
    try:
        tipo = request.json["tipo"]
        if not controlador_tipo_prenda.tipo_prenda_existe(tipo):
            controlador_tipo_prenda.insertar_tipo_prenda(tipo)
            response["code"] = 0
            response["message"] = "Tipo de prenda guardada correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: El tipo de prenda ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_tipo_prenda", methods=["POST"])
@jwt_required()
def api_actualizar_tipo_prenda():
    response = dict()
    datos = []
    try:
        id_tipo_prenda = request.json["id_tipo_prenda"]
        tipo = request.json["tipo"]
        if not controlador_tipo_prenda.tipo_prenda_existe_por_id(id_tipo_prenda):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if not controlador_tipo_prenda.tipo_prenda_existe(tipo):
                controlador_tipo_prenda.actualizar_tipo_prenda(
                    tipo, id_tipo_prenda)
                response["code"] = 0
                response["message"] = "Tipo de prenda actualizada correctamente"
            else:
                response["code"] = 4
                response["message"] = "Error: El tipo de prenda ya existe"
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_tipo_prenda", methods=["POST"])
@jwt_required()
def api_eliminar_tipo_prenda():
    response = dict()
    datos = []
    try:
        id_tipo_prenda = request.json["id_tipo_prenda"]
        if controlador_tipo_prenda.tipo_prenda_existe_por_id(id_tipo_prenda):
            controlador_tipo_prenda.eliminar_tipo_prenda(id_tipo_prenda)
            response["code"] = 0
            response["message"] = "Tipo de prenda eliminada correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


# ? APIS Venta

@app.route("/api_obtener_venta")
@jwt_required()
def api_obtener_venta():
    response = dict()
    datos = []
    try:
        ventas = controlador_venta.obtener_venta()
        for venta in ventas:
            objVenta = clase_venta.Venta(
                venta[0], venta[1], venta[2], venta[3], venta[4], venta[5], venta[6])
            datos.append(objVenta.obtenerObjetoSerializable())
        response["code"] = 0
        response["message"] = "Ventas listadas correctamente."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_venta_por_id", methods=["POST"])
@jwt_required()
def api_venta_por_id():
    response = dict()
    datos = []
    try:
        id = request.json["id_venta"]
        if not controlador_venta.venta_existe(id):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            venta = controlador_venta.obtener_venta_id(id)
            objVenta = clase_venta.Venta(
                venta[0], venta[1], venta[2], venta[3], venta[4], venta[5], venta[6])
            datos.append(objVenta.obtenerObjetoSerializable())
            response["code"] = 0
            response["message"] = "Venta encontrada correctamente."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_guardar_venta", methods=["POST"])
@jwt_required()
def api_guardar_venta():
    response = dict()
    datos = []
    try:
        id_venta = request.json["id_venta"]
        monto_total = request.json["monto_total"]
        descuento = request.json["descuento"]
        id_usuario = int(request.json["id_usuario"])
        id_tipo_comprobante = int(request.json["id_tipo_comprobante"])

        if not controlador_venta.venta_existe(id_venta):
            controlador_venta.insertar_venta(
                id_venta, monto_total, descuento, id_usuario, id_tipo_comprobante)
            response["code"] = 0
            response["message"] = "Venta guardada correctamente."
        else:
            response["code"] = 4
            response["message"] = "Error: La venta ya existe."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene la clave correcta."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_actualizar_venta", methods=["POST"])
@jwt_required()
def api_actualizar_venta():
    response = dict()
    datos = []
    try:
        id_venta = request.json["id_venta"]
        fecha = request.json["fecha"]
        estado = request.json["estado"]
        monto_total = request.json["monto_total"]
        descuento = request.json["descuento"]
        id_usuario = int(request.json["id_usuario"])
        id_tipo_comprobante = int(request.json["id_tipo_comprobante"])

        if not controlador_venta.venta_existe(id_venta):
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
        else:
            if controlador_venta.venta_existe(id_venta):
                controlador_venta.actualizar_venta(
                    id_venta, fecha, estado, monto_total, descuento, id_usuario, id_tipo_comprobante)
                response["code"] = 0
                response["message"] = "Venta actualizada correctamente"
            else:
                response["code"] = 4
                response["message"] = "Error: La venta ya existe"
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


@app.route("/api_eliminar_venta", methods=["POST"])
@jwt_required()
def api_eliminar_venta():
    response = dict()
    datos = []
    try:
        id = request.json["id_venta"]
        if controlador_venta.venta_existe(id):
            controlador_venta.eliminar_venta(id)
            response["code"] = 0
            response["message"] = "Venta eliminada correctamente."
        else:
            response["code"] = 3
            response["message"] = "Error: El ID proporcionado no fue encontrado."
    except KeyError:
        response["code"] = 2
        response["message"] = "Error: El JSON proporcionado no contiene las claves correctas."
    except Exception as e:
        response["code"] = 1
        response["message"] = f"Error al procesar consumo de API: {str(e)}"
    response["data"] = datos
    return jsonify(response)


#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
