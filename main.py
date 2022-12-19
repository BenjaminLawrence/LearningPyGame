import pygame, sys
from pygame.locals import *

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

DISPLAYSURF = pygame.display.set_mode((300, 300))

BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
GREY = pygame.Color(128, 128, 128)
RED = pygame.Color(255, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
