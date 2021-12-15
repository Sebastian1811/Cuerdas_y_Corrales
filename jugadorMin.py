from tablero import *

def jugar(tablero,minplay):
    while True:
        try:
            integers = list(map(int,minplay.split()))
            if integers == 0:
                return False
            coordenadas = ((integers[0], integers[1]), (integers[2], integers[3]))

            jugadaValidad = tablero.jugada(coordenadas, 0)

            if jugadaValidad == 0:
                return coordenadas
                # break
            elif jugadaValidad == -1:
                return 0#print("coordenadas invalidas!")
        except SyntaxError:
            print("Intenta de nuevo que te equivocaste")
    return True