# storage/file.py
import json
from datetime import date
from typing import List, Optional
from tasks.tasks import Task
from helpers.args import parse_date
from helpers.table import format_date


DATA_FILE = "tasks.json"


def save(items: List[Task]) -> None:
    """
    Сохраняет список задач в JSON-файл.
    """
    data = {
        "tasks": [
            {
                "id": task["id"],
                "title": task["title"],
                "priority": task["priority"],
                "status": task["status"],
                "tags": task["tags"] or [],
                "due": format_date(task["due"]) if task["due"] else None
            }
            for task in items
        ]
    }
    
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")


def load() -> tuple[List[Task], int]:
    """
    Загружает задачи из JSON-файла.
    - Если файла нет → возвращает ([], 1)
    - Если JSON повреждён → выводит предупреждение и возвращает ([], 1)
    """
    tasks: List[Task] = []
    next_id = 1

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        # Файл ещё не создан — это нормально
        return [], 1
    except json.JSONDecodeError as e:
        print(f"[WARN] Файл {DATA_FILE} повреждён (неверный JSON): {e}")
        print("[INFO] Будет создан новый пустой список задач.")
        return [], 1
    except Exception as e:
        print(f"[ERROR] Ошибка чтения файла {DATA_FILE}: {e}")
        return [], 1

    # Если вдруг структура совсем другая
    if not isinstance(raw, dict) or "tasks" not in raw:
        print(f"[WARN] Неверный формат данных в {DATA_FILE}, ожидаются задачи в ключе 'tasks'")
        return [], 1

    for item in raw["tasks"]:
        try:
            due_date: Optional[date] = None
            if item.get("due"):
                due_date = parse_date(item["due"])

            task: Task = {
                "id": int(item["id"]),
                "title": str(item["title"]),
                "priority": str(item["priority"]),
                "status": str(item.get("status", "new")),
                "tags": [str(t) for t in (item.get("tags") or [])],
                "due": due_date
            }
            tasks.append(task)
            next_id = max(next_id, task["id"] + 1)
        except (KeyError, TypeError, ValueError) as e:
            print(f"[WARN] Пропущена некорректная задача в файле: {e} → {item}")

    print(f"[INFO] Загружено задач: {len(tasks)}")
    return tasks, next_id
