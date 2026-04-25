import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Practice 11")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)

font = pygame.font.SysFont("Arial", 25)

# Snake settings
snake = [(100, 100)]
dx, dy = CELL, 0
snake_speed = 10

score = 0

# Function for creating random food
def create_food():
    x = random.randrange(0, WIDTH, CELL)
    y = random.randrange(0, HEIGHT, CELL)
    weight = random.choice([1, 2, 3])
    start_time = time.time()
    return x, y, weight, start_time

food_x, food_y, food_weight, food_time = create_food()
food_life = 5  # food disappears after 5 seconds

running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)
    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == (food_x, food_y):
        score += food_weight

        # Snake grows according to food weight
        for i in range(food_weight - 1):
            snake.append(snake[-1])

        food_x, food_y, food_weight, food_time = create_food()
    else:
        snake.pop()

    # Food disappears after timer
    if time.time() - food_time > food_life:
        food_x, food_y, food_weight, food_time = create_food()

    # Collision with walls
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT
    ):
        running = False

    # Collision with itself
    if new_head in snake[1:]:
        running = False

    # Draw snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (food_x, food_y, CELL, CELL))

    # Draw food weight
    weight_text = font.render(str(food_weight), True, YELLOW)
    screen.blit(weight_text, (food_x + 4, food_y - 3))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()