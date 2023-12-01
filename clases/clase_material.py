class Material:
    id_tipo_material = 0
    material = ""

    def __init__(self,p_id_tipo_material,p_material):
        self.id_tipo_material=p_id_tipo_material
        self.material=p_material

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_tipo_material"] = self.id_tipo_material
        dicTemp["material"] = self.material
        return dicTemp
