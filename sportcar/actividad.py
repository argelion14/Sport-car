from datetime import datetime


class Actividad:

    def __init__(self, nombre, fecha_inicio, fecha_final, tipo, intensidad, localizacion, ciudad):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.tipo = tipo
        self.ciudad = ciudad
        self.intensidad = intensidad
        self.localizacion = localizacion
