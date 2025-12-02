"""Модуль вывода задач"""
from helpers.table import stringify_table
from helpers.args import parse_list
from tasks.tasks import Task


def list_command(tasks: list[Task], args: list[str]):
    subset = tasks[:]
    by = parse_list(args)
    if by == "prio":
        order = {"high": 0, "med": 1, "low": 2}
        subset = sorted(subset, key=lambda t: order.get(t["priority"], 1))
    if by == "due":
        subset = sorted(subset, key=lambda t: (t["due"] is None, t["due"]))
    if not subset:
        print("Список задач пуст")
        return
    print(stringify_table(subset))
