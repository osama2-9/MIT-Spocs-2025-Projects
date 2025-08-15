# main.py

import tkinter as tk
from task_manager import TaskManager
from ui_components import TaskListUI

def main():
    root = tk.Tk()
    task_manager = TaskManager()
    TaskListUI(root, task_manager)
    root.mainloop()

if __name__ == "__main__":
    main()
