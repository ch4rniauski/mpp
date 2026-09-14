import json


objects = []

print("Ввод объектов (пустая строка в имени — завершить)")
print("Каждый объект: имя, фамилия, возраст")

while True:
    name = input("\nИмя: ").strip()
    if name == "":
        break

    while True:
        surname = input("Фамилия: ").strip()
        if surname:
            break
        print("Ошибка: фамилия не может быть пустой.")

    while True:
        age_text = input("Возраст: ").strip()
        try:
            age = int(age_text)
        except Exception:
            print("Ошибка: возраст должен быть целым числом.")
            continue
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным.")
            continue
        break

    obj = {
        "name": name,
        "surname": surname,
        "age": age,
    }
    objects.append(obj)
    print(f"Добавлен объект: {obj}")

if not objects:
    print("Список объектов пуст. Файл не создан.")
else:
    json_string = json.dumps(objects, ensure_ascii=False, indent=4)
    print("\nJSON:")
    print(json_string)

    filename = input("\nВведите имя файла для сохранения: ").strip()
    if not filename:
        filename = "objects.json"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_string)

    print(f"Данные сохранены в файл '{filename}'.")
