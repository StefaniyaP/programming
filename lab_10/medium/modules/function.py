class Calc:
    def __init__(self, x, k):
        self.x = x
        self.k = k

    def y(self):
        if self.x == 0:
            raise ValueError('x should not be 0')

        y_0 = 1
        b_0 = 1 / (2 * self.x)
        y_k = 0
        for i in range(1, self.k+1):
            b_k = b_0 * self.x**2
            y_k = b_k * y_0

            y_0 = y_k
            b_0 = b_k

        return y_k
