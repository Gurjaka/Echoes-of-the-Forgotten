import os
import sys
import pygame
from core.config import *
from core.player import *
from core.start_screen import *
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
    start_screen = Start_screen(config)
    player = Player(config)

    prologue = Prologue(config, data_dir)

    greet_play = False
    prologue_play = False

    pygame.mixer.music.load(f"{data_dir}/audio/prologue.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.2)

    game_start = pygame.time.get_ticks()

    while running:
        # Update delta time
        config.update_dt()

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # fill the screen with a color to wipe away anything from last frame
        config.screen.fill("black")

        # RENDER YOUR GAME HERE
        if not greet_play:
            current_time = pygame.time.get_ticks()
            start_screen.display()
            pygame.display.flip()
            if current_time - game_start > 4 * 1000:
                greet_play = True
            continue

        if not prologue_play:
            config.screen.fill("black")  # Clear once per frame
            prologue_play = prologue.calculate_prologue_time()
            prologue.load_prologue_images()
            prologue.display_image()
            prologue.display_text()  # This should NOT contain flip()
            pygame.display.flip()  # Single display update
            continue

        config.screen.fill("black")
        pygame.display.flip()
        # flip() the display to put your work on screen
        # greet = 1
        # time.sleep(2)
        #
        # player.move()
        # player.spawn_player()
        # pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
