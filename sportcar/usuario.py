class Usuario:

    def __init__(self, nombre, vehiculo, telefono, ciudad):
        self._nombre = nombre
        self._vehiculo = vehiculo
        self._telefono = telefono
        self._ciudad = ciudad

    def get_nombre(self):
        return self._nombre

    def get_vehiculo(self):
        return self._vehiculo

    def get_telefono(self):
        return self._telefono

    def get_ciudad(self):
        return self._ciudad
