from game.components.enemies.enemy2 import Enemy2, Enemy  # Importa la nueva clase Enemy2

class EnemyManager:
    def __init__(self, player):
        self.player = player
        self.enemies = []

    def update(self, bullet_manager):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy1 = Enemy('game/assets/Enemy/enemy_1.png', enemy_type=1)
            enemy2 = Enemy2('game/assets/Enemy/enemy_2.png', enemy_type=2)  # Crea un nuevo enemigo tipo 2
            self.enemies.append(enemy1)
            self.enemies.append(enemy2)  # Agrega el nuevo enemigo tipo 2 a la lista
        


    def reset(self):
        self.enemies = []
        


        