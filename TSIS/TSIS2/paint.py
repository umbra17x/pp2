import pygame
import math
from tools import flood_fill, save_canvas

pygame.init()

WIDTH, HEIGHT = 1000, 700
TOOLBAR_HEIGHT = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")

clock = pygame.time.Clock()

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill((255, 255, 255))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 220, 0)
PURPLE = (150, 0, 200)

colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, WHITE]

current_color = BLACK
current_tool = "pencil"
brush_size = 5

font = pygame.font.SysFont("Arial", 22)
text_font = pygame.font.SysFont("Arial", 32)

drawing = False
start_pos = None
last_pos = None

typing = False
text_pos = None
text_value = ""


def canvas_pos(pos):
    return pos[0], pos[1] - TOOLBAR_HEIGHT


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    info = (
        f"Tool: {current_tool} | Size: {brush_size} | "
        "Keys: P pencil, L line, R rect, C circle, E eraser, F fill, T text, "
        "S square, A right triangle, Q eq triangle, D rhombus | 1/2/3 size | Ctrl+S save"
    )

    text = font.render(info, True, BLACK)
    screen.blit(text, (10, 10))

    for i, color in enumerate(colors):
        rect = pygame.Rect(10 + i * 40, 45, 30, 25)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)


def draw_shape(surface, tool, start, end, color, size):
    x1, y1 = start
    x2, y2 = end

    rect = pygame.Rect(
        min(x1, x2),
        min(y1, y2),
        abs(x2 - x1),
        abs(y2 - y1)
    )

    if tool == "line":
        pygame.draw.line(surface, color, start, end, size)

    elif tool == "rect":
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "circle":
        radius = int(math.dist(start, end))
        pygame.draw.circle(surface, color, start, radius, size)

    elif tool == "square":
        side = max(abs(x2 - x1), abs(y2 - y1))
        square_rect = pygame.Rect(x1, y1, side, side)
        pygame.draw.rect(surface, color, square_rect, size)

    elif tool == "right_triangle":
        points = [
            (x1, y1),
            (x1, y2),
            (x2, y2)
        ]
        pygame.draw.polygon(surface, color, points, size)

    elif tool == "equilateral_triangle":
        side = abs(x2 - x1)
        height = int(side * math.sqrt(3) / 2)
        points = [
            (x1, y1),
            (x1 - side // 2, y1 + height),
            (x1 + side // 2, y1 + height)
        ]
        pygame.draw.polygon(surface, color, points, size)

    elif tool == "rhombus":
        cx, cy = x1, y1
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        points = [
            (cx, cy - dy),
            (cx + dx, cy),
            (cx, cy + dy),
            (cx - dx, cy)
        ]
        pygame.draw.polygon(surface, color, points, size)


running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    draw_toolbar()

    mouse_pos = pygame.mouse.get_pos()
    mouse_on_canvas = mouse_pos[1] > TOOLBAR_HEIGHT

    # Live preview
    if drawing and start_pos and current_tool not in ["pencil", "eraser"] and mouse_on_canvas:
        preview = canvas.copy()
        draw_shape(
            preview,
            current_tool,
            start_pos,
            canvas_pos(mouse_pos),
            current_color,
            brush_size
        )
        screen.blit(preview, (0, TOOLBAR_HEIGHT))

    # Text preview
    if typing and text_pos:
        preview_text = text_font.render(text_value + "|", True, current_color)
        screen.blit(preview_text, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LCTRL] and event.key == pygame.K_s:
                save_canvas(canvas)

            elif typing:
                if event.key == pygame.K_RETURN:
                    final_text = text_font.render(text_value, True, current_color)
                    canvas.blit(final_text, text_pos)
                    typing = False
                    text_value = ""
                    text_pos = None

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_value = ""
                    text_pos = None

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]

                else:
                    text_value += event.unicode

            else:
                if event.key == pygame.K_p:
                    current_tool = "pencil"
                elif event.key == pygame.K_l:
                    current_tool = "line"
                elif event.key == pygame.K_r:
                    current_tool = "rect"
                elif event.key == pygame.K_c:
                    current_tool = "circle"
                elif event.key == pygame.K_e:
                    current_tool = "eraser"
                elif event.key == pygame.K_f:
                    current_tool = "fill"
                elif event.key == pygame.K_t:
                    current_tool = "text"
                elif event.key == pygame.K_s:
                    current_tool = "square"
                elif event.key == pygame.K_a:
                    current_tool = "right_triangle"
                elif event.key == pygame.K_q:
                    current_tool = "equilateral_triangle"
                elif event.key == pygame.K_d:
                    current_tool = "rhombus"

                elif event.key == pygame.K_1:
                    brush_size = 2
                elif event.key == pygame.K_2:
                    brush_size = 5
                elif event.key == pygame.K_3:
                    brush_size = 10

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos

                # Color picker
                if y < TOOLBAR_HEIGHT:
                    for i, color in enumerate(colors):
                        rect = pygame.Rect(10 + i * 40, 45, 30, 25)
                        if rect.collidepoint(event.pos):
                            current_color = color

                else:
                    pos = canvas_pos(event.pos)

                    if current_tool == "fill":
                        flood_fill(canvas, pos, current_color)

                    elif current_tool == "text":
                        typing = True
                        text_pos = pos
                        text_value = ""

                    else:
                        drawing = True
                        start_pos = pos
                        last_pos = pos

        # Mouse movement
        if event.type == pygame.MOUSEMOTION:
            if drawing and mouse_on_canvas:
                pos = canvas_pos(event.pos)

                if current_tool == "pencil":
                    pygame.draw.line(canvas, current_color, last_pos, pos, brush_size)
                    last_pos = pos

                elif current_tool == "eraser":
                    pygame.draw.line(canvas, WHITE, last_pos, pos, brush_size)
                    last_pos = pos

        # Mouse release
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = canvas_pos(event.pos)

                if current_tool not in ["pencil", "eraser"]:
                    draw_shape(
                        canvas,
                        current_tool,
                        start_pos,
                        end_pos,
                        current_color,
                        brush_size
                    )

                drawing = False
                start_pos = None
                last_pos = None

    pygame.display.update()
    clock.tick(60)

pygame.quit()