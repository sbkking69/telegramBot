from main import CursorPosition
class Point:
    def __init__(self, x, y, sym):
        self.x = x
        self.y = y
        self.sym = sym
    def Move(self, x, y):
        '''Перемещение координаты точки'''
        pass
    def Draw(self):
        CursorPosition = (self.x, self.y)
        print(self.sym)
    def Clear(self):
        CursorPosition = (self.x, self.y)
        print(' ')