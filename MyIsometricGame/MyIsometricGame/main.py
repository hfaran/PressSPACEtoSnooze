import pygame
from pygame.locals import *
from random import randint, choice
from itertools import chain

from MyIsometricGame.constants import *
from MyIsometricGame.utils import utils
from MyIsometricGame.tile import Tile


def generate_floor(numx, numy):
    """Create a tiled floor of size numx, numy"""
    __colors = ["pink"]

    def getx(x, y, w, h):
        """Get pixel x-coordinate to set tile at"""
        return int((numy + x - y) * w / 2.0)

    def gety(x, y, w, h):
        """Get pixel y-coordinate to set tile at"""
        return int((x + y) * w / 4.0)

    def create_tile(x, y):
        """Create tile at coordiantes (x, y)"""
        t = Tile(choice(__colors))
        width, height = t.image.get_size()
        t.set_pos(getx(x, y, width, height), gety(x, y, width, height))
        return t

    return [create_tile(x, y) for y in xrange(numx) for x in xrange(numy)]
    # l = []
    # for y in xrange(numx):
    #     for x in xrange(numy):
    #         t = create_tile(x, y)
    #         l.append(t)
    # return l


def main():
    # Init screen
    pygame.init()
    screen = pygame.display.set_mode((MIG_WIDTH, MIG_HEIGHT))
    pygame.display.set_caption('MyIsometricGame')

    # Load images
    tiles = generate_floor(5, 5)

    # Fill background
    bg = pygame.Surface(screen.get_size())
    # bg.fill((100,) * 3)

    # Add tiles
    screen.blit(bg, (0,) * 2)
    for t in tiles:
        screen.blit(t.image, t.get_pos())
    pygame.display.flip()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print x, y
                for n, t in enumerate(reversed(tiles)):
                    if t.point_collision((x - t._x, y - t._y)):
                        print n
                        break


if __name__ == '__main__':
    main()
