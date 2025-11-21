import sys

books = {
    "Ангелы и Демоны": "Ден Браун",
    "Код Да Винчи": "Ден Браун",
    "Золушка": "Шарль Перро",
    "Принцесса Марса": "Эдгар Берроуз",  # исправил опечатку в имени
}

def main():
    if len(sys.argv) < 2:
        print("Использование: python books.py <action> [аргументы]")
        return

    action = sys.argv[1]

    # Формируем строку "Книга — Автор" для каждой книги
    def format_book(title):
        return f"{title} — {books[title]}"

    if action == "filter":
        if len(sys.argv) < 3:
            print("Укажите автора для фильтрации: python books.py filter \"Ден Браун\"")
            return

        author_to_find = sys.argv[2]

        # Фильтруем книги по автору + сразу форматируем
        filtered_books = filter(lambda title: books[title] == author_to_find, books.keys())
        result = map(format_book, filtered_books)

        for line in result:
            print(line)

        # Если ничего не нашли
        if not any(books[title] == author_to_find for title in books):
            print("Книг этого автора не найдено.")

    elif action == "sort":
        if len(sys.argv) < 3:
            print("Укажите поле для сортировки: python books.py sort author  или  python books.py sort book")
            return

        sort_by = sys.argv[2].lower()

        # Сначала получаем список пар (книга, автор)
        items = list(books.items())  # [("Ангелы и Демоны", "Ден Браун"), ...]

        if sort_by == "author":
            # Сортировка по автору (второму элементу кортежа)
            sorted_items = sorted(items, key=lambda x: x[1])
        elif sort_by == "book":
            # Сортировка по названию книги (первому элементу)
            sorted_items = sorted(items, key=lambda x: x[0])
        else:
            print("Неверное поле. Используйте 'author' или 'book'")
            return

        # Формируем строки через map
        result = map(lambda pair: f"{pair[0]} — {pair[1]}", sorted_items)

        for line in result:
            print(line)

    else:
        print("Неизвестное действие. Доступно: filter, sort")

if __name__ == "__main__":
    main()
