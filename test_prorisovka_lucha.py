import pygame


WHITE = (255, 255, 255)
FPS = 10

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
x1 = 10
x2 = 350
y1 = 300
y2 = 400
n_step = 1
m_step = 15
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
   
    pygame.draw.line(screen, WHITE, (x1, y1), (x1+(x2-x1)*n_step/m_step, y1+(y2-y1)*n_step/m_step), 1)
    if n_step != m_step:

        n_step += 1
        

    pygame.display.update()