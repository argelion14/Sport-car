import unittest
import sys
sys.path.append(".")

import sportcar.actividad
import sportcar.usuario
import sportcar.errores

class Tests (unittest.TestCase):
    
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