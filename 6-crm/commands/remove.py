"""Модуль для удаления команды"""
from tasks.tasks import remove_task
from helpers.args import parse_flags

def remove_command(tasks: list, raw_args: list[str]):
    args = parse_flags(raw_args)
    task_id = args.get("--id")
    if not task_id:
        print("Использование: remove --id 5")
        return
    try:
        task_id = int(task_id)
    except:
        print("ID должен быть числом")
        return
    if remove_task(tasks, task_id):
        print(f"Заказ {task_id} удалён!")
    else:
        print(f"Заказ {task_id} не найден")