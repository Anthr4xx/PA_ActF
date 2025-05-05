import os
import sys

import pygame

def main(args = None):
    if args is None:
        args = sys.argv[1:]

# Simple pygame program

    hero_image_filename = ["shmup", "assets", "images", "hero.png"]

    # Import and initialize the pygame library
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([640, 480], 0, 32)
    pygame.display.set_caption("Hello World...")

    # Load hero image
    hero_image = pygame.image.load(os.path.abspath(os.path.join(*hero_image_filename))).convert_alpha()
    hero_image_half_width = hero_image.get_width() / 2
    hero_image_half_height = hero_image.get_height() / 2

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # get user mouse position
        x, y = pygame.mouse.get_pos()
        x -= hero_image_half_width
        y -= hero_image_half_height

        # Fill the background with black
        screen.fill((0, 0, 0))

        # Render hero image in mouse position
        screen.blit(hero_image, (x, y))

        # Flip the display
        pygame.display.update()

    # Done! Time
    pygame.quit()

if __name__ == "__main__":
    sys.exit(main())