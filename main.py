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
import hashlib
import random
import os
from werkzeug.utils import secure_filename
from flask_paginate import Pagination

app = Flask(__name__)

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


@app.route("/vista_admin")
def vista_admin():
    if validar_token():
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
            return redirect("/index")
    return render_template("client/login.html")


#! Redireccion entre vistaUsuario

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


@app.route("/catalogo-ropa")
def catalogoRopa():
    return render_template("client/catalogo_ropa.html")


@app.route("/catalogo-novedades")
def catalogoNovedades():
    return render_template("client/catalogo_novedades.html")


@app.route("/catalogo-femenino")
def catalogoFemenino():
    #! Contar el número total de registros
    registros = controlador_prenda.obtener_total_registros()

    #! Obtener el número de página actual y la cantidad de resultados por página
    page_num = request.args.get('page', 1, type=int)
    per_page = 6

    #! Calcular el índice del primer registro y limitar la consulta a un rango de registros
    start_index = (page_num - 1) * per_page + 1

    prendas = controlador_prenda.prendas_paginacion(per_page, start_index)

    #! Calcular el índice del último registro
    end_index = min(start_index + per_page, registros)
    # end_index = start_index + per_page - 1
    if end_index > registros:
        end_index = registros

    #! Crear objeto paginable
    pagination = Pagination(page = page_num, total=registros, per_page = per_page, css_framework='bootstrap')
    
    return render_template("client/catalogo_femenino.html", prendas = prendas, pagination = pagination)


@app.route("/catalogo-masculino")
def catalogoMasculino():
    return render_template("client/catalogo_masculino.html")


@app.route("/carrito-compras")
def carritoCompras():
    return render_template("client/carrito.html")


@app.route("/listaDeseados")
def listaDeseados():
    return render_template("client/Lista_de_deseos.html")


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
    if usuario is not None:
        if encpass == usuario[2]:
            # Calculando el hash del entero aleatorio
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
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("client/login")


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

        # Realiza una consulta en la base de datos para verificar si el username y el email ya existen
        username_existente = controlador_usuarios.username_existente(username)
        email_existente = controlador_usuarios.email_existente(email)

        if username_existente:
            return jsonify({"error": "El nombre de usuario ya está en uso. Por favor, elija otro."})
        elif email_existente:
            return jsonify({"error": "La dirección de correo electrónico ya está en uso. Por favor, elija otra."})
        else:
            # Si el username y el email son válidos y disponibles, procede con el registro
            controlador_usuarios.insertar_usuario(username, email, password)
            return redirect("/login")


#! Lógica Tipo de Prenda

@app.route("/tipo_prenda")
def tipo_prenda():
    if validar_token():
        tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
        return render_template("admin/tipo_prenda.html", tipo_prendas=tipo_prendas)
    return redirect("/login")


@app.route("/agregar_tipo_prenda")
def agregar_tipo_prenda():
    if validar_token():
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
    if validar_token():
        color_prendas = controlador_color_prenda.obtener_color_prenda()
        return render_template("admin/color_prenda.html", color_prendas=color_prendas)
    return redirect("/login")


@app.route("/agregar_color_prenda")
def agregar_color_prenda():
    if validar_token():
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
    if validar_token():
        temporada_prendas = controlador_temporadas.obtener_temporada()
        return render_template("admin/temporada.html", temporada_prendas=temporada_prendas)
    return redirect("/login")


@app.route("/agregar_temporada")
def agregar_temporada():
    if validar_token():
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
    if validar_token():
        material_prendas = controlador_material.obtener_material()
        return render_template("admin/material.html", material_prendas=material_prendas)
    return redirect("/login")


@app.route("/agregar_material")
def agregar_material():
    if validar_token():
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
    if validar_token():
        talla_prendas = controlador_talla_prenda.obtener_talla_prenda()
        return render_template("admin/talla.html", talla_prendas=talla_prendas)
    return redirect("/login")


@app.route("/agregar_talla")
def agregar_talla():
    if validar_token():
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
    if validar_token():
        prendas = controlador_prenda.obtener_prenda()
        return render_template("admin/prenda.html", prendas=prendas)
    return redirect("/login")


@app.route("/agregar_prenda")
def agregar_prenda():
    if validar_token():
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
    codigo = request.form["cod_prenda"]
    nomPrenda = request.form["nom_prenda"]
    descripcion = request.form["desc_prenda"]
    tipo_prenda = int(request.form["tipo_prenda"])
    color_prenda = int(request.form["color_prenda"])
    temporada_prenda = int(request.form["temporada_prenda"])
    material_prenda = int(request.form["material_prenda"])
    file = request.files["imagen"]
    imagen = recibeFoto(file, codigo)
    controlador_prenda.actualizar_prenda(
        codigo, nomPrenda, descripcion, tipo_prenda, color_prenda, material_prenda, temporada_prenda, imagen, id)
    return redirect("/prenda")


@app.route("/eliminar_prenda", methods=["POST"])
def eliminar_prenda():
    controlador_prenda.eliminar_prenda(request.form["id"])
    return redirect("/prenda")

#! Lógica de Disponibilidad Prenda


@app.route("/disponibilidad_prenda")
def disponibilidad_prenda():
    if validar_token():
        disponibilidad_prendas = controlador_disponibilidad.obtener_disponibilidad_prenda()
        return render_template("admin/disponibilidad_prenda.html", disponibilidad_prendas=disponibilidad_prendas)
    return redirect("/login")


@app.route("/agregar_disponibilidad")
def agregar_disponibilidad():
    if validar_token():
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
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = codProd + extension
    upload_path = os.path.join (basepath, 'static/products', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

# -------------------------------------------- APIS -------------------------------------------- #

# ? APIS Temporada


@app.route("/api_obtener_temporada_prenda")
def api_obtener_temporada_prenda():
    temporada_prendas = controlador_temporadas.obtener_temporada()
    return jsonify(temporada_prendas)


@app.route("/api_guardar_temporada", methods=["POST"])
def api_guardar_temporada():
    nomTemp = request.json["nombre_temporada"]
    controlador_temporadas.insertar_temporada(nomTemp)
    return jsonify({"codigo": "1", "mensaje": "Temporada guardado correctamente."})


@app.route("/api_actualizar_temporada", methods=["POST"])
def api_actualizar_temporada():
    id = request.json["id"]
    nomTemporada = request.json["nombre_temporada"]
    controlador_temporadas.actualizar_temporada(nomTemporada, id)
    return jsonify({"codigo": "1", "mensaje": "Temporada actualizada correctamente."})


@app.route("/api_eliminar_temporada", methods=["POST"])
def api_eliminar_temporada():
    controlador_temporadas.eliminar_temporada(request.json["id"])
    return jsonify({"codigo": "1", "mensaje": "Temporada eliminada correctamente."})


# ? APIS Tipo de Prenda

@app.route("/api_obtener_tipo_prenda")
def api_obtener_tipo_prenda():
    tipo_prendas = controlador_tipo_prenda.obtener_tipo_prenda()
    return jsonify(tipo_prendas)


@app.route("/api_guardar_tipo_prenda", methods=["POST"])
def api_guardar_tipo_prenda():
    nombre_tipo = request.json["nombre_tipo"]
    controlador_tipo_prenda.insertar_tipo_prenda(nombre_tipo)
    return jsonify({"codigo": "1", "mensaje": "Tipo de prenda guardado correctamente."})


@app.route("/api_actualizar_tipo_prenda", methods=["POST"])
def api_actualizar_tipo_prenda():
    id = request.json["id"]
    nombre_tipo = request.json["nombre_tipo"]
    controlador_tipo_prenda.actualizar_tipo_prenda(nombre_tipo, id)
    return jsonify({"codigo": "1", "mensaje": "Tipo de prenda actualizado correctamente."})


@app.route("/api_eliminar_tipo_prenda", methods=["POST"])
def api_eliminar_tipo_prenda():
    controlador_tipo_prenda.eliminar_tipo_prenda(request.json["id"])
    return jsonify({"codigo": "1", "mensaje": "Tipo de prenda eliminada correctamente."})


# ? APIS Material de Prenda

@app.route("/api_material_prenda")
def api_material_prenda():
    material_prendas = controlador_material.obtener_material()
    return jsonify(material_prendas)


@app.route("/api_guardar_material", methods=["POST"])
def api_guardar_material():
    nomMat = request.json["nombre_material"]
    controlador_material.insertar_material(nomMat)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Codigo": "1", "Mensaje": "Material guardado correctamente."})


@app.route("/api_actualizar_material", methods=["POST"])
def api_actualizar_material():
    id = request.json["id"]
    nomMaterial = request.json["nombre_material"]
    controlador_material.actualizar_material(nomMaterial, id)
    return jsonify({"Codigo": "1", "Mensaje": "Material actualizado correctamente."})


@app.route("/api_eliminar_material", methods=["POST"])
def api_eliminar_material():
    controlador_material.eliminar_material(request.json["id"])
    return jsonify({"Codigo": "1", "Mensaje": "Material eliminado correctamente."})


# ? APIS Color de Prenda

@app.route("/api_obtener_color_prenda")
def api_obtener_color_prenda():
    color_prendas = controlador_color_prenda.obtener_color_prenda()
    return jsonify(color_prendas)


@app.route("/api_guardar_color_prenda", methods=["POST"])
def api_guardar_color_prenda():
    nombre_color = request.json["nombre_color"]
    controlador_color_prenda.insertar_color_prenda(nombre_color)
    return jsonify({"codigo": "1", "mensaje": "Color de prenda agregado correctamente."})


@app.route("/api_actualizar_color_prenda", methods=["POST"])
def api_actualizar_color_prenda():
    id = request.json["id"]
    nombre_color = request.json["nombre_color"]
    controlador_color_prenda.actualizar_color_prenda(nombre_color, id)
    return jsonify({"codigo": "1", "mensaje": "Color de prenda actualizado correctamente."})


@app.route("/api_eliminar_color_prenda", methods=["POST"])
def api_eliminar_color_prenda():
    controlador_color_prenda.eliminar_color_prenda(request.json["id"])
    return jsonify({"codigo": "1", "mensaje": "Color de prenda eliminado correctamente."})
