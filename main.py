from CryptoSelfMethods.MyUserClass import MyUser
from CryptoSelfMethods.SelfDiffueHelman import generate_g


def act_1():
    """Создать общий секретный ключ k"""
    N = 109417386415705274218097073220403576120037329454492059909138421314763499842889347847179972578912673324976257528997818337970765372440271467435315933543338974563728164539274563715647292635473920374657489365648392736457483
    g, q, p = generate_g(N)
    print(f"""Число g = {g}
    \nЧисло q = {q}
    \nЧисло p = {p}
    \n""")


def users():
    """Иммитация обмена данными между пользователями"""
    g = int(input('Введите g\n--> '))
    p = int(input('Введите p\n--> '))
    q = int(input('Введите q\n--> '))
    user1 = MyUser(p, g, q)
    user2 = MyUser(p, g, q)

    user1.generate_random_number()  # Пользователь 1 генерирует случайное число
    user2.generate_random_number()  # Пользователь 2 генерирует случайное число

    user1.create_k(user2.X)  # Пользователь 1 генерирует число k
    user2.create_k(user1.X)  # Пользователь 2 генерирует число k'

    print(MyUser.check_k(user1.k, user2.k))
    # Если все сделано правильно, то числа будут одинаковые, следовательно общий ключ создан


def menu():
    while True:
        act = int(input(
            "Выберите действие:"
            "\n1 - Генерация ключей"
            "\n2 - Пользователи"
            "\n0 - Закрыть"
            "\n--> "))
        if act == 1:
            act_1()
        elif act == 2:
            users()
        elif act == 0:
            print("До свидания!")
            exit()


if __name__ == "__main__":
    menu()
