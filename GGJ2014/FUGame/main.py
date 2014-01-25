import pygame
from pygame.locals import *

from itertools import chain

from FUGame.constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((FU_WIDTH, FU_HEIGHT))
    pygame.display.set_caption('FUGame')
