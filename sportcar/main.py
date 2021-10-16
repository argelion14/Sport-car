from actividad import *
from usuario import *


def pruebas():
    usuario_1 = Usuario('Luis', True, '658323232', 'Granada', 'M')
    fecha_inicio = datetime(2021, 11, 28, 15, 30, 00, 0000)
    fecha_final = datetime(2021, 11, 28, 16, 30, 00, 0000)
    actividad1 = Actividad('Escalada con ritmo #25', fecha_inicio, fecha_final, 'Escalada', 2, 'RockandBloc', 'Granada')

    print("Información Usuario 1")
    print("Nombre: " + usuario_1.nombre)
    print("¿Posee vehiculo? " + "Si tiene" if usuario_1.vehiculo else "No tiene")
    print("Ciudad: " + usuario_1.ciudad)

    print("Información Actividad 1")
    print("Nombre: " + actividad1.nombre)
    print("Dia de la actividad: {}".format(actividad1.fecha_inicio.day) + "/{}".format(actividad1.fecha_inicio.month)
          + "/{}".format(actividad1.fecha_inicio.year))
    print("Hora de inicio de la actividad: {}".format(actividad1.fecha_inicio.hour)
          + ":{}".format(actividad1.fecha_inicio.minute))
    print("Ciudad: " + usuario_1.ciudad)


if __name__ == '__main__':
    pruebas()