import pygame

from options import *

BACKGROUND_IMAGE = pygame.image.load('./assets/stars.jpg').convert()
ROCKET_IMAGE = pygame.image.load('./assets/rocket.png').convert_alpha()
METEOR_IMAGE = pygame.image.load('./assets/meteor.png').convert_alpha()


SCORE_FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', SCORE_FONT_SIZE)
SCORE_FONT_COLOR = (255, 255, 255)