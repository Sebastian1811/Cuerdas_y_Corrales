from random import randint 

class cuadrado:
    coordenadas = []
    CoordenadaInicial = 0
    Lineas = []
    jugador = 0
    completo = 0
    Arriba = 0
    Abajo = 0
    Derecha = 0
    Izquierda = 0
    Puntaje = 0

    def __init__(self,x,y):
        self.coordenadas = [(x,y),(x+1,y),(x,y+1),(x+1,y+1)]
        self.Arriba = False
        self.Derecha = False
        self.Abajo = False
        self.Izquierda = False
        
        self.completo = False
        self.jugador = None
        self.Puntaje = randint(1, 5)

        self.CoordenadaInicial = (x, y)
        self.LineaArriba = (self.coordenadas[0], self.coordenadas[1])

        self.LineaDerecha = (self.coordenadas[1], self.coordenadas[3])
        
        self.LineaAbajo = (self.coordenadas[2],  self.coordenadas[3])
        
        self.LineaIzquierda = (self.coordenadas[0],  self.coordenadas[2])
        
        self.lineas = ([self.LineaArriba, self.LineaDerecha, self.LineaAbajo, self.LineaIzquierda])

    def conectarPuntos(self, coordenadas):
        linea = coordenadas # coordenadas de los puntos a conectar
        conectado = 0 #Estan conectados las coordenadas?

        if linea in self.lineas:
            if linea == self.LineaArriba and self.Arriba is False:
                self.Arriba = True
                conectado = True
            elif linea == self.LineaDerecha and self.Derecha is False:
                self.Derecha = True
                conectado = True
            elif linea == self.LineaAbajo and self.Abajo is False:
                self.Abajo = True
                conectado = True
            elif linea == self.LineaIzquierda and self.Izquierda is False:
                self.Izquierda = True
                conectado = True
                
        if self.Arriba is True and self.Derecha is True and self.Abajo is True and self.Izquierda is True:
            self.completo = True
        return conectado


