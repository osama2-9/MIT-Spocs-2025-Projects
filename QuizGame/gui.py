import tkinter as tk

class QuizGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("لعبة الأسئلة")
        self.root.geometry("500x400")
        self.root.configure(bg="#ffe6f0")

        self.welcome_frame = tk.Frame(root, bg="#f5f5dc")
        welcome_label = tk.Label(self.welcome_frame, text="أهلاً بك في لعبة الأسئلة ", font=("Arial", 22),
                                 bg="#f5f5dc", fg="#8B4513")
        start_button = tk.Button(self.welcome_frame, text="ابدأ", font=("Arial", 18), command=self.start_game,
                                 bg="#f5f5dc", fg="#8B4513", padx=20, pady=10)
        welcome_label.pack(pady=60)
        start_button.pack()
        self.welcome_frame.pack(fill="both", expand=True)

        self.quiz_frame = tk.Frame(root, bg="#ffe6f0")
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16), bg="#ffe6f0", wraplength=400)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.quiz_frame, text="", font=("Arial", 15), width=35,
                            command=lambda i=i: self.check_answer(i), bg="#ffccdd")
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("Arial", 16), bg="#ffe6f0")
        self.feedback_label.pack(pady=10)

    def start_game(self):
        self.controller.reset()
        self.welcome_frame.pack_forget()
        self.show_question()

    def show_question(self):
        question_data = self.controller.get_current_question()
        if question_data:
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.feedback_label.config(text="")
            self.quiz_frame.pack()
        else:
            self.end_game()

    def check_answer(self, index):
        selected_text = self.option_buttons[index]["text"]
        correct = self.controller.check_answer(selected_text)

        if correct:
            self.feedback_label.config(text="✔ صح", fg="green")
        else:
            self.feedback_label.config(text="✖ خطأ", fg="red")

        self.root.after(1000, self.show_question)

    def end_game(self):
        self.quiz_frame.pack_forget()
        result = self.controller.get_score()
        result_label = tk.Label(self.root, text=f"أجبت {result} من {self.controller.total()} بشكل صحيح",
                                font=("Arial", 18), bg="#ffe6f0", fg="black")
        result_label.pack(pady=30)