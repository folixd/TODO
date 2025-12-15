from task import Task

def test_mark_done():
    """
    Tests that a task is correctly marked as completed.
    """
    task = Task("Test task")
    task.mark_done()
    assert task.completed is True
