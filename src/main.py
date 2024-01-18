# Importing pygame package
import pygame

# Importing pygame.locals package
from copy import deepcopy

# Set the width and height of the grid in terms of the number of tiles.
WIDTH, HEIGHT = 10, 20

# Set the size of each tile in pixels.
TILE_SIZE = 45

# Calculate the window resolution based on the grid dimensions and tile size.
WIN_RES = WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE

# Set the frames per second for the game loop.
FPS = 60

# Initializes the Pygame library
pygame.init()

# Creating a Pygame window with the specified resolution (WIN_RES)
g_screen = pygame.display.set_mode(WIN_RES)

# Creating a Pygame clock object that can be used to control the frame rate of the game.
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

# Specify where each block is in relation to a reference point.
block_pos =[[(-1,0),(-2,0),(0,0),(1,0)],
            [(0,-1),(-1,-1),(-1,0),(0,0)],
            [(-1,0),(-1,1),(0,0),(0,-1)],
            [(0,0),(-1,0),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(-1,-1)],
            [(0,0),(0,-1),(0,1),(1,-1)],
            [(0,0),(0,-1),(0,1),(-1,0)]]

# Create an empty list to store rectangles
blocks = []

# Loop through each (x, y) pair in 'block_pos'
for blk_pos in block_pos:
    # Create a list to store rectangles for the current (x, y) pair
    row = []
    
    # Loop through each (x, y) in the current pair
    for x, y in blk_pos:
        # Create a rectangle and add it to the current row
        rect = pygame.Rect(x + WIDTH // 2, y + 1, 1, 1)
        row.append(rect)
    
    # Add the row of rectangles to the 'blocks' list
    blocks.append(row)

# Specify a rectangle to symbolise the block.
blk_rect = pygame.Rect(0,0, TILE_SIZE - 2, TILE_SIZE - 2)

# Create a deep copy of the first block in the 'blocks' list and assign it to 'block'
block = deepcopy(blocks[0])

# Define a function to check if the block is within the horizontal borders
def check_borders():
    # Check if the x-coordinate of any element in 'block' is outside the horizontal borders
    if block[i].x < 0 or block[i].x > WIDTH - 1:
        return False
    # If all x-coordinates are within the borders, return True
    return True


# Main game loop
while True :
    # Initialize the x-coordinate of the block
    dx = 0

    # Clear the screen by filling it with a black color.
    g_screen.fill(pygame.Color('black'))

    # Check for events in the Pygame event queue.
    for event in pygame.event.get():
        # If the event is a QUIT event (user closes the window):
        if event.type == pygame.QUIT:
            # Exit the program.
            exit()

        # Check for KEYDOWN events
        if event.type == pygame.KEYDOWN:
            # Check if the pressed key is the left arrow key
            if event.key == pygame.K_LEFT:
                # Set the x-directional movement to -1
                dx = -1

            # Check if the pressed key is the right arrow key
            if event.key == pygame.K_RIGHT:
                # Set the x-directional movement to 1
                dx = 1
    
    # Create a deep copy of the first block in the 'blocks' list and assign it to 'block_old'
    block_old = deepcopy(block)

    # Move the block in the x-direction based on the defined movement
    for i in range(4):
        
        # Update the x-coordinate of each element in 'block' based on the movement 'dx'
        block[i].x += dx
        
        # Check if the updated block position is within the horizontal borders
        if not check_borders():
            # If the block is outside the borders, revert 'block' to the previous state and break out of the loop
            block = deepcopy(block_old)
            break


    # Define the color
    line_color = (40, 40, 40)

    # Loop through each rectangle in the grid and draw a rectangle with a border
    for i_rect in grid:
        pygame.draw.rect(g_screen, line_color, i_rect, 1)
    
    # Loop through the first four elements of the 'block' list
    for i in range(4):
        # Set the position of 'blk_rect' based on the current element in 'block'
        blk_rect.x = block[i].x * TILE_SIZE
        blk_rect.y = block[i].y * TILE_SIZE
    
        # Draw a white rectangle on the screen at the updated position
        pygame.draw.rect(g_screen, pygame.Color('white'), blk_rect)

    # Updates the display to reflect the changes made during the current frame.
    pygame.display.flip()

    # Control the frame rate using the Pygame clock
    clock.tick(FPS) # Replace FPS with your desired frames per second value