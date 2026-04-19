import pygame
from clock import MickeyClock

# Initialize pygame
pygame.init()

# Set window size
WIDTH = 800
HEIGHT = 800

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Create clock object (controls FPS)
clock = pygame.time.Clock()

# Create MickeyClock object
mickey = MickeyClock(screen, WIDTH, HEIGHT)

running = True
while running:
    # Handle events (close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update time
    mickey.update()

    # Draw everything
    mickey.draw()

    # Update display
    pygame.display.flip()

    # Limit updates to once per second
    clock.tick(1)

# Quit pygame
pygame.quit()