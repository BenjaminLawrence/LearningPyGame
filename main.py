import pygame, sys
from pygame.locals import *
from colors import *
from enemy import Enemy
from player import Player
from screen import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

player = Player()
enemy1 = Enemy()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    player.update()
    enemy1.move()

    DISPLAYSURF.fill(WHITE)
    player.draw(DISPLAYSURF)
    enemy1.draw(DISPLAYSURF)

    pygame.display.update()
