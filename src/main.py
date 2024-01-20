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

# Set the resolution of the Pygame window
RES = 752, 940

# Set the frames per second for the game loop.
FPS = 60

# Initializes the Pygame library
pygame.init()

# Set up the Pygame display with the specified resolution
screen = pygame.display.set_mode(RES)

# Create a Pygame surface with the specified resolution
g_screen = pygame.Surface(WIN_RES)

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

'''Loading in Assests'''
# Load and convert the background image for the window
background = pygame.image.load('images/bg.jpg').convert()

# Load and convert the background image for the game screen
game_background = pygame.image.load('images/game_bg.jpg').convert()

# Load fonts for text rendering
main_font = pygame.font.Font('font/font.ttf', 65)
font = pygame.font.Font('font/font.ttf', 45)

# Render the text 'TETRIS' using the main font with a specified color
title_tetris = main_font.render('TETRIS', True, pygame.Color('darkblue'))

# Render the text 'Score:' using the 'font' and store it in 'title_score'
title_score = font.render('Score:', True, pygame.Color('green'))

# Render the text 'Record:' using the 'font' and store it in 'title_record'
title_record = font.render('Record:', True, pygame.Color('purple'))

# Function to get a random color
def get_color():
    red = randrange(30, 256)
    green = randrange(30, 256)
    blue = randrange(30, 256)
    return red, green, blue

# Create a deep copy of a randomly chosen block from the 'blocks' list and assign it to 'block'
# Also, create a deep copy of the next block for preview and assign it to 'next_block'
block, next_block = deepcopy(choice(blocks)), deepcopy(choice(blocks))

# Call the function to get a random color for the current block and the next block for preview
color, next_color = get_color(), get_color()

# Initialize score and lines variables
score, lines = 0,0

# Define a dictionary mapping the number of cleared lines to corresponding scores
scores = {0:0, 1: 100, 2:300, 3: 700, 4:1500}

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

''' Recording Records'''
# Define a function to retrieve the record from a file
def get_record():
    try:
        # Try to open the 'record' file and read the first line
        with open('record') as f:
            return f.readline()
        
    except FileNotFoundError:
        # If the 'record' file is not found, create it and initialize with '0'
        with open('record','w') as f:
            f.write('0')

# Define a function to set the record value in a file
def set_record(record, score):
    # Determine the maximum value between the existing record and the current score
    rec = max(int(record), score)

    # Open the 'record' file and write the new record value
    with open('record','w') as f:
            f.write(str(rec))

'''Main Game Loop'''
while True :
    # Call the 'get_record' function to retrieve the record value from the file
    record = get_record()

    # Initialize the x-coordinate of the block
    dx, rotate = 0, False

    # Draw the main menu background on the Pygame window
    screen.blit(background, (0, 0))

    # Draw the content of 'g_screen' on the Pygame window at a specific position
    screen.blit(g_screen,(20,20))

    # Draw the game background on 'g_screen'
    g_screen.blit(game_background, (0,0))

    # Pause the game for a short duration for visual effect
    for i in range(lines):
        pygame.time.wait(200)

    ''' Game Control '''
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
                    # Set the color of the grid position corresponding to the previous block state
                    field[block_old[i].y][block_old[i].x] = color
                
                # Set the current block and color to the next block and color
                block, color = next_block, next_color

                # Generate a new next block and color for preview
                next_block, next_color = deepcopy(choice(blocks)), get_color()

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

    ''' Checking the Lines'''
    # Initialize variables for line and lines
    line, lines = HEIGHT - 1, 0

    # Iterate through each row in reverse order
    for row in range(HEIGHT - 1, -1, -1):
        count = 0
        
        # Count the filled blocks in the current row
        for col in range(WIDTH):
            if field[row][col]:
                count += 1
            
            # Copy the row to the line below if there are still blocks in the row
            field [line][col] = field[row][col]
        
        # Move the line pointer up if the row has no filled blocks
        if count < WIDTH:
            line -= 1
        else:
            # Increase animation speed and increment the lines counter
            anim_speed += 3
            lines += 1
    
    ''' Calculating Score'''
    # Increment the score based on the number of cleared lines using the 'scores' dictionary
    score += scores[lines]

    ''' Drawing Grid'''
    # Define the color
    line_color = (40, 40, 40)

    # Loop through each rectangle in the grid and draw a rectangle with a border
    for i_rect in grid:
        pygame.draw.rect(g_screen, line_color, i_rect, 1)
    
    ''' Drawing Blocks'''
    # Loop through the first four elements of the 'block' list
    for i in range(4):
        # Set the position of 'blk_rect' based on the current element in 'block'
        blk_rect.x = block[i].x * TILE_SIZE
        blk_rect.y = block[i].y * TILE_SIZE
    
        # Draw a rectangle on the 'g_screen' surface with a specified color and position
        pygame.draw.rect(g_screen, color, blk_rect)
    
    ''' Drawing Field'''
    # Loop through each row (y-coordinate) and column (x-coordinate) in the 'field' grid
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            # Check if the color at the current grid position is non-zero (indicating a filled block)
            if col:
                # Set the position of 'blk_rect' based on the current grid position
                blk_rect.x, blk_rect.y = x * TILE_SIZE, y * TILE_SIZE

                # Draw a colored rectangle on the screen at the updated position
                pygame.draw.rect(g_screen, col, blk_rect)

    '''Drawing next Block for Preview'''
    # draw next block
    # Loop through the first four elements of the 'block' list
    for i in range(4):
        # Set the position of 'blk_rect' based on the current element in 'next_block'
        blk_rect.x = next_block[i].x * TILE_SIZE + 380
        blk_rect.y = next_block[i].y * TILE_SIZE + 185
    
        # Draw a rectangle on the 'screen' surface with the color of the next block and specified position
        pygame.draw.rect(screen, next_color, blk_rect)

    ''' Drawing Titles'''
    # Draw the 'title_tetris' text surface on the Pygame screen at a specific position
    screen.blit(title_tetris, (485, -10))

    # Draw the 'title_score' text surface on the Pygame screen at a specific position
    screen.blit(title_score, (535, 780))
    # Render the player's score as text using the 'font' and draw it on the screen
    screen.blit(font.render(str(score), True, pygame.Color('white')), (550,840))

    # Draw the 'title_record' text surface on the Pygame screen at a specific position
    screen.blit(title_record, (525, 650))
    # Render the record value as text using the 'font' and draw it on the screen
    screen.blit(font.render(record, True, pygame.Color('gold')), (550,710))

    '''Game Over State'''
    # Check if there is a filled block in the top row (row index 0)
    for i in range(WIDTH):
        # If there is a filled block in the top row, update the record with the current score
        if field[0][i]:

            # If there is a filled block in the top row, update the record with the current score
            set_record(record, score)

            # Reset the game grid by filling 2D array filled with zeros
            field = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]

            # Reset animation variables
            anim_count, anim_speed, anim_limit = 0, 60, 2000

            # Reset the score to zer
            score = 0

            # Loop through each rectangle in the 'grid' list
            for i_rect in grid:
                # Draw a rectangle on the 'g_screen' surface with a random color
                pygame.draw.rect(g_screen, get_color(), i_rect)

                # Draw 'g_screen' on the 'screen' surface at a specific position
                screen.blit(g_screen, (20, 20))

                # Update the display
                pygame.display.flip()
                
                # Control the frames per second (FPS) by waiting for a specific amount of time
                clock.tick(200)

    # Updates the display to reflect the changes made during the current frame.
    pygame.display.flip()

    # Control the frame rate using the Pygame clock
    clock.tick(FPS) # Replace FPS with your desired frames per second value