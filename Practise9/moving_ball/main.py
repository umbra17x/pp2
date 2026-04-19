import pygame
from ball import Ball


# Window settings
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Red Ball")

    clock = pygame.time.Clock()

    # Ball settings
    radius = 25
    step = 20

    ball = Ball(
        x=WIDTH // 2,
        y=HEIGHT // 2,
        radius=radius,
        color=RED,
        screen_width=WIDTH,
        screen_height=HEIGHT,
        step=step
    )

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move_up()
                elif event.key == pygame.K_DOWN:
                    ball.move_down()
                elif event.key == pygame.K_LEFT:
                    ball.move_left()
                elif event.key == pygame.K_RIGHT:
                    ball.move_right()

        screen.fill(WHITE)
        ball.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()