from copy import deepcopy
import jugadorMin
from tablero import *

class juego:

    jugadamin = 0
    jugadamax = 0
    def __init__(self, filas, columnas, profundidadArbol):
        self.profundidadarbol = profundidadArbol
        self.tablero = Tablero(filas, columnas)

    def jugar(self):
        
        print("Cuerdas y corrales")
        while len(self.tablero.PosiblesJugadas) > 0:
            print("Ejemplo de jugada == x,y,x2,y2")
            print("presiona 0 para terminar el juego")

            self.tablero.displaytablero()

            jugadaValida = jugadorMin.jugar(self.tablero)
            if not jugadaValida :
                break
            else:
                self.jugadamin = jugadaValida

            print("\nEspera a jugador MAX \n")
            self.jugadamax = self.jugadorMax()
        self.ganador()

    def jugadorMax(self):
        
        tableroCopia = deepcopy(self.tablero)
        PosiblesJugadas = deepcopy(self.tablero.PosiblesJugadas)

        coordenadas = self.minimax(tableroCopia, PosiblesJugadas, self.profundidadarbol, True)
        self.tablero.jugada(coordenadas[1], 1)
        return coordenadas[1]

    def minimax(self, tableroActual, PosiblesJugadas, profundidadarbol, min_max):
        
        if min_max :
            valorNodo = (-1000000, None)
        else:
            valorNodo = (1000000, None)

        if profundidadarbol == 0 or len(PosiblesJugadas) == 0:
            heuristica = self.funcionHeuristica(tableroActual)
            return (heuristica, None)

        
        for i in range(0, len(PosiblesJugadas)):
           
            jugada = PosiblesJugadas.pop()
           
            tableroActualCopia = deepcopy(tableroActual)
            PosiblesJugadasCopy = deepcopy(PosiblesJugadas)
            tableroActualCopia.jugada(jugada, min_max)

            PosiblesJugadas.appendleft(jugada)

            heuristica = self.funcionHeuristica(tableroActualCopia)
            if min_max :
                if heuristica >= tableroActualCopia.valorMin:
                    return (heuristica, jugada)
                else:
                    tableroActualCopia.valorMax = max(tableroActualCopia.valorMax, heuristica)
            else:
                if heuristica <= tableroActualCopia.valorMax:
                    return (heuristica, jugada)
                else:
                    tableroActualCopia.beta = min(tableroActualCopia.valorMin, heuristica)

            
            proximoMovimiento = self.minimax(tableroActualCopia, PosiblesJugadasCopy, profundidadarbol - 1, not min_max)

            
            if min_max :
                
                if proximoMovimiento[0] > valorNodo[0]:
                    valorNodo = (proximoMovimiento[0], jugada)
            else:

                if proximoMovimiento[0] < valorNodo[0]:
                    valorNodo = (proximoMovimiento[0], jugada)
        return valorNodo

    def funcionHeuristica(self, tableroActual):
        heuristica = tableroActual.puntajeJugadorMax - tableroActual.puntajeJugadorMin
        return heuristica

    def ganador(self):
        
        self.tablero.displaytablero()
        if self.tablero.puntajeJugadorMin > self.tablero.puntajeJugadorMax:
            print("gana Jugador Min")
        elif self.tablero.puntajeJugadorMin < self.tablero.puntajeJugadorMax:
            print("gana Jugador Max")
        else:
            print("Empate!")
        print("JugadorMinPuntaje: %s" % self.tablero.puntajeJugadorMin)
        print("JugadorMaxPuntaje: %s" % self.tablero.puntajeJugadorMax)
        print("\nFin del juego")