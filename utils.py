from colorama import Fore, Style

def print_task(task, index):
    """
    Prints a task with color depending on completion status.
    """
    status = "✓" if task.completed else " "
    color = Fore.GREEN if task.completed else Fore.YELLOW

    print(
        color +
        f"{index}. [{status}] {task.title}" +
        Style.RESET_ALL
    )
