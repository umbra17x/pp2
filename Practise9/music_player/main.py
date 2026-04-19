import os
import pygame
from player import MusicPlayer


# Window settings
WIDTH = 900
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (60, 120, 220)
GRAY = (180, 180, 180)
LIGHT_GRAY = (230, 230, 230)


def draw_text(screen, text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()

    font_big = pygame.font.SysFont("Arial", 32)
    font_medium = pygame.font.SysFont("Arial", 24)
    font_small = pygame.font.SysFont("Arial", 20)

    music_folder = os.path.join(os.path.dirname(__file__), "music")
    player = MusicPlayer(music_folder)

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()

                elif event.key == pygame.K_s:
                    player.stop()

                elif event.key == pygame.K_n:
                    player.next_track()

                elif event.key == pygame.K_b:
                    player.previous_track()

                elif event.key == pygame.K_q:
                    running = False

        player.check_auto_next()

        # Drawing
        screen.fill(LIGHT_GRAY)

        draw_text(screen, "Simple Music Player", font_big, BLACK, 30, 20)

        draw_text(screen, "Keyboard controls:", font_medium, BLACK, 30, 80)
        draw_text(screen, "P = Play", font_small, BLACK, 50, 120)
        draw_text(screen, "S = Stop", font_small, BLACK, 50, 150)
        draw_text(screen, "N = Next track", font_small, BLACK, 50, 180)
        draw_text(screen, "B = Previous track", font_small, BLACK, 50, 210)
        draw_text(screen, "Q = Quit", font_small, BLACK, 50, 240)

        draw_text(screen, "Current track:", font_medium, BLUE, 30, 300)
        draw_text(screen, player.get_current_track_name(), font_medium, BLACK, 30, 335)

        progress = player.get_progress_seconds()
        draw_text(screen, f"Playback position: {progress} sec", font_medium, BLACK, 30, 380)

        status = "Stopped"
        if player.is_playing:
            status = "Playing"

        draw_text(screen, f"Status: {status}", font_medium, BLACK, 30, 420)

        draw_text(screen, "Playlist:", font_medium, BLUE, 500, 80)

        playlist_lines = player.get_playlist_info()
        if not playlist_lines:
            draw_text(screen, "No audio files in music folder", font_small, BLACK, 500, 120)
        else:
            y = 120
            for line in playlist_lines:
                draw_text(screen, line, font_small, BLACK, 500, y)
                y += 30

        pygame.display.flip()

    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    main()