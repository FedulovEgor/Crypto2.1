from CryptoSelfMethods.GeneratePrimeNumber import GeneratePrime, IsPrime
from CryptoSelfMethods.SelfModExp import ModExp
from CryptoSelfMethods.MyUserClass import MyUser
from random import randint


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


def act_1():
    """Создать общий секретный ключ k"""
    N = 109417386415705274218097073220403576120037329454492059909138421314763499842889347847179972578912673324976257528997818337970765372440271467435315933543338974563728164539274563715647292635473920374657489365648392736457483
    g, q, p = GenerateG(N)
    print(f"""Число g = {g}\nЧисло q = {q}\nЧисло p = {p}\n""")


def act_2():
    pass


def act_3():
    pass


def UserA():
    g = int(input('Введите g'))
    p = int(input('Введите p'))
    # print(f"""Первый пользователь сегенировал число X = {ModExp(g, randint(2, p - 1), p)}""")
    user1 = MyUser(p)
    user1.GenerateRandomNum(g)


def UserB():
    g = int(input('Введите g'))
    p = int(input('Введите p'))
    print(f"""Второй пользователь сегенировал число Y = {ModExp(g, randint(2, p - 1), p)}""")


def Menu():
    while True:
        act = int(input(
            "Выберите действие:"
            "\n1 - Генерация ключей"
            "\n2 - Зашифровать сообщение"
            "\n3 - Расшифровать сообщение"
            "\n4 - Пользователь A"
            "\n5 - Пользователь B"
            "\n0 - Закрыть"
            "\n--> "))
        if act == 1:
            act_1()
        elif act == 2:
            act_2()
        elif act == 3:
            act_3()
        elif act == 4:
            UserA()
        elif act == 5:
            UserB()
        elif act == 0:
            print("До свидания!")
            exit()


if __name__ == "__main__":
    Menu()
