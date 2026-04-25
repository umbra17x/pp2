import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Practice 11")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
PURPLE = (150, 0, 200)

font = pygame.font.SysFont("Arial", 24)

screen.fill(WHITE)

# Current shape
shape = "square"

running = True
while running:
    # Show instruction text
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 40))
    text = font.render(
        "1 Square | 2 Right Triangle | 3 Equilateral Triangle | 4 Rhombus",
        True,
        BLACK
    )
    screen.blit(text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Choose shape by keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "square"
            elif event.key == pygame.K_2:
                shape = "right_triangle"
            elif event.key == pygame.K_3:
                shape = "equilateral_triangle"
            elif event.key == pygame.K_4:
                shape = "rhombus"
            elif event.key == pygame.K_c:
                screen.fill(WHITE)

        # Draw shape by mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            size = 80

            # Draw square
            if shape == "square":
                pygame.draw.rect(screen, BLUE, (x, y, size, size), 3)

            # Draw right triangle
            elif shape == "right_triangle":
                points = [
                    (x, y),
                    (x, y + size),
                    (x + size, y + size)
                ]
                pygame.draw.polygon(screen, RED, points, 3)

            # Draw equilateral triangle
            elif shape == "equilateral_triangle":
                height = int(size * math.sqrt(3) / 2)
                points = [
                    (x, y),
                    (x - size // 2, y + height),
                    (x + size // 2, y + height)
                ]
                pygame.draw.polygon(screen, GREEN, points, 3)

            # Draw rhombus
            elif shape == "rhombus":
                points = [
                    (x, y - size // 2),
                    (x + size, y),
                    (x, y + size // 2),
                    (x - size, y)
                ]
                pygame.draw.polygon(screen, PURPLE, points, 3)

    pygame.display.update()

pygame.quit()