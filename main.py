import pygame
import random
from clases import *

WIDTH = 360
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

listObj = []
listObj.append(Boll())

# Цикл игры
running = True
for obj in listObj:
    obj.Start(screen)

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    TimeList = []

    for obj in listObj:
        obj.Update()        
        if obj.y <= 500:
            TimeList.append(obj)
    listObj = TimeList
    if len(listObj) < 3:
        a = randint(1,100)
        if a <= 30:
            b = WhiteBall()
            b.Start(screen)
            listObj.append(b)
        else:
            b = Boll()
            b.Start(screen)
            listObj.append(b)

        

    pygame.display.update()