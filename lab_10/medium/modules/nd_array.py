import numpy as np


class Calc:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def create_n_dim_array(self):
        arr = []
        string = [f'level {self.m}']
        if self.m == 1:
            return string * self.n
        elif self.m == 2:
            for i in range(self.n):
                arr.append(string * self.n)
            return arr
        elif self.m == 3:
            arr = np.full((self.n, self.n, self.n), string)
            return arr
