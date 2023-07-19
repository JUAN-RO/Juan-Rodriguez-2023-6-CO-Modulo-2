import math
from game.components.bullets import bullet_manager
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy2(Enemy):
    def __init__(self, image_path, enemy_type):
        super().__init__(image_path, enemy_type)

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

        # Llamamos al método shoot() para que el enemigo tipo 2 dispare balas
        self.shoot(bullet_manager)

         # Si el enemigo desciende más allá de la parte inferior de la pantalla o alcanza el hit_count, lo eliminamos
        if self.rect.bottom <= 0 or self.hit_count >= 5:
            self.enemy_bullets.remove(Enemy2)

    