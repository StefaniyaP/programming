import doctest

# Сколько единиц содержится в двоичной записи значения выражения: 4^511+2^511−511?

x = 4 ** 511 + 2 ** 511 - 511


def convert(x):
    '''
    >>> convert(x)
    504

    >>> convert(127)
    102

    >>> type(convert(127))
    <class 'str'>
    '''

    b = ''
    while x > 0:
        a = x % 2
        b += str(a)
        x //= 2
    return b.count('1')

print(convert(x))

doctest.testmod(name='convert', verbose=True)