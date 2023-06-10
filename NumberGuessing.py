import random
print("Добро пожаловать в числовую угадайку!")
name = input('Привет, как тебя зовут? ')

def is_valid(num):
    if num.isdigit() and 0 < int(num) < 101:
        return True
    return False

def number_guessing():
    counter = 0
    generate = random.randint(1, 100)
    while True:
        counter += 1
        num = input(f'{name}, введи число от 1 до 100: ')
        if is_valid(num) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            num = int(num)
            if num == generate:
                print('Вы угадали, поздравляем!')
                break
            elif num > generate:
                print('Слишком много, попробуйте еще раз')
            else:
                print('Слишком мало, попробуйте еще раз')
    print('Спасибо, что играли в числовую угадайку. Попробовать еще раз?...(Да/Нет)')
    if input() == 'Да':
        number_guessing()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

number_guessing()