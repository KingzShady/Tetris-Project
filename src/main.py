# Importing pygame package
import pygame

# Importing pygame.locals package
from copy import deepcopy

# Import the 'choice' and 'randrange' functions from the 'random' module
from random import choice, randrange

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

# Create an empty grid (2D list) filled with zeros
field = []

# Loop through each row
for i in range(HEIGHT):
    # Create a row filled with zeros and add it to the grid
    row = [0] * WIDTH
    field.append(row)

# Initialize variables for animation: current count, animation speed, and animation limit
anim_count, anim_speed, anim_limit = 0, 60, 2000

# Create a deep copy of a randomly chosen block from the 'blocks' list and assign it to 'block'
block = deepcopy(choice(blocks))

# Define a function to check if the block is within the horizontal borders
def check_borders():
    # Check if the x-coordinate of any element in 'block' is outside the horizontal borders
    if block[i].x < 0 or block[i].x > WIDTH - 1:
        return False
    
    # Check if the y-coordinate of any element in 'block' is outside the vertical borders
    # or if there is a non-zero value in the corresponding field position
    elif block[i].y > HEIGHT - 1 or field[block[i].y][block[i].x]:
        return False
    # If all x-coordinates are within the borders, return True
    return True


# Main game loop
while True :
    # Initialize the x-coordinate of the block
    dx, rotate = 0, False

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
            
            # Check if the pressed key is the down arrow key
            if event.key == pygame.K_DOWN:
                # Set a new animation limit for faster animation when the down arrow key is pressed
                anim_limit = 100
            
            # Check if the pressed key is the up arrow key
            if event.key == pygame.K_UP:
                rotate = True

    ''' Moving X of Block'''
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

    ''' Moving Y Axis of Block'''
    # Increment the animation count by the animation speed
    anim_count += anim_speed

    # Check if the animation count is greater than the animation limit
    if anim_count >= anim_limit:
        # Reset the animation count to 0
        anim_count = 0

        # Create a deep copy of the first block in the 'blocks' list and assign it to 'block_old'
        block_old = deepcopy(block)

        # Move the block in the x-direction based on the defined movement
        for i in range(4):
            # Update the x-coordinate of each element in 'block' based on the movement 'dx'
            block[i].y += 1
        
            # Check if the updated block position is within the horizontal borders
            if not check_borders():
                # Set the corresponding positions in the 'field' grid to the color white for each element in 'block'
                for i in range(4):
                    # Set the color of the grid position defined by the current element in 'block' to white
                    field[block_old[i].y][block_old[i].x] = pygame.Color('white')
                
                # If the block is outside the borders, revert 'block' to the previous state and break out of the loop
                block = deepcopy(choice(blocks))

                # Reset the animation limit to its original value
                anim_limit = 2000
                break

    ''' Rotating blocks'''
    # Set 'center' as the first element of 'block' (assuming it represents the center of rotation)
    center = block[0]

    # Check if the 'rotate' flag is set to True
    if rotate:
        # Move the block in the x and y directions based on the defined rotation
        for i in range(4):
            # Calculate the new coordinates relative to the center of rotation
            x = block[i].y - center.y
            y = block[i].x - center.x

            # Update the block coordinates with the rotated values
            block[i].x = center.x - x
            block[i].y = center.y + y

            # Check if the updated block position is within the horizontal borders
            if not check_borders():
                # If the block is outside the borders, revert 'block' to the previous state and break out of the loop
                block = deepcopy(block_old)
                break
    
    # check for lines
    line = HEIGHT - 1
    for row in range(HEIGHT - 1, -1, -1):
        count = 0
        for col in range(WIDTH):
            if field[row][col]:
                count += 1
            field [line][col] = field[row][col]
        if count < WIDTH:
            line -= 1

    ''' Drawing Grid'''
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
    
    # Loop through each row (y-coordinate) and column (x-coordinate) in the 'field' grid
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            # Check if the color at the current grid position is non-zero (indicating a filled block)
            if col:
                # Set the position of 'blk_rect' based on the current grid position
                blk_rect.x, blk_rect.y = x * TILE_SIZE, y * TILE_SIZE

                # Draw a colored rectangle on the screen at the updated position
                pygame.draw.rect(g_screen, col, blk_rect)

    # Updates the display to reflect the changes made during the current frame.
    pygame.display.flip()

    # Control the frame rate using the Pygame clock
    clock.tick(FPS) # Replace FPS with your desired frames per second value