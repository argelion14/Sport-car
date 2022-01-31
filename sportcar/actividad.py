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
    """
    Clase que define un usuario
    Attributes
    ----------
    _nombre : nombre
        Nombre de la actividad
    _fecha_inicio : datetime
        Inicio de la actividad
    _fecha_final : datetime
        Final de la actividad
    _tipo : TipoActividad
        Tipo de la actividad
    _ubicación : str
        Lugar donde se realizará la actividad
    _ciudad : str
        Ciudad donde se realizará la actividad
    Methods
    -------
    get_nombre
        Devuelve el nombre de la actividad
    
    """
    def __init__(self, nombre, fecha_inicio, fecha_final, tipo, ubicacion, ciudad):

        if (nombre not in ActividadesDisponibles._member_names_):
            raise NombreFormatError()

        if (tipo not in TipoActividad._member_names_):
            raise TipoActividadFormatError()

        assert_that(fecha_inicio).is_before(fecha_final) #Nos da un AssertionError en caso de que la fecha de inicio sea posterior a la de final

        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_final
        self._tipo = tipo
        self._ciudad = ciudad
        self._ubicacion = ubicacion

    def get_nombre(self):
        """
        Devuelve el nombre de la actividad
        """
        return self._nombre

    def get_fecha_inicio(self):
        """
        Devuelve la fecha de inicio de la actividad
        """
        return self._fecha_inicio

    def get_fecha_final(self):
        """
        Devuelve la fecha final de la actividad
        """
        return self._fecha_final

    def get_ciudad(self):
        """
        Devuelve la ciudad donde se realiza la actividad
        """
        return self._ciudad

    def get_tipo(self):
        """
        Devuelve el tipo de actividad
        """
        return self._ciudad

    def get_ubicacion(self):
        """
        Devuelve la ubicacion donde se realiza la actividad
        """
        return self._ubicacion