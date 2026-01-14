import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60

pygame.init()

def is_rect_pressed(click_pos, rect):
    x_left, y_up, width, height = rect
    x, y = click_pos
    return x > x_left and x < x_left + width and y > y_up and y < y + height
    
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()


rect_buttons = [
    (250, 50, 100, 200),
    (400, 50, 50, 100),
    (500, 50, 30, 100),
    (600, 50, 100, 150),
]

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     
            for ind in range(len(rect_buttons)):
                button = rect_buttons[ind]
                if is_rect_pressed(event.pos, button):
                    print(ind)

    screen.fill(BLACK)

    pygame.draw.circle(screen, GREEN, (100, 100), 50)

    for button in rect_buttons:
        pygame.draw.rect(screen, BLUE, button)


    pygame.display.update()
