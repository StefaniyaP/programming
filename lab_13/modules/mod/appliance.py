from abc import ABC, abstractmethod


class Appliance(ABC):
    def __init__(self, power, usage_time, cost, n):
        self.power = power
        self.usage_time = usage_time
        self.cost = cost
        self.n = n

    @abstractmethod
    def power_consumption(self, power, usage_time, n):
        pass

    @abstractmethod
    def price(self, cost):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __repr__(self):
        return f"{self.__class__.__name__}(power={self.power})"
