import pygame, sys
from pygame.locals import *

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

DISPLAYSURF = pygame.display.set_mode((300, 300))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
