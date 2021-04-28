from random import randint
from CryptoSelfMethods.GeneratePrimeNumber import *
from CryptoSelfMethods.SelfModExp import *


def generate_g(N):
    """Генерация параметра g"""
    q = generate_prime(2 ** 256)

    n = randint(2, N)
    p = n * q + 1
    while not is_prime(p):
        n = randint(2, N)
        p = n * q + 1

    a = randint(2, p - 1)
    g = mod_exp(a, n, p)
    while g == 1:
        a = randint(2, p - 1)
        g = mod_exp(a, n, p)

    return g, q, p


def diffie_hellman(g, x, q, p):
    """Функция вычисления g^x mod p"""
    xx = x % q
    big_x = mod_exp(g, xx, p)

    return big_x
