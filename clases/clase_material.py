class Material:
    id = 0
    material = ""

    def __init__(self,p_id,p_material):
        self.id=p_id
        self.material=p_material

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id"] = self.id
        dicTemp["material"] = self.material
        return dicTemp
