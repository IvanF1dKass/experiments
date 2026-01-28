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
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

R_pol = 15
pol_c_x_mas = 1000
pol_c_x_alpha = 1000
pol_c_x_len = 1000
pol_xL = 825
pol_xR = 1175
pol_y_mas = 50
pol_y_alpha = 100
pol_y_len = 150

ceiling_y = 30
ceiling_xL = 75
ceiling_xR = 275

is_grabbed_pol_mas = False
is_grabbed_pol_len = False
is_grabbed_pol_alpha = False
mas_min = 5
mas_max = 30
mas = (mas_min + mas_max) / 2
alpha_min = 20
alpha_max = 70  
alpha = (alpha_min + alpha_max) / 2 
len_min = 50
len_max = 300
length = (len_min + len_max) / 2 



while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if (x - pol_c_x_mas)**2 + (y - pol_y_mas)**2 <= R_pol ** 2:
                is_grabbed_pol_mas = True
            elif (x - pol_c_x_len)**2 + (y - pol_y_len)**2 <= R_pol ** 2:
                is_grabbed_pol_len = True
            elif (x - pol_c_x_alpha)**2 + (y - pol_y_alpha)**2 <= R_pol ** 2:
                is_grabbed_pol_alpha = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_grabbed_pol_mas = False
            is_grabbed_pol_len = False
            is_grabbed_pol_alpha = False
        elif is_grabbed_pol_mas and event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            pol_c_x_mas += dx
            if pol_c_x_mas > pol_xR: 
                pol_c_x_mas = pol_xR
            elif pol_c_x_mas < pol_xL:
                pol_c_x_mas = pol_xL
            mas = mas_min + int((mas_max - mas_min) * (pol_c_x_mas - pol_xL) / (pol_xR - pol_xL))
        elif is_grabbed_pol_alpha and event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            pol_c_x_alpha += dx
            if pol_c_x_alpha > pol_xR: 
                pol_c_x_alpha = pol_xR
            elif pol_c_x_alpha < pol_xL:
                pol_c_x_alpha = pol_xL
            alpha = alpha_min + int((alpha_max - alpha_min) * (pol_c_x_alpha - pol_xL) / (pol_xR - pol_xL))
        elif is_grabbed_pol_len and event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            pol_c_x_len += dx
            if pol_c_x_len > pol_xR: 
                pol_c_x_len = pol_xR
            elif pol_c_x_len < pol_xL:
                pol_c_x_len = pol_xL
            length = len_min + int((len_max - len_min) * (pol_c_x_len - pol_xL) / (pol_xR - pol_xL))

    screen.fill(BLACK)
    pygame.draw.line(screen, RED, (pol_xL, pol_y_mas), (pol_xR, pol_y_mas), 2)
    pygame.draw.line(screen, RED, (pol_xL, pol_y_len), (pol_xR, pol_y_len), 2)
    pygame.draw.line(screen, RED, (pol_xL, pol_y_alpha), (pol_xR, pol_y_alpha), 2)
    pygame.draw.circle(screen, GREEN, (pol_c_x_mas, pol_y_mas), R_pol)
    pygame.draw.circle(screen, GREEN, (pol_c_x_alpha, pol_y_alpha), R_pol)
    pygame.draw.circle(screen, GREEN, (pol_c_x_len, pol_y_len), R_pol)

    pygame.draw.line(screen, RED, (ceiling_xL, ceiling_y), (ceiling_xR, ceiling_y), 2)
    pygame.draw.line(screen, RED, (ceiling_xR, 0), (ceiling_xR, ceiling_y), 2)
    pygame.draw.line(screen, RED, (ceiling_xL, 0), (ceiling_xL, ceiling_y), 2)
    x1 = (ceiling_xR + ceiling_xL) / 2

    alpha_rad = alpha * math.pi / 180
    x_object = x1 - length * math.sin(alpha_rad)
    y_object = ceiling_y + length * math.cos(alpha_rad)
    pygame.draw.line(screen, WHITE, (x_object, y_object), (x1, ceiling_y), 2)
    pygame.display.update()        
    print(mas, alpha, length)