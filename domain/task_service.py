# domain/task_service.py

from .task import Task

class TaskService:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def add_task(self, title: str):
        task = Task(title)
        self.task_repository.save(task)

    def get_all_tasks(self):
        return self.task_repository.get_all()

    def complete_task(self, title: str):
        task = self.task_repository.find_by_title(title)
        if task:
            task.complete()
            self.task_repository.save(task)
