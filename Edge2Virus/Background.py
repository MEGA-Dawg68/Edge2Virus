import pygame
import itertools

def create_blue_screen():
    # Initialize the pygame
    pygame.init()

    # Set resolution higher than the computer resolution so it is full screen and windows can overlap
    screen = pygame.display.set_mode((3840, 2160), pygame.RESIZABLE)
    

    # Colours
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]
    color_iterator = itertools.cycle(colors)

    # current color
    current_color = next(color_iterator)

    # Fill the screen with the current color
    screen.fill(current_color)

    # Update the display
    pygame.display.flip()

    
    start_ticks = pygame.time.get_ticks()

    
    running = True
    while running:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000 
        if seconds > 0.1: # 0.1 seconds
            current_color = next(color_iterator)
            screen.fill(current_color)
            pygame.display.flip()
            start_ticks = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
    pygame.quit()


create_blue_screen()