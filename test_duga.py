import pygame
import math
## пример от чатаГПТ
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Параметры дуги
center = (200, 200)
radius = 100
color = (255, 255, 0)
width = 3

# Прямоугольник, в который вписана окружность
rect = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)

# Углы в радианах
start_angle = math.radians(0)        # начало с оси X вправо
end_angle = math.radians(30)         # 30 градусов дуги

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.arc(screen, color, rect, start_angle, end_angle, width)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
