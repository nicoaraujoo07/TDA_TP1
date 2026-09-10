from algoritmo import solucion
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: ./tp1 path/entrada.txt")
        return
    
    path_entrada = sys.argv[1]

    with open(path_entrada, 'r') as f:
        f.readline()  # salteo la primer línea (comentario)
        monedas = list(map(int, f.readline().strip().split(";")))

    monedas_sophia, _ = solucion(monedas)
    ganancia = sum(monedas_sophia)

    print("Ganancia: " + str(ganancia))


if __name__ == "__main__":
    main()