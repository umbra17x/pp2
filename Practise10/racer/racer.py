# Imports
import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing pygame
pygame.init()
pygame.mixer.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Speed and score variables
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# Load images
background = pygame.image.load("AnimatedStreet.png")
player_image = pygame.image.load("Player.png")
enemy_image = pygame.image.load("Enemy.png")

# Load sounds
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)   # -1 means loop forever

# Coin image made by drawing a circle
def create_coin_surface():
    surface = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.circle(surface, GOLD, (15, 15), 15)
    pygame.draw.circle(surface, BLACK, (15, 15), 15, 2)
    pygame.draw.circle(surface, (255, 240, 120), (11, 11), 5)
    return surface


class Enemy(pygame.sprite.Sprite):
    """
    Enemy car class.
    Enemy moves from top to bottom.
    If it leaves the screen, it appears again from the top.
    """
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Random x position inside the road
        self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), random.randint(-150, -50))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # If enemy leaves the screen, increase score and reset position
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_position()


class Player(pygame.sprite.Sprite):
    """
    Player car class.
    Player can move left and right.
    """
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep the player inside the road borders
        if self.rect.left < 35:
            self.rect.left = 35

        if self.rect.right > SCREEN_WIDTH - 35:
            self.rect.right = SCREEN_WIDTH - 35


class Coin(pygame.sprite.Sprite):
    """
    Coin class.
    Coins appear randomly on the road and move downward.
    Player can collect them.
    """
    def __init__(self):
        super().__init__()
        self.image = create_coin_surface()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(80, SCREEN_WIDTH - 80), random.randint(-200, -40))

    def move(self):
        self.rect.move_ip(0, SPEED)

        # If coin leaves screen, remove it
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# Create player
P1 = Player()

# Create enemies
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1, E2, E3)

coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, E2, E3)

# User events
INC_SPEED = pygame.USEREVENT + 1
SPAWN_COIN = pygame.USEREVENT + 2

# Increase speed every 5 seconds
pygame.time.set_timer(INC_SPEED, 5000)

# Spawn a coin every 1.5 seconds
pygame.time.set_timer(SPAWN_COIN, 1500)


# Game loop
while True:

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Increase speed from time to time
        if event.type == INC_SPEED:
            SPEED += 0.5

        # Randomly create coins on the road
        if event.type == SPAWN_COIN:
            # Not every timer event creates a coin, for randomness
            if random.randint(1, 100) <= 80:
                new_coin = Coin()
                coins.add(new_coin)
                all_sprites.add(new_coin)

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Show score in top left corner
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # Show collected coins in top right corner
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        if hasattr(entity, "move"):
            entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check if player collects a coin
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    if collected_coins:
        COINS_COLLECTED += len(collected_coins)

    # Check collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        crash_sound.play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))

        final_score = font_small.render(f"Final Score: {SCORE}", True, BLACK)
        final_coins = font_small.render(f"Coins Collected: {COINS_COLLECTED}", True, BLACK)

        DISPLAYSURF.blit(final_score, (120, 330))
        DISPLAYSURF.blit(final_coins, (100, 360))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)