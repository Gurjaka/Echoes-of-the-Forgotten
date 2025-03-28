import pygame
from core.config import *
from core.player import *


# pygame setup
pygame.init()
running = True
main_character = "Kaelen Drystar"  # we might not even use this
conf = Config()
py = Player(conf)

while running:
    # Update delta time
    conf.update_dt()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    conf.screen.fill("#242933")

    # RENDER YOUR GAME HERE
    py.move()  # Move the player first
    py.spawn_player()  # Then draw the player

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
