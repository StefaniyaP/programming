# без использования рекурсии
# def y(k, x):
#     if x == 0:
#         raise ValueError('x should not be 0')
#
#     y_0 = 1
#     b_0 = 1 / (2 * x)
#     y_k = 0
#     for i in range(1, k+1):
#         b_k = b_0 * x**2
#         y_k = b_k * y_0
#
#         y_0 = y_k
#         b_0 = b_k
#
#     return y_k
#
#
# print(y(3, 2))


# с использованием рекурсии
def b(k, x):
    if k == 0:
        return 1.0 / (2.0 * x)
    bk = b(k-1, x) * x ** 2
    return bk


def y(k, x):
    if x == 0:
        raise ValueError('x should not be 0')
    if k == 0:
        return 1
    yk = b(k, x) * y(k-1, x)
    return yk


print(y(3, 2))
