import pygame


class Config:
    def __init__(self, data) -> None:
        self.data_dir = data
        self.font = pygame.font.Font(
            f"{self.data_dir}/fonts/DeterminationMonoWebRegular-Z5oq.ttf", 120
        )
        self.flags = pygame.FULLSCREEN
        self.infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode(
            (self.infoObject.current_h, self.infoObject.current_w), self.flags, vsync=1
        )
        self.clock = pygame.time.Clock()
        self.dt = 0  # delta time in seconds since last frame (calculate fps)
        self.center = pygame.Vector2(
            self.screen.get_width() / 2, self.screen.get_height() / 2
        )  # calculate center of the screen

    def update_dt(self) -> None:
        self.dt = self.clock.tick(60) / 1000.0  # Ensure float division
