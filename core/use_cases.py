from core.entities import Task
from datetime import datetime

class TaskManager:
    def __init__(self, task_repo):
        self.task_repo = task_repo 

    def add_task(self, title, description, priority, due_date):

        task = Task(
            id=self.task_repo.next_id(),
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )
        self.task_repo.save(task)
        return task

    def list_tasks(self):
        return self.task_repo.get_all()

    def complete_task(self, task_id):
        task = self.task_repo.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.is_completed = True
        self.task_repo.update(task)
