"""Модуль для получения таблицы"""
from tasks.tasks import Task
from datetime import date

def format_date(d: date) -> str:
    return date.strftime(d, "%Y-%m-%d")

def stringify_table(tasks: list[Task]) -> str:
    headers = ["ID", "Название", "Сумма", "Статус", "Приоритет", "Теги", "Дата"]  # ← добавили "Сумма"
    rows = []
    for task in tasks:
        tags = ",".join(sorted(task["tags"])) if task["tags"] else "-"
        amount = f"{task.get('amount', 0):.2f}" if task.get("amount") is not None else "-"
        rows.append([
            str(task["id"]),
            task["title"],
            amount,                                     # ← новая колонка
            task["status"],
            task["priority"],
            tags,
            format_date(task["due"]) if task["due"] else "-"
        ])
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(col)))

    def fmt_row(row):
        return " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(row))

    out = []
    out.append(fmt_row(headers))
    out.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        out.append(fmt_row(row))
    return "\n".join(out)


