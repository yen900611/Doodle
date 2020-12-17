import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,40))
        self.image = pygame.image.load(path.join(IMAGE_DIR, "player.png"))
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.acceleration = 9.8 #加速度
        self.velocity_y = 0
        self.height = y
        self.time_interval = 1 / FPS
        self.state ="START" # BEGIN JUMP-UP JUMP-DOWN

    def update(self, command, is_collide):
        # TODO 1 change state
        # if is_collide and "Jump" in command:
        if is_collide:
            self.jump()
        self.move(command)
        self.keep_in_screen()
        self.velocity_y = self.velocity_y + self.acceleration * self.time_interval
        self.rect.y = self.rect.y+self.velocity_y
        pass

    def move(self,direction):
        if move_right in direction:
            self.rect.x +=3
        if move_left in direction:
            self.rect.x -=3
            pass

    def keep_in_screen(self):
        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0

    def draw(self):
        pass

    def jump(self):
        self.velocity_y = -5
        # self.acceleration = 9.8
