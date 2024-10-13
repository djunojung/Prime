# First, you need to install Pygame. You can do this by running:
# pip install pygame
# in your command line or terminal.

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Ball")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_width = 100
player_height = 20
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5

# Ball
ball_size = 20
ball_x = random.randint(0, width - ball_size)
ball_y = 0
ball_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Move the ball
    ball_y += ball_speed

    # Check for collision
    if ball_y + ball_size >= player_y and player_x < ball_x < player_x + player_width:
        score += 1
        ball_x = random.randint(0, width - ball_size)
        ball_y = 0
        ball_speed += 0.5

    # Check if ball is out of bounds
    if ball_y > height:
        ball_x = random.randint(0, width - ball_size)
        ball_y = 0

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Draw the ball
    pygame.draw.circle(screen, BLUE, (ball_x, int(ball_y)), ball_size // 2)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)