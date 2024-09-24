# main.py

from adapters.database_adapter import InMemoryTaskRepository
from adapters.cli_adapter import CLIAdapter
from domain.task_service import TaskService

if __name__ == "__main__":
    task_repository = InMemoryTaskRepository()
    task_service = TaskService(task_repository)
    cli_adapter = CLIAdapter(task_service)

    cli_adapter.run()
