import pygame
from game.components import spaceship
from game.components.menu import Menu

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager(self.player)
        self.bullet_manager = BulletManager(self.player, self.enemy_manager)
        self.spaceship = spaceship.Spaceship()
        self.running = False
        self.menu = Menu(message='Press any key to start...', game=self)
        self.death_count = 0
        self.score = 0
        


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            self.show_score()  
            pygame.display.flip()
            self.clock.tick(60)
        pygame.display.quit()
        pygame.quit()
        
  

    def run(self):
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
      

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)  # Add the bullet_manager parameter here
        self.enemy_manager.update(self.bullet_manager)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset(self.screen)

        if self.death_count > 0:
            self.menu.update_message('New Message')
        
        self.menu.draw(self.screen)
        self.menu.update(self)


    def show_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score:{self.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

