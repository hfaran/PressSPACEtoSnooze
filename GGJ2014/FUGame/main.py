import pygame
from pygame.locals import *

from itertools import chain

from FUGame.constants import *

def main():
    pygame.init()
    #screen = pygame.display.set_mode((FU_WIDTH, FU_HEIGHT))
    screenInfo = pygame.display.Info()
    print((screenInfo.current_w, screenInfo.current_h))
    screen = pygame.display.set_mode((screenInfo.current_w, screenInfo.current_h), pygame.FULLSCREEN)
    pygame.display.set_caption('FUGame')
