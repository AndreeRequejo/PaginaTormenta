CREATE TABLE usuarios (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    email varchar(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    token VARCHAR(255),
    nombre VARCHAR(60),
    apellido VARCHAR(60),
    telefono VARCHAR(9),
    docid VARCHAR(11)
);

CREATE TABLE tipo_prenda (
    id_tipo_prenda SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo varchar(40) NOT NULL
);

CREATE TABLE color_prenda (
    id_color_prenda SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    color varchar(40) NOT NULL
);

CREATE TABLE tipo_material (
    id_tipo_material SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    material varchar(40) NOT NULL
);

CREATE TABLE prenda_temporada (
    id_prenda_temporada SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    temporada varchar(100) NOT NULL
);

CREATE TABLE prenda (
    id_prenda BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    codigo CHAR(7) NOT NULL,
    nomPrenda VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    id_tipo_prenda SMALLINT UNSIGNED NOT NULL REFERENCES tipo_prenda(id_tipo_prenda),
    id_color_prenda SMALLINT UNSIGNED NOT NULL REFERENCES color_prenda(id_color_prenda),
    id_tipo_material SMALLINT UNSIGNED NOT NULL  REFERENCES tipo_material(id_tipo_material),
    id_prenda_temporada SMALLINT UNSIGNED NOT NULL REFERENCES prenda_temporada(id_prenda_temporada),
    imagen VARCHAR(100) NOT NULL
);

CREATE TABLE talla_prenda (
    id_talla_prenda SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_talla VARCHAR(3) NOT NULL
);

CREATE TABLE disponibilidad_prenda (
    id_prenda SMALLINT NOT NULL REFERENCES prenda(id_prenda),
    id_talla_prenda SMALLINT NOT NULL REFERENCES talla_prenda(id_talla_prenda),
    precio NUMERIC(6,2) NOT NULL,
    stock SMALLINT NOT NULL,
    CONSTRAINT pk_disponibilidad_prenda PRIMARY KEY (id_prenda,id_talla_prenda)
);

CREATE TABLE metodo_pago (
    id_metodo_pago SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_pago varchar(100) NOT NULL
);

CREATE TABLE compra (
    id_compra BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(8) NOT NULL,
    fecha DATE NOT NULL,
    estado TINYINT(1) NOT NULL,
    modalidad_entrega VARCHAR(30) NOT NULL,
    id_usuario BIGINT NOT NULL REFERENCES usuarios (id)
);

CREATE TABLE tipo_comprobante_venta (
    id_tipo_comprobante_venta SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo_comprobante varchar(100) NOT NULL
);

CREATE TABLE venta (
    id_venta BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cod_venta char(6) NOT NULL,
    fecha DATE NOT NULL,
    estado BOOLEAN NOT NULL,
    monto_total NUMERIC(8,2) NOT NULL,
    descuento NUMERIC(6,2) NOT NULL,
    id_usuario BIGINT NOT NULL REFERENCES usuarios (id),
    id_tipo_comprobante SMALLINT NOT NULL REFERENCES tipo_comprobante_venta(id_tipo_comprobante_venta)
);

CREATE TABLE detalle_venta (
    id_venta BIGINT NOT NULL REFERENCES venta(id_venta),
    id_prenda SMALLINT NOT NULL REFERENCES disponibilidad_prenda (id_prenda,id_talla_prenda),
    id_talla_prenda SMALLINT NOT NULL REFERENCES disponibilidad_prenda (id_prenda,id_talla_prenda),
    precio NUMERIC(5, 2) NOT NULL,
    cantidad INT NOT NULL,
    CONSTRAINT pk_detalle_venta PRIMARY KEY (id_venta,id_prenda,id_talla_prenda)
);