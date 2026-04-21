import pygame
import random
import sys

# -----------------------------
# INITIALIZATION
# -----------------------------
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

# Grid size
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 30, 30)
GRAY = (70, 70, 70)
YELLOW = (255, 215, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 50)

# Clock
clock = pygame.time.Clock()

# Initial speed
snake_speed = 8

# -----------------------------
# WALLS
# -----------------------------
# Example walls inside the field
walls = [
    (10, 10), (11, 10), (12, 10), (13, 10),
    (18, 18), (18, 19), (18, 20), (18, 21),
    (5, 25), (6, 25), (7, 25), (8, 25),
]

# -----------------------------
# SNAKE SETTINGS
# -----------------------------
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)  # moving right
next_direction = direction

score = 0
level = 1

# How many foods are needed to pass each level
FOODS_PER_LEVEL = 4


# -----------------------------
# FOOD GENERATION
# -----------------------------
def generate_food():
    """
    Generates food in a random position.
    Food must not appear:
    1. On the snake
    2. On a wall
    """
    while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)

        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)


food = generate_food()


# -----------------------------
# DRAW FUNCTIONS
# -----------------------------
def draw_grid():
    """
    Draws grid lines.
    """
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def draw_walls():
    """
    Draws wall blocks.
    """
    for wall in walls:
        rect = pygame.Rect(wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect)


def draw_snake():
    """
    Draws snake head and body.
    """
    for i, segment in enumerate(snake):
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)

        if i == 0:
            pygame.draw.rect(screen, YELLOW, rect)  # head
        else:
            pygame.draw.rect(screen, GREEN, rect)   # body

        pygame.draw.rect(screen, BLACK, rect, 1)


def draw_food():
    """
    Draws food.
    """
    rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)


def draw_info():
    """
    Draws score, level and speed.
    """
    score_text = font_small.render(f"Score: {score}", True, WHITE)
    level_text = font_small.render(f"Level: {level}", True, WHITE)
    speed_text = font_small.render(f"Speed: {snake_speed}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))
    screen.blit(speed_text, (10, 60))


# -----------------------------
# GAME OVER SCREEN
# -----------------------------
def game_over():
    """
    Shows game over screen and exits the game.
    """
    screen.fill(BLACK)

    text1 = font_big.render("GAME OVER", True, RED)
    text2 = font_small.render(f"Final Score: {score}", True, WHITE)
    text3 = font_small.render(f"Level: {level}", True, WHITE)
    text4 = font_small.render("Press ESC to quit", True, WHITE)

    screen.blit(text1, text1.get_rect(center=(WIDTH // 2, 240)))
    screen.blit(text2, text2.get_rect(center=(WIDTH // 2, 320)))
    screen.blit(text3, text3.get_rect(center=(WIDTH // 2, 350)))
    screen.blit(text4, text4.get_rect(center=(WIDTH // 2, 400)))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


# -----------------------------
# MAIN GAME LOOP
# -----------------------------
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Change snake direction with arrow keys
            # Snake cannot move directly in the opposite direction
            if event.key == pygame.K_UP and direction != (0, 1):
                next_direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                next_direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                next_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                next_direction = (1, 0)

    # Update direction
    direction = next_direction

    # Calculate new head position
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # -----------------------------------
    # CHECK BORDER COLLISION
    # If snake leaves the playing area, game over
    # -----------------------------------
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS:
        game_over()

    # -----------------------------------
    # CHECK WALL COLLISION
    # -----------------------------------
    if new_head in walls:
        game_over()

    # -----------------------------------
    # CHECK SELF COLLISION
    # -----------------------------------
    if new_head in snake:
        game_over()

    # Move snake
    snake.insert(0, new_head)

    # -----------------------------------
    # CHECK FOOD COLLISION
    # -----------------------------------
    if new_head == food:
        score += 1
        food = generate_food()

        # -----------------------------------
        # LEVEL SYSTEM
        # Every 4 foods -> next level
        # -----------------------------------
        if score % FOODS_PER_LEVEL == 0:
            level += 1
            snake_speed += 2   # increase speed at next level

    else:
        # Remove tail if food was not eaten
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_grid()
    draw_walls()
    draw_snake()
    draw_food()
    draw_info()

    pygame.display.update()
    clock.tick(snake_speed)