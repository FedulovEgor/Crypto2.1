from CryptoSelfMethods.SelfDiffueHelman import *
from random import randint


class MyUser:
    """Класс, реализующий пользователя"""
    def __init__(self, p, g,q):
        self.X = None
        self.k = None
        self.p = p
        self.g = g
        self.q = q
        self.x = randint(2, self.p - 1)

    def generate_random_number(self):
        """Сгенерировать случайное число пользователя"""
        self.X = diffie_hellman(self.g, self.x, self.q, self.p)
        print(f"""Пользователь {id(self)} сгенерировал число {self.X}""")

    def create_k(self, anotherUserX):
        """Вычисление числа k пользователя, который получил случайное число от другого пользователя"""
        self.k = mod_exp(anotherUserX, self.x, self.p)
        print(f"""Пользователь {id(self)} сгенерировал число k = {self.k}""")

    @staticmethod
    def check_k(k1, k2):
        """Проверка чисел k и k' пользователей"""
        if k1 == k2:
            return "Числа одинаковые"
        return "Числа разные"
