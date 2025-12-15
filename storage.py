import json
import os
from task import Task

FILE_NAME = "tasks.json"

def load_tasks():
    """
    Loads tasks from a JSON file.
    If the file does not exist, returns an empty list.
    """
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        data = json.load(file)
        return [Task.from_dict(item) for item in data]

def save_tasks(tasks):
    """
    Saves all tasks to a JSON file.
    """
    with open(FILE_NAME, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=2)
