import doctest
from itertools import *

# Иван составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует 
# своё кодовое слово. В качестве кодовых слов Иван использует все пятибуквенные слова в алфавите 
# {A, B, C, D, E}, удовлетворяющие такому условию: кодовое слово не может начинаться с буквы E 
# и заканчиваться буквой A. Сколько различных кодовых слов может использовать Иван?

alphabet = {'A', 'B', 'C', 'D', 'E'}

def iter(alphabet):
    '''
    >>> iter(alphabet)
    91

    >>> iter({'N', 'V', 'K'})
    43

    >>> iter(12)
    3
    '''

    b = []
    s = ''
    c = 0
    comb = permutations(alphabet)
    for i in comb:
        if i[1] != 'E' and i[-1] != 'A':
            c += 1
            s = ''.join(i)
        b.append(s)
    # return c, b
    return c

print(iter(alphabet))

doctest.testmod(name='iter', verbose=True)

