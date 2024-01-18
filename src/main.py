# importing pygame package
import pygame

# Set the width and height of the grid in terms of the number of tiles.
WIDTH, HEIGHT = 10, 20

# Set the size of each tile in pixels.
TILE = 45

# Calculate the window resolution based on the grid dimensions and tile size.
WIN_RES = WIDTH * TILE, HEIGHT * TILE

# Set the frames per second for the game loop.
FPS = 60

# initializes the Pygame library
pygame.init()

# creating a Pygame window with the specified resolution (WIN_RES)
g_screen = pygame.display.set_mode(WIN_RES)

# creating a Pygame clock object that can be used to control the frame rate of the game.
clock = pygame.time.Clock()

# Main game loop
while True :
     # Clear the screen by filling it with a black color.
    g_screen.fill(pygame.Color('black'))

    # Check for events in the Pygame event queue.
    for event in pygame.event.get():
        # If the event is a QUIT event (user closes the window):
        if event.type == pygame.QUIT:
            # Quit Pygame and exit the program.
            exit()
    
    # updates the display to reflect the changes made during the current frame.
    pygame.display.flip()

    # Control the frame rate using the Pygame clock
    clock.tick(FPS) # Replace FPS with your desired frames per second value