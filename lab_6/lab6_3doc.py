import doctest


def m(n):
    '''
    >>> type(m(n))
    <class 'int'>
    '''
    s = []
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            s.append(d)
            s.append(n // d)

    if len(s) >= 5:
        s = sorted(s)
        return s[0] * s[1] * s[2] * s[3] *s[4]
    else:
        return 0


n = 200000001


def res(n):
    '''
    >>> res(n)
    ['1728 - 200000004', '21632 - 200000008', '1260 - 200000010', '1152 - 200000016', '4127787 - 200000019']

    >>> res(128)
    3

    >>> type(res(n))
    <class 'int'>
    '''
    c = 0
    a = []
    while c < 5:
        if 0 < m(n) < n:
            a.append(str(m(n)) + ' - ' + str(n))
            c += 1
        n += 1  
    return a
    

print(res(n))

doctest.testmod(name='res', verbose=True)

