from CryptoSelfMethods.GeneratePrimeNumber import *
from CryptoSelfMethods.SelfModExp import *
from CryptoSelfMethods.SelfDiffueHelman import *
from random import randint


class MyUser:
    def __init__(self, p, g,q):
        self.X = None
        self.k = None
        self.p = p
        self.g = g
        self.q = q
        self.x = randint(2, self.p - 1)

    def GenerateRandomNum(self):
        """Сгенерировать случайное число пользователя"""
        self.X = DiffieHelman(self.g, self.x, self.q, self.p)
        print(f"""Пользователь {id(self)} сгенерировал число {self.X}""")

    def CreateK(self, anotherUserX):
        """Вычисление числа k пользователя, который получил случайное число от другого пользователя"""
        # self.k = ModExp(anotherUserX, self.x, self.p)
        self.k = DiffieHelman(anotherUserX, self.x, self.q, self.p)
        print(f"""Пользователь {id(self)} сгенерировал число k = {self.k}""")

    @staticmethod
    def CheckK(k1, k2):
        """Проверка чисел k и k' пользователей"""
        if k1 == k2:
            return True
        return False
