# importing pygame package
import pygame

# Set the width and height of the grid in terms of the number of tiles.
WIDTH, HEIGHT = 10, 20

# Set the size of each tile in pixels.
TILE_SIZE = 45

# Calculate the window resolution based on the grid dimensions and tile size.
WIN_RES = WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE

# Set the frames per second for the game loop.
FPS = 60

# initializes the Pygame library
pygame.init()

# creating a Pygame window with the specified resolution (WIN_RES)
g_screen = pygame.display.set_mode(WIN_RES)

# creating a Pygame clock object that can be used to control the frame rate of the game.
clock = pygame.time.Clock()

# Initialize an empty list to store rectangles
grid = []

# Loop through each x-coordinate and y-coordinate to create rectangles
for x in range(WIDTH):
    for y in range(HEIGHT):
        # Create a rectangle at the current position with the specified size
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        
        # Add the rectangle to the grid list
        grid.append(rect)

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

    # Define the color
    line_color = (40, 40, 40)

    # Loop through each rectangle in the grid and draw a rectangle with a border
    for i_rect in grid:
        pygame.draw.rect(g_screen, line_color, i_rect, 1)


    # updates the display to reflect the changes made during the current frame.
    pygame.display.flip()

    # Control the frame rate using the Pygame clock
    clock.tick(FPS) # Replace FPS with your desired frames per second value