import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Fire Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player (fireball)
fireball_radius = 20
fireball_x = window_width // 2
fireball_y = window_height - fireball_radius * 2
fireball_speed = 5

# Set up the obstacle
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, window_width - obstacle_width)
obstacle_y = 0
obstacle_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the fireball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        fireball_x -= fireball_speed
    if keys[pygame.K_RIGHT]:
        fireball_x += fireball_speed

    # Move the obstacle
    obstacle_y += obstacle_speed

    # Check for collision
    if (
        obstacle_y + obstacle_height >= fireball_y
        and obstacle_y <= fireball_y + fireball_radius * 2
        and obstacle_x + obstacle_width >= fireball_x
        and obstacle_x <= fireball_x + fireball_radius * 2
    ):
        running = False

    # Check if obstacle reached the bottom
    if obstacle_y >= window_height:
        obstacle_x = random.randint(0, window_width - obstacle_width)
        obstacle_y = 0

    # Clear the window
    window.fill(WHITE)

    # Draw the fireball
    pygame.draw.circle(window, RED, (fireball_x, fireball_y), fireball_radius)

    # Draw the obstacle
    pygame.draw.rect(
        window, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    )

    # Update the display
    pygame.display.update()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
