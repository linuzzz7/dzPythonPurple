books = {"Ангелы и Демоны": "Ден Браун",
         "Код Да Винчи": "Ден Браун",
         "Золушка": "Шарль Перро",
         "Принцесса Марса": "Эдгар Бероузов", }

print(f'Список всех книг:')
for book in books.keys():
    print("-", book)

autors = set()

for autor in books.values():
    autors.add(autor)

print('\nУникальные авторы:')
for autor in autors:
    print("-", autor)
