import pygame
import subprocess
import sys
import random
import time
import pyautogui

# Initialize Pygame
pygame.init()

# Get the screen width and height
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set up display in full screen mode
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Flashing Colors")

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a random color
    screen.fill(random_color())

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(50000)  # Adjust the value to change the flashing speed

   
# Quit Pygame
pygame.quit()
sys.exit()
