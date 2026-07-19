# import pygame module in this program
import pygame

# activate the pygame library .
# initiate pygame and give permission to use pygame's functionality.
pygame.init()

# define the RGB value for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object of specific dimension (X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Image')

# Set up a clock to manage framerate smoothly
clock = pygame.time.Clock()

# create a surface object, image is drawn on it.
# NOTE: Make sure the file path below matches an actual image on your computer!
try:
    image = pygame.image.load(r'C:\Users\zohai\OneDrive\Pictures\geek.png')
except pygame.error:
    # Fallback if the image path doesn't exist so the script doesn't crash
    print("Warning: Image file not found. Creating a temporary placeholder surface.")
    image = pygame.Surface((200, 200))
    image.fill((0, 200, 255))

# Variable to keep our game loop running
running = True

# infinite loop
while running:
    # 1. ALWAYS handle events at the very beginning of the loop
    for event in pygame.event.get():
        # if event object type is QUIT
        if event.type == pygame.QUIT:
            running = False

    # 2. Clear/Fill the surface object with white colour
    display_surface.fill(white)

    # 3. Blit (copy) the image surface object to the display surface at (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    # 4. Update the actual display monitor
    pygame.display.update()

    # 5. Cap the framerate at 60 FPS to stop the window from freezing/lagging
    clock.tick(60)

# Cleanly exit out of the application
pygame.quit()
quit()