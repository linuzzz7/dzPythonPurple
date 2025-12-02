"""Модуль для редактирования тегов"""
from tasks.tasks import find_task
from helpers.args import parse_flags

def tags_command(tasks: list[Task], raw_args: list[str]):
    args = parse_flags(raw_args)
    task_id = args.get("--id")

    if not task_id:
        print("Использование: tags --id 5 [--add work,urgent] [--remove old]")
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

    if "tags" not in task or task["tags"] is None:
        task["tags"] = []

    changed = False

    if "--add" in args:
        new_tags = [t.strip().lower() for t in args["--add"].split(",") if t.strip()]
        for tag in new_tags:
            if tag not in task["tags"]:
                task["tags"].append(tag)
                changed = True

    if "--remove" in args:
        del_tags = [t.strip().lower() for t in args["--remove"].split(",") if t.strip()]
        for tag in del_tags:
            if tag in task["tags"]:
                task["tags"].remove(tag)
                changed = True

    if not changed and ("--add" in args or "--remove" in args):
        print("Нечего менять")
    elif changed:
        print(f"Теги обновлены для заказа {task_id}")