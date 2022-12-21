import pygame
import random
from random import randint
class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Start()
    
    def Start(self):
        pass

    def Update(self):
        self.Event()
        self.Draw()

    def Event(self):
        pass

    def Draw():
        pass

    def Destroy(self):
        pass

class Boll(GameObject):
    def Start(self):
        super().Start()
        self.y = -30
        self.x = randint(31, 329)

    def Update(self):
        super().Update()

    def Draw(self, screen, RED):
        pygame.draw.circle(screen, RED, (self.x, self.y), 30)

class Player(GameObject):
    def Start(self):
        super().Start()
    
    def Update(self):
        super().Update()

    def Event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x += 10
                elif event.key == pygame.K_RIGHT:
                    self.x -= 10