token = "5919401327:AAHlByvIwXn9EcE9oyWDJhyM_YfVBHB0DQQ"

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
        