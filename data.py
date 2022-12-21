from enum import Enum
token = "5919401327:AAHlByvIwXn9EcE9oyWDJhyM_YfVBHB0DQQ"

class TypeUser(Enum):
    user = 0
    admin = 312

class WorkShop:
    def __init__(self, id, title, authour, data, prise) -> None:
        self.id = id
        self.title = title
        self.authour = authour
        self.data = data
        self.prise = prise
    
    def info(self) -> str:
        return str('ID: ' + self.id + '\nTitle: ' + self.title + 
        '\nAuthour: ' + self.authour + "\nData: " + self.data + 
        '\nPrise: ' + self.prise)

class User:
    def __init__(self, id, name, type) -> None:
        self.id = id
        self.name = name
        self.type = type      

    def info(self) -> str:
        return str("Id: " + self.id + "\nName: " + self.name + '\nType: ' + self.type)