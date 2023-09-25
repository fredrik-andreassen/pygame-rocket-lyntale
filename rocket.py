import pygame

from options import *


vec = pygame.math.Vector2

class Rocket(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.rot = 0

        self._image = pygame.image.load('./assets/rocket.png').convert_alpha()
        self._image = pygame.transform.scale_by(self._image, 1.6)

        self.image = self._image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        

    def update(self):
        self.vel = vec(0, 0)

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            self.vel = vec(3, 0).rotate(self.rot)
        
        if keys_pressed[pygame.K_LEFT]:
            self.rot = (self.rot - 2) % 360

        if keys_pressed[pygame.K_RIGHT]:
            self.rot = (self.rot + 2) % 360

        self.pos += self.vel

        if self.pos.x > WIDTH:
            self.pos.x = 0
        
        if self.pos.x < 0:
            self.pos.x = WIDTH
        
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.image = pygame.transform.rotate(self._image, -self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos