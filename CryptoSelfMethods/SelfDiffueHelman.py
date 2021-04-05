from random import randint
from CryptoSelfMethods.GeneratePrimeNumber import *
from CryptoSelfMethods.SelfModExp import *


def GenerateG(N):
    """Генерация параметра g"""
    q = GeneratePrime(2 ** 256)

    n = randint(2, N)
    p = n * q + 1
    while not IsPrime(p):
        n = randint(2, N)
        p = n * q + 1

    a = randint(2, p - 1)
    g = ModExp(a, n, p)
    while g == 1:
        a = randint(2, p - 1)
        g = ModExp(a, n, p)

    return g, q, p


def DiffieHelman(g, x, q, p):
    """Функция вычисления g^x mod p"""
    xx = x % q
    bigX = ModExp(g, xx, p)

    return bigX
