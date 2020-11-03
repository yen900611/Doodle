import pygame
from player import Player
from board import Board
from setting import *
import random

class PlayingMode():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        '''set group'''
        self.all_sprite = pygame.sprite.Group()
        self.boards = pygame.sprite.Group()

        self._create_board()
        self.player = Player(WIDTH/2,HEIGHT-50)
        # self._create_board()
        self.all_sprite.add(self.player)
        self.all_sprite.add(self.board)
        pass


    def update(self,command):
        self.player.update(command)
        # self._create_board()
        return self.all_sprite
        pass


    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def handle_event(self,is_close:bool):
        if is_close:
            self.running = False

    def _create_board(self):
        for board in range(10):
            self.board = Board(random.randint(0, 300), random.randint(0, 400))
            self.all_sprite.add(self.board)

    # boards = _create_board
    # boards = pygame.sprite.Group()

    '''碰撞'''

    # TODO
    # 解碼Function放在update裡面-->規定command的格式

