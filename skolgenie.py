import pygame
import math

WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)

YELLOW      = (255, 255, 0)
CYAN        = (0, 255, 255)
MAGENTA     = (255, 0, 255)

ORANGE      = (255, 165, 0)
PURPLE      = (128, 0, 128)
PINK        = (255, 105, 180)
BROWN       = (139, 69, 19)
GRAY        = (128, 128, 128)
LIGHT_GRAY  = (200, 200, 200)
DARK_GRAY   = (50, 50, 50)

LIGHT_BLUE_1 = (149, 212, 222)
BLUE_GRAY_2 = (116, 184, 193)
DIRTY_BLUE_3 = (100, 164, 173)
DARK_ORANGE_4 = (223, 127, 93)
BEIGE_FON = (253, 245, 228)
FPS = 60

pygame.init()
font = pygame.font.Font(None, 100)
font1 = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()


Ox = xu = x1_line = 20
Ax = x2_line = 600
yu = y_line = 500
b = (Ax - xu)
Oy = y_vert_line = 250
a = yu - Oy
d = 40
h = 25
m = 10
k = 5
g = 10
alpha = 40
Vp = 0
Xt = Xp = 0

x_pol = 700 + 200
y_pol = 250
R = 10
right_x = 1100
left_x = 700

Tx = Ox
Ty = Oy
while True:
    clock.tick(FPS)
    screen.fill(BEIGE_FON)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if (x - x_pol)**2 + (y - y_pol)**2 <= R ** 2:
                is_grabbed_pol = True
            elif is_grabbed_pol and event.type == pygame.MOUSEMOTION:
                dx, dy = event.rel
            x_pol += dx
            if x_pol > right_x:
                x_pol = right_x
            elif x_pol < left_x:
                x_pol = left_x
            alpha = 5 + int(85 * (x_pol - left_x) / (right_x - left_x))
    alpha_rad = math.pi * alpha / 180
    N = m*g*math.cos(alpha_rad)
    dt = 1 / FPS
    a = (m*g*math.sin(alpha_rad) - k*N)/m
    Vt = Vp + a*dt
    Xt = Xp + Vt*dt + (a*dt**2)/2
    Xp = Xt
    Vp = Vt
    
    

    pygame.draw.line(screen, BLACK, (x1_line, y_line), (x2_line, y_line), 2)
    pygame.draw.line(screen, BLACK, (x1_line, y_line), (x1_line, y_vert_line), 2)
    pygame.draw.line(screen, BLACK, (x1_line, y_vert_line), (x2_line, y_line), 2)
    pygame.draw.line(screen, BLACK, (700, 250), (1100, 250), 2)
    pygame.draw.circle(screen, DARK_ORANGE_4, (x_pol, y_pol), R)
    OA = ((x2_line - x1_line) ** 2 + (y_line - y_vert_line)**2) ** 0.5
 
    Kx = Tx + d * abs(x2_line - x1_line) / OA
    Ky = Ty + d * abs(y_line - y_vert_line) / OA
    y2 = 100  #  случайное число
    x2 = -abs(y_line - y_vert_line) * y2 / abs(x2_line - x1_line)
    xy2 = (x2 ** 2 + y2 ** 2) ** 0.5
    Px = Tx - h * x2 / xy2
    Py = Ty - h * y2 / xy2

    Sx = Px + d * abs(x2_line - x1_line) / OA 
    Sy = Py + d * abs(y_line - y_vert_line) / OA
    pygame.draw.line(screen, BLACK, (Tx, Ty), (Kx, Ky), 2)
    pygame.draw.line(screen, BLACK, (Tx, Ty), (Px, Py), 2)
    pygame.draw.line(screen, BLACK, (Sx, Sy), (Kx, Ky), 2)
    pygame.draw.line(screen, BLACK, (Sx, Sy), (Px, Py), 2)
    pygame.display.update()
    Tx += abs(x2_line - x1_line) / OA
    Ty += abs(y_line - y_vert_line) / OA

