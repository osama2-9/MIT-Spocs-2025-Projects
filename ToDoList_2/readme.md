# 🧠 KRW To-Do List

A simple and interactive **To-Do List desktop application** built using Python's `Tkinter` GUI toolkit. This application allows users to add, edit, move, and delete tasks with categorized status columns: **To Do**, **Doing**, and **Done**.

---

## 📦 Features

- 📝 Add new tasks with a title
- ✎ Edit existing task titles inline
- 🔄 Move tasks between "To Do", "Doing", and "Done"
- ❌ Delete tasks
- ✅ Mark tasks as completed
- GUI built with `Tkinter`
- Task logic managed via the `TaskManager` class
- Unit tests included

---

## 🖼️ UI Overview

The app features a clean three-column layout:

##############################################################

📝 To Do 🔄 Doing ✅ Done

[ ] Task A [ ] Task B [x] Task C

Each task includes buttons to:
- Move it to another status
- Edit the title inline
- Delete the task

---

## 🚀 Getting Started

### Requirements

- Python 3.6+
- No external libraries required (uses built-in `tkinter`)

### How to Run

```bash
python main.py
##############################################################################
🗂️ Project Structure

KRW-ToDo-App/
├── main.py                # App entry point (starts the GUI)
├── task_manager.py        # Business logic for managing tasks
├── ui_components.py       # Tkinter GUI code (TaskListUI class)
├── test_task_manager.py   # Unit tests for TaskManager
└── README.md              # This file
##################################################################################
How It Works

The UI is built using the TaskListUI class in ui_components.py

Tasks are stored as dictionaries and managed by the TaskManager class

Each task has: id, title, and status (To Do, Doing, Done)

Task list is dynamically updated in the GUI when tasks are added, edited, or removed
#######################################################################################
Author

Made with ❤️ by Ramadan, Walaa, Kareem


