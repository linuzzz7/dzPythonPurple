from typing import TypedDict

# Зададим приоритеты
STATUS = {"new", "in_progress", "done", "cancelled"}


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: set
    created_at: None
    due: None
    closed_at: None

def create_order():
    pass

def list_orders():
    pass

def edit_order():
    pass

def remove_order():
    pass
