# Inport pygame by running the code pip install pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 800
window_height = 600

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption('Pong')

# Set the background color of the window
window.fill((0, 0, 0))

# Create the ball
ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_color = (255, 255, 255)

# Create the paddles
paddle_width = 15
paddle_height = 100
paddle_color = (255, 255, 255)
left_paddle_x = 10
right_paddle_x = window_width - 10 - paddle_width
left_paddle_y = right_paddle_y = (window_height - paddle_height) // 2

# Set the initial velocity of the ball
ball_vx = 3
ball_vy = 3

# Set the initial scores
left_score = 0
right_score = 0

# Set the font for the scores
font = pygame.font.Font(None, 36)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                left_paddle_y = max(0, left_paddle_y - 5)
            elif event.key == pygame.K_DOWN:
                left_paddle_y = min(window_height - paddle_height, left_paddle_y + 5)

    # Update the ball position
    ball_x += ball_vx
    ball_y += ball_vy

    # Check for ball collision with paddles
    if ball_x < left_paddle_x + paddle_width and ball_y > left_paddle_y and ball_y < left_paddle_y + paddle_height:
        ball_vx = -ball_vx
    elif ball_x + ball_radius > right_paddle_x and ball_y > right_paddle_y and ball_y < right_paddle_y + paddle_height:
        ball_vx = -ball_vx

    # Check for ball collision with top and bottom of screen
    if ball_y < 0 or ball_y + ball_radius > window_height:
        ball_vy = -ball_vy

    # Check for ball scoring
    if ball_x < 0:
        right_score += 1
        ball_x = window_width // 2
        ball_y = window_height // 2
    elif ball_x + ball_radius > window_width:
        left_score += 1
        ball_x = window_width // 2
        ball_y = window_height // 2

    # Clear the window
    window.fill((0,
