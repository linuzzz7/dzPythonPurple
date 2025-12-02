# storage/file.py
import json
from datetime import date
from typing import List, Optional
from tasks.tasks import Task
from helpers.args import parse_date
from helpers.table import format_date

DATA_FILE = "tasks.json"

def save(items: List[Task]) -> None:
    data = {
        "tasks": [
            {
                "id": t["id"],
                "title": t["title"],
                "priority": t["priority"],
                "status": t["status"],
                "tags": t["tags"] or [],
                "due": format_date(t["due"]) if t["due"] else None,
                "amount": t.get("amount"),           # ← ДОБАВИЛИ
                "email": t.get("email")              # ← ДОБАВИЛИ
            }
            for t in items
        ]
    }
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить задачи: {e}")

def load() -> tuple[List[Task], int]:
    tasks: List[Task] = []
    next_id = 1

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
        print("[INFO] Файл успешно прочитан в UTF-8")
    except FileNotFoundError:
        return [], 1
    except UnicodeDecodeError:
        print("[WARN] Файл не в UTF-8, пробуем Windows-1251...")
        try:
            with open(DATA_FILE, "r", encoding="cp1251") as f:
                raw = json.load(f)
            print("[INFO] Успешно прочитано в cp1251. Пересохраняю в UTF-8...")
        except Exception as e:
            print(f"[ERROR] Не удалось прочитать даже в cp1251: {e}")
            return [], 1
    except json.JSONDecodeError as e:
        print(f"[WARN] Повреждённый JSON: {e}")
        return [], 1
    except Exception as e:
        print(f"[ERROR] Ошибка загрузки: {e}")
        return [], 1

    if not isinstance(raw, dict) or "tasks" not in raw:
        print("[WARN] Неверный формат файла задач")
        return [], 1

    for item in raw["tasks"]:
        try:
            due_date: Optional[date] = None
            if item.get("due"):
                due_date = parse_date(item["due"])

            task: Task = {
                "id": int(item["id"]),
                "title": str(item.get("title", "")),
                "priority": str(item.get("priority", "med")),
                "status": str(item.get("status", "new")),
                "tags": [str(t) for t in (item.get("tags") or [])],
                "due": due_date,
                "amount": float(item["amount"]) if item.get("amount") is not None else None,  # ← ВОССТАНАВЛИВАЕМ
                "email": str(item.get("email", ""))                                          # ← ВОССТАНАВЛИВАЕМ
            }
            tasks.append(task)
            next_id = max(next_id, task["id"] + 1)
        except Exception as e:
            print(f"[WARN] Пропущена битая задача: {e}")

    if tasks:
        save(tasks)  # пересохраняем в UTF-8, если читали из cp1251
    print(f"[INFO] Загружено задач: {len(tasks)}")
    return tasks, next_id