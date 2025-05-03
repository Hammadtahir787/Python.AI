
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pac-Man settings
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5
direction = 'STOP'

# Dots
dots = []
dot_radius = 5
for x in range(50, WIDTH, 50):
    for y in range(50, HEIGHT, 50):
        dots.append(pygame.Rect(x, y, dot_radius * 2, dot_radius * 2))

# Enemies
enemies = []
num_enemies = 3
enemy_speed = 3
for _ in range(num_enemies):
    ex = random.randint(0, WIDTH)
    ey = random.randint(0, HEIGHT)
    enemies.append(pygame.Rect(ex, ey, 20, 20))

# Main game loop
running = True
game_over = False
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'

    if not game_over:
        # Move Pac-Man
        if direction == 'LEFT':
            pacman_x -= pacman_speed
        elif direction == 'RIGHT':
            pacman_x += pacman_speed
        elif direction == 'UP':
            pacman_y -= pacman_speed
        elif direction == 'DOWN':
            pacman_y += pacman_speed

        # Keep Pac-Man inside screen
        pacman_x = max(0, min(WIDTH, pacman_x))
        pacman_y = max(0, min(HEIGHT, pacman_y))

        # Move enemies randomly
        for enemy in enemies:
            move_dir = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
            if move_dir == 'LEFT':
                enemy.x -= enemy_speed
            elif move_dir == 'RIGHT':
                enemy.x += enemy_speed
            elif move_dir == 'UP':
                enemy.y -= enemy_speed
            elif move_dir == 'DOWN':
                enemy.y += enemy_speed

            # Keep enemies inside screen
            enemy.x = max(0, min(WIDTH - 20, enemy.x))
            enemy.y = max(0, min(HEIGHT - 20, enemy.y))

        # Check collision with dots
        for dot in dots[:]:
            if dot.collidepoint(pacman_x, pacman_y):
                dots.remove(dot)

        # Check collision with enemies
        pacman_rect = pygame.Rect(pacman_x - 15, pacman_y - 15, 30, 30)
        for enemy in enemies:
            if pacman_rect.colliderect(enemy):
                game_over = True

    # Draw dots
    for dot in dots:
        pygame.draw.circle(screen, WHITE, dot.center, dot_radius)

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), 15)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Game over message
    if game_over:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))

    pygame.display.flip()
