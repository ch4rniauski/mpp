while True:
    text = input("Введите первое число: ")
    try:
        a = float(text)
        break
    except Exception:
        print("Ошибка: нужно ввести число. Попробуйте снова.")

while True:
    text = input("Введите второе число: ")
    try:
        b = float(text)
        break
    except Exception:
        print("Ошибка: нужно ввести число. Попробуйте снова.")

while True:
    text = input("Введите третье число: ")
    try:
        c = float(text)
        break
    except Exception:
        print("Ошибка: нужно ввести число. Попробуйте снова.")

average = (a + b + c) / 3

print(f"\nСреднее арифметическое: {average}")
