import pygame
import random

from options import *
from assets import *


class score:
    score = 0


vec = pygame.math.Vector2

class Meteor(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.pos = vec(0, 0)
        self.vel = vec(0, 0)

        self.image = pygame.transform.scale_by(METEOR_IMAGE, METEOR_SIZE_SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        spawn_side = random.choice(['top', 'bottom', 'left', 'right'])

        if spawn_side in ['top', 'bottom']:
            self.pos.x = random.randint(-METEOR_SPAWN_PADDING, WIDTH + METEOR_SPAWN_PADDING)
            
            if spawn_side == 'top':
                self.pos.y = -METEOR_SPAWN_PADDING
                self.vel.y = METEOR_SPEED
            else:
                self.pos.y = HEIGHT + METEOR_SPAWN_PADDING
                self.vel.y = -METEOR_SPEED

        elif spawn_side in ['left', 'right']:
            self.pos.y = random.randint(-METEOR_SPAWN_PADDING, HEIGHT + METEOR_SPAWN_PADDING)

            if spawn_side == 'left':
                self.pos.x = -METEOR_SPAWN_PADDING
                self.vel.x = METEOR_SPEED

            elif spawn_side == 'right':
                self.pos.x = WIDTH + METEOR_SPAWN_PADDING
                self.vel.x = -METEOR_SPEED

        self.vel = self.vel.rotate(random.randint(-30, 30))


    def update(self):
        if self.pos.x < -METEOR_SPAWN_PADDING or self.pos.x > WIDTH + METEOR_SPAWN_PADDING or self.pos.y < -METEOR_SPAWN_PADDING or self.pos.y > HEIGHT + METEOR_SPAWN_PADDING:
            self.kill()
            score.score += 1

        self.pos += self.vel
        self.rect = self.image.get_rect()
        self.rect.center = self.pos