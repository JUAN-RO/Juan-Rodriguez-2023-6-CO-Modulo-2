import random
import pygame.sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(120, SCREEN_WIDTH - 120)
        self.type = type
        self.start_time = 0

    def update(self, game_speed, powerups):
        self.rect.y += game_speed

        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            powerups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)