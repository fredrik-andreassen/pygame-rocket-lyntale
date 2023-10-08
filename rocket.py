import pygame

from options import *
from assets import *


vec = pygame.math.Vector2

class Rocket(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.rot = 0

        self._update_image()
        self._update_rect()
    

    def _update_image(self):
        self.image = pygame.transform.scale_by(ROCKET_IMAGE, ROCKET_SIZE_SCALE)
        self.image = pygame.transform.rotate(self.image, -self.rot)
    

    def _update_rect(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.pos        
        

    def update(self):
        self.vel = vec(0, 0)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            self.vel = vec(ROCKET_SPEED, 0).rotate(self.rot)
        
        if keys_pressed[pygame.K_LEFT]:
            self.rot = (self.rot - ROCKET_ROTATION_SPEED) % 360

        if keys_pressed[pygame.K_RIGHT]:
            self.rot = (self.rot + ROCKET_ROTATION_SPEED) % 360

        self.pos += self.vel
        
        self.pos.x = self.pos.x % WIDTH
        self.pos.y = self.pos.y % HEIGHT

        self._update_image()
        self._update_rect()