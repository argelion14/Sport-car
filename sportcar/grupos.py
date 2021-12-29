import sportcar.actividad
import sportcar.usuario
import sportcar.grupo
from sportcar.errores import GruposVacio

class Grupos:
    """
    Clase que representa los grupos que se pueden tener en nuestra aplicación, así como para poder trabajar con ellos para sacar estadísticas
    
    Attributes
        ----------
        _grupos : grupo
            Lista de grupos
        Methods
        -------
        ciudadPreferida()
            Nos devuelve la ciudad preferida por los usuarios para realizar actividades basada en una media

        aniadir_grupo(grupo)
            Aniade un nuevo grupo
    """

    def __init__(self):
        """
        Contructor que inicializa la clase con los grupos los cuales son necesarios para crear estadisticas

        Parameters
        ----------
        None
        """
        self._grupos = {}
    
    def aniadir_grupo(self,grupo):
        """
        Aniade un nuevo objeto valor grupo a la lista de grupos

        Parameters
        ----------
        grupo : grupo
        """
        self._grupos.append(grupo)

    def ciudadPreferida(self):
        """
        Se analizan los grupos y segun el número de personan que lo conformen, y sus ciudades se elige la ciudad favorita

        Parameters
        ----------
        None

        Returns
        -------
        ciudadFav : str
            Ciudad favorita elegida mediante la estadistica
        """
        if not self._grupos:
            raise GruposVacio()
        ciudadFav = 'Granada'