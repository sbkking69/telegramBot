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

counterFont = pygame.font.SysFont('serif', 48)



index = 0

listObj = []
pl = Player()

listObj.append(Boll())

# Цикл игры
running = True
for obj in listObj:
    obj.Start(screen)
pl.Start(screen)
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        pl.Event(event)

    screen.fill((0,0,0))

    pl.Update()

    TimeList = []

    for obj in listObj:
        obj.Update()
        col = pl.Collision(obj)      
        if obj.y <= 500 and not col:
            TimeList.append(obj)
        if col:
            pl.health -= 1
            index += 1
            print(index)
    listObj = TimeList


    if len(listObj) < 7:
        a = randint(1,100)
        if a <= 30:
            b = WhiteBall()
            b.Start(screen)
            listObj.append(b)
        else:
            b = Boll()
            b.Start(screen)
            listObj.append(b)
        

    counterText = counterFont.render(str(index), False, (255, 255, 255))
    screen.blit(counterText, (165, 0))
    
    HealthText = counterFont.render(str(pl.health*"♥"), False, (64, 128, 255))
    screen.blit(HealthText, (0, 0))

    if(pl.health <= 0):
        running = False


    pygame.display.update()