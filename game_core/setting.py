from os import path
WIDTH = 450
HEIGHT = 600
FPS = 30

'''Color'''
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)

'''command'''
move_right = "MOVE_RIGHT"
move_left = "MOVE_LEFT"

'''data path'''
IMAGE_DIR = path.join(path.dirname(__file__),"image")
BACKGROUND_IMAGE = ["background.jpg", "background_2.jpg"]