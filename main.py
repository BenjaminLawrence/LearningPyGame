import pygame, sys, time
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
        if self.on_init() == False:
            self._running = False

        while (self._running):
            GameClock = pygame.time.Clock()

            inc_speed = pygame.USEREVENT + 1
            pygame.time.set_timer(inc_speed, 1000)

            player = Player()
            enemy1 = Enemy()

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

                self._display_surf.fill(WHITE)

                player.draw(self._display_surf)
                player.move()
                
                for entity in enemies:
                    entity.draw(self._display_surf)
                    entity.move(speed)

                if pygame.sprite.spritecollideany(player, enemies):
                    self._display_surf.fill(RED)
                    pygame.display.update()
                    player.kill()
                    for entity in enemies:
                        entity.kill()
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()

                pygame.display.update()
                GameClock.tick(FPS)

if __name__ == "__main__":
    app = App()
    app.on_execute()
