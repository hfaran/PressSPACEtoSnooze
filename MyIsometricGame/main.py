import pygame
from pygame.locals import QUIT
from MyIsometricGame.utils import utils

def main():
    # Init screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('MyIsometricGame')

    # Load images
    image = utils.convert_white_to_transparent(
        pygame.image.load("assets/tiles/default.png").convert_alpha())

    # Fill background
    b = pygame.Surface(screen.get_size())
    b=b.convert_alpha()
    b.fill((100,)*3)

    #Blit to screen
    screen.blit(b, (0,)*2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # Blit images
        screen.blit(image, (20,20))
        screen.blit(image, (-20, -20))
        pygame.display.flip()

if __name__ == '__main__':
    main()
