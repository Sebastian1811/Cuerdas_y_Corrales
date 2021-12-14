import sys, pygame
import time


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Cuerdas o Corrales")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    pygame.display.update()