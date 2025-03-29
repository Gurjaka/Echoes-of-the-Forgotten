import pygame
from pygame.locals import *
from typing import Union


class Settings:
    def __init__(self, conf) -> None:
        self.config = conf

    def display(self) -> None:
        title_text = self.config.font.render("Working in progress", True, ("white"))
        title_rect = title_text.get_rect(center=self.config.screen.get_rect().midtop)
        title_rect.y += self.config.infoObject.current_h / 100 * 35
        self.config.screen.blit(title_text, title_rect)

        back_font = self.font = pygame.font.Font(
            f"{self.config.data_dir}/fonts/DeterminationMonoWebRegular-Z5oq.ttf", 60
        )

        back_text = back_font.render('Press "Space" to return', True, ("#81a1c1"))
        back_rect = back_text.get_rect(center=self.config.screen.get_rect().midbottom)
        back_rect.y -= self.config.infoObject.current_h / 100 * 35
        self.config.screen.blit(back_text, back_rect)

    def handle_input(self, events) -> Union[str, None]:
        for event in events:
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_screen = "start_menu"
                    return "start_menu"
        return None
