import sys, pygame
from juego import *
class gui:
    pygame.init()
    size = width, height = 1000, 678
    white = 255, 255, 255
    red = 255, 0 , 0
    input_box = pygame.Rect(840, 380, 140, 32)
    coloron =pygame.Color('lightskyblue3')
    coloroff = pygame.Color('gray15')
    color = coloroff
    active = False
    screen = pygame.display.set_mode((size))
    Fuente = pygame.font.Font(None,80)
    fuente = pygame.font.Font(None,30)
    font = pygame.font.Font(None,25)
    pygame.display.set_caption("Cuerdas y Corrales ")
    morty = pygame.image.load("img/morty.png")
    morty = pygame.transform.scale(morty, (100, 100))
    robot = pygame.image.load("img/robot.png")
    robot = pygame.transform.scale(robot,(100,100))
    portal = pygame.image.load("img/portal.png")
    portal = pygame.transform.scale(portal,(80,80))
    player1 = pygame.image.load("img/player1.png")
    player1 = pygame.transform.scale(player1, (90, 90))
    player2 = pygame.image.load("img/player2.jpg")
    player2 = pygame.transform.scale(player2, (90, 90))
    count = 1
    cuadros = None
    tablero = None
    coordenadas = []
    gameMatrix = [[6,0,6,0,6,0,6],[0,-1,0,-1,0,-1,0],
                 [6,0,6,0,6,0,6],[0,-1,0,-1,0,-1,0],
                 [6,0,6,0,6,0,6],[0,-1,0,-1,0,-1,0],[6,0,6,0,6,0,6]]
    puntajes = []
    ia_score = '0'
    morty_score = '0'
    userText = ''
    iniciar = 0
    pausa = 1
    detenido = 0
    warning = None
    jugadaMin =None
    jugadaMax = None

    def setTablero(self,filas,columnas):
        self.tablero = juego(filas,columnas,10)
        self.cuadros = self.tablero.tablero.cuadradosPosibles
        for i in range(filas):
            for j in range(columnas):
                self.coordenadas.append(self.cuadros[i][j].CoordenadaInicial)
                self.puntajes.append(self.cuadros[i][j].Puntaje)

    def paint(self):
        x = 0
        y = 0
        x1=96
        y1=96
        factor = 3
        factorY = 3
        count = 0
        self.setScore()
        for i in range(7):
            for j in range(7):
                if self.gameMatrix[i][j] == 6:
                    self.screen.blit(self.portal,[x+5,y+5])
                elif self.gameMatrix[i][j] == 0:
                    pygame.draw.rect(self.screen,self.white,[x,y,95,95])   
                elif self.gameMatrix[i][j] <= 5 and self.gameMatrix[i][j] >=1:
                    numero = self.Fuente.render(str(self.gameMatrix[j][i]),True,(255,200,200)) 
                    pygame.draw.rect(self.screen,self.red,[y,x,95,95])  
                    self.screen.blit(numero,[y1,x1])
                    count += 1
                    x1 = 96*factor
                    if factor < 5:
                        factor +=2 
                    if count == 3:
                        y1 =96*factorY
                        count = 0
                        x1 = 96
                        factor = 3
                        if factorY < 5:
                            factorY +=2
                elif self.gameMatrix[i][j] == 9:
                    self.screen.blit(self.player1,[x+5,y+5])
                elif self.gameMatrix[i][j] == 10:
                    self.screen.blit(self.player2,[x+5,y+5])
                x += 96
            x = 0    
            y +=96
         
    def setScore(self):
        count = 0
        for i in range(7):
            for j in range(7):
                if self.gameMatrix[j][i] == -1:
                    self.gameMatrix[j][i] = self.puntajes[count]
                    count +=1           
    def jugar(self):
        if self.iniciar and  not self.pausa:
            #self.tablero.tablero.displaytablero()
            jugadaValida = jugadorMin.jugar(self.tablero.tablero,self.userText)
            if not jugadaValida :
                self.pausa = 1
                self.detenido = 1
                self.warning = self.fuente.render("¡¡¡JUGADA INVALIDA!!!",0,(255,0,0))
                self.screen.blit(self.warning,(700, 440))
                return 0
            else:
                self.screen.fill((0,0,0))
                self.jugadaMin  = jugadaValida
                self.convertirCoordenadas(1)
                self.morty_score =str(self.tablero.tablero.puntajeJugadorMin)

            self.jugadaMax = self.tablero.jugadorMax()
            self.convertirCoordenadas(0)
            self.ia_score = str(self.tablero.tablero.puntajeJugadorMax)
            #self.tablero.tablero.displaytablero()
            self.pausa = 1
            if len(self.tablero.tablero.PosiblesJugadas) == 0:
                condicion = self.tablero.ganador()
                if condicion == 1:
                    msj = self.font.render("GANA MORTY!!!!",0,(0,255,0))
                    self.screen.blit(msj,(780,550))
                elif  condicion == 0:   
                    msj = self.font.render("GANA ROBOT MANTEQUILLA!!!!",0,(0,255,0))
                    self.screen.blit(msj,(700,550)) 
                elif condicion == -1:
                    msj = self.font.render("EMPATE!!!!",0,(0,255,0))
                    self.screen.blit(msj,(780,550))    

    def convertirCoordenadas(self,player):
        convertY2 = 0
        convertX2 = 0
        convertX =0
        convertY =0
        if player:
            if self.jugadaMin[0] == (0,0):
                convertX = 0
                convertY = 0
            elif self.jugadaMin[0][1] == 0 and self.jugadaMin[0][0] !=0:
                convertX = 0 
                convertY = self.jugadaMin[0][0]*2
            elif self.jugadaMin[0][1] != 0 and self.jugadaMin[0][0] ==0:
                convertX =  (self.jugadaMin[0][1]*2 ) 
                convertY = 0 
            else:
                convertY = self.jugadaMin[0][0] *2
                convertX = self.jugadaMin[0][1] *2
                
            if self.jugadaMin[1] == (0,0):
                convertX2 = 0
                convertY2 = 0
            elif  self.jugadaMin[1][1] == 0 and self.jugadaMin[1][0] != 0:
                convertX2 = self.jugadaMin[1][1]*2
                convertY2 = 0

            elif self.jugadaMin[1][1] != 0 and self.jugadaMin[1][0] ==0:
                convertX2 =  (self.jugadaMin[1][1]*2 ) 
                convertY2 = 0 
            else:
                convertY2 = self.jugadaMin[1][0] *2
                convertX2 = self.jugadaMin[1][1] *2
            if self.Ishorizontal(convertX,convertX2):
                self.gameMatrix[convertX][convertY+1] = 9
            elif self.Isvertical(convertY,convertY2):
                self.gameMatrix[convertX+1][convertY] = 9   
        else:
            if self.jugadaMax[0] == (0,0):
                convertX = 0
                convertY = 0
            elif self.jugadaMax[0][1] == 0 and self.jugadaMax[0][0] !=0:
                convertX = 0
                convertY =self.jugadaMax[0][0]*2
            elif self.jugadaMax[0][1] != 0 and self.jugadaMax[0][0] ==0:
                convertX =  (self.jugadaMax[0][1]*2 ) 
                convertY = 0 
            else:
                convertY = self.jugadaMax[0][0] *2
                convertX = self.jugadaMax[0][1] *2
            if self.jugadaMax[1] == (0,0):
                convertX2 = 0
                convertY2 = 0
            elif  self.jugadaMax[1][1] == 0 and self.jugadaMax[1][0] != 0:
                convertX2 = self.jugadaMax[1][1]*2
                convertY2 = 0
            elif self.jugadaMax[1][1] != 0 and self.jugadaMax[1][0] ==0:
                convertX2 =  (self.jugadaMax[1][1]*2 ) 
                convertY2 = 0 
            else:
                convertY2 = self.jugadaMax[1][0] *2
                convertX2 = self.jugadaMax[1][1] *2
            if self.Ishorizontal(convertX,convertX2):
                self.gameMatrix[convertX][convertY+1] = 10
            elif self.Isvertical(convertY,convertY2):
                self.gameMatrix[convertX+1][convertY] = 10   
               
    def Ishorizontal(self,x,x1):
        if x1 - x == 0:
            return 1
        else: 
            return 0    
    def Isvertical(self,y,y1):
        if y1 - y == 0:
            return 1
        else:
            return 0           
        
    def interfaz(self):
        while True:
            self.paint()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.active = True    
                    else:
                        self.active =  False 
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key==pygame.K_BACKSPACE:
                            self.userText = self.userText[:-1]
                        else:
                            self.userText += event.unicode  
                        if event.key == pygame.K_RETURN:
                            self.userText = self.userText[:-1]
                            self.active = 0
                            self.iniciar = 1
                            self.pausa = 0
            if self.active:
                self.color = self.coloron
            else:
                self.color = self.coloroff    
            pygame.draw.rect(self.screen,self.color,self.input_box)   
            text_surface = self.font.render(self.userText, True, (255,255,255))
            scoreIa = self.font.render("Score: "+self.ia_score,0,(255,0,0))
            scoremorty = self.font.render("Score: "+self.morty_score,0,(0,0,255))
            jugada = self.font.render("Jugada: ",0,(0,0,255))
            self.screen.blit(jugada,(770,390))
            self.screen.blit(scoreIa,(780,140))
            self.screen.blit(scoremorty,(780,285))
            instrucciones = self.font.render("Ejemplo de jugada == x y x2 y2",0,self.coloron)
            self.screen.blit(instrucciones,(720, 40))
            self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))
            self.input_box.w = max(100,text_surface.get_width()+ 10)
            self.screen.blit(self.morty,(880,250))
            self.screen.blit(self.robot,(880,100))
            self.jugar()
            pygame.display.flip()
            
