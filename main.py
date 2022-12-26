import pygame, sys
from pygame.locals import *
from colors import *
from enemy import Enemy
from player import Player
from screen import FPS, SCREEN_WIDTH, SCREEN_HEIGHT

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = 0, 0
        self._image_surf = None

    def on_init(self):
        pygame.init()
        self._running = True
        self._display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._display_surf.fill(WHITE)
        pygame.display.set_caption("Game")

    def on_execute(self):
        inc_speed = pygame.USEREVENT + 1
        pygame.time.set_timer(inc_speed, 1000)

        if self.on_init() == False:
            self._running = False

        while (self._running):
            GameClock = pygame.time.Clock()

            player = Player()
            enemy1 = Enemy()

            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            all_sprites.add(enemy1)
            
            enemies = pygame.sprite.Group()
            enemies.add(enemy1)

            speed = 0

            # Game loop
            while True:
                for event in pygame.event.get():
                    if event.type == inc_speed:
                        speed += 2
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                player.update()
                enemy1.move()

                self._display_surf.fill(WHITE)
                player.draw(self._display_surf)
                enemy1.draw(self._display_surf)

                pygame.display.update()
                GameClock.tick(FPS)

if __name__ == "__main__":
    app = App()
    app.on_execute()
