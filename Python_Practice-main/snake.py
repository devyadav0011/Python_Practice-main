import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
FPS = 10

# Colors (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def new_food():
    """Generate new food position not overlapping snake."""
    while True:
        food = (random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE))
        if food not in snake:
            return food

# Initial snake: list of (x, y) tuples
snake = [(10 * CELL_SIZE, 10 * CELL_SIZE),
         (9 * CELL_SIZE, 10 * CELL_SIZE),
         (8 * CELL_SIZE, 10 * CELL_SIZE)]
direction = (CELL_SIZE, 0)  # Initial direction: right
food = new_food()
score = 0

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                # Restart game
                snake = [(10 * CELL_SIZE, 10 * CELL_SIZE),
                         (9 * CELL_SIZE, 10 * CELL_SIZE),
                         (8 * CELL_SIZE, 10 * CELL_SIZE)]
                direction = (CELL_SIZE, 0)
                food = new_food()
                score = 0
                game_over = False

    if not game_over:
        # Move snake
        head = snake[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])
        snake.insert(0, new_head)

        # Check food collision
        if new_head == food:
            score += 1
            food = new_food()
        else:
            snake.pop()

        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake):
            game_over = True

    # Draw everything
    screen.fill(BLACK)
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render('Game Over! Press SPACE to restart', True, WHITE)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()