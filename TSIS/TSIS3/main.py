import pygame
from racer import RacerGame
from ui import Button, draw_text
from persistance import load_settings, save_settings, load_leaderboard

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Racer")

font = pygame.font.SysFont("Arial", 28)
clock = pygame.time.Clock()

settings = load_settings()


def get_username():
    name = ""
    active = True

    while active:
        screen.fill((255, 255, 255))
        draw_text(screen, "Enter your name:", 28, WIDTH // 2, 200)
        draw_text(screen, name + "|", 28, WIDTH // 2, 260)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Player"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

    return name


def main_menu():
    buttons = [
        Button(100, 180, 200, 50, "Play"),
        Button(100, 250, 200, 50, "Leaderboard"),
        Button(100, 320, 200, 50, "Settings"),
        Button(100, 390, 200, 50, "Quit")
    ]

    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, "Racer Game", 40, WIDTH // 2, 100)

        for button in buttons:
            button.draw(screen, font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons[0].is_clicked(pos):
                    return "play"
                elif buttons[1].is_clicked(pos):
                    return "leaderboard"
                elif buttons[2].is_clicked(pos):
                    return "settings"
                elif buttons[3].is_clicked(pos):
                    return "quit"


def leaderboard_screen():
    leaderboard = load_leaderboard()
    back = Button(100, 520, 200, 50, "Back")

    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, "Top 10 Scores", 35, WIDTH // 2, 50)

        y = 110
        for i, item in enumerate(leaderboard):
            text = f"{i + 1}. {item['name']} | {item['score']} | {item['distance']}m"
            surface = font.render(text, True, (0, 0, 0))
            screen.blit(surface, (30, y))
            y += 35

        back.draw(screen, font)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.is_clicked(event.pos):
                    return "menu"


def settings_screen():
    global settings

    buttons = [
        Button(80, 170, 240, 50, "Toggle Sound"),
        Button(80, 240, 240, 50, "Change Car Color"),
        Button(80, 310, 240, 50, "Change Difficulty"),
        Button(80, 450, 240, 50, "Back")
    ]

    colors = ["blue", "red", "green"]
    difficulties = ["easy", "normal", "hard"]

    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, "Settings", 36, WIDTH // 2, 80)

        draw_text(screen, f"Sound: {settings['sound']}", 22, WIDTH // 2, 130)
        draw_text(screen, f"Car: {settings['car_color']}", 22, WIDTH // 2, 370)
        draw_text(screen, f"Difficulty: {settings['difficulty']}", 22, WIDTH // 2, 400)

        for button in buttons:
            button.draw(screen, font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if buttons[0].is_clicked(pos):
                    settings["sound"] = not settings["sound"]

                elif buttons[1].is_clicked(pos):
                    index = colors.index(settings["car_color"])
                    settings["car_color"] = colors[(index + 1) % len(colors)]

                elif buttons[2].is_clicked(pos):
                    index = difficulties.index(settings["difficulty"])
                    settings["difficulty"] = difficulties[(index + 1) % len(difficulties)]

                elif buttons[3].is_clicked(pos):
                    save_settings(settings)
                    return "menu"


def game_over_screen():
    buttons = [
        Button(100, 260, 200, 50, "Retry"),
        Button(100, 330, 200, 50, "Main Menu")
    ]

    while True:
        screen.fill((255, 255, 255))
        draw_text(screen, "Game Over", 40, WIDTH // 2, 150)

        for button in buttons:
            button.draw(screen, font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].is_clicked(event.pos):
                    return "retry"
                elif buttons[1].is_clicked(event.pos):
                    return "menu"


def main():
    while True:
        action = main_menu()

        if action == "quit":
            break

        elif action == "play":
            username = get_username()

            while True:
                game = RacerGame(screen, username, settings)
                result = game.run()

                if result == "quit":
                    pygame.quit()
                    return

                over_action = game_over_screen()

                if over_action == "retry":
                    continue
                elif over_action == "menu":
                    break
                elif over_action == "quit":
                    pygame.quit()
                    return

        elif action == "leaderboard":
            result = leaderboard_screen()
            if result == "quit":
                break

        elif action == "settings":
            result = settings_screen()
            if result == "quit":
                break

    pygame.quit()


main()