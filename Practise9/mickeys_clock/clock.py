import pygame
from datetime import datetime


class MickeyClock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        # Load images from the images folder
        self.background = pygame.image.load("images/mickeyclock.png").convert_alpha()
        self.right_hand = pygame.image.load("images/right_hand.png").convert_alpha()
        self.left_hand = pygame.image.load("images/left_hand.png").convert_alpha()

        # Scale background to fit window
        self.background = pygame.transform.scale(self.background, (width, height))

        # Set clock center
        self.center_x = width // 2
        self.center_y = height // 2

        # Time values
        self.minutes = 0
        self.seconds = 0

    def update(self):
        # Get current system time
        now = datetime.now()
        self.minutes = now.minute
        self.seconds = now.second

    def draw_rotated(self, image, angle, x, y):
        # Rotate image around its center
        rotated_image = pygame.transform.rotate(image, -angle)

        # Set rotated image position
        rect = rotated_image.get_rect(center=(x, y))

        # Draw rotated image
        self.screen.blit(rotated_image, rect.topleft)

    def draw(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))

        # Calculate angles
        minute_angle = self.minutes * 6
        second_angle = self.seconds * 6

        # Draw minute and second hands
        self.draw_rotated(self.right_hand, minute_angle, self.center_x, self.center_y)
        self.draw_rotated(self.left_hand, second_angle, self.center_x, self.center_y)

        # Draw center point
        pygame.draw.circle(self.screen, (0, 0, 0), (self.center_x, self.center_y), 6)