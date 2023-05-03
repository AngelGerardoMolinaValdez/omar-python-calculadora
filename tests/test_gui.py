import unittest
from tkinter import Tk
import sys
import os


package_path = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.insert(0, package_path)


from main import Calculadora


class TestCalculadora(unittest.TestCase):
    
    def setUp(self) -> None:
        """se instancia el objeto que crea la calculadora
        """
        self.root = Tk()
        self.calculadora = Calculadora(self.root)
        
    def tearDown(self) -> None:
        """se especifican los procesos finales
        de la regresion
        """
        self.root.destroy()
        
    def test_press_key(self) -> None:
        """ test_press_key
        Prueba que la suma de dos números funciona correctamente
        """
        self.calculadora.press_key("1")
        self.assertEqual(self.calculadora.display.get(), "1")
        
        self.calculadora.press_key("+")
        self.assertEqual(self.calculadora.display.get(), "1+")
        
        self.calculadora.press_key("2")
        self.assertEqual(self.calculadora.display.get(), "1+2")
        
        self.calculadora.press_key("=")
        self.assertEqual(self.calculadora.display.get(), "3")
        
        self.calculadora.press_key("C")
        self.assertEqual(self.calculadora.display.get(), "")

    def test_suma(self) -> None:
        """ test_suma
        Prueba que la suma de dos números funciona correctamente
        """
        self.calculadora.press_key("1")
        self.calculadora.press_key("+")
        self.calculadora.press_key("2")
        self.calculadora.press_key("=")
        self.assertEqual(self.calculadora.display.get(), "3")

    def test_resta(self) -> None:
        """ test_resta
        Prueba que la resta de dos números funciona correctamente
        """
        self.calculadora.press_key("5")
        self.calculadora.press_key("-")
        self.calculadora.press_key("3")
        self.calculadora.press_key("=")
        self.assertEqual(self.calculadora.display.get(), "2")

    def test_multiplicacion(self) -> None:
        """ test_multiplicacion
        Prueba que la multiplicación de dos números funciona correctamente
        """
        self.calculadora.press_key("4")
        self.calculadora.press_key("*")
        self.calculadora.press_key("3")
        self.calculadora.press_key("=")
        self.assertEqual(self.calculadora.display.get(), "12")

    def test_division(self) -> None:
        """ test_division
        Prueba que la división de dos números funciona correctamente
        """
        self.calculadora.press_key("8")
        self.calculadora.press_key("/")
        self.calculadora.press_key("2")
        self.calculadora.press_key("=")
        self.assertEqual(self.calculadora.display.get(), "4.0")

    def test_division_por_cero(self) -> None:
        """ test_division_por_cero
        Prueba que la calculadora muestra un mensaje de error al dividir por cero
        """
        self.calculadora.press_key("5")
        self.calculadora.press_key("/")
        self.calculadora.press_key("0")
        self.calculadora.press_key("=")
        self.assertEqual(self.calculadora.display.get(), "Error")

    def test_borrado_pantalla(self) -> None:
        """ test_borrado_pantalla
        Prueba que el botón "C" borra correctamente la pantalla
        """
        self.calculadora.press_key("1")
        self.calculadora.press_key("2")
        self.calculadora.press_key("3")
        self.calculadora.press_key("C")
        self.assertEqual(self.calculadora.display.get(), "")


if __name__ == '__main__':
    unittest.main()
