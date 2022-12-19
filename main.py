import pygame, sys
from pygame.locals import *
import colors
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(colors.WHITE)
pygame.display.set_caption("Game")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
