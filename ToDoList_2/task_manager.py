# task_manager.py

# ToDo List to keep track of task and should be dictionary
# Ex: [{"task_id": 1, "title": "AUC CLass", "priority": "High", "status": "To Do" }]
# Task_id => Number
# Title => String
# Priority => String ("High" / "Medium" / "Low")
# Status => String ("To Do" / "Doing" / "Done")
# Description => String

class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    # ToDo => Function to validate task, task will be a dictionary
    def validation(self, task_input):
        for field in ["title", "priority", "status"]:

            if field not in task_input:
                raise ValueError(f"Missing required field: {field}")

        if task_input["priority"] not in ["Low", "Medium", "High"]:
            raise ValueError(f"Invalid priority: {task_input['priority']}. Must be one of ['Low', 'Medium', 'High']")

        if task_input["status"].title() not in ["Todo", "Doing", "Done"]:
            raise ValueError(f"Invalid status: {task_input['status']}. Must be one of ['Todo', 'Doing', 'Done']")
        return True

    # ToDo => Function to add a new task, task will be a dictionary
    def add_task(self, task_data):
        if self.validation(task_data):
            task = {
                "id": self._next_id,
                **task_data
            }
            self.tasks.append(task)
            self._next_id += 1

    def get_tasks_by_status(self, status):
        tasks_by_status = []

        for task in self.tasks:
            if task["status"].lower() == status.lower():
                tasks_by_status.append(task)

        return tasks_by_status

    # ToDo => Function to remove a task by ID
    def remove_task(self, task_id):
        # write your code here
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task with ID {task_id} has been removed successfully!")
                return True

    # ToDo => Function to mark a task as completed
    def complete_task(self, task_id):
        # write your code here
        result = self.edit_task(task_id, 'status', 'Done')
        return result

    # ToDo => Function to get task by id
    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    # ToDo => Function to edit a task
    def edit_task(self, task_id, field, new_value):
        # write your code here
        for task in self.tasks:
            if task["id"] == task_id:
                if field in task:
                    task[field] = new_value
                    print(f"Task {task_id} updated: set {field} to {new_value}")
                    return task
                else:
                    print(f"Field '{field}' does not exist in task {task_id}.")
                    return None
        return None
