from sportcar.errores import VehiculoFormatError, NombreUsuarioTooLongError, NombreUsuarioTooShortError
from sportcar.constantes import Contantes
class Usuario:
    """
    Clase que define un usuario
    Attributes
    ----------
    _nombre : str
        Nombre del usuario
    _vehiculo : boolean
        Booleano que indica la disposición del vehiculo
    _ciudad : str
        Ciudad donde reside el usuario
    Methods
    -------
    get_nombre
        Devuelve el nombre del usuario
    get_vehiculo
        Devuelve la disposicion o no del vehiculo del usuario
    get_ciudad
        Devuelve la ciudad del usuario
    """
    def __init__(self, nombre, vehiculo, ciudad):
        """
        Constructor que forma un objeto usuario en base a su nombre su disposición o no de vehículo y la ciudad donde reside
        Parameters
        ----------
        nombre : str
            Nombre del usuario
        vehiculo : boolean
            Booleano que indica la disposición del vehiculo
        ciudad : str
            Ciudad donde reside el usuario
        """
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
        """
        Devuelve el nombre del usuario
        """
        return self._nombre

    def get_vehiculo(self):
        """
        Devuelve la disposicion o no del vehiculo del usuario
        """
        return self._vehiculo

    def get_ciudad(self):
        """
        Devuelve la ciudad del usuario
        """
        return self._ciudad