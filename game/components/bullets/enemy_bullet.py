import pygame
import random
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):

        self.image = pygame.Surface((5, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_x = 0
        self.speed_y = 0
        self.enemy_bullets = pygame.sprite.Group()
        width = 5
        height = 20

        # Inicializar las propiedades de la bala, como posición y velocidad
        self.rect = pygame.Rect(x, y, width, height)
        self.speed_x = 0
        self.speed_y = 0

        if random.random() < 0.1:
            enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            self.enemy_bullets.add(enemy_bullet) 

    def update(self):
        # Actualizar la posición de la bala en función de su velocidad
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Eliminar la bala si sale de la pantalla
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.enemy_bullets.remove()