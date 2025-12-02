"""Изменение статуса заказа"""
from tasks.tasks import find_task
from helpers.args import parse_flags

VALID_STATUSES = {"new", "paid", "canceled", "done", "in_progress"}

def status_command(tasks: list[Task], raw_args: list[str]):
    args = parse_flags(raw_args)
    task_id = args.get("--id")
    new_status = args.get("--status") or next((v for k, v in args.items() if k not in ["--id"]), None)

    if not task_id or not new_status:
        print("Использование: status --id 5 paid")
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

    new_status = new_status.lower()
    if new_status not in VALID_STATUSES:
        print(f"Статус должен быть: {', '.join(VALID_STATUSES)}")
        return

    task["status"] = new_status
    print(f"Статус заказа {task_id} изменён на: {new_status}")
