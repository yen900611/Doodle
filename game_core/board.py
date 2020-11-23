import pygame
import random
from setting import *

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((70,20))
        # self.image.fill(YELLOW)
        self.image = pygame.image.load(path.join(IMAGE_DIR, "cloud.png"))
        self.image = pygame.transform.scale(self.image, (random.randint(70,200), 25))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self, *args, **kwargs) -> None:
        self.kill_board()

    def kill_board(self):#自己的事在自己家做
        if self.rect.top > 550:
            # print(":3")
            # for self.rect in range:
                self.kill()