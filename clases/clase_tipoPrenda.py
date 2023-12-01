class TipoPrenda:
    id_tipo_prenda = 0
    tipo = ""

    def __init__(self,p_id_tipo_prenda,p_tipo):
        self.id_tipo_prenda=p_id_tipo_prenda
        self.tipo=p_tipo

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_tipo_prenda"] = self.id_tipo_prenda
        dicTemp["tipo"] = self.tipo
        return dicTemp
