import os
import sys
import pygame
from core.config import *
from core.player import *
from core.start_menu import *
from core.prologue import *


def main():
    # pygame setup
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    pygame.init()
    pygame.font.init()
    pygame.mixer.get_init()

    if not pygame.font.get_init():
        print("Warning, fonts disabled")
        sys.exit()
    if not pygame.mixer.get_init():
        print("Warning, sound disabled")
        sys.exit()

    running = True
    main_character = "Kaelen Drystar"  # we might not even use this

    config = Config(data_dir)
    start_menu = StartMenu(config)
    player = Player(config)

    prologue = Prologue(config, data_dir)
    current_screen = "start_menu"

    pygame.mixer.music.load(f"{data_dir}/audio/prologue.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.2)

    while running:
        # Update delta time
        events = pygame.event.get()
        config.update_dt()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        # fill the screen with a color to wipe away anything from last frame
        config.screen.fill("black")

        if current_screen == "start_menu":
            result = start_menu.handle_input(events)
            if result == "START":
                current_screen = "prologue"
            elif result == "SETTINGS":
                current_screen = "settings"
            # Clear screen and draw menu
            start_menu.display()

        elif current_screen == "prologue":
            if prologue.result:
                current_screen = prologue.result
            else:
                prologue.display()

        # flip() the display to put your work on screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
