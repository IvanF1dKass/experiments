import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

x2 = 500
y1 = 10
y2 = 400

def draw_light (alpha):
    angle = alpha * math.pi / 180
    x3 = (y2 - y1) / math.tan(angle) + x2
    x1 = x2 - (y2 - y1) / math.tan(angle)

    pygame.draw.line(screen, WHITE, (x3, y1), (x2, y2), 1)
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 1)

x_pol = 500
y_pol = 500
left_x = 300
right_x = 700
is_grabbed_pol = False
R = 10
alpha = 5 + int(85 * (x_pol - left_x) / (right_x - left_x))

font = pygame.font.Font(None, 32)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if (x - x_pol)**2 + (y - y_pol)**2 <= R ** 2:
                is_grabbed_pol = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_grabbed_pol = False
        elif is_grabbed_pol and event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            x_pol += dx
            if x_pol > right_x:
                x_pol = right_x
            elif x_pol < left_x:
                x_pol = left_x
            alpha = 5 + int(85 * (x_pol - left_x) / (right_x - left_x))
    screen.fill(BLACK)
    draw_light(alpha)
    
    pygame.draw.line(screen, RED, (left_x, y_pol), (right_x, y_pol), 2)
    pygame.draw.circle(screen, GREEN, (x_pol, y_pol), R)
    pygame.draw.line(screen, GREEN, (0, y2), (1000, y2), 2)

    text = font.render(f'ТЕкст про углы = {alpha}', True, WHITE)
    screen.blit(text, (100, 600))

    pygame.display.update()
