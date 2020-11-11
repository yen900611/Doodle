import pygame
from player import Player
from setting import *

class PlayingMode():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprite = pygame.sprite.Group()
        self.player = Player(WIDTH/2,HEIGHT-50)
        self.all_sprite.add(self.player)
        self.address = "GameMode"
        pass

    def update(self,data):
        command = None
        if data["Address"] == self.address:
            command = data["Data"]
        self.player.update(command)
        return {"Address":"GameView",
                "Type":type(self.all_sprite),
                "Data":self.all_sprite}

    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def handle_event(self,is_close:bool):
        if is_close:
            self.running = False

    '''碰撞'''

