def task1():
    filename = input("Введите имя файла: ").strip()
    if not filename:
        print("Ошибка: имя файла не может быть пустым.")
        return

    print("Введите текст (пустая строка для завершения):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("Ошибка: текст не может быть пустым.")
        return

    try:
        with open(filename, "w") as file:
            file.write("\n".join(lines))
        print(f"Данные сохранены в файл '{filename}'.")
    except Exception:
        print("Ошибка: не удалось записать файл.")


def task2():
    filename = input("Введите имя файла: ").strip()
    if not filename:
        print("Ошибка: имя файла не может быть пустым.")
        return

    try:
        with open(filename, "r") as file:
            content = file.read()
    except Exception:
        print("Ошибка: не удалось прочитать файл.")
        return

    words = content.split()
    print(f"Количество слов: {len(words)}")


def task3():
    filename = input("Введите имя файла: ").strip()
    if not filename:
        print("Ошибка: имя файла не может быть пустым.")
        return

    keyword = input("Введите ключевое слово: ").strip()
    if not keyword:
        print("Ошибка: ключевое слово не может быть пустым.")
        return

    try:
        with open(filename, "r") as file:
            for line in file:
                if keyword in line:
                    print(line, end="")
    except Exception:
        print("Ошибка: не удалось прочитать файл.")


def main():
    print("1 — Сохранение ввода с клавиатуры в файл")
    print("2 — Подсчёт слов в файле")
    print("3 — Поиск строк по ключевому слову")
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
