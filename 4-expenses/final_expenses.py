all_expenses = [100, 123, 200, 50, 234, 766, 1500]
# final
def add_expense(expenses: list, value):
    return expenses.append(value)

def delete_expense(expenses: list, index):
    return expenses.pop(index)

def get_total(expenses: list):
    return sum(expenses)

def get_average(expenses: list):
    return round(sum(expenses) / len(expenses), 2)

def print_report(expenses: list):
    print(expenses)

while True:
    print(
        "1 - Добавить расход",
        "2 - Показать все расходы",
        "3 - Показать сумму и средний расход",
        "4 - Удалить расход по номеру",
        "5 - Выход",
        sep="\n"
    )
    user_input = input('Выберите один из вариантов: ')
    print("-" * 30)
    match user_input:
        case "1":
            consumption = int(input('Введите расход: '))
            add_expense(all_expenses, consumption)
        case "2":
            print_report(all_expenses)
        case "3":
            print(f'Сумму всех расходов: {get_total(all_expenses)}')
            print(f'Средний расход: {get_average(all_expenses)}')
        case "4":
            print(f"Выберите расход для удаления {all_expenses}")
            index = int(input('Номер: '))
            delete_expense(all_expenses, index)
        case "5":
            break
    print('-'*30)
