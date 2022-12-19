import pygame, sys
from pygame.locals import *

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

DISPLAYSURF = pygame.display.set_mode((300, 300))

colorBlack = pygame.Color(0, 0, 0)
colorWhite = pygame.Color(255, 255, 255)
colorGrey = pygame.Color(128, 128, 128)
colorRed = pygame.Color(255, 0, 0)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
