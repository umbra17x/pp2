import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    # Canvas background color
    background_color = (0, 0, 0)
    screen.fill(background_color)

    # Brush settings
    radius = 8
    color = (0, 0, 255)  # default blue

    # Modes: pen, rectangle, circle, eraser
    tool = 'pen'

    # For free drawing
    drawing = False
    last_pos = None

    # For shapes
    start_pos = None
    current_pos = None

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # Quit events
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)   # red
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)   # green
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)   # blue
                elif event.key == pygame.K_y:
                    color = (255, 255, 0) # yellow
                elif event.key == pygame.K_w:
                    color = (255, 255, 255) # white

                # Tool selection
                elif event.key == pygame.K_p:
                    tool = 'pen'
                elif event.key == pygame.K_t:
                    tool = 'rectangle'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_e:
                    tool = 'eraser'

                # Brush size
                elif event.key == pygame.K_UP:
                    radius = min(50, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)

            # Mouse pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button
                    drawing = True
                    start_pos = event.pos
                    current_pos = event.pos
                    last_pos = event.pos

                    # For pen and eraser we start drawing immediately
                    if tool == 'pen':
                        pygame.draw.circle(screen, color, event.pos, radius)
                    elif tool == 'eraser':
                        pygame.draw.circle(screen, background_color, event.pos, radius)

            # Mouse released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if tool == 'rectangle' and start_pos and current_pos:
                        draw_rectangle(screen, color, start_pos, current_pos)
                    elif tool == 'circle' and start_pos and current_pos:
                        draw_circle(screen, color, start_pos, current_pos)

                    drawing = False
                    start_pos = None
                    current_pos = None
                    last_pos = None

            # Mouse motion
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_pos = event.pos

                    if tool == 'pen':
                        drawLineBetween(screen, last_pos, event.pos, radius, color)
                        last_pos = event.pos

                    elif tool == 'eraser':
                        drawLineBetween(screen, last_pos, event.pos, radius, background_color)
                        last_pos = event.pos

        # Draw preview for shapes
        temp_screen = screen.copy()

        if drawing and start_pos and current_pos:
            if tool == 'rectangle':
                draw_rectangle(temp_screen, color, start_pos, current_pos)
            elif tool == 'circle':
                draw_circle(temp_screen, color, start_pos, current_pos)

        # Show current frame
        if drawing and tool in ['rectangle', 'circle']:
            screen.blit(temp_screen, (0, 0))

        # Small info text
        font = pygame.font.SysFont("Verdana", 18)
        info = f"Tool: {tool} | Radius: {radius} | Keys: P-pen T-rect C-circle E-eraser R/G/B/Y/W-colors"
        text = font.render(info, True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 25))
        screen.blit(text, (5, 3))

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, start, end, width, color):
    """
    Draw a smooth thick line between two mouse positions.
    """
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    if iterations == 0:
        pygame.draw.circle(screen, color, start, width)
        return

    for i in range(iterations + 1):
        progress = i / iterations
        x = int(start[0] + (end[0] - start[0]) * progress)
        y = int(start[1] + (end[1] - start[1]) * progress)
        pygame.draw.circle(screen, color, (x, y), width)


def draw_rectangle(screen, color, start, end):
    """
    Draw rectangle using start and end mouse positions.
    """
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])

    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect, 2)


def draw_circle(screen, color, start, end):
    """
    Draw circle using bounding box from start and end positions.
    """
    x = (start[0] + end[0]) // 2
    y = (start[1] + end[1]) // 2

    radius_x = abs(start[0] - end[0]) // 2
    radius_y = abs(start[1] - end[1]) // 2

    radius = min(radius_x, radius_y)

    if radius > 0:
        pygame.draw.circle(screen, color, (x, y), radius, 2)


main()