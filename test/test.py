from logging import error
import unittest
import sys
import datetime
sys.path.append(".")

import sportcar.actividad
import sportcar.usuario
import sportcar.errores
import sportcar.grupo
import sportcar.grupos
from assertpy import assert_that

class TestActividad (unittest.TestCase):
    
    def test_nombreOpcion(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un nombre que no se encuentra entre las opciones disponibles
        """
        with self.assertRaises(sportcar.errores.NombreFormatError):
            actividad = sportcar.actividad.Actividad('NATACiION',datetime.datetime(2022,1,2,3,4,5,6), datetime.datetime(2023,1,2,3,4,5,6), 'DEPORTIVA', 'ubicacion', 'ciudad')

    def test_tipoOpcion(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un tipo que no se encuentra entre las opciones disponibles
        """
        with self.assertRaises(sportcar.errores.TipoActividadFormatError):
            actividad = sportcar.actividad.Actividad('NATACION',datetime.datetime(2022,1,2,3,4,5,6), datetime.datetime(2023,1,2,3,4,5,6), 'DEPORTiIVA', 'ubicacion', 'ciudad')

    def test_fechaCorrecta(self):
        """
        Test que comprueba que se da el AssertionError cuando la fecha introducida de inicio es posterios a la de final
        """
        with self.assertRaises(AssertionError):
            actividad = sportcar.actividad.Actividad('NATACION',datetime.datetime(2022,1,2,3,4,5,6), datetime.datetime(2021,2,3,4,5,6,7), 'DEPORTIVA', 'ubicacion', 'ciudad')
        
class TestUsuario (unittest.TestCase):

    def test_nombreUsuarioLargo(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un nombre de usuario demasiado largo
        """
        with self.assertRaises(sportcar.errores.NombreUsuarioTooLongError):
            usuario = sportcar.usuario.Usuario('Don idelfonso de la mancha que vive bien lejos el tio macho y encima guapo',True,'Granada')

    def test_nombreUsuarioCorto(self):
        """
        Test para comprobar que se levanta la excepción cuando se da un nombre de usuario demasiado corto
        """
        with self.assertRaises(sportcar.errores.NombreUsuarioTooShortError):
            usuario = sportcar.usuario.Usuario('J',True,'Granada')

    def test_vehiculo(self):
        """
        Test para comprobar que se da la excepción cuando no se introduce un formato de vehículo correcto
        """
        with self.assertRaises(sportcar.errores.VehiculoFormatError):
            usuario = sportcar.usuario.Usuario('Angel','NO','Granada')

class TestGrupos (unittest.TestCase):

    def test_grupoVacio(self):
        """
        Test para comprobar que se levanta la excepcion cuando se quiere realizar alguna estadistica y no existe ningun grupo
        """
        with self.assertRaises(sportcar.errores.GruposVacio):
            grupos = sportcar.grupos.Grupos()
            ciudadFav = grupos.ciudadPreferida()

if __name__ == '__main__':
    unittest.main()