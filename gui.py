import sys, pygame
from juego import *




class gui:
    pygame.init()
    size = width, height = 678, 1000
    white = 255, 255, 255
    red = 255, 0 , 0
    screen = pygame.display.set_mode((size))
    pygame.display.set_caption("Cuerdas o Corrales ")
    morty = pygame.image.load("img/morty.png")
    morty = pygame.transform.scale(morty, (100, 100))
    robot = pygame.image.load("img/robot.png")
    robot = pygame.transform.scale(robot,(100,100))
    portal = pygame.image.load("img/portal.png")
    portal = pygame.transform.scale(portal,(80,80))
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
                print(self.cuadros[i][j].LineaArriba)
                print(self.cuadros[i][j].Puntaje)
                print(self.cuadros[i][j].LineaAbajo)
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
         

    def pintarmapa(self):

        print(len(self.matrizJuego))
        x=0
        y=0
        for i in range(len(self.matrizJuego)):
            a=i+1
            if (a % 2) !=0:
                for j in range(len(self.matrizJuego)):
                    b = j+1
                    if(b % 2) !=0:
                        self.screen.blit(self.portal,[x+10,y+10])
                        x+=96
                    else:
                        pygame.draw.rect(self.screen,self.white,[x,y,95,95],0)
                        x+=96 
            else:
                for z in range(len(self.matrizJuego)):
                    c = z+1
                    if(c % 2) !=0:
                        pygame.draw.rect(self.screen,self.white,[x,y,95,95],0)
                        x+=96
                    else:
                        """F=96
                        C=96
                        for i in range(0,2):
                            C=C+96
                            for j in range(0,2):
                              self.screen.blit(str(self.cuadros[i][j].Puntaje),(F,C))
                              F=F+96  """ 
                        pygame.draw.rect(self.screen,self.red,[x,y,95,95],0)
                        x+=96                
            x=0
            y+=96


    def interfaz(self):
        self.pintarmapa()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            if self.count:
                #self.setTablero(5,5)
                self.count+=1      
            self.screen.blit(self.morty,(580,720))
            self.screen.blit(self.robot,(580,880))
            pygame.display.flip()



gu = gui()
gu.setTablero(4,4)
gu.interfaz()
"""print(gu.coordenadas)
print(gu.puntajes)"""



"""for fila in range(len(self.matrizJuego)):
            for  columna in range(len(self.matrizJuego[fila])):
                if self.matrizJuego[fila][columna] == 0:
                    pygame.draw.rect(self.screen,self.white,[x,y,95,95],0)
                    x+=96
                if self.matrizJuego[fila+1][columna+1] == 0:
                    self.screen.blit(self.portal,[x+10,y+10])
                    x+=96""" 