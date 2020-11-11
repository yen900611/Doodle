from setting import *
import pygame

class PygameView():
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Doodle Jump!")
        self.address = "GameView"

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

    def flip(self):
        pygame.display.flip()

    def draw_information(self, surf, text, size, x, y):
        font = pygame.font.Font(pygame.font.match_font("arial"), size)
        text_surface = font.render(text , True , WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surf.blit(text_surface , text_rect)
