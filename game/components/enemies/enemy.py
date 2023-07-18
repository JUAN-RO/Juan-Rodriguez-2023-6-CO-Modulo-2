import math
import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets import bullet_manager
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60

    Y_POS = 20

    SPEED_X = 5
    SPEED_Y = 1

    MOV_X = {0: 'left', 1: 'right'}

    INITIAL_SHOOTING_TIME = 2000
    FINAL_SHOOTING_TIME = 4000

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
        self.type = 'enemy'
        self.shooting_time = random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)

    def update(self, ships, bullet_manager):
        self.rect.y += self.SPEED_Y
        self.shoot(bullet_manager)

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


    def shoot(self, bullet_manger):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manger.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)

    