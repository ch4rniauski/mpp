def f(x):
    if x < -1:
        return x + 4
    elif -1 <= x < 1:
        return x ** 2 + 2
    else:
        return 2 * x


print("Введите границы интервала a и b (целые числа).")
print("Для завершения введите 'стоп'.")

while True:
    a_str = input("\na = ")
    if a_str.lower() == "стоп":
        print("Программа завершена.")
        break

    b_str = input("b = ")
    if b_str.lower() == "стоп":
        print("Программа завершена.")
        break

    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        print("Ошибка: a и b должны быть целыми числами.")
        continue

    if a > b:
        print("Ошибка: a не должно быть больше b.")
        continue

    print(f"Значения f(x) на интервале [{a}, {b}]:")
    for x in range(a, b + 1):
        print(f"f({x}) = {f(x)}")
