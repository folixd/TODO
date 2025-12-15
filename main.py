from task import Task
from storage import load_tasks, save_tasks
from utils import print_task

def main():
    """
    Main function that runs the application.
    """
    tasks = load_tasks()

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            for index, task in enumerate(tasks):
                print_task(task, index)

        elif choice == "2":
            title = input("Enter task title: ")
            tasks.append(Task(title))
            save_tasks(tasks)

        elif choice == "3":
            index = int(input("Enter task index: "))
            tasks[index].mark_done()
            save_tasks(tasks)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
