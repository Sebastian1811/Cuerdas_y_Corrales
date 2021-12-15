import sys, pygame
from juego import *




class gui:
    pygame.init()
    size = width, height = 1000, 678
    white = 255, 255, 255
    red = 255, 0 , 0
    input_box = pygame.Rect(700, 200, 140, 32)
    coloron =pygame.Color('lightskyblue3')
    coloroff = pygame.Color('gray15')
    color = coloroff
    active = False
    screen = pygame.display.set_mode((size))
    Fuente = pygame.font.Font(None,80)
    font = pygame.font.Font(None,25)
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
    userText = ''
    def setTablero(self,filas,columnas):
        self.tablero = juego(filas,columnas,10)
        self.cuadros = self.tablero.tablero.cuadradosPosibles
        self.setMatrizJuego(7,7)
        
        for i in range(filas):
            for j in range(columnas):
                self.coordenadas.append(self.cuadros[i][j].CoordenadaInicial)
                self.puntajes.append(self.cuadros[i][j].Puntaje)

    def setMatrizJuego(self,filas,columnas):
        ancho = []
        for i in range(filas): # rellenar una matriz #filas * #columnas de cuadros
            for j in range(columnas):
                ancho.append(0)
            self.matrizJuego.append(ancho)
            ancho = [] 
         

    def pintarmapa(self):
        x=0
        y=0
        F=130
        C=120
        for i in range(len(self.matrizJuego)):
            a=i+1
            m=0
            if (a % 2) !=0:
                for j in range(len(self.matrizJuego)):
                    b = j+1
                    if(b % 2) !=0:
                        self.screen.blit(self.portal,[x+5,y+5])
                        x+=96
                    else:
                        pygame.draw.rect(self.screen,self.white,[x,y,95,95],0)
                        x+=96 
            else:
                d=0
                for k in range(len(self.matrizJuego)):
                    c = k+1
                    if(c % 2) !=0:
                        pygame.draw.rect(self.screen,self.white,[x,y,95,95],0)
                        x+=96
                    else:
                        pygame.draw.rect(self.screen,self.red,[x,y,95,95],0)
                        x+=96
                        numero = self.Fuente.render(str(self.cuadros[m][d].Puntaje),True,(255,200,200))
                        self.screen.blit(numero,[F,C])
                        d += 1
                        F+=192
                C+=192
                F=130   
                m+=1
            x=0
            y+=96

    def interfaz(self):
        self.pintarmapa()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.active = True    
                    else:
                        self.active =  False 
                if event.type == pygame.KEYDOWN:
                # If the user clicked on the input_box rect.
                    if self.active:
                        if event.key==pygame.K_BACKSPACE:
                        # Toggle the active variable.
                            self.userText = self.userText[:-1]
                        else:
                            self.userText += event.unicode  
            if self.active:
                self.color = self.coloron
            else:
                self.color = self.coloroff    
            pygame.draw.rect(self.screen,self.color,self.input_box)   
            text_surface = self.font.render(self.userText, True, (255,255,255))
            self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))
            self.input_box.w = max(100,text_surface.get_width()+ 10)
            self.screen.blit(self.morty,(880,150))
            self.screen.blit(self.robot,(880,250))
            pygame.display.flip()

#ayudaaaaaaaaaaaaaa

gu = gui()
gu.setTablero(4,4)
gu.interfaz()
