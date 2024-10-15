import unittest
from unittest import TestCase
from src.logic.Conjunto import Conjunto
class TestConjunto(TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())


if __name__ == '__main__':
    unittest.main()