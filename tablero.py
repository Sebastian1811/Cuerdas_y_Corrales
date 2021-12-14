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

        # For alpha beta pruning
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

    def displaytablero(self):
        '''
        This function generates a text-based representation of the current board state
        to be displayed on the command line. The display is based on the row & column
        values stored on the board, along with the connectedVectors set objects, which
        stores previously connected dots.
        '''
        print("Player 1: %s" % self.puntajeJugadorMin)
        print("Player AI: %s" % self.puntajeJugadorMax)
        # Set X axis Labels
        str1 = "\n  "
        for i in range(self.filas + 1):
            str1 = str1 + "   %s" % i
        print(str1)

        # Draw remaining board
        boxVal = " "
        for i in range(self.filas + 1):
            # Append the Y axis label to the beginning of a row
            str1 = "%s " % i
            str2 = "     "
            for j in range(self.columnas + 1):
                #a = self.cuadradosPosibles[j][i - 1]
                #print(type(a))
                # Check for horizontal connections
                if ((j - 1, i), (j, i)) in self.JugadasHechas:
                    str1 = str1 + "---*"
                else:
                    str1 = str1 + "   *"

                # Check for the box value of a given square based on the top left coordinate
                if j < self.columnas:
                    #print(self.cuadradosPosibles[j][i - 1].CoordenadaInicial)
                    if self.cuadradosPosibles[j][i - 1].CoordenadaInicial == (j, i - 1):
                        boxVal = self.cuadradosPosibles[j][i - 1].Puntaje
                else:
                    boxVal = " "

                # Check for vertical connections
                if ((j, i - 1), (j, i)) in self.JugadasHechas:
                    str2 = str2 + "| %s " % boxVal
                else:
                    str2 = str2 + "  %s " % boxVal
            print(str2)
            print(str1)
        print("")

if __name__ == '__main__':
    tablero = Tablero(4,4)
    #tablero.displayBoard()
  
