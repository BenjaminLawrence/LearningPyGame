import pygame, sys
from pygame.locals import *

pygame.init()

# Game loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
