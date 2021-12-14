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
    tablero = None
    def setTablero(self,filas,columnas):
        self.tablero = juego(filas,columnas,10)

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

