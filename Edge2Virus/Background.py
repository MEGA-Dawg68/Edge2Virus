import pygame
import random

def create_infinite_colors_screen():
    # Initialize pygame
    pygame.init()

    # Set resolution higher than the computer resolution so it is full screen and windows can overlap
    screen = pygame.display.set_mode((3840, 2160), pygame.RESIZABLE)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Generate random RGB values for the color
        current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.fill(current_color)
        pygame.display.flip()

        clock.tick(50000)  # Adjust the frame rate (frames per second) as needed

    pygame.quit()

create_infinite_colors_screen()
