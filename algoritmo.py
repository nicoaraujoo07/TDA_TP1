def solucion(monedas):
    ini = 0
    fin = len(monedas) - 1
    mon_s = []
    mon_m = []
    turno = 0

    while ini <= fin:
        izq = monedas[ini]
        der = monedas[fin]
        if turno % 2 == 0:
            if izq > der:
                mon_s.append(izq)
                ini += 1
            else:
                mon_s.append(der)
                fin -= 1
        else:
            if izq < der:
                mon_m.append(izq)
                ini += 1
            else:
                mon_m.append(der)
                fin -= 1
        turno += 1
    return mon_s, mon_m