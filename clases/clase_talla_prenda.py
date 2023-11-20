class Prenda:
    id = 0
    prenda = ""

    def __init__(self,p_id,p_prenda):
        self.id=p_id
        self.prenda=p_prenda

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id"] = self.id
        dicTemp["prenda"] = self.prenda
        return dicTemp
