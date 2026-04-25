import pygame
import random

pygame.init()

# Window
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()

# Load images
road = pygame.image.load("AnimatedStreet.png")
player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")

# Resize images
player_img = pygame.transform.scale(player_img, (50, 80))
enemy_img = pygame.transform.scale(enemy_img, (50, 80))

# Sounds
crash_sound = pygame.mixer.Sound("crash.wav")
# pygame.mixer.music.load("background.wav")
# pygame.mixer.music.play(-1)

font = pygame.font.SysFont("Arial", 28)

# Player
player = player_img.get_rect(center=(200, 500))
player_speed = 5

# Enemy
enemy = enemy_img.get_rect(center=(random.randint(50, 350), -100))
enemy_speed = 5

# Coins
coin_radius = 15
coin_x = random.randint(50, 350)
coin_y = -30
coin_weight = random.choice([1, 2, 3])

score = 0
N = 5

running = True
while running:
    # Draw road
    screen.blit(road, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Enemy movement
    enemy.y += enemy_speed
    if enemy.top > HEIGHT:
        enemy.x = random.randint(50, 350)
        enemy.y = -100

    # Coin movement
    coin_y += 4
    if coin_y > HEIGHT:
        coin_x = random.randint(50, 350)
        coin_y = -30
        coin_weight = random.choice([1, 2, 3])

    coin_rect = pygame.Rect(coin_x - 15, coin_y - 15, 30, 30)

    # Collect coin
    if player.colliderect(coin_rect):
        score += coin_weight

        # Increase enemy speed
        if score % N == 0:
            enemy_speed += 1

        coin_x = random.randint(50, 350)
        coin_y = -30
        coin_weight = random.choice([1, 2, 3])

    # Collision
    if player.colliderect(enemy):
        crash_sound.play()
        pygame.time.delay(1000)
        running = False

    # Draw objects
    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)

    # Draw coin
    pygame.draw.circle(screen, (255, 215, 0), (coin_x, coin_y), coin_radius)
    weight_text = font.render(str(coin_weight), True, (0, 0, 0))
    screen.blit(weight_text, (coin_x - 7, coin_y - 10))

    # Score
    score_text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()