from typing import Any
import pygame

from pygame.sprite import Group, Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    BULLET_SIDE = pygame.transform.scale(BULLET, (9, 32))
    BULLET_ENEMY_SIDE = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    BULLETS = {'player': BULLET_SIDE, 'enemy': BULLET_ENEMY_SIDE}
    PLAYER_SPEED = -2  # Set the player bullet speed for upwards direction
    ENEMY_SPEED = 20 
    

    def __init__(self, spaceship):
        self.image = self.BULLETS [spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type 

        if spaceship.type == 'player':
            self.SPEED = self.PLAYER_SPEED
        elif spaceship.type == 'enemy':
            self.SPEED = self.ENEMY_SPEED

    def update(self, bullets):
        self.rect.y += self.SPEED

        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)


    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))