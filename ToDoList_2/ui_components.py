# ui_component.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

BIG_ICON_FONT = ("Arial", 14, "bold")

class TaskListUI:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager
        self.task_widgets = {}

        self.root.title("KRW To-Do List")
        self.root.geometry("800x800")
        self.root.configure()

        # Title
        header = tk.Label(self.root, text="🧠 Task Board", font=("Helvetica", 18, "bold"))
        header.pack(pady=10)

        # Add task area
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.task_entry = ttk.Entry(input_frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=10)

        add_button = ttk.Button(input_frame, text="Add", command=self.add_task)
        add_button.grid(row=0, column=1)

        # Container for 3 columns
        self.column_frame = tk.Frame(self.root, bg="white")
        self.column_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        self.todo_frame = self.create_section("📝 To Do")
        self.doing_frame = self.create_section("🔄 Doing")
        self.done_frame = self.create_section("✅ Done")

        self.refresh_task_list()

    def create_section(self, title):
        frame = tk.Frame(self.column_frame, bd=1, relief=tk.SOLID)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        label = tk.Label(frame, text=title, font=("Helvetica", 14, "bold"))
        label.pack(pady=5)

        container = tk.Frame(frame)
        container.pack(fill=tk.BOTH, expand=True)

        return container

    def refresh_task_list(self):
        print("refresh_task_list")
        self.task_widgets.clear()
        for section in [self.todo_frame, self.doing_frame, self.done_frame]:
            for widget in section.winfo_children():
                widget.destroy()

        self.add_tasks_to_section("todo", self.todo_frame)
        self.add_tasks_to_section("doing", self.doing_frame)
        self.add_tasks_to_section("done", self.done_frame)

    def add_tasks_to_section(self, status, section_frame):
        tasks = self.task_manager.get_tasks_by_status(status)
        for task in tasks:
            task_id = task["id"]
            title = task["title"]

            task_row = tk.Frame(section_frame, pady=3)
            task_row.pack(fill=tk.X, padx=5, pady=2)

            label = tk.Label(task_row, text=title, anchor="w")
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.task_widgets[task_id] = {'frame': task_row, 'label': label, 'entry': None}

            # move_btn
            move_btn = ttk.Menubutton(task_row, text="status")
            menu = tk.Menu(move_btn, tearoff=0)
            for target_status in ["todo", "doing", "done"]:
                if target_status != status:
                    menu.add_command(label=f"Move to {target_status.title()}",
                                     command=lambda tid=task_id, s=target_status: self.move_task(tid, s))
            move_btn["menu"] = menu
            move_btn.pack(side=tk.RIGHT, padx=2)

            # delete_btn
            del_button = tk.Button(
                task_row,
                text="✖",
                width=2,
                font=BIG_ICON_FONT,
                command=lambda tid=task_id: self.delete_task(tid),
                fg="red",
            )
            del_button.pack(side=tk.RIGHT, padx=2)

            # edit_btn
            edit_button = tk.Button(
                task_row,
                text="✎",
                width=2,
                font=BIG_ICON_FONT,
                command=lambda tid=task_id: self.edit_task(tid),
                fg="blue"
            )
            edit_button.pack(side=tk.RIGHT, padx=2)

    def add_task(self):
        title = self.task_entry.get().strip()
        print(f"Adding task: {title}")  # Debug print
        if title:
            self.task_manager.add_task({
                "title": title,
                "priority": "High",
                "status": "todo",
            })
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning(title="Input Error", message="Please enter a task title.")
            self.task_entry.delete(0, tk.END)

    def delete_task(self, task_id):
        print(task_id, 'remove id')
        result = self.task_manager.remove_task(task_id)
        if result:
            self.refresh_task_list()
            messagebox.showinfo("Success", f"Your task deleted successfully!")

    def move_task(self, task_id, new_status):
        print(task_id, 'move status', new_status)
        if new_status == 'done': self.task_manager.complete_task(task_id)
        else: self.task_manager.edit_task(task_id, 'status', new_status)
        self.refresh_task_list()

    def edit_task(self, task_id):
        widgets = self.task_widgets.get(task_id)
        if not widgets:
            print('No widgets found for task:', task_id)
            return

        # Prevent opening multiple edit boxes
        if widgets.get('entry') is not None:
            print('Already editing this task.')
            return

        label = widgets.get('label')
        if label is not None:
            label.destroy()
            self.task_widgets[task_id]['label'] = None
        else:
            print('Label already destroyed or not found.')
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print('Task not found:', task_id)
            return

        task_row = widgets['frame']

        # Create an Entry widget in the same frame
        entry = tk.Entry(task_row)
        entry.insert(0, task["title"])
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.task_widgets[task_id]['entry'] = entry

        entry.focus_set()

        # Bind Enter key to save
        entry.bind("<Return>", lambda event: self.save_task(task_id))

    def save_task(self, task_id):
        widgets = self.task_widgets.get(task_id)
        if not widgets:
            return

        entry = widgets.get('entry')
        if not entry:
            return

        new_title = entry.get().strip()
        if not new_title:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
            entry.focus_set()
            return

        # Update task in task manager
        self.task_manager.edit_task(task_id, 'title', new_title)

        # Remove Entry widget
        entry.destroy()

        # Refresh sections
        self.refresh_task_list()

        messagebox.showinfo("Success", f"Your task updated successfully!")