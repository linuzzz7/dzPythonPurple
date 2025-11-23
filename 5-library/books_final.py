import sys


# Базовый класс для всех ошибок приложения
class BooksAppError(Exception):
    """Базовое исключение для приложения"""
    pass


# Конкретные ошибки
class MissingArgumentError(BooksAppError):
    def __init__(self, action):
        self.action = action
        super().__init__(f"Для команды '{action}' не указан обязательный аргумент.")


class UnknownActionError(BooksAppError):
    def __init__(self, action):
        self.action = action
        super().__init__(f"Неизвестная команда: '{action}'. Доступные: filter, sort")


class InvalidSortFieldError(BooksAppError):
    def __init__(self, field):
        self.field = field
        super().__init__(f"Неверное поле для сортировки: '{field}'. Используйте 'author' или 'book'")


# Данные
books = {
    "Ангелы и Демоны": "Ден Браун",
    "Код Да Винчи": "Ден Браун",
    "Золушка": "Шарль Перро",
    "Принцесса Марса": "Эдгар Берроуз",
}


def format_book(title):
    return f"{title} — {books[title]}"


def filter_by_author(author_to_find):
    matching_titles = [title for title in books if books[title] == author_to_find]
    if not matching_titles:
        print("Книг этого автора не найдено.")
        return

    for title in matching_titles:
        print(format_book(title))


def sort_books(by_field):
    items = list(books.items())

    if by_field == "author":
        sorted_items = sorted(items, key=lambda x: x[1])
    elif by_field == "book":
        sorted_items = sorted(items, key=lambda x: x[0])
    else:
        raise InvalidSortFieldError(by_field)

    for title, author in sorted_items:
        print(f"{title} — {author}")


def main():
    try:
        if len(sys.argv) < 2:
            print("Использование: python books.py <action> [аргументы]")
            print("Команды: filter <автор> | sort <author|book>")
            return

        action = sys.argv[1].lower()

        if action == "filter":
            if len(sys.argv) < 3:
                raise MissingArgumentError("filter")
            author = sys.argv[2]
            filter_by_author(author)

        elif action == "sort":
            if len(sys.argv) < 3:
                raise MissingArgumentError("sort")
            sort_field = sys.argv[2].lower()
            sort_books(sort_field)

        else:
            raise UnknownActionError(action)

    except BooksAppError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        # На всякий случай ловим неожиданные ошибки
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
