import pygame
import random
from game.components.power_ups.shield import Shield

class PowerupManager:
    POWER_UP_INITIAL_TIME = 5000
    POWER_UP_FINAL_TIME = 6000

    def __init__(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)
        self.duration = random.randint(3, 5)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.POWER_UP_INITIAL_TIME, now + self.POWER_UP_FINAL_TIME)

    def generate_power_up(self):
        power_up = Shield()
        self.power_ups.append(power_up)
        self.when_appears += random.randint(self.POWER_UP_INITIAL_TIME, self.POWER_UP_FINAL_TIME)
