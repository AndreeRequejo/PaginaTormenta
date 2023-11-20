class Disponibilidad:
    id_prenda = 0
    prenda = ""
    id_talla_prenda = 0
    talla = ""
    precio = 0
    stock = 0

    def __init__(self, p_prenda,p_talla, p_precio,p_stock, p_idPrenda, p_idTalla):
        self.prenda = p_prenda
        self.talla = p_talla
        self.precio = p_precio
        self.stock = p_stock
        self.id_prenda = p_idPrenda
        self.id_talla_prenda = p_idTalla

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["nomPrenda"] = self.prenda
        dicTemp["tipo_talla"] = self.talla
        dicTemp["precio"] = self.precio
        dicTemp["stock"] = self.stock
        dicTemp["id_prenda"] = self.id_prenda
        dicTemp["id_talla_prenda"] = self.id_talla_prenda
        return dicTemp
