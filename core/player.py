import pygame
from core.config import Config


class Player:
    """class for player related functions and settings"""

    def __init__(self, config: Config) -> None:
        """define necessary settings for player"""
        self.config = config
        self.player_pos = self.config.center

    def spawn_player(self) -> None:
        pygame.draw.circle(self.config.screen, "red", self.player_pos, 40)

    def move(self) -> None:
        """calculate new player position based on pressed key"""
        keys = pygame.key.get_pressed()
        speed = 300  # pixels per second

        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_DOWN]:
            direction.y += 1
        if keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_RIGHT]:
            direction.x += 1

        # Normalize direction to prevent faster diagonal movement
        if direction.length() != 0:
            direction.normalize_ip()

        self.player_pos += direction * speed * self.config.dt
