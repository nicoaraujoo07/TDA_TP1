import random

N = 1_000_000

with open(f"{N}.txt", "w") as f:
    f.write("# Los valores de las monedas de la fila se muestran tal cual su orden correspondiente, separados por ;\n")

    for i in range(N):
        f.write(str(random.randint(1, 1000)))

        if i < N - 1:
            f.write(";")

    f.write("\n")

print("Archivo generado correctamente.")