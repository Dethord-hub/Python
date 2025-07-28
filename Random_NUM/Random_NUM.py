import random


def hello_player():
    print('''Привет, игрок!
В данной игре твоя задача угадать рандомно загаданное число.
Каждый раз, когда твое число будет больше или меньше, программа будет уведомлять тебя об этом!
Если захочешь закончить игру - напиши 'exit' или 'выход'
А теперь, выбери режим игры:''')
    choose_mode()


def choose_mode():
    while True:
        print('''1 - Число будет рандомно сгенерировано из диапазона [1,100].
2 - Число будет рандомно сгенерировано из диапазона, заданного тобой.''')
        mode = input().strip().lower()
        if mode in ['exit', 'выход']:
            return
        if mode == '1':
            secret_number_game(1, 100)
            break
        elif mode == '2':
            print('Введите границы генерируемого числа!')
            while True:
                try:
                    x, y = map(int, input().split())
                    if x < y:
                        secret_number_game(x, y)
                        break
                    else:
                        print("Первая граница должна быть меньше, попробуй еще раз")
                except ValueError:
                    print("Введи два целых числа! Попробуй еще раз.")
        else:
            print('Что-то ты ввел некорректно, попробуй еще раз!')


def secret_number_game(min_value, max_value):
    print('Ваше число сгенерировано, попробуйте угадать!')
    count = 0
    secret_number = random.randint(min_value, max_value)
    while True:
        count += 1
        print(f'Номер попытки - {count}: ', end='')
        guess = is_valid(min_value, max_value)
        if guess in ['exit', 'выход']:
            print('Игра прервана. Прощай!')
            return
        if guess == secret_number:
            print("Вы угадали число, поздравляю!")
            count_attempts(count)
            break
        elif guess > secret_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif guess < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')


def is_valid(min_value, max_value):
    while True:
        n = input().strip().lower()
        if n in ['exit', 'выход']:
            return 'exit'
        try:
            num = int(n)
            if min_value <= num <= max_value:
                return num
            else:
                print(
                    f'Ты уверен, что ввел корректные данные?\nНе забывай - число должно быть от {min_value} до {max_value} и быть числом')
        except ValueError:
            print(f'Введите целое число от {min_value} до {max_value} (или "exit" для выхода)!')


def count_attempts(count):
    if count == 1:
        print("Одна попытка? А ты хорош")
    elif 1 <= count <= 10:
        print(f"Нормально, нормально\nКоличество попыток - {count}")
    else:
        print(f"Настоящий трудяга, молодец\nКоличество попыток - {count}")


def play_again():
    while True:
        print('Хочешь ли сыграть еще разок? (да/нет)')
        ans = input().lower().strip()
        if ans in ['да', 'д', 'yes', 'y']:  # Убрал 'lf', 'l' — если нужно, верни
            return True
        elif ans in ['нет', 'н', 'no', 'n', 'exit', 'выход']:
            return False
        else:
            print("Введите 'да' или 'нет'!")


while True:
    hello_player()
    if not play_again():
        print('Спасибо за игру, прощай!')
        break
