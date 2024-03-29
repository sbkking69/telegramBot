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
        super().Start(sr)
        self.y = randint(-100, -20)
        self.x = randint(11, 349)
        self.r = randint(10,20)
        self.speed = randint(3,7)
        self.tag = 'ball'

    def Update(self):
        super().Update()
        self.y += self.speed
        

    def Draw(self):
        pygame.draw.circle(self.sr, (255, 0, 0) , (self.x, self.y), self.r)

class WhiteBall(Boll):
    def Start(self, sr):
        super().Start(sr)
        self.speed = 5
        self.x = 170
        self.tag = 'enum'
        self.speed2 = randint(-25,25)


    def Update(self):
        super().Update()
        if self.x < 20 or self.x > 340:
            self.speed2 *= -1
        self.y += self.speed
        self.x += self.speed2

        



    def Draw(self):
        pygame.draw.circle(self.sr, (255, 255, 255) , (self.x, self.y), 10)


class Player(GameObject):
    def Start(self,sr):
        super().Start(sr)  
        self.width = 100
        self.hight = 25      
        self.y = 400
        self.x = 180
        self.speed = 50
        self.x_new = 180
        self.plavnoti = 5
        self.health = 3

    
    def Update(self):
        super().Update()
        if self.x != self.x_new:
            if self.x > self.x_new:
                self.x -= self.plavnoti
            else:
                self.x += self.plavnoti

    def Event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(self.x_new - self.speed < 0): self.x_new = 0
                else: self.x_new -= self.speed
            elif event.key == pygame.K_RIGHT:
                if(self.x_new  + 100 + self.speed > 360): self.x_new = 260
                else: self.x_new += self.speed
    
    def Draw(self):
        pygame.draw.rect(self.sr, (64, 128, 255) , (self.x, self.y, self.width, self.hight))

    def Collision(self, obj):
        if obj.x + obj.r > self.x - obj.r and obj.x - obj.r < self.x + obj.r + self.width and obj.y > self.y and obj.y < self.y + self.hight:
            return True
        return False