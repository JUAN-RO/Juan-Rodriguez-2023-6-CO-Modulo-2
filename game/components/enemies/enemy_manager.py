from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 100:
            enemy1 = Enemy('game/assets/Enemy/enemy_1.png', enemy_type=1)  # Primero enemigo con apariencia original
            enemy2 = Enemy('game/assets/Enemy/enemy_2.png', enemy_type=2) 
            self.enemies.append(enemy1)
            self.enemies.append(enemy2)


        