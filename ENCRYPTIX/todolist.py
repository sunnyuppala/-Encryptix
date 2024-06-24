class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, task_description):
        if task_name in self.tasks:
            print("Task already exists. Please choose a different name.")
        else:
            self.tasks[task_name] = task_description
            print(f"Task '{task_name}' added successfully.")

    def update_task(self, task_name, new_description):
        if task_name in self.tasks:
            self.tasks[task_name] = new_description
            print(f"Task '{task_name}' updated successfully.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def delete_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted successfully.")
        else:
            print(f"Task '{task_name}' does not exist.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task, description in self.tasks.items():
                print(f"Task: {task}\nDescription: {description}\n")

    def run(self):
        while True:
            print("\n1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. View Tasks")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                self.add_task(task_name, task_description)
            elif choice == "2":
                task_name = input("Enter task name: ")
                new_description = input("Enter new task description: ")
                self.update_task(task_name, new_description)
            elif choice == "3":
                task_name = input("Enter task name: ")
                self.delete_task(task_name)
            elif choice == "4":
                self.view_tasks()
            elif choice == "5":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()