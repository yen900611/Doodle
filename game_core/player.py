import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.state = None

    def update(self, command):
        self.move(command)
        self.keep_in_screen()
        self.jump()
        pass

    def move(self,direction):
        if move_right in direction:
            self.rect.x +=1
        if move_left in direction:
            self.rect.x -=1
            pass

    def keep_in_screen(self):
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0

    def draw(self):
        pass

    def jump(self):
        pass