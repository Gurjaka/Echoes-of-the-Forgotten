import pygame


class Prologue:
    def __init__(self, conf, data) -> None:
        self.data_dir = data
        self.config = conf

        self.prologue_duration = 30  # Display for 30 seconds
        self.prologue_start_time = pygame.time.get_ticks() + 5 * 1000
        self.prol_img = 0
        self.prol_img_start_time = pygame.time.get_ticks() + 5 * 1000

        self.img = None
        self.img_width = self.config.infoObject.current_w / 100 * 40
        self.img_height = self.config.infoObject.current_h / 100 * 35

        self.story = [
            [
                "The world once thrived with humans and mythical creatures living side by side.",
                "The humans, in their quest for control and power, created an ancient artifact that disturbed the balance of the world.",
                "This artifact allowed them to seal the creatures into an underground realm, forever separating them from the human world.",
            ],
            [
                "Years passed, and the creatures were forgotten. Humans lived their lives,",
                "oblivious to the damage they had caused, while the underground realm became",
                "nothing more than a myth. But one fateful day, you, a curious young adventurer,",
                "stumble upon an old, enchanted stone. As you touch it, the world around you twists,",
                "and you are pulled into the depths of the underground.",
            ],
            [
                "You awaken in a strange, dark world, where creatures of all shapes and sizes stare at you with suspicion.",
                "Some are friendly, others are hostile. The only thing you know for certain",
                "is that you are trapped in a world where humans have not set foot for centuries.",
            ],
        ]

        self.text_index = 0  # To track which line of text to display
        self.current_text = ""  # Store the current text being displayed
        self.text_timer = 0  # Track the position in the current line of text
        self.last_update_time = pygame.time.get_ticks()  # Time of last text update
        self.text_speed = 2000  # Milliseconds between each letter
        self.text_y = 0

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

            pygame.display.flip()

    def calculate_image_time(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.prol_img_start_time > 6 * 1000:
            if self.prol_img < 5:
                self.prol_img += 1
                self.prol_img_start_time = pygame.time.get_ticks()

    def calculate_prologue_time(self) -> bool:
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.prologue_start_time > self.prologue_duration * 1000:
            print("Prologue ended, moving to next stage")
            return True
        return False
