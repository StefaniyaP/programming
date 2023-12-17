def create_n_dim_array(m, n):
    a = 0
    for i in range(n):
        a += 1
    string = f'level {a}'
    if m == 1:
        return [string] * n
    else:
        return [create_n_dim_array(m - 1, n)] * n