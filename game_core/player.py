import pygame
from game_core.setting import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,40))
        self.board = pygame.Surface((50,10))
        self.board.fill(BLACK)
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect_2 = self.board.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        #
        self.acceleration = 9.8 #加速度
        self.velocity_y = 0
        self.hight = 10.0
        self.time_interval = 1 / FPS
        self.state ="NONE" # BEGIN JUMP-UP JUMP-DOWN

    def update(self, command):
        print(command)
        # TODO 1 change state
        if command == "Jump":
            self.state = "Jump"
        else:
            self.state = "None"
        # TODO 2 detect state to jump
        self.move(command)
        self.keep_in_screen()
        self.jump()
        self.velocity_y = self.velocity_y + self.acceleration * self.time_interval
        self.rect.y = self.rect.y+self.velocity_y
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
    def jump(self):
        if self.state == "Jump":
            self.velocity_y = -10
         












