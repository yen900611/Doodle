import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.state = None

    def update(self, command):
        self.move(command)
        self.keep_in_screen()
        pass

    def move(self,direction):
        if direction == move_right:
            self.rect.x +=1
        elif direction == move_left:
            self.rect.x -=1
        else:
            pass

    def keep_in_screen(self):
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0

    def draw(self):
        pass