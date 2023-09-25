import pygame
import sys, random, time

from options import *
from rocket import Rocket
from meteor import Meteor


pygame.init()
pygame.display.set_caption('pygame-rocket')

clock = pygame.time.Clock()


display = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('./assets/stars.jpg').convert()

rockets = pygame.sprite.Group()
meteors = pygame.sprite.Group()

rockets.add(Rocket())

pygame.score = 0

font = pygame.font.Font('./assets/dpcomic.ttf', 32)
score_text = font.render(f'Score: {pygame.score}', True, (255, 255, 255))
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

    display.blit(background, (0, 0))
    rockets.draw(display)
    meteors.draw(display)
    
    score_text = font.render(f'Score: {pygame.score}', True, (255, 255, 255))
    display.blit(score_text, score_rect)

    if pygame.sprite.groupcollide(rockets, meteors, False, False):
        time.sleep(3)
        pygame.score = 0
        rockets.empty()
        meteors.empty()
        rockets.add(Rocket())

    pygame.display.update()
    clock.tick(FRAMERATE)