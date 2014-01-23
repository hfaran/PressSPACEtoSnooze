import pygame


def convert_white_to_transparent(image):
    """Make white (255) in image transparent"""
    image = image.convert_alpha()
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            if image.get_at((x, y)) == (255, 255, 255, 255):
                image.set_at((x, y), (255, 255, 255, 0))
    return image
