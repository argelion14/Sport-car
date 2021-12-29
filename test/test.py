import unittest
import sys
import datetime
sys.path.append(".")

import sportcar.actividad
import sportcar.usuario
import sportcar.errores

class TestActividad (unittest.TestCase):
    
    def test_nombreOpcion(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un nombre que no se encuentra entre las opciones disponibles
        """
        with self.assertRaises(sportcar.errores.NombreFormatError):
            actividad = sportcar.actividad.Actividad('NATACiION','fecha_inicio', 'fecha_final', 'DEPORTIVA', 'ubicacion', 'ciudad')

    def test_tipoOpcion(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un tipo que no se encuentra entre las opciones disponibles
        """
        with self.assertRaises(sportcar.errores.TipoActividadFormatError):
            actividad = sportcar.actividad.Actividad('NATACION','fecha_inicio', 'fecha_final', 'DEPORTiIVA', 'ubicacion', 'ciudad')

class TestUsuario (unittest.TestCase):

    def test_nombreUsuarioLargo(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un nombre de usuario demasiado largo
        """
        with self.assertRaises(sportcar.errores.NombreUsuarioTooLongError):
            usuario = sportcar.usuario.Usuario('Don idelfonso de la mancha que vive bien lejos el tio macho y encima guapo',True,'695641699','Granada')

    def test_nombreUsuarioCorto(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un nombre de usuario demasiado corto
        """
        with self.assertRaises(sportcar.errores.NombreUsuarioTooShortError):
            usuario = sportcar.usuario.Usuario('J',True,'695641699','Granada')

    def test_vehiculo(self):
        """
        Test para comprobar que se da la excepción cuando no se introduce un formato de vehículo correcto
        """
        with self.assertRaises(sportcar.errores.VehiculoFormatError):
            usuario = sportcar.usuario.Usuario('Angel','NO','695641699','Granada')
    
    def test_telefono(self):
        """
        Test para comprobar que se da la excepción cuando el formato de telefono que se da no es correcto
        """
        with self.assertRaises(sportcar.errores.TelefonoFormatError):
            usuario = sportcar.usuario.Usuario('Angel',True,695641699,'Granada')

if __name__ == '__main__':
    unittest.main()