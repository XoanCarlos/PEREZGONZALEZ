import unittest
import clients
import conexion
import var


class MyTestCase(unittest.TestCase):
    def test_dni(self):
        dni = '00000000T'
        value = clients.Clientes.validarDni(str(dni))
        msg = 'Proba Errónea'
        self.assertTrue(value, msg)

    def test_fact(self):
        valor = 40.03
        self.assertEqual(round(float(valor),), round(float(var.fac),2))

if __name__ == '__main__':
    unittest.main()
