import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    FINAL_SHOOTING_TIME = 400
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500
    SPACESHIP_SPEED = 10

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.bullet_limit = 3  # Límite de balas para el jugador
        self.bullets_fired = 0  # Contador de balas disparadas por el jugador
        self.shooting_time = 0  # Initialize the shooting_time attribute
        self.bullet_limit = 3
        self.bullets_fired = 0


    def update(self, keys, bullet_manager):
        if keys[pygame.K_SPACE]:
            self.shoot(bullet_manager)

        if keys[pygame.K_UP]:
          if self.rect.y > SCREEN_HEIGHT // 2:
            if self.rect.y > 0:
                self.rect.y -= self.SPACESHIP_SPEED

        if keys[pygame.K_SPACE]:
            self.shoot(bullet_manager)


        
                
        if keys[pygame.K_DOWN]:
            if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGHT:
                self.rect.y += self.SPACESHIP_SPEED
        if keys[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= self.SPACESHIP_SPEED
            else:
                self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
        if keys[pygame.K_RIGHT]:
            if self.rect.x < SCREEN_WIDTH - self.SPACESHIP_WIDTH:
                self.rect.x += self.SPACESHIP_SPEED
            else:
                self.rect.x = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()


        if self.bullets_fired < self.bullet_limit and current_time - self.shooting_time >= self.FINAL_SHOOTING_TIME:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time = current_time
            self.bullets_fired += 1

        if self.bullets_fired >= self.bullet_limit:
            self.bullets_fired = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))