import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont("Arial", size)
    surface = font.render(text, True, BLACK)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)