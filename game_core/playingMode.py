import pygame
from player import Player
from setting import *
from board import Board
import random

class PlayingMode():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        # self.board = Board(40,40)
        self.all_sprite = pygame.sprite.Group()
        self.boards = pygame.sprite.Group()
        self._create_board()
        # self._create_board = pygame.sprite.Group()
        self.player = Player(WIDTH/2,HEIGHT-50)
        self.all_sprite.add(self.player)
        self.boards.add(self.board)###原：self.all_sprite.add(self.board)
        # self.boards.add(self._create_board())######
        self.address = "GameMode"
        pass

    def update(self,data):
        command = None
        if data["Address"] == self.address:
            command = data["Data"]
        self.player.update(command)
        self.scroll_window()#######
        self.boards.update()
        # print(len(self.boards))
        return {"Address":"GameView",
                "Type":type(self.all_sprite),
                "Data":self.all_sprite}

    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def handle_event(self,is_close:bool):
        if is_close:
            self.running = False

    def _create_board(self):
        self.board = Board(random.randint(0, 389), -80)
        self.boards.add(self.board)#
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(0, 389), random.randint(0, 80))
        self.boards.add(self.board)#原：self.all_sprite.add(self.board)
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(0, 389), random.randint(80, 160))
        self.boards.add(self.board)#
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(0, 389), random.randint(160, 240))
        self.boards.add(self.board)#
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(0, 389), random.randint(240, 320))
        self.boards.add(self.board)#
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(0, 389), random.randint(320, 400))
        self.boards.add(self.board)#
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(0, 389), random.randint(400, 480))
        self.boards.add(self.board)#
        self.all_sprite.add(self.board)

    def scroll_window(self):
        if self.player.rect.centery < 300:
            for self.board in self.boards:#原：for board in self.boards:
                self.board.rect.centery += 3#board.rect.centery += 3

        if len(self.boards) <=6:
            self.board = Board(random.randint(0, 389), -80)
            self.boards.add(self.board)
            self.all_sprite.add(self.board)