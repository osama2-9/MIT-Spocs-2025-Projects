# run.py

import tkinter as tk
from controller import QuizController
from gui import QuizGUI

if __name__ == "__main__":
    root = tk.Tk()
    controller = QuizController()
    app = QuizGUI(root, controller)
    root.mainloop()