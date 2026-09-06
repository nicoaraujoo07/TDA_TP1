import unittest
from random import randint
from solucion import solucion

class TestJuegoMonedas(unittest.TestCase):

    def test_sofia_gana_caso_aleatorio(self):
        """Prueba que en casos aleatorios Sofia siempre obtenga un puntaje mayor o igual."""
        for _ in range(1000):
            monedas = [randint(1, 1000) for _ in range(10)]
            mon_s, mon_m = solucion(monedas)
            
            self.assertGreaterEqual(sum(mon_s), sum(mon_m), f"Mateo supero a Sofia con: {monedas}")

    def test_casos_limite(self):
        """Prueba escenarios específicos controlados (casos borde)."""
        # Caso 1: Todas las monedas iguales
        mon_s, mon_m = solucion([5, 5, 5, 5])
        self.assertEqual(sum(mon_s), 10)
        self.assertEqual(sum(mon_m), 10)

        # Caso 2: Lista vacia
        mon_s, mon_m = solucion([])
        self.assertEqual(mon_s, [])
        self.assertEqual(mon_m, [])

        # Caso 3: Una sola moneda
        mon_s, mon_m = solucion([10])
        self.assertEqual(mon_s, [10])
        self.assertEqual(mon_m, [])

if __name__ == "__main__":
    unittest.main()
