import datetime
from sportcar.errores import NombreFormatError , TipoActividadFormatError
from enum import Enum
from assertpy import assert_that

class ActividadesDisponibles(Enum):
    ESCALADA = "Escalada en rocodromo"
    NATACION = "Natación en pabellón"
    PADEL = "Padel en pista"

class TipoActividad(Enum):
    DEPORTIVA = "Actividad deportiva"
    CULTURA = "Actividad cultural"
    APRENDIZAJE = "Actividad en la que se prioriza el querer aprender"

class Actividad:

    def __init__(self, nombre, fecha_inicio, fecha_final, tipo, ubicacion, ciudad):

        if (nombre not in ActividadesDisponibles._member_names_):
            raise NombreFormatError()

        if (tipo not in TipoActividad._member_names_):
            raise TipoActividadFormatError()

        assert_that(fecha_inicio).is_after(fecha_final) #Nos da un assert en caso de que la fecha

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

