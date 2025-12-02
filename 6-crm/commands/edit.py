"""Модуль для редактирования задачи"""
from helpers.args import parse_flags
from helpers.table import stringify_table
from tasks.tasks import find_task, update_task

def edit_command(tasks: list, raw_args: list[str]):
    args = parse_flags(raw_args)
    task_id = args.get("--id")
    if not task_id:
        print("Использование: edit --id 5 [--title ...] [--amount ...] [--email ...] [--due ...]")
        return
    try:
        task_id = int(task_id)
    except:
        print("ID должен быть числом")
        return

    task = find_task(tasks, task_id)
    if not task:
        print(f"Заказ {task_id} не найден")
        return

    changes = {}
    if "--title" in args:
        changes["title"] = args["--title"]
    if "--amount" in args:
        try:
            changes["amount"] = float(args["--amount"])
        except:
            print("amount должен быть числом")
            return
    if "--email" in args:
        changes["email"] = args["--email"]
    if "--due" in args:
        from helpers.args import parse_date
        try:
            changes["due"] = parse_date(args["--due"])
        except:
            print("Неправильный формат даты")
            return

    if not changes:
        print("Ничего не указано для изменения")
        return

    # ручная правка полей
    if "title" in changes:
        task["title"] = changes["title"].strip()
    if "amount" in changes:
        task["amount"] = changes["amount"]
    if "email" in changes:
        task["email"] = changes["email"]
    if "due" in changes:
        task["due"] = changes["due"]

    print("Заказ изменён!")
    print(stringify_table([task]))