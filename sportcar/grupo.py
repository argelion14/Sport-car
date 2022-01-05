import sportcar.actividad
import sportcar.usuario

class Grupo:
    """
    Objeto valor de grupos

    Attributes
    ----------
    _usuarios : usuario
        Lista de usuarios que pertenencen al grupo
    _actividad : actividad
        Actividad del grupo
    Methods
    -------
    Aniadir_usuario_grupo
        Nos añade un nuevo usuario al grupo donde se realiza la actividad      
    """

    def __init__(self, usuario, actividad):
        """
        Contructor que necesitará un usuario y una actividad para poder existir minimamente un grupo

        Parameters
        ----------
        usuario : usuario
            Primer integrante y formador del grupo
        actividad : actividad
            Una actividad que determinar que hará el grupo
        """
        if type(usuario) != sportcar.usuario.Usuario:
            raise TypeError()

        if type(actividad) != sportcar.actividad.Actividad:
            raise TypeError()

        self._usuarios = [usuario]
        self._actividad = actividad
        
    def aniadir_usuario_grupo(self, usuario):
        """
        Aniadimos un nuevo usuario al grupo

        Parameters
        ----------
        usuario : usuario
        """
        if type(usuario) != sportcar.usuario.Usuario:
            raise TypeError()
        self._usuarios.append(usuario)