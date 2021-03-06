import pygame
from setting import *

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMAGE_DIR, "cloud.png"))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.height = y
        self.rect.centerx = x

    def update(self, *args, **kwargs) -> None:
        self.kill_board()

    def kill_board(self):#自己的事在自己家做
        if self.rect.top > 550:
                self.kill()