class Calc:
    def __init__(self, usage_time, cost, n, power):
        self.usage_time = usage_time
        self.cost = cost
        self.n = n
        self.power = power

    def power_consumption(self):
        self.p_c = 1
        if self.usage_time == "дни":
            self.p_c = self.power * (24 * self.n)
        elif self.usage_time == 'месяцы':
            self.p_c = self.power * (24 * 30 * self.n)
        elif self.usage_time == 'годы':
            self.p_c = self.power * (24 * 30 * 12 * self.n)
        return self.p_c

    def price(self):
        p = self.cost * self.p_c
        return p


