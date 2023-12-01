class Talla:
    id_talla_prenda = 0
    tipo_talla = ""

    def __init__(self,p_id_talla_prenda,p_tipo_talla):
        self.id_talla_prenda=p_id_talla_prenda
        self.tipo_talla=p_tipo_talla

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_talla_prenda"] = self.id_talla_prenda
        dicTemp["tipo_talla"] = self.tipo_talla
        return dicTemp
