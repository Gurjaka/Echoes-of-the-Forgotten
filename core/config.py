import pygame


class Config:
    def __init__(self) -> None:
        pygame.init()  # Add this initialization
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.dt = 0  # delta time in seconds since last frame (calculate fps)

    def update_dt(self):
        self.dt = self.clock.tick(60) / 1000.0  # Ensure float division
