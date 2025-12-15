from datetime import datetime

class Task:
    """
    Represents a single task in the TODO application.
    Demonstrates Object-Oriented Programming (OOP).
    """

    def __init__(self, title: str):
        """
        Constructor that runs when a Task object is created.
        """
        self.title = title                  # Task name
        self.created = datetime.now()       # Timestamp when task is created
        self.completed = False              # Task status

    def mark_done(self):
        """
        Marks the task as completed.
        """
        self.completed = True

    def to_dict(self):
        """
        Converts the Task object to a dictionary.
        Used when saving to JSON.
        """
        return {
            "title": self.title,
            "created": self.created.isoformat(),
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Task object from a dictionary.
        Used when loading from JSON.
        """
        task = Task(data["title"])
        task.created = datetime.fromisoformat(data["created"])
        task.completed = data["completed"]
        return task
