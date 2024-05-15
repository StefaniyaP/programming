import random


# декоратор принимает параметр (по умолчанию 'изменено'), после чего меняет поведение исходной функции, а именно:
# срабатывает цикл, благодаря чему пользователь может понижать или повышать хп персонажа до тех
# пор, пока не введет определенную команду, после которой цикл будет прерван
def new_return_with_option(option='изменить'):
    def decorator(func):
        def wrapper(x):
            letter = 'н'
            if option == 'понизить':
                letter = 'ж'
            elif option == 'повысить':
                letter = 'ш'

            while True:
                nex_ = int(input(f'{option.capitalize()} еще?\n'
                                 '1. да\n'
                                 '2. нет\n'))
                if nex_ == 1:
                    x, _ = func(x)
                    print(f'{x} хп, хп {option[:4:] + letter}ено')
                else:
                    x = 'Завершение работы программы'
                    break
            return x
        return wrapper
    return decorator


def hp():
    # значение хп рандомно задается в диапазоне от 0 до 100
    x = random.randint(0, 101)
    print(f'у вас {x} хп')

    # функция high_hp понижает число хп
    @new_return_with_option('понизить')
    def high_hp(x):
        r = random.randint(0, 50)
        x -= r
        if x <= 1:
            return 1, f'Хп понижено на {r}'
        return x, f'Хп понижено на {r}'

    # функция low_hp повышает число хп
    @new_return_with_option('повысить')
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


print(hp())
