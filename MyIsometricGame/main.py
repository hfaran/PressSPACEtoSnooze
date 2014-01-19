import pygame
from MyIsometricGame.utils import utils

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    image = pygame.image.load("assets/tiles/default.png")
    image_2 = utils.convert_white_to_transparent(image)

    b = pygame.Surface(screen.get_size())
    b=b.convert()
    b.fill((100,)*3)

    while True:
        from time import sleep
        sleep(1)

if __name__ == '__main__':
    main()
