# adapters/database_adapter.py

class InMemoryTaskRepository:
    def __init__(self):
        self.tasks = []

    def save(self, task):
        # Verificar si la tarea ya existe
        for i, t in enumerate(self.tasks):
            if t.title == task.title:
                self.tasks[i] = task
                return
        self.tasks.append(task)

    def get_all(self):
        return self.tasks

    def find_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
