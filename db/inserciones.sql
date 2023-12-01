-- INSERCIONES DE USUARIOS

INSERT INTO usuarios VALUES (1,'admin','root@gmail.com',SHA2('admin',256),'','Administrador', 'Tormenta', 'Website', '987654321','00000000');
INSERT INTO usuarios VALUES (2,'andree','andree@gmail.com',SHA2('andree',256),'','Andree', 'Requejo', 'Diaz', '92820528','74020421');
INSERT INTO usuarios VALUES (3,'edu','edu@gmail.com',SHA2('edu',256),'','Davist Edu', 'Bustamante', 'Sánchez', '999658213','72956821');
INSERT INTO usuarios VALUES (4,'juana','juana@gmail.com',SHA2('juana',256),'','Juana', 'Isique', 'Aurazo', '971114200','74152384');

-- INSERCIONES DE TIPOS DE PRENDAS

INSERT INTO tipo_prenda (tipo) VALUES ('Jeans');
INSERT INTO tipo_prenda (tipo) VALUES ('Pantalones');
INSERT INTO tipo_prenda (tipo) VALUES ('Polos');
INSERT INTO tipo_prenda (tipo) VALUES ('Casacas');
INSERT INTO tipo_prenda (tipo) VALUES ('Poleras');
INSERT INTO tipo_prenda (tipo) VALUES ('Tops');
INSERT INTO tipo_prenda (tipo) VALUES ('Vestidos');
INSERT INTO tipo_prenda (tipo) VALUES ('Blusas');
INSERT INTO tipo_prenda (tipo) VALUES ('Faldas');
INSERT INTO tipo_prenda (tipo) VALUES ('Shorts');

-- INSERCIONES DE COLORES

INSERT INTO color_prenda (color) VALUES ('Rojo');
INSERT INTO color_prenda (color) VALUES ('Blanco');
INSERT INTO color_prenda (color) VALUES ('Azul');
INSERT INTO color_prenda (color) VALUES ('Gris');
INSERT INTO color_prenda (color) VALUES ('Rosado');
INSERT INTO color_prenda (color) VALUES ('Negro');
INSERT INTO color_prenda (color) VALUES ('Denim');
INSERT INTO color_prenda (color) VALUES ('Morado');
INSERT INTO color_prenda (color) VALUES ('Multicolor');
INSERT INTO color_prenda (color) VALUES ('Granate');
INSERT INTO color_prenda (color) VALUES ('Amarillo');
INSERT INTO color_prenda (color) VALUES ('Beige');
INSERT INTO color_prenda (color) VALUES ('Crema');
INSERT INTO color_prenda (color) VALUES ('Celeste');
INSERT INTO color_prenda (color) VALUES ('Fucsia');
INSERT INTO color_prenda (color) VALUES ('Hueso');
INSERT INTO color_prenda (color) VALUES ('Marrón');
INSERT INTO color_prenda (color) VALUES ('Morado');
INSERT INTO color_prenda (color) VALUES ('Naranja');

-- INSERCIONES DE MATERIALES

INSERT INTO tipo_material (material) VALUES ('Algodón');
INSERT INTO tipo_material (material) VALUES ('Poliéster');
INSERT INTO tipo_material (material) VALUES ('Lino');
INSERT INTO tipo_material (material) VALUES ('Lana');
INSERT INTO tipo_material (material) VALUES ('Cuero');
INSERT INTO tipo_material (material) VALUES ('Seda');
INSERT INTO tipo_material (material) VALUES ('Piel');
INSERT INTO tipo_material (material) VALUES ('Licra');

-- INSERCIONES DE TEMPORADAS

INSERT INTO prenda_temporada (temporada) VALUES ('Temporada de Verano');
INSERT INTO prenda_temporada (temporada) VALUES ('Temporada de Primavera');
INSERT INTO prenda_temporada (temporada) VALUES ('Temporada de Otoño');
INSERT INTO prenda_temporada (temporada) VALUES ('Temporada de Invierno');

-- INSERCIONES DE TALLAS

INSERT INTO talla_prenda (tipo_talla) VALUES ('XS');
INSERT INTO talla_prenda (tipo_talla) VALUES ('S');
INSERT INTO talla_prenda (tipo_talla) VALUES ('M');
INSERT INTO talla_prenda (tipo_talla) VALUES ('L');
INSERT INTO talla_prenda (tipo_talla) VALUES ('XL');
INSERT INTO talla_prenda (tipo_talla) VALUES ('28');
INSERT INTO talla_prenda (tipo_talla) VALUES ('30');
INSERT INTO talla_prenda (tipo_talla) VALUES ('32');
INSERT INTO talla_prenda (tipo_talla) VALUES ('34');
INSERT INTO talla_prenda (tipo_talla) VALUES ('36');

-- INSERCIONES DE PRENDAS

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0001', 'POLO ROXY CLASSIC', '', 3, 4, 1, 1,'PD0001.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0002', 'POLERA INSIGNE HOODY', '', 5, 4, 1, 1,'PD0002.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0003', 'CASACA ROXY', '', 4, 6, 1, 1,'PD0003.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0004', 'JEAN HUNTER IC', '', 1, 7, 1, 4,'PD0004.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0005', 'CHOMPA ROXY SWEATER', '', 4, 6, 1, 1,'PD0005.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0006', 'POLERA LIPPI', '', 5, 8, 1, 3,'PD0006.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0007', 'LESEM TOP STASSIE', '', 6, 9, 1, 2,'PD0007.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0008', 'CASACA DVK LIGHT DIDI', '', 4, 10, 1, 4,'PD0008.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0009', 'FALDA ROXY COSMIC GLOW', '', 9, 9, 1, 1,'PD0009.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0010', 'POLERA CHAMPION VELOUR', '', 5, 6, 2, 3,'PD0010.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0011', 'BLUSA DVK BEA HSO', '', 8, 2, 1, 1,'PD0011.webp');

INSERT INTO prenda (codigo, nomPrenda, descripcion, id_tipo_prenda, id_color_prenda, id_tipo_material, id_prenda_temporada, imagen)
VALUES ('PD0012', 'PANTALON POSER CARGO', '', 2, 6, 2, 3,'PD0012.webp');

-- INSERCIONES DE DISPONIBILIDAD_PRENDAS

-- 1
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (1,1,49.50,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (1,2,49.50,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (1,3,49.50,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (1,4,49.50,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (1,5,49.50,50);

-- 2
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (2,1,75.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (2,2,75.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (2,3,75.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (2,4,75.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (2,5,75.90,50);

-- 3
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (3,1,120.90,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (3,2,120.90,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (3,3,120.90,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (3,4,120.90,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (3,5,120.90,80);

-- 4
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (4,6,85.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (4,7,85.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (4,8,85.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (4,9,85.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (4,10,85.40,70);

-- 5
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (5,1,103.90,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (5,2,103.90,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (5,3,103.90,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (5,4,103.90,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (5,5,103.90,70);

-- 6
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (6,1,105.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (6,2,105.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (6,3,105.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (6,4,105.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (6,5,105.90,50);

-- 7
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (7,1,64.90,60);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (7,2,64.90,60);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (7,3,64.90,60);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (7,4,64.90,60);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (7,5,64.90,60);

-- 8
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (8,1,135.90,65);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (8,2,135.90,65);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (8,3,135.90,65);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (8,4,135.90,65);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (8,5,135.90,65);

-- 9
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (9,6,55.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (9,7,55.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (9,8,55.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (9,9,55.40,70);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (9,10,55.40,70);

-- 10
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (10,1,115.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (10,2,115.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (10,3,115.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (10,4,115.90,50);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (10,5,115.90,50);

-- 11
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (11,1,68.90,100);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (11,2,68.90,100);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (11,3,68.90,100);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (11,4,68.90,100);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (11,5,68.90,100);

-- 12
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (12,6,75.40,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (12,7,75.40,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (12,8,75.40,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (12,9,75.40,80);
INSERT INTO disponibilidad_prenda (id_prenda, id_talla_prenda, precio, stock) VALUES (12,10,75.40,80);
