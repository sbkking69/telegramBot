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

    def Update(self):
        super().Update()
