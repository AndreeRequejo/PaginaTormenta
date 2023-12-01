class Temporada:
    id_prenda_temporada = 0
    temporada = ""

    def __init__(self,p_id_prenda_temporada,p_temporada):
        self.id_prenda_temporada=p_id_prenda_temporada
        self.temporada=p_temporada

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_prenda_temporada"] = self.id_prenda_temporada
        dicTemp["temporada"] = self.temporada
        return dicTemp
