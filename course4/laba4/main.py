def read_numbers():
    while True:
        text = input("Введите числа через пробел: ")
        parts = text.split()
        if not parts:
            print("Ошибка: список не может быть пустым.")
            continue
        try:
            return [int(x) for x in parts]
        except Exception:
            print("Ошибка: все элементы должны быть целыми числами.")


def count_words(text):
    for sep in ".!?":
        text = text.replace(sep, " ")
    return len([word for word in text.split() if word])


def count_sentences(text):
    for sep in ".!?":
        text = text.replace(sep, "\n")
    return len([part for part in text.split("\n") if part.strip()])


def task1():
    text = input("Введите строку: ")
    if not text.strip():
        print("Ошибка: строка не может быть пустой.")
        return

    chars = len(text)
    words = count_words(text)
    sentences = count_sentences(text)

    print(f"Символов: {chars}")
    print(f"Слов: {words}")
    print(f"Предложений: {sentences}")


def task2():
    text = input("Введите строки через запятую: ")
    strings = [s.strip() for s in text.split(",") if s.strip()]
    if not strings:
        print("Ошибка: список строк не может быть пустым.")
        return

    result = "-".join(strings)
    print(f"Результат: {result}")


def task3():
    numbers = read_numbers()

    while True:
        choice = input("Сортировка (1 — по возрастанию, 2 — по убыванию): ")
        if choice == "1":
            numbers.sort()
            break
        if choice == "2":
            numbers.sort(reverse=True)
            break
        print("Ошибка: выберите 1 или 2.")

    print(f"Отсортированный список: {numbers}")


def main():
    print("1 — Количество символов, слов и предложений в строке")
    print("2 — Объединение списка строк через разделитель '-'")
    print("3 — Сортировка списка чисел")
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
