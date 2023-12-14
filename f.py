import random

#def invisible_return(func):
   # def wrapper(x):
    #    x, _ = func(x)
    #    return x
   # return wrapper
    
def hp():
    x = random.randint(0, 100)
    print(f'у вас {x} хп')

    #@invisible_return
    def high_hp(x):
        r = random.randint(0, 50)   
        x -= r       
        if x <= 1:
            return 1, f'Хп понижено на {r}'
        return x, f'Хп понижено на {r}'
    
    #@invisible_return
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


