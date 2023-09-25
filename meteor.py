import pygame
import random

from options import *


vec = pygame.math.Vector2

class Meteor(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.angle = random.randint(-30, 30)

        spawn_side = random.choice(['top', 'bottom', 'left', 'right'])

        if spawn_side == 'top':
            self.pos.x = random.randint(-METEOR_SPAWN_PADDING, WIDTH + METEOR_SPAWN_PADDING)
            self.pos.y = -METEOR_SPAWN_PADDING
            self.vel.y = 3

        elif spawn_side == 'bottom':
            self.pos.x = random.randint(-METEOR_SPAWN_PADDING, WIDTH + METEOR_SPAWN_PADDING)
            self.pos.y = HEIGHT + METEOR_SPAWN_PADDING
            self.vel.y = -3
        
        elif spawn_side == 'left':
            self.pos.x = -METEOR_SPAWN_PADDING
            self.pos.y = random.randint(-METEOR_SPAWN_PADDING, HEIGHT + METEOR_SPAWN_PADDING)
            self.vel.x = 3

        elif spawn_side == 'right':
            self.pos.x = WIDTH + METEOR_SPAWN_PADDING
            self.pos.y = random.randint(-METEOR_SPAWN_PADDING, HEIGHT + METEOR_SPAWN_PADDING)
            self.vel.x = -3

        self._image = pygame.image.load('./assets/meteor.png').convert_alpha()
        self._image = pygame.transform.scale_by(self._image, 1.8)

        self.image = self._image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def update(self):
        if self.pos.x < -METEOR_SPAWN_PADDING or self.pos.x > WIDTH + METEOR_SPAWN_PADDING or self.pos.y < -METEOR_SPAWN_PADDING or self.pos.y > HEIGHT + METEOR_SPAWN_PADDING:
            self.kill()
            pygame.score += 1

        self.pos += self.vel.rotate(self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos