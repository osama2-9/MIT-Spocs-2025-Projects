import tkinter as tk
from GUI import SudokuGUI

def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "main":
    main()