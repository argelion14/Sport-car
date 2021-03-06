class VehiculoFormatError (Exception):
    def __init__(self, message = "Debe ser un booleano"):
        self.message = message

class NombreFormatError (Exception):
    def __init__(self, message = "Debe ser un nombre admitido"):
        self.message = message

class NombreUsuarioTooLongError (Exception):
    def __init__(self, message = "Nombre demasiado largo"):
        self.message = message

class NombreUsuarioTooShortError (Exception):
    def __init__(self, message = "Nombre demasiado corto"):
        self.message = message

class TipoActividadFormatError (Exception):
    def __init__(self, message = "Debe ser un tipo admitido"):
        self.message = message

class GruposVacio (Exception):
    def __init__(self, message = "No existen grupos"):
        self.message = message