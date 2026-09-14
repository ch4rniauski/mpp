import requests


API_KEY = "oaF6uuNBKLHDA4rBG9eHRS8C1zdILr7h8AI3vu4p"
#API_KEY = "DEMO_KEY"


def show_apod():
    date = input("Введите дату (ГГГГ-ММ-ДД) или Enter для сегодня: ").strip()

    params = {"api_key": API_KEY}
    if date:
        params["date"] = date

    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)

    print(f"\nСтатус: {response.status_code} {response.reason}")

    if response.status_code != 200:
        print("Ошибка:", response.text)
        return

    data = response.json()
    print("Заголовок:", data.get("title"))
    print("Дата:", data.get("date"))
    print("Тип медиа:", data.get("media_type"))
    print("URL:", data.get("url"))
    print("Описание:", data.get("explanation"))


def show_space_photos():
    query = input("Введите запрос (например: mars, galaxy, moon): ").strip()
    if not query:
        query = "mars"

    response = requests.get(
        "https://images-api.nasa.gov/search",
        params={
            "q": query,
            "media_type": "image",
        },
    )

    print(f"\nСтатус: {response.status_code} {response.reason}")

    if response.status_code != 200:
        print("Ошибка:", response.text)
        return

    items = response.json().get("collection", {}).get("items", [])
    print(f"Найдено изображений: {len(items)}")

    if not items:
        print("Ничего не найдено.")
        return

    limit = min(5, len(items))
    print(f"Показываю первые {limit}:\n")

    for i, item in enumerate(items[:limit], start=1):
        data = item.get("data", [{}])[0]
        links = item.get("links", [{}])
        href = links[0].get("href") if links else None

        description = data.get("description") or ""
        if len(description) > 200:
            description = description[:200] + "..."

        print(f"{i}. {data.get('title')}")
        print(f"   Дата: {data.get('date_created')}")
        print(f"   Описание: {description}")
        print(f"   URL: {href}")
        print()


def show_neo():
    date = input("Введите дату (ГГГГ-ММ-ДД) или Enter для 2020-07-01: ").strip()
    if not date:
        date = "2020-07-01"

    response = requests.get(
        "https://api.nasa.gov/neo/rest/v1/feed",
        params={
            "start_date": date,
            "end_date": date,
            "api_key": API_KEY,
        },
    )

    print(f"\nСтатус: {response.status_code} {response.reason}")

    if response.status_code != 200:
        print("Ошибка:", response.text)
        return

    data = response.json()
    near_earth = data.get("near_earth_objects", {}).get(date, [])
    print(f"Объектов рядом с Землёй за {date}: {len(near_earth)}\n")

    if not near_earth:
        print("Объектов не найдено.")
        return

    limit = min(5, len(near_earth))
    print(f"Показываю первые {limit}:\n")

    for i, obj in enumerate(near_earth[:limit], start=1):
        diameter = obj.get("estimated_diameter", {}).get("meters", {})
        approach = obj.get("close_approach_data", [{}])[0]

        print(f"{i}. Название: {obj.get('name')}")
        print(f"   Опасный: {obj.get('is_potentially_hazardous_asteroid')}")
        print(
            f"   Диаметр (м): "
            f"{diameter.get('estimated_diameter_min'):.1f} - "
            f"{diameter.get('estimated_diameter_max'):.1f}"
        )
        print(f"   Сближение: {approach.get('close_approach_date')}")
        print(
            f"   Скорость (км/ч): "
            f"{approach.get('relative_velocity', {}).get('kilometers_per_hour')}"
        )
        print(
            f"   Расстояние (км): "
            f"{approach.get('miss_distance', {}).get('kilometers')}"
        )
        print()


def main():
    print("NASA API — космические фото и события")
    print("1 — Фото дня (APOD)")
    print("2 — Поиск космических фото")
    print("3 — Близкие к Земле объекты (NEO)")
    print("0 — Выход")

    while True:
        choice = input("\nВыберите действие: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            show_apod()
        elif choice == "2":
            show_space_photos()
        elif choice == "3":
            show_neo()
        else:
            print("Ошибка: выберите 0, 1, 2 или 3.")


if __name__ == "__main__":
    main()
