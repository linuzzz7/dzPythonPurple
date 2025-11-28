# commands/tasks.py
from typing import TypedDict, Optional, List
from datetime import date

PRIORITIES = {"low", "med", "high"}

class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: Optional[list[str]]
    status: str
    due: Optional[date]

# Глобальное хранилище задач
tasks: List[Task] = []
_next_id = 1

def _get_next_id() -> int:
    global _next_id
    id_ = _next_id
    _next_id += 1
    return id_

def create_order(title: str, priority: str = "med", due: Optional[date] = None, tags: Optional[list[str]] = None) -> Task:
    """Создать новую задачу"""
    if priority not in PRIORITIES:
        raise ValueError("Приоритет должен быть: low, med или high")
    if tags:
        tags = [t.strip() for t in tags if t.strip()]

    task: Task = {
        "id": _get_next_id(),
        "title": title.strip(),
        "priority": priority,
        "tags": tags,
        "status": "new",
        "due": due
    }
    tasks.append(task)
    return task

def list_orders() -> List[Task]:
    """Вернуть все задачи (отсортированные по ID)"""
    return sorted(tasks, key=lambda t: t["id"])

def _find_task(task_id: int) -> Task:
    """Вспомогательная: найти задачу по ID или ошибка"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise ValueError(f"Задача с id={task_id} не найдена")

def edit_order(task_id: int, title: Optional[str] = None, priority: Optional[str] = None, due: Optional[date] = None) -> Task:
    """Редактировать задачу"""
    task = _find_task(task_id)
    if title is not None:
        task["title"] = title.strip()
    if priority is not None:
        if priority not in PRIORITIES:
            raise ValueError("Неверный приоритет")
        task["priority"] = priority
    if due is not None:
        task["due"] = due
    return task

def remove_order(task_id: int) -> None:
    """Удалить задачу"""
    task = _find_task(task_id)
    tasks.remove(task)

def done_order(task_id: int) -> Task:
    """Отметить как выполненную"""
    task = _find_task(task_id)
    task["status"] = "done"
    return task

def add_tag(task_id: int, tag: str) -> Task:
    task = _find_task(task_id)
    if task["tags"] is None:
        task["tags"] = []
    tag = tag.strip()
    if tag not in task["tags"]:
        task["tags"].append(tag)
    return task

def remove_tag(task_id: int, tag: str) -> Task:
    task = _find_task(task_id)
    if task["tags"] and tag.strip() in task["tags"]:
        task["tags"].remove(tag.strip())
    return task