class Actividad:

    def __init__(self, nombre, fecha_inicio, fecha_final, tipo, ubicacion, ciudad):
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_final
        self._tipo = tipo
        self._ciudad = ciudad
        self._ubicacion = ubicacion

    def get_nombre(self):
        return self._nombre

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_fecha_final(self):
        return self._fecha_final

    def get_ciudad(self):
        return self._ciudad

    def get_tipo(self):
        return self._ciudad

    def get_ubicacion(self):
        return self._ubicacion

