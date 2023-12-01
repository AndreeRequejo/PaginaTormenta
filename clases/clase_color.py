class Color:
    id_color_prenda = 0
    color = ""

    def __init__(self,p_id_color_prenda,p_color):
        self.id_color_prenda=p_id_color_prenda
        self.color=p_color

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_color_prenda"] = self.id_color_prenda
        dicTemp["color"] = self.color
        return dicTemp
