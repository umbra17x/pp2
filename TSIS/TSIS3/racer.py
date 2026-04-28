import pygame
import random
import time
import os
from persistance import save_score

WIDTH, HEIGHT = 400, 600
ASSETS = "assets"


class RacerGame:
    def __init__(self, screen, username, settings):
        self.screen = screen
        self.username = username
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)

        # Load images
        self.road_img = pygame.image.load(os.path.join(ASSETS, "AnimatedStreet.png"))
        self.player_img = pygame.image.load(os.path.join(ASSETS, "Player.png"))
        self.enemy_img = pygame.image.load(os.path.join(ASSETS, "Enemy.png"))

        self.road_img = pygame.transform.scale(self.road_img, (WIDTH, HEIGHT))
        self.player_img = pygame.transform.scale(self.player_img, (50, 80))
        self.enemy_img = pygame.transform.scale(self.enemy_img, (50, 80))

        # Load sounds
        self.crash_sound = pygame.mixer.Sound(os.path.join(ASSETS, "crash.wav"))

        if self.settings["sound"]:
            pygame.mixer.music.load(os.path.join(ASSETS, "background.wav"))
            pygame.mixer.music.play(-1)

        # Player
        self.player = self.player_img.get_rect(center=(WIDTH // 2, 500))
        self.player_speed = 6

        # Game objects
        self.traffic = []
        self.obstacles = []
        self.powerups = []
        self.coins_list = []

        # Score
        self.coins = 0
        self.score = 0
        self.distance = 0
        self.finish_distance = 2000

        # Power-ups
        self.shield = False
        self.active_power = None
        self.power_end_time = 0

        # Timers
        self.spawn_timer = 0
        self.power_timer = 0
        self.coin_timer = 0

        self.running = True

        # Difficulty
        if settings["difficulty"] == "easy":
            self.enemy_speed = 4
        elif settings["difficulty"] == "hard":
            self.enemy_speed = 8
        else:
            self.enemy_speed = 6

    def safe_x(self):
        while True:
            x = random.randint(40, WIDTH - 90)
            if abs(x - self.player.x) > 80:
                return x

    def spawn_traffic(self):
        car = self.enemy_img.get_rect(topleft=(self.safe_x(), -90))
        self.traffic.append(car)

    def spawn_obstacle(self):
        rect = pygame.Rect(self.safe_x(), -40, 50, 35)
        kind = random.choice(["oil", "barrier", "pothole"])
        self.obstacles.append([rect, kind])

    def spawn_powerup(self):
        rect = pygame.Rect(self.safe_x(), -30, 30, 30)
        kind = random.choice(["nitro", "shield", "repair"])
        created_time = time.time()
        self.powerups.append([rect, kind, created_time])

    def spawn_coin(self):
        rect = pygame.Rect(self.safe_x(), -25, 25, 25)
        weight = random.choice([1, 2, 3])
        self.coins_list.append([rect, weight])

    def activate_powerup(self, kind):
        if self.active_power is not None:
            return

        self.active_power = kind

        if kind == "nitro":
            self.player_speed = 10
            self.power_end_time = time.time() + 4

        elif kind == "shield":
            self.shield = True

        elif kind == "repair":
            if self.obstacles:
                self.obstacles.pop(0)
            self.active_power = None

    def update_powerup(self):
        if self.active_power == "nitro" and time.time() > self.power_end_time:
            self.player_speed = 6
            self.active_power = None

    def handle_collision(self):
        for car in self.traffic[:]:
            if self.player.colliderect(car):
                if self.shield:
                    self.shield = False
                    self.active_power = None
                    self.traffic.remove(car)
                else:
                    if self.settings["sound"]:
                        self.crash_sound.play()
                    self.running = False

        for obstacle_data in self.obstacles[:]:
            obstacle, kind = obstacle_data

            if self.player.colliderect(obstacle):
                if kind == "oil":
                    self.player_speed = 3

                elif kind == "barrier":
                    if self.shield:
                        self.shield = False
                        self.active_power = None
                        self.obstacles.remove(obstacle_data)
                    else:
                        if self.settings["sound"]:
                            self.crash_sound.play()
                        self.running = False

                elif kind == "pothole":
                    self.score -= 20
                    self.obstacles.remove(obstacle_data)

    def draw_ui(self):
        texts = [
            f"Name: {self.username}",
            f"Score: {self.score}",
            f"Coins: {self.coins}",
            f"Distance: {self.distance}/{self.finish_distance}",
            f"Power: {self.active_power if self.active_power else 'None'}"
        ]

        y = 10
        for text in texts:
            surface = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(surface, (10, y))
            y += 25

    def draw_obstacle(self, obstacle, kind):
        if kind == "oil":
            color = (0, 0, 0)
        elif kind == "barrier":
            color = (160, 80, 40)
        else:
            color = (80, 80, 80)

        pygame.draw.rect(self.screen, color, obstacle)

    def draw_powerup(self, rect, kind):
        if kind == "nitro":
            color = (0, 255, 255)
        elif kind == "shield":
            color = (255, 255, 0)
        else:
            color = (0, 255, 0)

        pygame.draw.rect(self.screen, color, rect)
        label = self.font.render(kind[0].upper(), True, (0, 0, 0))
        self.screen.blit(label, (rect.x + 7, rect.y + 3))

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.player.left > 0:
                self.player.x -= self.player_speed
            if keys[pygame.K_RIGHT] and self.player.right < WIDTH:
                self.player.x += self.player_speed
            if keys[pygame.K_UP] and self.player.top > 0:
                self.player.y -= self.player_speed
            if keys[pygame.K_DOWN] and self.player.bottom < HEIGHT:
                self.player.y += self.player_speed

            self.distance += 1
            self.score = self.distance + self.coins * 10

            if self.distance >= self.finish_distance:
                self.running = False

            self.spawn_timer += 1
            self.power_timer += 1
            self.coin_timer += 1

            difficulty_bonus = self.distance // 500

            if self.spawn_timer > max(25, 70 - difficulty_bonus * 10):
                self.spawn_traffic()

                if random.randint(1, 3) == 1:
                    self.spawn_obstacle()

                self.spawn_timer = 0

            if self.power_timer > 300:
                self.spawn_powerup()
                self.power_timer = 0

            if self.coin_timer > 100:
                self.spawn_coin()
                self.coin_timer = 0

            for car in self.traffic:
                car.y += self.enemy_speed

            for obstacle, kind in self.obstacles:
                obstacle.y += self.enemy_speed

            for powerup in self.powerups:
                powerup[0].y += self.enemy_speed

            for coin in self.coins_list:
                coin[0].y += self.enemy_speed

            self.traffic = [car for car in self.traffic if car.y < HEIGHT]
            self.obstacles = [o for o in self.obstacles if o[0].y < HEIGHT]
            self.coins_list = [c for c in self.coins_list if c[0].y < HEIGHT]

            self.powerups = [
                p for p in self.powerups
                if p[0].y < HEIGHT and time.time() - p[2] < 6
            ]

            for powerup in self.powerups[:]:
                rect, kind, created = powerup

                if self.player.colliderect(rect):
                    self.activate_powerup(kind)
                    self.powerups.remove(powerup)

            for coin in self.coins_list[:]:
                rect, weight = coin

                if self.player.colliderect(rect):
                    self.coins += weight
                    self.coins_list.remove(coin)

            self.update_powerup()
            self.handle_collision()

            # Draw road
            self.screen.blit(self.road_img, (0, 0))

            # Draw player
            self.screen.blit(self.player_img, self.player)

            # Draw traffic
            for car in self.traffic:
                self.screen.blit(self.enemy_img, car)

            # Draw obstacles
            for obstacle, kind in self.obstacles:
                self.draw_obstacle(obstacle, kind)

            # Draw power-ups
            for rect, kind, created in self.powerups:
                self.draw_powerup(rect, kind)

            # Draw coins
            for rect, weight in self.coins_list:
                pygame.draw.circle(self.screen, (255, 215, 0), rect.center, 13)
                text = self.font.render(str(weight), True, (0, 0, 0))
                self.screen.blit(text, (rect.x + 7, rect.y))

            self.draw_ui()

            pygame.display.update()

        pygame.mixer.music.stop()
        save_score(self.username, self.score, self.distance)
        return "game_over"