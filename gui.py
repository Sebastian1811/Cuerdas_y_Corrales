import sys, pygame
from juego import *

class gui:
    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode((size))
    pygame.display.set_caption("Cuerdas o Corrales ")
    morty = pygame.image.load("img/morty.png")
    morty = pygame.transform.scale(morty, (100, 100))
    robot = pygame.image.load("img/robot.png")
    robot = pygame.transform.scale(robot,(100,100))
    count = 1
    cuadros = None
    tablero = None
    coordenadas = []
    matrizJuego= []
    puntajes = []

    def setTablero(self,filas,columnas):
        self.tablero = juego(filas,columnas,10)
        self.cuadros = self.tablero.tablero.cuadradosPosibles
        self.setMatrizJuego(7,7)
        
        for i in range(filas):
            for j in range(columnas):
                """print(self.cuadros[i][j].LineaArriba)
                print(self.cuadros[i][j].Puntaje)
                print(self.cuadros[i][j].LineaAbajo)"""
                self.coordenadas.append(self.cuadros[i][j].CoordenadaInicial)
                self.puntajes.append(self.cuadros[i][j].Puntaje)

                print()
        print(self.matrizJuego)    

    def setMatrizJuego(self,filas,columnas):
        ancho = []
        for i in range(filas): # rellenar una matriz #filas * #columnas de cuadros
            for j in range(columnas):
                ancho.append(0)
            self.matrizJuego.append(ancho)
            ancho = []  

    def interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            if self.count:
                self.setTablero(5,5)
                self.count+=1        
            self.screen.blit(self.morty,(750,650))
            self.screen.blit(self.robot,(750,780))
            pygame.display.update()

gu = gui()

gu.setTablero(4,4)
print(gu.coordenadas)
print(gu.puntajes)