from random import randint
def Game(hui):
    x = randint(1,10)
    if hui == x:
        return True, x
    if hui != x:
        return False, x