import pygame
from game.components import game
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class BulletManager:
    PLAYER_SPEED = -20

    def __init__(self, spaceship, enemy_manager):
        self.player_bullets = []
        self.enemy_bullets = []
        if spaceship.type == 'player':
            self.SPEED = -20
        self.enemy_manager = enemy_manager  # Guardamos la referencia al EnemyManager

        if spaceship.type == 'player':
            self.SPEED = self.PLAYER_SPEED

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            # Modifique la coordenada Y de la viñeta del jugador para que se mueva hacia arriba
            bullet.rect.y += self.SPEED

        # Verificar colisiones entre balas del jugador y enemigos
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            # Colisionar con enemigos tipo 1
            for enemy in self.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and enemy.enemy_type == 1:
                    self.player_bullets.remove(bullet)
                    self.enemy_manager.enemies.remove(enemy)

            # Colisionar con enemigos tipo 2
            for enemy in self.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and enemy.enemy_type == 2:
                    self.player_bullets.remove(bullet)
                    enemy.hit_count += 1
                    if enemy.hit_count >= 4:
                        self.enemy_manager.enemies.remove(enemy)

    def draw(self, screen):
        for bullet in self.player_bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)


    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player':
            self.player_bullets.append(bullet)