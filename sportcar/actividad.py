from datetime import datetime

class Actividad:

	def __init__(self, nombre, fecha_inicio, fecha_final, tipo, intensidad, localizacion):
		self.nombre = nombre
		self.fecha_inicio = fecha_inicio
		self.fecha_final = fecha_final
		self.tipo = tipo
		self.intensidad = intensidad
		self.localizacion = localizacion