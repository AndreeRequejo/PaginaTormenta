class Color:
    id = 0
    color = ""

    def __init__(self,p_id,p_color):
        self.id=p_id
        self.color=p_color

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id"] = self.id
        dicTemp["color"] = self.color
        return dicTemp
