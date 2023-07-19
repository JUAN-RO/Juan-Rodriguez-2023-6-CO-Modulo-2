import pygame
from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2
    MENU_COLOR = (255, 255, 255)
    MESSAGE_COLOR = (0, 0, 0)
    
    def __init__(self, message, game):
        self.message = message
        self.game = game  # Almacenar la referencia al objeto Game
        #self.background_image = pygame.image.load("game/assets/Other/Final.png").convert()
        #self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, self.MESSAGE_COLOR)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
        self.update_message('Press any key to restart') 
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
         

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                self.game.playing = False
            elif event.type == pygame.KEYDOWN:
                self.game.run()

    def reset(self, screen):
        screen.fill(self.MENU_COLOR)


    def update_message(self, message):
        self.text = self.font.render(message,True, self.MESSAGE_COLOR)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)
    