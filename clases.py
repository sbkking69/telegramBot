class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Start()
    
    def Start(self):
        pass

    def Update(self):
        pass

    def Draw(self):
        pass

    def Destroy():
        pass

class Player(GameObject):
    def Start(self):
        pass        

    def Update(self):
        pass

class Boll(GameObject):
    def Start(self, x):
        self.x = x    

    def Update(self):
        pass


p = Player()
