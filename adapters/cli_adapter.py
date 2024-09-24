# adapters/cli_adapter.py

class CLIAdapter:
    def __init__(self, task_service):
        self.task_service = task_service

    def display_menu(self):
        print("1. Añadir tarea")
        print("2. Listar Tareas")
        print("3. Completar Tareas")
        print("4. salir")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Seleccionar opcion: ")
            if choice == '1':
                title = input("Ingrese el titulo de la tarea: ")
                self.task_service.add_task(title)
            elif choice == '2':
                tasks = self.task_service.get_all_tasks()
                for task in tasks:
                    print(task)
            elif choice == '3':
                title = input("Enter task title to complete: ")
                self.task_service.complete_task(title)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
