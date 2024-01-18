# importing pygame package
import pygame

# setting the window resolution of the game
WIN_RES = 800,600

# initializes the Pygame library
pygame.init()

# creating a Pygame window with the specified resolution (WIN_RES)
g_screen = pygame.display.set_mode(WIN_RES)

# creating a Pygame clock object that can be used to control the frame rate of the game.
clock = pygame.time.Clock()

# Main game loop
while true :
     # Clear the screen by filling it with a black color.
    g_screen.fill(pygame.Color('black'))

