"""Модуль для редактирования тегов"""
from tasks.tasks import Task, find_task


def tags_command(tasks: list[Task], args: list[str]):
    if len(args) < 3:
        print("Использование: tags <id> add|remove <tag>")
    try:
        task_id = int(args[0])
    except ValueError:
        print("[ERROR]: id должен быть числом")
        return
    action = args[1].lower()
    tag = args[2].lower().strip()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Задача {task_id} не найдена")
        return

    if action == "add":
        if not task["tags"]:
            task["tags"] = [tag]
            return
        if tag not in task["tags"]:
            task["tags"].append(tag)
            return

    if action == "remove":
        if not task["tags"]:
            return
        try:
            task["tags"].remove(tag)
        except ValueError:
            pass
