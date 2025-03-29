from pygame.locals import *
from typing import Union


class StartMenu:
    def __init__(self, conf) -> None:
        self.config = conf
        self.menu_items = ["START", "SETTINGS"]
        self.selected_index = 0
        self.button_rects = []
        self.horizontal_gap = 600  # Space between buttons

    def handle_input(self, events) -> Union[str, None]:
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.selected_index = max(0, self.selected_index - 1)
                elif event.key == K_RIGHT:
                    self.selected_index = min(
                        len(self.menu_items) - 1, self.selected_index + 1
                    )
                elif event.key in [K_RETURN, K_SPACE]:
                    return self.menu_items[self.selected_index]

            if event.type == MOUSEMOTION:
                for i, rect in enumerate(self.button_rects):
                    if rect.collidepoint(event.pos):
                        self.selected_index = i

            if event.type == MOUSEBUTTONDOWN:
                for i, rect in enumerate(self.button_rects):
                    if rect.collidepoint(event.pos):
                        return self.menu_items[i]
        return None

    def draw_button(self, text, position, selected) -> None:
        color = ("#88c0d0") if selected else (255, 255, 255)
        text_surface = self.config.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.button_rects.append(text_rect)
        self.config.screen.blit(text_surface, text_rect)

    def display(self) -> None:
        self.button_rects = []
        screen_rect = self.config.screen.get_rect()

        # Draw title
        title_text = self.config.font.render(
            "Echoes of the Forgotten", True, ("#81a1c1")
        )
        title_rect = title_text.get_rect(center=screen_rect.midtop)
        title_rect.y += self.config.infoObject.current_h // 100 * 30
        self.config.screen.blit(title_text, title_rect)

        # Calculate button positions
        button_y = screen_rect.centery
        start_x = screen_rect.centerx - self.horizontal_gap // 2
        settings_x = screen_rect.centerx + self.horizontal_gap // 2

        # Draw buttons
        self.draw_button("START", (start_x, button_y), self.selected_index == 0)
        self.draw_button("SETTINGS", (settings_x, button_y), self.selected_index == 1)
