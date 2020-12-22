import pygame
from player import Player
from setting import *
from board import Board
from gameView import PygameView
import random

class PlayingMode():
    def __init__(self):
        pygame.font.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprite = pygame.sprite.Group()
        self.boards = pygame.sprite.Group()
        self._create_board()
        self.height = 0
        self.player = Player(WIDTH/2,0)
        self.all_sprite.add(self.player)
        self.address = "GameMode"
        self.gameview = PygameView()
        self.score = 0
        pass

    def update(self,data):
        if self.running:
            command = None
            if data["Address"] == self.address:
                command = data["Data"]
            self.player.update(command, self.collision())
            if self.player.height > self.score:
                self.score = self.player.height
            self.scroll_window()
            self.boards.update()
            if self.is_game_end():
                self.height = self.player.height
                if self.height < -500:
                    self.running = False
        return {"Address":"GameView",
                "Type":type(self.all_sprite),
                "Data":self.all_sprite,
                "height":self.height}

    def ticks(self,fps = FPS):
        self.clock.tick(fps)


    def _create_board(self):
        self.board = Board(WIDTH /2, -55, WIDTH, 40)
        self.boards.add(self.board)
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(20, WIDTH), random.randint(100, 200), random.randint(100,200), 30)
        self.boards.add(self.board)
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(20, WIDTH), random.randint(200, 300), random.randint(100,200), 30)
        self.boards.add(self.board)
        self.all_sprite.add(self.board)
        self.board = Board(random.randint(20, WIDTH), random.randint(300, 400), random.randint(100,200), 30)
        self.boards.add(self.board)
        self.all_sprite.add(self.board)

    def scroll_window(self):
        if self.player.height - self.height > 350:
            self.height+=20
        if len(self.boards) <=6:
            self.board = Board(random.randint(0, 389),self.height +600 , random.randint(100,200), 20)
            self.boards.add(self.board)
            self.all_sprite.add(self.board)

    def collision(self):
        hits = pygame.sprite.spritecollide(self.player,self.boards, False, pygame.sprite.collide_mask)
        if hits:
            self.player.rect.centerx +=1
            self.player.height = hits[0].height+50
            self.player.rect.centerx -=1
            self.player.velocity_y = 0
            return True
        return False

    def is_game_end(self):
        if self.player.height < -20:
            return True
        return False

    def show_score(self):
        if self.running == False:
            print(self.score)
