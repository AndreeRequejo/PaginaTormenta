## PÁGINA WEB TORMENTA - CRUD

Proyecto - Tormenta, es un sistema de comercio electrónico (e-commerce) que incorpora funcionalidades clave para la administración eficiente de una plataforma de compras en línea. Desarrollado como un CRUD con un enfoque modular, Tormenta ofrece un conjunto diverso de características para facilitar la gestión de usuarios, productos, compras y transacciones de venta.

### Creación de entorno virtual y dependencias:

> py -3 -m venv .venv
> .venv\Scripts\activate

> pip install Flask
> pip install pymysql
> pip install flask-paginate
> pip install Flask-JWT
> pip install Flask==2.3.3

### Configuración de BD:
> XAMPP

def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                port=3306,
                                user='root',
                                password='',
                                db='bdproyectofinal')

> Local (MySQL WorkBench)

def obtener_conexion():
    return pymysql.connect(host='127.0.0.1',
                                port=3306,
                                user='root',
                                password='1234',
                                db='bdproyectofinal')
        
> Python Anywhere

def obtener_conexion():
    return pymysql.connect(host='GrupoWeb1.mysql.pythonanywhere-services.com',
                                user='GrupoWeb1',
                                password='Vale 2502',
                                db='GrupoWeb1$ProyectoFinal')

> Clonar Repositorio:

[Consola] (git clone https://github.com/AndreeRequejo/PaginaTormenta.git)