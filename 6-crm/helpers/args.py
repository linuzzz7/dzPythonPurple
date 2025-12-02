"""Модуль разбора аргументов"""
from datetime import date, datetime

def parse_list(args: list[str]):
    by = None
    for arg in args:
        if arg.startswith("by="):
            by = arg.split("=", 1)[1]
    return by

def parse_add(args: list[str]):
    if not args:
        raise ValueError("Использование: add <название> [prio=low|med|high] [due=YYYY-MM-DD] [tags=tag1,tag2]")

    title = args[0]
    prio, due, tags = "med", None, None

    for arg in args[1:]:
        if arg.startswith("prio="):
            prio = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_str = arg.split("=", 1)[1]
            try:
                due = parse_date(due_str)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {due_str}. Ожидаем YYYY-MM-DD"
                ) from e
        elif arg.startswith("tags="):
            tags_str = arg.split("=", 1)[1]
            tags = tags_str.split(",")

    return title, prio, due, tags

def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def parse_edit(args: list[str]):
    if len(args) < 2:
        raise ValueError("Неверно передана команда")
    task_id = 0
    try:
        task_id = int(args[0])
    except ValueError as e:
        raise ValueError("Неверно передан ID задачи") from e
    changes = {}
    for arg in args[1:]:
        if arg.startswith("title="):
            changes["title"] = arg.split("=", 1)[1]
        if arg.startswith("prio="):
            changes["prio"] = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_str = arg.split("=", 1)[1]
            try:
                changes["due"] = parse_date(due_str)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {due_str}. Ожидаем YYYY-MM-DD"
                ) from e
    return task_id, changes

def parse_flags(args_list: list[str]) -> dict:
    """Превращает ['--title', 'Купить молоко', '--amount', '150.5'] в словарь"""
    result = {}
    i = 0
    while i < len(args_list):
        arg = args_list[i]
        if arg.startswith("--"):
            key = arg
            if i + 1 < len(args_list) and not args_list[i+1].startswith("--"):
                result[key] = args_list[i+1]
                i += 2
            else:
                result[key] = True
                i += 1
        else:
            i += 1
    return result

def get_id_from_args(args_dict: dict) -> int | None:
    if "--id" in args_dict:
        try:
            return int(args_dict["--id"])
        except:
            pass
    return None