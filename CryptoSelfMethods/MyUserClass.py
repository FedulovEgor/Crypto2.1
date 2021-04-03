from CryptoSelfMethods.GeneratePrimeNumber import GeneratePrime, IsPrime
from CryptoSelfMethods.SelfModExp import ModExp
from random import randint


class MyUser:
    def __init__(self, p):
        self.X = None
        self.k = None
        self.p = p

    def GenerateRandomNum(self, g):
        self.X = ModExp(g, randint(2, self.p - 1), self.p)
        print(f"""Пользователь {self} сгенерировал число {self.X}""")

    def CreateK(self, anotherUserX):
        self.k = ModExp(anotherUserX, self.X, self.p)
