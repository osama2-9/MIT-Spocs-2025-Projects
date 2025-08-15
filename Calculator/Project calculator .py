import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Arial", 18), borderwidth=2, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def add_to_display(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expr = display.get()
        result = eval(expr)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def sci_calc(func):
    try:
        val = float(display.get())
        if func == "x²":
            result = val ** 2
        elif func == "sin":
            result = math.sin(math.radians(val))
        elif func == "cos":
            result = math.cos(math.radians(val))
        elif func == "tan":
            result = math.tan(math.radians(val))
        elif func == "log":
            result = math.log10(val)
        else:
            result = "Error"
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

tk.Button(root, text="7", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("7")).grid(row=1, column=0)
tk.Button(root, text="8", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("8")).grid(row=1, column=1)
tk.Button(root, text="9", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("9")).grid(row=1, column=2)
tk.Button(root, text="/", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("/")).grid(row=1, column=3)

tk.Button(root, text="4", background="red", fg="white", width=5, height=2, command=lambda: add_to_display("4")).grid(row=2, column=0)

tk.Button(root, text="5", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("5")).grid(row=2, column=1)
tk.Button(root, text="6", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("6")).grid(row=2, column=2)
tk.Button(root, text="X", background="black", fg="white", width=5, height=2, command=lambda: add_to_display("*")).grid(row=2, column=3)

tk.Button(root, text="1", background="red", fg="white", width=5, height=2, command=lambda: add_to_display("1")).grid(row=3, column=0)
tk.Button(root, text="2", background="red", fg="white", width=5, height=2, command=lambda: add_to_display("2")).grid(row=3, column=1)

tk.Button(root, text="3", width=5, height=2, command=lambda: add_to_display("3")).grid(row=3, column=2)
tk.Button(root, text="-", width=5, height=2, command=lambda: add_to_display("-")).grid(row=3, column=3)

tk.Button(root, text="0", background="red", fg="white", width=5, height=2, command=lambda: add_to_display("0")).grid(row=4, column=0)

tk.Button(root, text=".", background="green", fg="white", width=5, height=2, command=lambda: add_to_display(".")).grid(row=4, column=1)
tk.Button(root, text="=", background="green", fg="white", width=5, height=2, command=calculate).grid(row=4, column=2)
tk.Button(root, text="+", background="green", fg="white", width=5, height=2, command=lambda: add_to_display("+")).grid(row=4, column=3)

tk.Button(root, text="x²", background="green" , fg="white", width=5, height=2, command=lambda: sci_calc("x²")).grid(row=5, column=0)
tk.Button(root, text="sin", background="green", fg="white", width=5, height=2, command=lambda: sci_calc("sin")).grid(row=5, column=1)
tk.Button(root, text="cos", background="green", fg="white", width=5, height=2, command=lambda: sci_calc("cos")).grid(row=5, column=2)
tk.Button(root, text="log", background="green", fg="white", width=5, height=2, command=lambda: sci_calc("log")).grid(row=5, column=3)

tk.Button(root, text="C", width=20, height=2, command=clear_display).grid(row=6, column=0, columnspan=4)

root.mainloop()