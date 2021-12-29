from dataclasses import dataclass
import sportcar.actividad
import sportcar.usuario
import sportcar.errores

class Grupo:

    def __init__(self, usuario, actividad):
        """
        Objeto valor de grupos, que para conformarse solo necesitará un usuario y una actividad

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
        self._usuarios = {usuario}
        self._actividad = actividad
        
    def aniadir_usuario_grupo(self, usuario):
        """
        Parameters
        ----------
        usuario : usuario
        """
        self._usuarios.append(usuario)


