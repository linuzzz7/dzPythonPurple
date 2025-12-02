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
