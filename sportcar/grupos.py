import sportcar.actividad
import sportcar.usuario
import sportcar.errores
import sportcar.grupo
from sportcar.errores import GruposVacio

class Grupos:

    def __init__(self):
        """
        Contructor que inicializa la clase con los grupos los cuales son necesarios para crear estadisticas
        
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
        self._grupos = {}
    
    def aniadir_grupo(self,grupo):
        """
        Aniade un nuevo objeto valor grupo a la lista de grupos
        Parameters
        ----------
        grupo : grupo
        """
        pass

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

    
        