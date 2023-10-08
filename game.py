import pygame
from options import *

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))

import sys, random, time

from assets import *
from rocket import Rocket
from meteor import Meteor


pygame.display.set_caption('pygame-rocket')

clock = pygame.time.Clock()

rockets = pygame.sprite.Group()
meteors = pygame.sprite.Group()
rockets.add(Rocket())

pygame.score = 0

score_text = SCORE_FONT_TYPE.render(f'Score: {pygame.score}', False, SCORE_FONT_COLOR)
score_rect = score_text.get_rect()
score_rect.topleft = (5, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if random.random() < METEOR_SPAWN_CHANCE:
        meteors.add(Meteor())
    
    rockets.update()
    meteors.update()

    display.blit(BACKGROUND_IMAGE, (0, 0))
    rockets.draw(display)
    meteors.draw(display)
    
    score_text = SCORE_FONT_TYPE.render(f'Score: {pygame.score}', False, SCORE_FONT_COLOR)
    display.blit(score_text, score_rect)

    if pygame.sprite.groupcollide(rockets, meteors, False, False):
        time.sleep(3)
        pygame.score = 0
        rockets.empty()
        meteors.empty()
        rockets.add(Rocket())

    pygame.display.update()
    clock.tick(FRAMERATE)