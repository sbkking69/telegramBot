from clases import Game

while True:
    try:
        user = int(input('Угадайте число от 1 до 10! Ваш вариант:'))
        if Game(user):
            print("Вы угадали!")
        else:
            print("Вы не угадали!")

        user = input('Вы хотите продолжить? (0 - выход)')
        if user == '0':
            break
    except:
        pass