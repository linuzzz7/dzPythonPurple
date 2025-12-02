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

def make_task(id_: int, title: str, due: Optional[date] = None, priority: str = "med", tags: Optional[list[str]] = None):  
    if priority not in PRIORITIES:  
        raise ValueError("Неверный приоритет. Доступные приоритеты: low | med |high")  
    task: Task = {  
        "id": id_,  
        "title": title.strip(),  
        "priority": priority,  
        "tags": tags,  
        "status": "new",  
        "due": due  
    }  
  
    return task

def remove_task(tasks: list[Task], task_id) -> bool:
    before_len = len(tasks)
    tasks[:] = list(filter(lambda  t: t["id"] != task_id, tasks))
    return  len(tasks) < before_len

# update_task(task, title="123", prio="low")
def update_task(task: Task, **changes):
    if "title" in changes:
        title = str(changes["title"]).strip()
        if not title:
            raise ValueError("Заголовок не может быть пустым")
        task["title"] = title
    if "prio" in changes:
        prio = str(changes["prio"]).strip().lower()
        if prio not in PRIORITIES:
            raise ValueError("Неверный приоритет. Только: low | med | high")
        task["priority"] = prio
    if "due" in changes:
        due = changes["due"]
        if due is not None and not isinstance(due, date):
            raise TypeError("Поле due должно быть date или None")
        task["due"] = due

def find_task(tasks: list[Task], id_: int) -> Optional[Task]:
    return next((t for t in tasks if t["id"] == id_), None)
