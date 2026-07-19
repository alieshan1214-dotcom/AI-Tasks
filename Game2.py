import pygame
import random
import sys
from pygame.locals import *

# 1. INITIALIZE & SET UP CONSTANTS
pygame.init()

# Window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GRID_SIZE = 20  # Each grid square is 20x20 pixels

# Color definitions (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up display window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game Challenge')
clock = pygame.time.Clock()

# 2. GAME STATE VARIABLES
# Initial snake position (head is the first element)
snake_body = [[100, 100], [80, 100], [60, 100]]

# Directions: [x_change, y_change]
direction = [GRID_SIZE, 0]  # Starting by moving Right
next_direction = direction


# Function to spawn food randomly aligned to the grid
def spawn_food():
    x = random.randrange(0, WINDOW_WIDTH, GRID_SIZE)
    y = random.randrange(0, WINDOW_HEIGHT, GRID_SIZE)
    return [x, y]


food_pos = spawn_food()
score = 0
game_over = False

# 3. MAIN GAME LOOP
while not game_over:

    # --- EVENT HANDLING (PLAYER INPUT) ---
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            # Change direction but prevent reverse-collision into itself
            if event.key == K_UP and direction != [0, GRID_SIZE]:
                next_direction = [0, -GRID_SIZE]
            elif event.key == K_DOWN and direction != [0, -GRID_SIZE]:
                next_direction = [0, GRID_SIZE]
            elif event.key == K_LEFT and direction != [GRID_SIZE, 0]:
                next_direction = [-GRID_SIZE, 0]
            elif event.key == K_RIGHT and direction != [-GRID_SIZE, 0]:
                next_direction = [GRID_SIZE, 0]

    # Commit the direction change for this frame
    direction = next_direction

    # --- UPDATE GAME STATE (MOVEMENT) ---
    # Calculate new head position
    new_head = [snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]]

    # Insert the new head to simulate moving forward
    snake_body.insert(0, new_head)

    # --- COLLISION CHECK: FOOD ---
    if snake_body[0] == food_pos:
        score += 1
        food_pos = spawn_food()
        # Do NOT pop the tail segment; snake grows longer!
    else:
        # Pop the last element to maintain regular length
        snake_body.pop()

    # --- COLLISION CHECK: WALLS ---
    head_x, head_y = snake_body[0][0], snake_body[0][1]
    if head_x < 0 or head_x >= WINDOW_WIDTH or head_y < 0 or head_y >= WINDOW_HEIGHT:
        game_over = True

    # --- COLLISION CHECK: SELF ---
    # Check if the head coordinates match any segment in the rest of the body
    if snake_body[0] in snake_body[1:]:
        game_over = True

    # --- DRAWING / RENDERING ---
    screen.fill(BLACK)

    # Draw Snake
    for index, segment in enumerate(snake_body):
        # Make the head a slightly different color or just render the full body green
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE - 2, GRID_SIZE - 2))

    # Draw Food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE - 2, GRID_SIZE - 2))

    # Refresh screen
    pygame.display.update()

    # --- REGULATE GAME SPEED ---
    # Controls how fast the snake updates. Try increasing this as the score goes up!
    clock.tick(10)

# 4. GAME OVER CLEANUP
print(f"Game Over! Final Score: {score}")
pygame.quit()
sys.exit()