import pygame
import random
from random import randint
class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def Start(self, sr):
        self.sr = sr

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
    def Start(self, sr):
        super().Start(sr)
        self.y = -20
        self.x = randint(11, 349)
        self.speed = 5

    def Update(self):
        super().Update()
        self.y += self.speed
        

    def Draw(self):
        pygame.draw.circle(self.sr, (255, 0, 0) , (self.x, self.y), 10)

class Player(GameObject):
    def Start(self,sr):
        super().Start(sr)        
        self.y = 400
        self.x = 180
    
    def Update(self):
        super().Update()

    def Event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x += 10
                elif event.key == pygame.K_RIGHT:
                    self.x -= 10
    
    def Draw(self):
        pygame.draw.rect(self.sr, (64, 128, 255) , (self.x, self.y, 100, 25), 10)