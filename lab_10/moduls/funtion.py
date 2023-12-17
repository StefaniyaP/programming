def b(k, x):
    if k == 0:
        return 1.0 / (2.0 * x)
    bk = b(k - 1, x) * x ** 2
    return bk


def y(k, x):
    if x == 0:
        raise ValueError('x should not be 0')
    if k == 0:
        return 1
    yk = b(k, x) * y(k - 1, x)
    return yk
