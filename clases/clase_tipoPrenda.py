class TipoPrenda:
    id = 0
    tipoPrenda = ""

    def __init__(self,p_id,p_tipoPrenda):
        self.id=p_id
        self.tipoPrenda=p_tipoPrenda

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id"] = self.id
        dicTemp["tipoPrenda"] = self.tipoPrenda
        return dicTemp
