from sportcar.errores import VehiculoFormatError, NombreUsuarioTooLongError, NombreUsuarioTooShortError
from sportcar.constantes import Contantes
class Usuario:

    def __init__(self, nombre, vehiculo, ciudad):
        
        if (len(nombre) > Contantes.LONGITUD_NOMBRE_MAXIMO):
            raise NombreUsuarioTooLongError()

        if (len(nombre) < Contantes.LONGITUD_NOMBRE_MINIMO):
            raise NombreUsuarioTooShortError()

        if type(vehiculo)!=bool:
            raise VehiculoFormatError()

        self._nombre = nombre
        self._vehiculo = vehiculo
        self._telefono = telefono
        self._ciudad = ciudad

    def get_nombre(self):
        return self._nombre

    def get_vehiculo(self):
        return self._vehiculo

    def get_ciudad(self):
        return self._ciudad