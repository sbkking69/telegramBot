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
        self.Draw()

    def Event(self, event):
        pass

    def Draw():
        pass

    def Destroy(self):
        pass

class Boll(GameObject):
    def Start(self, sr):
        super().Start()
        self.sr = sr
        self.y = randint(-1000, -20)
        self.x = randint(11, 349)
        self.speed = 5

    def Update(self):
        super().Update()
        self.y += self.speed
        

    def Draw(self):
        pygame.draw.circle(self.sr, (255, 0, 0) , (self.x, self.y), 10)

class WhiteBall(Boll):
    def Draw(self):
        pygame.draw.circle(self.sr, (255, 255, 255) , (self.x, self.y), 10)


class Player(GameObject):
    def Start(self,sr):
        super().Start(sr)        
        self.y = 400
        self.x = 180
        self.speed = 50
        self.x_new = 180
    
    def Update(self):
        super().Update()
        if self.x != self.x_new:
            if self.x > self.x_new:
                self.x -= 10
            else:
                self.x += 10

    def Event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(self.x_new - self.speed < 0): self.x_new = 0
                else: self.x_new -= self.speed
            elif event.key == pygame.K_RIGHT:
                if(self.x_new  + 100 + self.speed > 360): self.x = 360
                else: self.x_new += self.speed
    
    def Draw(self):
        pygame.draw.rect(self.sr, (64, 128, 255) , (self.x, self.y, 100, 25))