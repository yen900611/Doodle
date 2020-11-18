import pygame
from Doodle_Jump import Doodle

if __name__ == "__main__":
    pygame.init()
    game = Doodle()
    while game.isRunning():
        game.update()

    pygame.quit()