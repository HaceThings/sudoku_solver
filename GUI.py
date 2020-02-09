import pygame
import os

grid_location = os.path.join(os.getcwd(), 'sudoku_grid.jpg')

# Initializes PyGame display module
pygame.display.init()

screen_height = 600
screen_width = 600

# Open display
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill([255, 255, 255])
grid = pygame.image.load(grid_location).convert()
pygame.display.flip()

# Close display
pygame.display.quit()
