import unittest
from unittest import TestCase
from src.logic.Conjunto import Conjunto
class TestConjunto(TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())
if __name__ == '__main__':
    unittest.main()