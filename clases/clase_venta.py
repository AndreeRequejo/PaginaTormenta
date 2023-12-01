class Venta:
    id_venta = 0
    fecha = ""
    estado = 0
    monto_total = 0.00
    descuento = 0.00
    id_usuario = 0
    id_tipo_comprobante = 0

    def __init__(self, v_id_venta,v_fecha,   v_estado, v_monto_total, v_descuento, v_id_usuario, v_id_tipo_comprobante):
        self.id_venta = v_id_venta
        self.fecha = v_fecha
        self.estado = v_estado
        self.monto_total = v_monto_total
        self.descuento = v_descuento
        self.id_usuario = v_id_usuario
        self.id_tipo_comprobante = v_id_tipo_comprobante

    def obtenerObjetoSerializable(self):
        dicTemp = dict()
        dicTemp["id_venta"] = self.id_venta
        dicTemp["fecha"] = self.fecha
        dicTemp["estado"] = self.estado
        dicTemp["monto_total"] = self.monto_total
        dicTemp["descuento"] = self.descuento
        dicTemp["id_usuario"] = self.id_usuario
        dicTemp["id_tipo_comprobante"] = self.id_tipo_comprobante
        return dicTemp