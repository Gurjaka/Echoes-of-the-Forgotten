import pygame
from pygame.locals import *


class Prologue:
    def __init__(self, conf, data) -> None:
        self.data_dir = data
        self.config = conf

        self.prologue_duration = 58  # Display for 30 seconds
        self.prologue_start_time = pygame.time.get_ticks() + 5 * 1000
        self.prol_img = 0
        self.prol_img_start_time = pygame.time.get_ticks() + 5 * 1000

        self.img = None
        self.img_width = self.config.infoObject.current_w / 100 * 40
        self.img_height = self.config.infoObject.current_h / 100 * 35

        self.story = [
            [
                "The world once thrived with humans and mythical creatures living side by side.",
                "The humans, in their quest for control and power,",
                "created an ancient artifact that disturbed the balance of the world.",
            ],
            [
                "This artifact allowed them to seal the creatures into an underground realm,",
                "forever separating them from the human world.",
                "Years passed, and the creatures were forgotten. Humans lived their lives,",
            ],
            [
                "oblivious to the damage they had caused, while the",
                "underground realm became nothing more than a myth.",
                "But one fateful day, you, a curious young adventurer,",
            ],
            [
                "stumble upon an old, enchanted stone. As you touch it, the world around you twists,",
                "and you are pulled into the depths of the underground.",
                "You awaken in a strange, dark world, where creatures of all shapes and sizes stare at you with suspicion.",
            ],
            [
                "Some are friendly, others are hostile. The only thing you know for certain",
                "is that you are trapped in a world where humans have not set foot for centuries.",
            ],
        ]

        self.char_index = 0
        self.text_index = 0
        self.text_font = self.font = pygame.font.Font(
            f"{self.data_dir}/fonts/DeterminationMonoWebRegular-Z5oq.ttf", 40
        )
        self.text_speed = 30
        self.current_text = ""  # Store the current text being displayed
        self.current_section = 0
        self.last_update_time = pygame.time.get_ticks()  # Time of last text update
        self.section_delay = 3000
        self.section_transition_start = -1

        self.section_images = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    def load_prologue_images(self) -> bool:
        try:
            self.img = pygame.image.load(
                f"{self.data_dir}/images/prologue-{self.prol_img}.png"
            ).convert()
            self.img = pygame.transform.scale(
                self.img, (self.img_width, self.img_height)
            )
        except FileNotFoundError as e:
            print(f"Error loading image: {e}")
            self.config.screen.fill("black")
            return False
        return True

    def display_image(self) -> None:
        if self.img:
            rect = self.img.get_rect(center=self.config.screen.get_rect().midtop)
            rect.y += self.config.infoObject.current_h / 100 * 25

            self.config.screen.blit(self.img, rect)

    def calculate_prologue_time(self) -> bool:
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.prologue_start_time > self.prologue_duration * 1000:
            print("Prologue ended, moving to next stage")
            return True
        return False

    def display_text(self) -> None:
        current_time = pygame.time.get_ticks()
        screen_rect = self.config.screen.get_rect()
        center_x = screen_rect.centerx
        y_start = screen_rect.centery - 50

        if current_time < self.prologue_start_time or self.current_section >= len(
            self.story
        ):
            return

        current_section = self.story[self.current_section]

        # Render all completed lines
        for i in range(self.text_index):
            if i < len(current_section):
                text_surface = self.text_font.render(current_section[i], True, "white")
                text_rect = text_surface.get_rect(center=(center_x, y_start + i * 50))
                self.config.screen.blit(text_surface, text_rect)

        # Handle current line
        if self.text_index < len(current_section):
            # Render current line letter-by-letter
            partial_text = current_section[self.text_index][: self.char_index]
            text_surface = self.text_font.render(partial_text, True, "white")
            text_rect = text_surface.get_rect(
                center=(center_x, y_start + self.text_index * 50)
            )
            self.config.screen.blit(text_surface, text_rect)

            # Update character animation
            if current_time - self.last_update_time > self.text_speed:
                self.char_index += 1
                self.last_update_time = current_time

                # Complete line when all characters shown
                if self.char_index > len(current_section[self.text_index]):
                    self.text_index += 1
                    self.char_index = 0
                    self.last_update_time = current_time

        # Handle section transition
        else:
            if self.section_transition_start == -1:
                self.section_transition_start = current_time

            if current_time - self.section_transition_start > self.section_delay:
                if self.current_section < len(self.story) - 1:
                    # Update section AND image together
                    self.current_section += 1
                    self.prol_img = self.section_images[self.current_section]
                    self.load_prologue_images()
                    self.text_index = 0
                    self.char_index = 0
                    self.section_transition_start = -1
                    self.last_update_time = current_time
                else:
                    # Prologue completed
                    pass
