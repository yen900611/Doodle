import pygame
from player import Player
from setting import *
import random

class PlayingMode():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        '''set group'''
        self.all_sprite = pygame.sprite.Group()
        self.player = Player(WIDTH/2,HEIGHT-50)
        self.all_sprite.add(self.player)
        pass


    def update(self,command):
        self.player.update(command)
        return self.all_sprite
        pass


    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def handle_event(self,is_close:bool):
        if is_close:
            self.running = False


    '''碰撞'''

    # TODO
    # 解碼Function放在update裡面-->規定command的格式

