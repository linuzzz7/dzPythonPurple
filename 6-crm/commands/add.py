"""Модуль для добавления команды"""
from tasks.tasks import Task, make_task
from helpers.args import parse_flags, get_id_from_args
from helpers.table import stringify_table

def add_command(tasks: list[Task], raw_args: list[str], next_id: int):
    args = parse_flags(raw_args)
    title = args.get("--title")
    amount = args.get("--amount")
    email = args.get("--email")
    due = args.get("--due")
    tags_str = args.get("--tags")

    if not title or not amount or not email:
        print("Ошибка: нужны --title, --amount и --email")
        return next_id

    try:
        amount = float(amount)
    except:
        print("Ошибка: --amount должен быть числом (например 123.45)")
        return next_id

    tags = None
    if tags_str:
        tags = [t.strip() for t in tags_str.split(",") if t.strip()]

    if due:
        from helpers.args import parse_date
        try:
            due = parse_date(due)
        except:
            print("Ошибка: --due должен быть в формате YYYY-MM-DD")
            return next_id

    task = make_task(next_id, title, due, "med", tags)
    task["amount"] = amount
    task["email"] = email
    tasks.append(task)
    print("Заказ добавлен!")
    print(stringify_table([task]))
    return next_id + 1