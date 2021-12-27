class TelefonoFormatError (Exception):
    def __init__(self, message = "Telefono debe ser cadena"):
        self.message = message

class VehiculoFormatError (Exception):
    def __init__(self, message = "Debe ser un booleano"):
        self.message = message