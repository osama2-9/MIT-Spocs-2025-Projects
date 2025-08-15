import tkinter as tk
import random
import copy
from solver import SudokuSolver
from sudoku_templates import sudoku_templates

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver")
        self.root.geometry("600x650")
        self.root.configure(bg="#f0f0f0")

        self.solver = SudokuSolver()
        self.current_puzzle = []
        self.original_puzzle = []
        self.entries = []

        self.setup_ui()
        self.generate_puzzle()

    def setup_ui(self):
        title_label = tk.Label(self.root, text="🧩 Sudoku Solver", font=("Arial", 24, "bold"),
                               bg='#f0f0f0', fg='#333')
        title_label.pack(pady=20)

        grid_frame = tk.Frame(self.root, bg='#333', bd=3, relief='solid')
        grid_frame.pack(pady=10)

        self.entries = []
        for i in range(9):
            row_entries = []
            for j in range(9):
                cell_frame = tk.Frame(grid_frame, bg='black', width=30, height=40)
                padx_left = 4 if j % 3 == 0 else 1
                padx_right = 4 if j % 3 == 2 else 1
                pady_top = 4 if i % 3 == 0 else 1
                pady_bottom = 4 if i % 3 == 2 else 1

                cell_frame.grid(row=i, column=j, padx=(padx_left, padx_right), pady=(pady_top, pady_bottom))
                cell_frame.grid_propagate(False)

                entry = tk.Entry(cell_frame, width=2, justify='center',
                                 font=("Arial", 20, "bold"), bd=0, highlightthickness=0)
                entry.pack(expand=True, fill='both', padx=2, pady=2)
                entry.bind('<KeyPress>', self.validate_input)
                row_entries.append(entry)
            self.entries.append(row_entries)

        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)

        button_style = {'font': ("Arial", 12, "bold"), 'width': 12, 'height': 2, 'relief': 'raised', 'bd': 3}

        tk.Button(button_frame, text="🚀 SOLVE", bg='#4CAF50', fg='white',
                  command=self.solve_puzzle, **button_style).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="🎲 GENERATE", bg='#2196F3', fg='white',
                  command=self.generate_puzzle, **button_style).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="🗑️ CLEAR", bg='#FF5722', fg='white',
                  command=self.clear_grid, **button_style).grid(row=0, column=2, padx=10)

        self.status_label = tk.Label(self.root, text="Ready! Click Generate for a new puzzle.",
                                     font=("Arial", 12), bg='#f0f0f0', fg='#666')
        self.status_label.pack(pady=10)

    def validate_input(self, event):
        char = event.char
        if char.isdigit() and '1' <= char <= '9':
            return True
        elif char in ['\b', '\x7f']:
            return True
        else:
            return "break"

    def update_grid_display(self):
        for i in range(9):
            for j in range(9):
                entry = self.entries[i][j]
                value = self.current_puzzle[i][j]

                entry.config(state='normal')  
                entry.delete(0, tk.END)

                if value != -1:
                    entry.insert(0, str(value))
                    entry.config(state='readonly', fg='black', bg='white')  
                else:
                    entry.config(fg='black', bg='white')

    def get_puzzle_from_grid(self):
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                row.append(int(value) if value.isdigit() else -1)
            puzzle.append(row)
        return puzzle

    def solve_puzzle(self):
        current_state = self.get_puzzle_from_grid()
        puzzle_copy = copy.deepcopy(current_state)
        self.status_label.config(text="🔄 Solving...", fg='#FF9800')
        self.root.update()

        if self.solver.solve(puzzle_copy):
            self.current_puzzle = puzzle_copy
            self.update_grid_display()
            self.status_label.config(text="✅ Puzzle solved successfully!", fg='#4CAF50')
        else:
            self.status_label.config(text="❌ No solution exists for this puzzle!", fg='#f44336')

    def generate_puzzle(self):
        template = random.choice(sudoku_templates)
        self.current_puzzle = copy.deepcopy(template)
        self.original_puzzle = copy.deepcopy(template)

        for row in self.entries:
            for entry in row:
                entry.config(state='normal')

        self.update_grid_display()
        self.status_label.config(text="🎲 New puzzle generated! Ready to solve.", fg='#2196F3')

    def clear_grid(self):
        self.current_puzzle = [[-1 for _ in range(9)] for _ in range(9)]
        self.original_puzzle = [[-1 for _ in range(9)] for _ in range(9)]

        for row in self.entries:
            for entry in row:
                entry.config(state='normal', bg='white', fg='black')
                entry.delete(0, tk.END)

        self.status_label.config(text="🗑️ Grid cleared! Enter your own puzzle or generate one.", fg='#FF5722')
