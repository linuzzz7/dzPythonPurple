"""Модуль вывода задач"""
from helpers.table import stringify_table
from helpers.args import parse_flags
from datetime import date

def list_command(tasks: list[Task], raw_args: list[str]):
    args = parse_flags(raw_args)

    subset = tasks[:]

    # Фильтр по тегу
    if "--tag" in args:
        tag = args["--tag"].lower()
        subset = [t for t in subset if tag in [tg.lower() for tg in (t.get("tags") or [])]]

    # Просроченные
    if "--overdue" in args:
        today = date.today()
        subset = [t for t in subset if t["due"] and t["due"] < today and t["status"] != "done"]

    # Лимит
    limit = None
    if "--limit" in args:
        try:
            limit = int(args["--limit"])
            subset = subset[:limit]
        except:
            print("[WARN] --limit должен быть числом")

    if not subset:
        print("Нет заказов по заданным фильтрам")
        return

    print(stringify_table(subset))