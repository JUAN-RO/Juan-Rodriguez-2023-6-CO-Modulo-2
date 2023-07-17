import math
import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60

    Y_POS = 20

    SPEED_X = 5
    SPEED_Y = 1

    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self, image_path, enemy_type):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ENEMY_WIDTH, SCREEN_WIDTH - self.ENEMY_WIDTH, self.ENEMY_WIDTH)
        self.rect.y = self.Y_POS
        self.rect_x = self.SPEED_X
        self.rect_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.movement_x_for = random.randint(30, 100)
        self.index = 0
        self.angle = 0.0
        self.enemy_type = enemy_type

    def update(self, ships):
        self.rect.y += self.SPEED_Y

        if self.enemy_type == 1:
            self.update_type1()
        elif self.enemy_type == 2:
            self.update_type2()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def update_type1(self):
        if self.movement_x == 'left':
            self.rect.x -= self.SPEED_X
            self.change_movement_x()
        else:
            self.rect.x += self.SPEED_X
            self.change_movement_x()

    def update_type2(self):
        # Movimiento sinusoidal mientras el enemigo desciende.
        amplitude = 10  # Amplitud de la oscilación
        frequency = 0.10  # Frecuencia de la oscilación

        # Movimiento horizontal en dirección opuesta al enemigo tipo 1
        if self.movement_x == 'left':
            self.rect.x -= self.SPEED_X
            if self.rect.left <= 0:
                self.movement_x = 'right'
        else:
            self.rect.x += self.SPEED_X
            if self.rect.right >= SCREEN_WIDTH:
                self.movement_x = 'left'

        # Calcula el desplazamiento vertical utilizando la función sinusoidal
        self.rect.y += self.SPEED_Y * 1  # Incremento de la velocidad vertical

        # Si el enemigo desciende más allá de la parte inferior de la pantalla, reiniciamos su posición en la parte superior
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.y = -self.ENEMY_HEIGHT

        # Calcula el desplazamiento vertical utilizando la función sinusoidal
        self.rect.y += amplitude * math.sin(frequency * self.rect.x)
       
            
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.movement_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.movement_x_for and self.movement_x == 'left') or (self.rect.x <= self.ENEMY_WIDTH):
            self.movement_x = 'right'
            self.index = 0