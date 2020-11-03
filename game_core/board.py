import pygame
# import random
from setting import *

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((70,20))
        # self.image.fill(YELLOW)
        self.image = pygame.image.load(path.join(IMAGE_DIR, "cloud.png"))
        self.image = pygame.transform.scale(self.image, (70, 25))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        # self.board_number = 1
        self.speedY = 3

    def update(self):
        self.rect.centery += self.speedY
        #在這邊做kill跑出視窗的板子

