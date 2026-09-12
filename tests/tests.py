import unittest
import subprocess
import re
from pathlib import Path


class TestJuegoMonedas(unittest.TestCase):

    ARCHIVOS = [
        "20.txt",
        "25.txt",
        "50.txt",
        "100.txt",
        "1000.txt",
        "10000.txt",
        "20000.txt",
        "100000.txt",
        "10000000.txt"
    ]

    BASE = Path(__file__).resolve().parent

    def obtener_resultados_esperados(self):
        """
        Lee resultados.txt y obtiene la ganancia de Sophia
        correspondiente a cada archivo.
        """
        resultados = {}
        archivo_actual = None

        ruta_resultados = self.BASE / "ejemplos" /"resultados.txt"

        with open(ruta_resultados, "r") as f:
            for linea in f:
                linea = linea.strip()

                match_archivo = re.match(r"(\d+\.txt)", linea)

                if match_archivo:
                    archivo_actual = match_archivo.group(1)
                    continue

                match_ganancia = re.fullmatch(
                    r"Ganancia de Sophia:\s*(\d+)",
                    linea
                )

                if match_ganancia and archivo_actual:
                    resultados[archivo_actual] = int(match_ganancia.group(1))

        return resultados

    def test_archivos(self):
        resultados_esperados = self.obtener_resultados_esperados()

        tp1 = self.BASE.parent / "tp1.py"

        for archivo in self.ARCHIVOS:
            with self.subTest(archivo=archivo):

                archivo_entrada = self.BASE / "ejemplos" / archivo


                self.assertIn(
                    archivo,
                    resultados_esperados,
                    f"No se encontró un resultado para {archivo} en resultados.txt"
                )

                esperado = resultados_esperados[archivo]

                resultado = subprocess.run(
                    ["python3", str(tp1), str(archivo_entrada)],
                    capture_output=True,
                    text=True
                )

                self.assertEqual(
                    resultado.returncode,
                    0,
                    f"tp1.py falló con {archivo}:\n{resultado.stderr}"
                )

                salida = resultado.stdout.strip()

                match = re.fullmatch(
                    r"Ganancia:\s*(\d+)",
                    salida
                )

                self.assertIsNotNone(
                    match,
                    f"Salida inesperada para {archivo}: {salida}"
                )

                ganancia_obtenida = int(match.group(1))

                self.assertEqual(
                    ganancia_obtenida,
                    esperado,
                    f"""
Resultado incorrecto para {archivo}:
Esperado: {esperado}
Obtenido: {ganancia_obtenida}
"""
                )


if __name__ == "__main__":
    unittest.main()
