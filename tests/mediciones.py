import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



archivos = [
    "20.txt",
    "25.txt",
    "50.txt",
    "100.txt",
    "500.txt",
    "1000.txt",
    "5000.txt",
    "10000.txt",
    "20000.txt",
    "50000.txt",
    "100000.txt",
    "200000.txt",
    "500000.txt",
    "1000000.txt",
    "2000000.txt",
    "5000000.txt",
    "7500000.txt",
    "10000000.txt"
]

REPETICIONES = 5

def datos_mediciones():
        
    n = []
    tiempos = []

    BASE = Path(__file__).resolve().parent
    CARPETA_TP1 = BASE.parent


    for archivo in archivos:

        archivo_entrada = BASE / "ejemplos" /archivo
        tp1 = CARPETA_TP1 / "tp1.py"

        cantidad = int(archivo.replace(".txt", ""))

        mediciones = []

        for _ in range(REPETICIONES):

            inicio = time.perf_counter()

            resultado = subprocess.run( ["python3", str(tp1), str(archivo_entrada)], 
                                    capture_output=True,
                                        text=True ) 
            
            if resultado.returncode != 0: exit(1)

            fin = time.perf_counter()

            mediciones.append(fin - inicio)

        promedio = sum(mediciones) / len(mediciones)

        n.append(cantidad)
        tiempos.append(promedio)

    return n, tiempos


def mapear_datos(n, tiempos):
    # Matriz A para ajustar T(n) = c1*n + c2
    A = np.array([[x, 1] for x in n])

    # Cuadrados mínimos
    AtA = A.T @ A
    Atb = A.T @ tiempos

    c = np.linalg.inv(AtA) @ Atb

    c1 = c[0]
    c2 = c[1]

    print("c1 =", c1)
    print("c2 =", c2)

    # Valores predichos por el ajuste
    ajuste = A @ c

    # Error absoluto de cada medición
    errores = np.abs(np.array(tiempos) - ajuste)

    # Error cuadrático total
    error = np.linalg.norm(ajuste - tiempos) ** 2

    print("Error cuadrático total =", error)

    # Gráfico de mediciones y ajuste
    plt.plot(n, tiempos, marker="o", label="Mediciones")
    plt.plot(n, ajuste, "--", label="Ajuste lineal")


    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución del Algoritmo (TP1)")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Gráfico del error absoluto
    plt.plot(n, errores, marker="o")

    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Error absoluto (s)")
    plt.title("Error absoluto del ajuste lineal")
    plt.grid(True)
    plt.show()

def main():
    n, tiempos = datos_mediciones()

    mapear_datos(n, tiempos)


if __name__ == "__main__":
    main()