from bd import obtener_conexion
import hashlib

def obtener_usuario(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, username, password, token FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario


def username_existente(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT username FROM usuarios WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def email_existente(email):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT email FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_token_usuario(username, token):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET token = %s WHERE username = %s",
                       (token, username))
    conexion.commit()
    conexion.close()

def quitar_token_usuario(username):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET token ='' WHERE username = %s",
                       (username))
    conexion.commit()
    conexion.close()    

def insertar_usuario(username,email,contraseña):
    conexion = obtener_conexion()
    h = hashlib.new('sha256')
    h.update(bytes(contraseña, encoding="utf-8"))
    encpass = h.hexdigest()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)",
                       (username,email,encpass))
    conexion.commit()
    conexion.close()