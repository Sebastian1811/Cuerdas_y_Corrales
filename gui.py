import sys, pygame



pygame.init()
size = width, height = 900, 900
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Cuerdas o Corrales ")
morty = pygame.image.load("img/morty.png")
morty = pygame.transform.scale(morty, (100, 100))
robot = pygame.image.load("img/robot.png")
robot = pygame.transform.scale(robot,(100,100))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.blit(morty,(750,650))
    screen.blit(robot,(750,780))
    pygame.display.update()

