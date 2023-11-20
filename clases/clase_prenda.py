class Prenda:
    id_prenda = 0
    codigo = ""
    nomPrenda = ""
    descripcion = ""
    id_tipo_prenda = 0
    id_color_prenda = 0
    id_tipo_material = 0
    id_prenda_temporada = 0
    imagen = ""

    def __init__(self, p_id_prenda, p_codigo, p_nomPrenda, p_descripcion, p_id_tipo_prenda, p_id_color_prenda, p_id_tipo_material, p_id_prenda_temporada, p_imagen):
        self.id_prenda = p_id_prenda
        self.codigo = p_codigo
        self.nomPrenda = p_nomPrenda
        self.descripcion = p_descripcion
        self.id_tipo_prenda = p_id_tipo_prenda
        self.id_color_prenda = p_id_color_prenda
        self.id_tipo_material = p_id_tipo_material
        self.id_prenda_temporada = p_id_prenda_temporada
        self.imagen = p_imagen

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_prenda"] = self.id_prenda
        dicTemp["codigo"] = self.codigo
        dicTemp["nomPrenda"] = self.nomPrenda
        dicTemp["descripcion"] = self.descripcion
        dicTemp["id_tipo_prenda"] = self.id_tipo_prenda
        dicTemp["id_color_prenda"] = self.id_color_prenda
        dicTemp["id_tipo_material"] = self.id_tipo_material
        dicTemp["id_prenda_temporada"] = self.id_prenda_temporada
        dicTemp["imagen"] = self.imagen
        return dicTemp
