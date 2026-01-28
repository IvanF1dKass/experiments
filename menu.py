import pygame

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
font = pygame.font.Font(None, 100)
font1 = pygame.font.Font(None, 32)

screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

state = 'menu'



while True:
    clock.tick(FPS)
    screen.fill(BEIGE_FON)
    if state == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                x, y = event.pos 
                if x < 400:
                    state = 'menu_7'
                elif x > 800:
                    state = 'menu_9'
                else:
                    state = 'menu_8'
        pygame.draw.rect(screen, LIGHT_BLUE_1, (0, 0, 400, 700))
        pygame.draw.rect(screen, BLUE_GRAY_2, (400, 0, 400, 700))
        pygame.draw.rect(screen, DIRTY_BLUE_3, (800, 0, 400, 700))
        text7 = font.render('7', True, DARK_ORANGE_4)
        screen.blit(text7, (175, 150))
        text8 = font.render('8', True, DARK_ORANGE_4)
        screen.blit(text8, (175 + 400, 150))
        text9 = font.render('9', True, DARK_ORANGE_4)
        screen.blit(text9, (175 + 800, 150))
        
    elif state == 'menu_7':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x > 1060 and y > 630:
                    state = 'menu'
        screen.fill(BEIGE_FON)
        pygame.draw.rect(screen, LIGHT_BLUE_1, (0, 0, 400, 700))
        text = font.render('7', True, DARK_ORANGE_4)
        screen.blit(text, (175, 150))
        pygame.draw.rect(screen, BLACK, (1060, 630, 1200, 700))
        text1 = font1.render('назад', True, WHITE)
        screen.blit(text1, (1100, 660))
        text_experement1 = font1.render('- Скольжение тела по наклонной плоскости', True, BLACK)
        screen.blit(text_experement1, (500, 100))
        text_experement2 = font1.render('- Инерция на примере сталкивания двух тел', True, BLACK)
        screen.blit(text_experement2, (500, 150))
        text_experement3 = font1.render('- Условия равновесия рычага', True, BLACK)
        screen.blit(text_experement3, (500, 200))
        
    elif state == 'menu_8':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 500 < x < 930 and 100 < y < 120:
                    state = 'exp_linza_focus'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x > 1060 and y > 630:
                    state = 'menu'
        screen.fill(BEIGE_FON)
        pygame.draw.rect(screen, BLUE_GRAY_2, (0, 0, 400, 700))
        text = font.render('8', True, DARK_ORANGE_4)
        screen.blit(text, (175, 150))
        pygame.draw.rect(screen, BLACK, (1060, 630, 1200, 700))
        text1 = font1.render('назад', True, WHITE)
        screen.blit(text1, (1100, 660))

        text_experement1 = font1.render('- Собирающая линза', True, BLACK)
        screen.blit(text_experement1, (500, 100))
        text_experement2 = font1.render('- Отражение луча', True, BLACK)
        screen.blit(text_experement2, (500, 150))
        text_experement3 = font1.render('- Рассеивающая линза', True, BLACK)
        screen.blit(text_experement3, (500, 200))
        
        
    elif state == 'menu_9':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill(BEIGE_FON)
        pygame.draw.rect(screen, DIRTY_BLUE_3, (0, 0, 400, 700))
        text = font.render('9', True, DARK_ORANGE_4)
        screen.blit(text, (175, 150))
        pygame.draw.rect(screen, BLACK, (1060, 630, 1200, 700))
        text1 = font1.render('назад', True, WHITE)
        screen.blit(text1, (1100, 660))
        text_experement1 = font1.render('- Математический маятник (на пружине)', True, BLACK)
        screen.blit(text_experement1, (500, 100))
        text_experement2 = font1.render('- Математический маятник (на нити)', True, BLACK)
        screen.blit(text_experement2, (500, 150))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if x > 1060 and y > 630:
                state = 'menu'
    
    elif state == 'exp_linza_focus':
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x > 1060 and y > 630:
                    state = 'menu'
        screen.fill(BEIGE_FON)
        d = x_prism - x_object
        h = y_line - y_object
        if d > F:
            f = F*d/(d-F)
            H = f*h/d
            pygame.draw.line(screen, RED, (x_object, y_object), (x_prism + f + 5*(x_prism + f - x_object), y_line + H + 5*(y_line + H - y_object)), 2)
            pygame.draw.line(screen, RED, (x_prism, y_object),(x_prism + f + 5*f, y_line + H + 5*(y_line + H - y_object)), 2)
            pygame.draw.line(screen, RED, (x_object, y_object), (x_prism, y_object), 2)
            text = font1.render('действительное изображение', True, BLACK)
            screen.blit(text, (100, 600))
        elif F == d:
            pygame.draw.line(screen, GREEN, (x_prism, y_object), (F_x1 + 3*(-x_prism + F_x1), y_line + 3*(-y_object + y_line)), 2)
            pygame.draw.line(screen, GREEN, (x_object, y_object), (x_prism + 5*(-x_prism + F_x1), y_line + 5*(-y_object + y_line)), 2)
            pygame.draw.line(screen, GREEN, (x_object, y_object), (x_prism, y_object), 2)
        if d < F:
            f = F*d/(d-F)
            H = f*h/d
            pygame.draw.line(screen, BLUE,(x_prism + f - 20*( -(x_prism + f) + x_object), y_line + H - 20*(-(y_line + H) + y_object)), (x_object, y_object), 2)
            pygame.draw.line(screen, BLUE, (x_prism + f - 20*(-f), y_line + H - 20*(-y_line -H + y_object)), (x_prism, y_object), 2)
            pygame.draw.line(screen, BLUE, (x_object, y_object), (x_prism, y_object), 2)
            text = font1.render('мнимое изображение', True, BLACK)
            screen.blit(text, (100, 600))


        pygame.draw.line(screen, BLACK, (x1_line, y_line), (x2_line, y_line), 2)
        pygame.draw.line(screen, BLACK, (x_prism, y1_prism), (x_prism, y2_prism), 6)
        pygame.draw.line(screen, BLACK, (x_prism, y1_prism), (x_prism - 20, y1_prism + 20), 6)
        pygame.draw.line(screen, BLACK, (x_prism, y1_prism), (x_prism + 20, y1_prism + 20), 6)
        pygame.draw.line(screen, BLACK, (x_prism, y2_prism), (x_prism - 20, y2_prism - 20), 6)
        pygame.draw.line(screen, BLACK, (x_prism, y2_prism), (x_prism + 20, y2_prism - 20), 6)
        pygame.draw.circle(screen, GREEN, (x_object, y_object), R_object)
        pygame.draw.line(screen, BLACK, (F_x1, F_y + 10), (F_x1, F_y - 10), 2)
        pygame.draw.line(screen, BLACK, (F_x2, F_y + 10), (F_x2, F_y - 10), 2)
        pygame.draw.rect(screen, BLACK, (1060, 630, 1200, 700))
        text1 = font1.render('назад', True, WHITE)
        screen.blit(text1, (1100, 660))
    pygame.display.update()

                    