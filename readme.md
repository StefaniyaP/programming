# Прог. Лабораторная работа №8

## Задание:
1. Решить обе задачи своего варианта
2. Применить декоратор к замыканию
3. оформить отчет в ```readme.md```, который должен содержать:
    - условия задач
    - описание проделанной работы
    - скриншоты результатов
    - ссылки на используемые материалы

## Мой вариант (7)
- Замыкание для отслеживания количества HP героя - HP не может подниматься больше 100 и опускаться ниже 0, герой может лечиться или получать урон.
- Декоратор для подавления вывода функции на консоль.

### Решение:

```Python
import random

def invisible_return(func):
    def wrapper(x):
        x, _ = func(x)
        return x
    return wrapper
    
def hp():
    x = random.randint(0, 100)
    print(f'у вас {x} хп')

    @invisible_return
    def high_hp(x):
        r = random.randint(0, 50)   
        x -= r       
        if x <= 1:
            return 1, f'Хп понижено на {r}'
        return x, f'Хп понижено на {r}'
    
    @invisible_return
    def low_hp(x):
        r = random.randint(0, 50)
        x += r
        if x >= 100:
            return 100, f'Хп повышено на {r}'
        return x, f'Хп повышено на {r}'

    if 50 <= x <= 100:
        choice = int(input('Желаете понизить хп?\n'
                            '1. да\n'
                            '2. нет\n'))
        if choice == 1:
            f = high_hp(x)
            return f
        else: 
            return f'по прежнему {x} хп'
    elif x < 50:
        choice = int(input('Желаете повысить хп?\n'
                            '1. да\n'
                            '2. нет\n'))
        if choice == 1:
            f = low_hp(x)
            return f
        else:
            return f'по прежнему {x} хп'

print(hp())
```

Вывод без применения декоратора:

![image](https://github.com/StefaniyaP/programming/assets/144994975/0bd7e8e1-62a2-4c9f-b77f-4231d70bbd6b)

Вывод с применением декоратора:

![image](https://github.com/StefaniyaP/programming/assets/144994975/552d7564-3508-4cdf-9926-921e9954cc50)

