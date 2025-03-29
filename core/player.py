import pygame


class Player:
    """class for player related functions and settings"""

    def __init__(self, config, data) -> None:
        """define necessary settings for player"""
        self.config = config
        self.data_dir = data
        self.character_sprite = None
        self.player_pos = self.config.center

    def spawn_player(self) -> None:
        character = pygame.image.load(f"{self.data_dir}/npc/nugzari.png")
        self.character_sprite = pygame.transform.scale(character, (156, 156))
        self.config.screen.blit(self.character_sprite, self.player_pos)

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
