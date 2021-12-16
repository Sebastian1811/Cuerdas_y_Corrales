from cuadrado import *
from collections import deque

class Tablero:

    puntajeJugadorMin = 0
    puntajeJugadorMax = 0
    columnas = 0
    filas = 0
    cuadradosPosibles = 0
    PosiblesJugadas = 0 # una jugada posible es una tupla de coordenadas que se pueden unir
    JugadasHechas = 0

    def __init__(self,columnas,filas):
        self.puntajeJugadorMin = 0
        self.puntajeJugadorMax = 0

        self.filas = filas
        self.columnas = columnas

        self.cuadradosPosibles = self.llenarTablero(filas, columnas)

        self.PosiblesJugadas = self.generarJugadasPosibles(filas, columnas)
        self.JugadasHechas = set()

        self.valorMax = -100000
        self.valorMin = 100000
        
    def llenarTablero(self,columnas,filas):
        filas = filas
        columnas = columnas
        cuadrados = []
        ancho = []

        for i in range(filas): # rellenar una matriz #filas * #columnas de cuadros
            for j in range(columnas):
                ancho.append(cuadrado(0,0))
            cuadrados.append(ancho)
            ancho = []    

        for i in range(filas):
            for j in range(columnas):
                cuadrados[i][j] = cuadrado(i,j)    # setear atributos de cada cuadrado de la matriz respecto a sus coordenadas
        
        return cuadrados

    def generarJugadasPosibles(self,filas,columnas):
        jugadas = deque()
        for i in range(0, filas+1):
            for j in range(0, columnas):
                jugadas.append(((j, i), (j + 1, i)))
                if i < filas:
                    jugadas.append(((j, i), (j, i + 1)))
            if i < filas:
                jugadas.append(((columnas, i), (columnas, i + 1)))
        return jugadas

    def verficarCuadrados(self, coordenadas, player):

        for i in range(self.filas):
            for j in range(self.columnas):

                cuadrado = self.cuadradosPosibles[i][j]

                if coordenadas in cuadrado.lineas:
                    cuadrado.conectarPuntos(coordenadas)

                if cuadrado.completo and cuadrado.jugador is None:
                    cuadrado.jugador = player
                    self.prevComplete = True
                    if player == 0:
                        self.puntajeJugadorMin += cuadrado.Puntaje
                    elif player == 1:
                        self.puntajeJugadorMax += cuadrado.Puntaje    

    def jugada(self, coordenadas, player): 
        if player:
            player = 1
        else:
            player = 0
        if coordenadas in self.PosiblesJugadas:
            self.PosiblesJugadas.remove(coordenadas)
            self.JugadasHechas.add(coordenadas)
            self.verficarCuadrados(coordenadas, player)
            return 0
        else:
            return -1

if __name__ == '__main__':
    tablero = Tablero(4,4)
   
  
