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

screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

pygame.init()

mid = (400, 350)
left_p = (50, 350)
right_p = (750, 350)

object_left = (50, 400)
object_right = (750, 400)
R_l = 20
R_r = 20
while True:
    clock.tick(FPS)
    screen.fill(BEIGE_FON)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            x, y = event.pos 
            if (x - object_left[0])**2 + (y - object_left[1])**2 <= R_l ** 2:
                R_l += 10
                if R_l > 50:
                    R_l = 50
            elif (x - object_right[0])**2 + (y - object_left[1])**2 <= R_r ** 2:
                R_r += 10
                if R_r > 50:
                    R_r = 50
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  
            x, y = event.pos 
            if (x - object_left[0])**2 + (y - object_left[1])**2 <= R_l ** 2:
                R_l -= 10
                if R_l < 10:
                    R_l = 10
            elif (x - object_right[0])**2 + (y - object_left[1])**2 <= R_r ** 2:
                R_r -= 10
                if R_r < 10:
                    R_r = 10
    pygame.draw.line(screen, BLACK, left_p, right_p, 2)
    pygame.draw.line(screen, BLACK, (325, 700), mid, 2)
    pygame.draw.line(screen, BLACK, (475, 700), mid, 2)
    pygame.draw.line(screen, BLACK, left_p, object_left, 2)
    pygame.draw.line(screen, BLACK, right_p, object_right, 2)
    pygame.draw.circle(screen, GREEN, (object_left), R_l)
    pygame.draw.circle(screen, GREEN, (object_right), R_r)
   
    pygame.display.update()
