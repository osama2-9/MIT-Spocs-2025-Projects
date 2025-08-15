# test_task_manager.py

from task_manager import TaskManager

tasks = [
        {"title": "Task One", "priority": "High", "status": "Todo"},
        {"title": "Task Two", "priority": "Low", "status": "Doing"},
        {"title": "Task Three", "priority": "Medium", "status": "Todo"}
]

def test_add_task():
    tm = TaskManager()
    task_input = {
        "title": "Go to the AUC",
        "priority": "High",
        "status": "Todo",
    }

    tm.add_task(task_input)

    expected = {
        "id": 1,
        **task_input
    }
    actual = tm.get_tasks_by_status('Todo')[0]
    print("Actual task:", actual)
    print("Expected task:", expected)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_get_tasks_by_status():
    tm = TaskManager()

    tm.add_task(tasks[0])
    tm.add_task(tasks[1])
    tm.add_task(tasks[2])

    # Test exact match
    todo_tasks = tm.get_tasks_by_status("Todo")
    assert len(todo_tasks) == 2
    assert todo_tasks[0]["title"] == "Task One"
    assert todo_tasks[1]["title"] == "Task Three"

    doing_tasks = tm.get_tasks_by_status("doing")
    assert len(doing_tasks) == 1
    assert doing_tasks[0]["title"] == "Task Two"

def test_remove_task():
    tm = TaskManager()
    tm.add_task(tasks[0])
    tm.add_task(tasks[1])

    result = tm.remove_task(1)
    assert result == True, f"Expected {True}, but got {False}"

def test_complete_task():
    tm = TaskManager()
    tm.add_task(tasks[0])
    tm.add_task(tasks[1])

    updated_task = tm.complete_task(1)

    assert updated_task["status"] == "Done"

def test_get_task():
    tm = TaskManager()
    tm.add_task(tasks[0])
    tm.add_task(tasks[1])

    result = tm.get_task(1)

    assert result["title"] == "Task One"

def test_edit_task():
    tm = TaskManager()
    tm.add_task(tasks[0])
    tm.add_task(tasks[1])

    updated_task = tm.edit_task(1, 'title', 'Updated Title')

    assert updated_task["title"] == "Updated Title"
    