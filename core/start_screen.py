from pygame.locals import *


class Start_screen:
    def __init__(self, conf) -> None:
        self.config = conf
        self.text_surface = conf.font.render("Echoes of the Forgotten", True, "#81a1c1")

    def display(self) -> None:
        text_rect = self.text_surface.get_rect(
            center=self.config.screen.get_rect().center
        )
        self.config.screen.blit(self.text_surface, text_rect)
