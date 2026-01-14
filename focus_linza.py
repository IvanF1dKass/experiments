import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

shrift = pygame.font.Font(None, 32)

FPS = 60

x_object = 250
y_object = 220
R_object = 10

F_y = 350

y_line = 350
x1_line = 0
x2_line = 1000
x_prism = 500
y1_prism = 200
y2_prism = 500
is_grabbed_object = False

F = 150
F_x1 = x_prism + F
F_x2 = x_prism - F

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if (x - x_object)**2 + (y - y_object)**2 <= R_object ** 2:
                is_grabbed_object = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_grabbed_object = False
        elif is_grabbed_object and event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            x_object += dx
            y_object += dy
            if x_object > x_prism - 60:
                x_object = x_prism - 60
            if x_object < 20:
                x_object = 20
            if y_object < y1_prism:
                y_object = y1_prism
            if y_object > y2_prism:
                y_object = y2_prism
        
    screen.fill(BLACK)
    d = x_prism - x_object
    h = y_line - y_object
    if d > F:
        f = F*d/(d-F)
        H = f*h/d
        pygame.draw.line(screen, RED, (x_object, y_object), (x_prism + f + 5*(x_prism + f - x_object), y_line + H + 5*(y_line + H - y_object)), 2)
        pygame.draw.line(screen, RED, (x_prism, y_object),(x_prism + f + 5*f, y_line + H + 5*(y_line + H - y_object)), 2)
        pygame.draw.line(screen, RED, (x_object, y_object), (x_prism, y_object), 2)
        text = shrift.render('действительное изображение', True, WHITE)
        screen.blit(text, (100, 600))
    elif F == d:
        pygame.draw.line(screen, GREEN, (x_prism, y_object), (F_x1 + 3*(-x_prism + F_x1), y_line + 3*(-y_object + y_line)), 2)
        pygame.draw.line(screen, GREEN, (x_object, y_object), (x_prism + 5*(-x_prism + F_x1), y_line + 5*(-y_object + y_line)), 2)
        pygame.draw.line(screen, GREEN, (x_object, y_object), (x_prism, y_object), 2)
    if d < F:
        f = F*d/(d-F)
        H = f*h/d
        pygame.draw.line(screen, BLUE,(x_prism + f - 5*( -(x_prism + f) + x_object), y_line + H - 5*(-(y_line + H) + y_object)), (x_object, y_object), 2)
        pygame.draw.line(screen, BLUE, (x_prism + f - 5*(-f), y_line + H - 5*(-y_line -H + y_object)), (x_prism, y_object), 2)
        pygame.draw.line(screen, BLUE, (x_object, y_object), (x_prism, y_object), 2)

    
    pygame.draw.line(screen, WHITE, (x1_line, y_line), (x2_line, y_line), 2)
    pygame.draw.line(screen, WHITE, (x_prism, y1_prism), (x_prism, y2_prism), 6)
    pygame.draw.line(screen, WHITE, (x_prism, y1_prism), (x_prism - 20, y1_prism + 20), 6)
    pygame.draw.line(screen, WHITE, (x_prism, y1_prism), (x_prism + 20, y1_prism + 20), 6)
    pygame.draw.line(screen, WHITE, (x_prism, y2_prism), (x_prism - 20, y2_prism - 20), 6)
    pygame.draw.line(screen, WHITE, (x_prism, y2_prism), (x_prism + 20, y2_prism - 20), 6)
    pygame.draw.circle(screen, GREEN, (x_object, y_object), R_object)
    pygame.draw.line(screen, WHITE, (F_x1, F_y + 10), (F_x1, F_y - 10), 2)
    pygame.draw.line(screen, WHITE, (F_x2, F_y + 10), (F_x2, F_y - 10), 2)
    pygame.display.update()
    