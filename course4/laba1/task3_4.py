while True:
    last_name = input("Введите фамилию: ").strip()
    if last_name != "":
        break
    print("Ошибка: фамилия не может быть пустой. Попробуйте снова.")

while True:
    first_name = input("Введите имя: ").strip()
    if first_name != "":
        break
    print("Ошибка: имя не может быть пустым. Попробуйте снова.")

while True:
    middle_name = input("Введите отчество: ").strip()
    if middle_name != "":
        break
    print("Ошибка: отчество не может быть пустым. Попробуйте снова.")

while True:
    text = input("Введите год рождения: ")
    try:
        birth_year = int(text)
        if 1900 <= birth_year <= 2026:
            break
        else:
            print("Ошибка: год рождения должен быть от 1900 до 2026.")
    except Exception:
        print("Ошибка: нужно ввести целое число. Попробуйте снова.")

print("\nДанные студента сохранены.")
print(f"ФИО: {last_name} {first_name} {middle_name}")
print(f"Год рождения: {birth_year}")

names = ["Фамилия", "Имя", "Отчество", "Год рождения"]
types = [str(type(last_name)), str(type(first_name)), str(type(middle_name)), str(type(birth_year))]
values = [last_name, first_name, middle_name, str(birth_year)]

min_width = max(len("Название"), len("Тип"), len("Значение"))
i = 0
while i < 4:
    min_width = max(min_width, len(names[i]), len(types[i]), len(values[i]))
    i = i + 1
min_width = min_width

while True:
    col_sep = input("Введите символ для разделителя столбцов: ")
    if len(col_sep) == 1:
        break
    print("Ошибка: нужно ввести ровно один символ. Попробуйте снова.")

while True:
    row_sep = input("Введите символ для разделителя строк: ")
    if len(row_sep) == 1:
        break
    print("Ошибка: нужно ввести ровно один символ. Попробуйте снова.")

while True:
    text = input("Введите количество символов в каждом столбце: ")
    try:
        width = int(text)
        if width >= min_width:
            break
        else:
            print(f"Ошибка: ширина столбца должна быть не меньше {min_width} "
                  f"(иначе данные не поместятся).")
    except Exception:
        print("Ошибка: нужно ввести целое число. Попробуйте снова.")

while True:
    fill_char = input("Введите символ для замены пропусков: ")
    if len(fill_char) != 1:
        print("Ошибка: нужно ввести ровно один символ. Попробуйте снова.")
    elif fill_char == col_sep:
        print("Ошибка: символ пропусков не должен совпадать с разделителем столбцов.")
    elif fill_char == row_sep:
        print("Ошибка: символ пропусков не должен совпадать с разделителем строк.")
    else:
        break

header_name = "Название".ljust(width, fill_char)
header_type = "Тип".center(width, fill_char)
header_value = "Значение".rjust(width, fill_char)
header_line = header_name + col_sep + header_type + col_sep + header_value
separator_line = row_sep * len(header_line)

print()
print(separator_line)
print(header_line)
print(separator_line)

i = 0
while i < 4:
    col1 = names[i].ljust(width, fill_char)
    col2 = types[i].center(width, fill_char)
    col3 = values[i].rjust(width, fill_char)
    print(col1 + col_sep + col2 + col_sep + col3)
    print(separator_line)
    i = i + 1
