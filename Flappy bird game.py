import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
jump_strength = -10

# Pipe settings
pipe_width = 70
pipe_gap = 150
pipe_velocity = 3
pipes = []

score = 0
game_over = False

# Add a new pipe
def add_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
    pipes.append((top_pipe, bottom_pipe))

# Main game loop
running = True
add_pipe()
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = jump_strength
            if event.key == pygame.K_r and game_over:
                # Restart the game
                bird_y = HEIGHT // 2
                bird_velocity = 0
                pipes.clear()
                add_pipe()
                score = 0
                game_over = False

    if not game_over:
        bird_velocity += gravity
        bird_y += bird_velocity

        # Move and manage pipes
        for i, (top_pipe, bottom_pipe) in enumerate(pipes):
            top_pipe.x -= pipe_velocity
            bottom_pipe.x -= pipe_velocity
            if top_pipe.right < 0:
                pipes.pop(i)
                add_pipe()
                score += 1

        # Add new pipes if needed
        if pipes[-1][0].x < WIDTH - 200:
            add_pipe()

        # Check collisions
        for top_pipe, bottom_pipe in pipes:
            if top_pipe.collidepoint(bird_x, bird_y) or bottom_pipe.collidepoint(bird_x, bird_y):
                game_over = True
        if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
            game_over = True

    # Draw bird
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), bird_radius)

    # Draw pipes
    for top_pipe, bottom_pipe in pipes:
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)

    # Draw score
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    # Game over message
    if game_over:
        over_text = font.render("Game Over! Press R to restart", True, RED)
        screen.blit(over_text, (20, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
