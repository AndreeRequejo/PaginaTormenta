class Temporada:
    id = 0
    temporada = ""

    def __init__(self,p_id,p_temporada):
        self.id=p_id
        self.temporada=p_temporada

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id"] = self.id
        dicTemp["temporada"] = self.temporada
        return dicTemp
