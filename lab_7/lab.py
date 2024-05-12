def create_n_dim_array(m, n):
    a = 0
    for i in range(n):
        a += 1
    string = f'level {a}'
    if m == 1:
        return [string] * n
    else:
        return [create_n_dim_array(m - 1, n)] * n
#
# print(create_n_dim_array(1, 3))
print(create_n_dim_array(2, 3))
print()
print(create_n_dim_array(3, 2))

# import numpy as np
#
#
# def create_n_dim_array(m, n):
#     arr = []
#     string = [f'level {m}']
#     if m == 1:
#         return string * n
#     elif m == 2:
#         for i in range(n):
#             arr.append(string * n)
#         return arr
#     elif m == 3:
#         arr = np.full((n, n, n), string)
#         return arr
#
#
# print(create_n_dim_array(2, 3))
# print()
# print(create_n_dim_array(3, 2))
