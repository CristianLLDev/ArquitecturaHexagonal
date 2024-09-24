# domain/task.py

class Task:
    def __init__(self, title: str):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def __repr__(self):
        return f"Task(Tarea=='{self.title}', Se completo tarea={self.completed})"
