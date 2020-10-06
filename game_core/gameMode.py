import pygame
from game_core.setting import *


class GameMode(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def handle_event(self,is_close:bool):
        if is_close:
            self.running = False
