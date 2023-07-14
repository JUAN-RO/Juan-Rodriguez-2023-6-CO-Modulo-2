
import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship:
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGT = 60
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500 
    SPACESHIP_SPEED = 10



    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS


    def update(self, user_input):
      if user_input[pygame.K_LEFT]:
        self.move_left()
      elif user_input[pygame.K_RIGHT]:
        self.move_right()
      elif user_input[pygame.K_UP]:
        self.move_up()
      elif user_input[pygame.K_DOWN]:
        self.move_down()
    
    def update(self, keys):
      if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        # Mover la nave en diagonal hacia arriba a la derecha
        self.rect.x += self.SPACESHIP_SPEED 
        self.rect.y -= self.SPACESHIP_SPEED
      elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        # Mover la nave en diagonal hacia arriba a la izquierda
        self.rect.x -= self.SPACESHIP_SPEED 
        self.rect.y -= self.SPACESHIP_SPEED 
      elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        # Mover la nave en diagonal hacia abajo a la derecha
        self.rect.x += self.SPACESHIP_SPEED 
        self.rect.y += self.SPACESHIP_SPEED 
      elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        # Mover la nave en diagonal hacia abajo a la izquierda
        self.rect.x -= self.SPACESHIP_SPEED 
        self.rect.y += self.SPACESHIP_SPEED 
      else:  
         if keys[pygame.K_UP]:
            if self.rect.y > 0:
                if self.rect.y > SCREEN_HEIGHT // 2:
                    self.rect.y -= self.SPACESHIP_SPEED 

         if keys[pygame.K_DOWN]:
            if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGT:
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

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))