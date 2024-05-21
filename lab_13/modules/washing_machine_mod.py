from lab_13.modules.mod.appliance import Appliance


class Calc(Appliance):
    def power_consumption(self, power, usage_time, n):
        self.p_c = 1
        if usage_time == "дни":
            self.p_c = power * (24 * n)
        elif usage_time == 'месяцы':
            self.p_c = power * (24 * 30 * n)
        elif usage_time == 'годы':
            self.p_c = power * (24 * 30 * 12 * n)
        return self.p_c

    def price(self, cost):
        p = cost * self.p_c
        return p

