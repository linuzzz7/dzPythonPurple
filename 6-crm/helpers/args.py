# helpers/args.py
from datetime import date, datetime
from typing import Optional


def parse_date(date_str: str) -> date:
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается: YYYY-MM-DD")


def parse_add(args: list[str]):
    if not args:
        raise ValueError("Использование: add <название> [prio=low|med|high] [due=YYYY-MM-DD] [tags=tag1,tag2]")

    title = args[0]
    prio = "med"
    due: Optional[date] = None
    tags: Optional[list[str]] = None

    for arg in args[1:]:
        if arg.startswith("prio="):
            prio = arg.split("=", 1)[1].lower()
        elif arg.startswith("due="):
            due = parse_date(arg.split("=", 1)[1])
        elif arg.startswith("tags="):
            tags_raw = arg.split("=", 1)[1]
            tags = [t.strip() for t in tags_raw.split(",") if t.strip()]

    return title, prio, due, tags