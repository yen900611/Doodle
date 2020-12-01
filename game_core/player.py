import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,40))
        self.image = pygame.image.load(path.join(IMAGE_DIR, "player.png"))
        self.image = pygame.transform.scale(self.image, (90, 90))
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.acceleration = 9.8 #加速度
        self.velocity_y = 0
        self.height = 0
        self.time_interval = 1 / FPS
        self.state ="START" # BEGIN JUMP-UP JUMP-DOWN

    def update(self, command):
        # TODO 1 change state
        if "Jump" in command and (self.state == "START" or "NONE"):
            self.jump()

        if self.state == "Jump" and self.velocity_y > 0:
            self.state = "Down"

        self.move(command)
        self.keep_in_screen()
        self.velocity_y = self.velocity_y + self.acceleration * self.time_interval
        self.rect.y = self.rect.y+self.velocity_y
        if self.rect.y >= HEIGHT-100 and self.state == "START":
            self.velocity_y = 0
            self.rect.y = HEIGHT-100
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
        self.state = "Jump"
        self.velocity_y = -10
        # self.acceleration = 9.8
