from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: int
    due_date: datetime
    is_completed: bool = False
