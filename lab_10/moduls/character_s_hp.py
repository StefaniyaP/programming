import random


def hp():
    # значение хп рандомно задается в диапазоне от 0 до 100
    x = random.randint(0, 101)
    print(f'у вас {x} хп')

    # функция high_hp понижает число хп
    def high_hp(x):
        r = random.randint(0, 50)
        x -= r
        if x <= 1:
            return 1, f'Хп понижено на {r}'
        return x, f'Хп понижено на {r}'

    # функция low_hp повышает число хп
    def low_hp(x):
        r = random.randint(0, 50)
        x += r
        if x >= 100:
            return 100, f'Хп повышено на {r}'
        return x, f'Хп повышено на {r}'

    # если x лежит в диапазоне от 50 до 100 включительно, то пользователю дается
    # выбор понизить хп или же оставить его прежним
    if 50 <= x <= 100:
        choice = int(input('Желаете понизить хп?\n'
                            '1. да\n'
                            '2. нет\n'))
        if choice == 1:
            f = high_hp(x)
            return f
        else:
            return f'по-прежнему {x} хп'
    # если x лежит в диапазоне до 50, то пользователю дается выбор повысить хп или же оставить его прежним
    elif x < 50:
        choice = int(input('Желаете повысить хп?\n'
                            '1. да\n'
                            '2. нет\n'))
        if choice == 1:
            f = low_hp(x)
            return f
        else:
            return f'по-прежнему {x} хп'