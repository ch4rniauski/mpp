import time

from alglib.factorial import factorial_iter, factorial_rec
from alglib.gcd import gcd_iter, gcd_rec
from alglib.max_element import max_element_iter, max_element_rec


def compare(name, iter_func, rec_func, *args, repeat=100000):
    start = time.perf_counter()
    for _ in range(repeat):
        iter_func(*args)
    iter_time = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(repeat):
        rec_func(*args)
    rec_time = time.perf_counter() - start

    print(f"\n{name}:")
    print(f"  Итеративный: {iter_time:.6f} с")
    print(f"  Рекурсивный: {rec_time:.6f} с")


def read_int(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except Exception:
            print("Ошибка: нужно ввести целое число.")


def read_array():
    while True:
        text = input("Введите элементы массива через пробел: ")
        parts = text.split()
        if not parts:
            print("Ошибка: массив не может быть пустым.")
            continue
        try:
            return [int(x) for x in parts]
        except Exception:
            print("Ошибка: все элементы должны быть целыми числами.")


def task_gcd():
    a = read_int("Введите первое число: ")
    b = read_int("Введите второе число: ")
    if a == 0 and b == 0:
        print("Ошибка: оба числа не могут быть равны нулю.")
        return

    print(f"НОД({a}, {b}) = {gcd_iter(a, b)}")
    compare(f"Сравнение производительности ({a}, {b})", gcd_iter, gcd_rec, a, b) # 1071 462 - евклид


def task_factorial():
    n = read_int("Введите неотрицательное число: ")
    if n < 0:
        print("Ошибка: число должно быть неотрицательным.")
        return

    print(f"{n}! = {factorial_iter(n)}")
    compare(f"Сравнение производительности (n={n})", factorial_iter, factorial_rec, n, repeat=50000)


def task_max_element():
    arr = read_array()
    print(f"Максимальный элемент: {max_element_iter(arr)}")

    compare(
        f"Сравнение производительности (массив из {len(arr)} элементов)",
        max_element_iter,
        max_element_rec,
        arr,
        repeat=max(100, 100000 // len(arr)),
    )


def main():
    print("1 — НОД двух чисел")
    print("2 — Факториал числа")
    print("3 — Максимальный элемент массива")
    print("0 — Выход")

    tasks = {
        "1": task_gcd,
        "2": task_factorial,
        "3": task_max_element,
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
