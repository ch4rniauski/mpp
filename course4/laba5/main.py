import math


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Сумма депозита должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise Exception("Недостаточно средств")
        self.balance -= amount


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise Exception("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


def read_positive_float(prompt):
    while True:
        text = input(prompt)
        try:
            value = float(text)
            if value <= 0:
                print("Ошибка: значение должно быть положительным.")
                continue
            return value
        except Exception:
            print("Ошибка: введите число.")


def read_int(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except Exception:
            print("Ошибка: введите целое число.")


def task1():
    name = input("Введите имя: ").strip()
    if not name:
        print("Ошибка: имя не может быть пустым.")
        return

    age = read_int("Введите возраст: ")
    if age < 0:
        print("Ошибка: возраст не может быть отрицательным.")
        return

    person = Person(name, age)
    print(person.info())


def task2():
    balance = read_int("Введите начальный баланс: ")
    if balance < 0:
        print("Ошибка: баланс не может быть отрицательным.")
        return

    account = BankAccount(balance)

    while True:
        print(f"\nТекущий баланс: {account.balance}")
        print("1 — Внести средства")
        print("2 — Снять средства")
        print("0 — Назад")

        choice = input("Выберите операцию: ")
        if choice == "0":
            break
        if choice not in ("1", "2"):
            print("Ошибка: выберите 0, 1 или 2.")
            continue

        amount = read_positive_float("Введите сумму: ")

        try:
            if choice == "1":
                account.deposit(amount)
                print("Средства внесены.")
            else:
                account.withdraw(amount)
                print("Средства сняты.")
        except Exception as e:
            print(e)


def task3():
    radius = read_positive_float("Введите радиус круга: ")
    circle = Circle(radius)

    print(f"Площадь: {circle.area():.2f}")
    print(f"Периметр: {circle.perimeter():.2f}")


def main():
    print("1 — Класс 'Человек'")
    print("2 — Класс 'Банковский счёт'")
    print("3 — Класс 'Круг'")
    print("0 — Выход")

    tasks = {
        "1": task1,
        "2": task2,
        "3": task3,
    }

    while True:
        choice = input("\nВыберите задание: ")
        if choice == "0":
            break
        if choice in tasks:
            tasks[choice]()
        else:
            print("Ошибка: выберите 0, 1, 2 или 3.")


if __name__ == "__main__":
    main()
