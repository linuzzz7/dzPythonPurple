"""Изменение статуса заказа"""
from tasks.tasks import find_task
from helpers.args import parse_flags

VALID_STATUSES = {"new", "paid", "canceled", "done", "in_progress"}

def status_command(tasks: list, raw_args: list[str]):
    args = parse_flags(raw_args)

    task_id_str = args.get("--id")
    if not task_id_str:
        print("Использование: status --id 5 paid")
        return

    try:
        task_id = int(task_id_str)
    except ValueError:
        print("ID должен быть числом")
        return

    # Ищем первый аргумент, который НЕ флаг (это и есть статус)
    status = None
    for arg in raw_args:
        if not arg.startswith("--"):
            status = arg.lower()
            break

    if not status:
        print("Укажите новый статус: new, paid, canceled, done, in_progress")
        return

    if status not in VALID_STATUSES:
        print(f"Недопустимый статус. Доступно: {', '.join(VALID_STATUSES)}")
        return

    task = find_task(tasks, task_id)
    if not task:
        print(f"Заказ {task_id} не найден")
        return

    old_status = task["status"]
    task["status"] = status
    print(f"Статус заказа {task_id} изменён: {old_status} → {status}")