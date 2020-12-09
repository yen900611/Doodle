import os

from setting import *
from os import path
import pygame

class PygameView():
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Doodle Jump!")
        self.address = "GameView"
        self.height = 0
        self.bg_image_1 = pygame.transform.scale(pygame.image.load(path.join(IMAGE_DIR,BACKGROUND_IMAGE[0])),(WIDTH, HEIGHT))
        self.bg_image_2 = pygame.transform.scale(pygame.image.load(path.join(IMAGE_DIR,BACKGROUND_IMAGE[1])),(WIDTH, HEIGHT*2))


    def draw(self,data):
        '''
        每個frame呼叫一次，把角色畫在螢幕上
        :param all_sprite:
        :return:
        '''
        all_sprite = None
        if data["Address"] == self.address:
            all_sprite = data["Data"]
        self.draw_screen()
        all_sprite.draw(self.screen)
        pass

    def draw_screen(self):
        self.screen.fill((WHITE))

        if self.height <= HEIGHT:
            rel_y = self.height % self.bg_image_1.get_rect().height
            bg_y = rel_y - self.bg_image_1.get_rect().height
            self.screen.blit(self.bg_image_2, (0, bg_y))
            if rel_y <= HEIGHT:
                self.screen.blit(self.bg_image_1, (0, rel_y))
        else:
            rel_y = self.height % self.bg_image_2.get_rect().height
            bg_y = rel_y - self.bg_image_2.get_rect().height
            self.screen.blit(self.bg_image_2, (0, bg_y))
            if rel_y <= HEIGHT:
                self.screen.blit(self.bg_image_2, (0, rel_y))

    def flip(self):
        pygame.display.flip()

    def draw_information(self, surf, text, size, x, y):
        font = pygame.font.Font(pygame.font.match_font("arial"), size)
        text_surface = font.render(text , True , WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surf.blit(text_surface , text_rect)
