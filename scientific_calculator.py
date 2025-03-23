import math
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Create an entry widget for the display
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief=tk.RIDGE)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Function to update the display
def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function for advanced operations (e.g., sin, cos, log)
def advanced_operation(operation):
    try:
        value = float(display.get())
        if operation == "sin":
            result = math.sin(math.radians(value))  # Convert degrees to radians
        elif operation == "cos":
            result = math.cos(math.radians(value))
        elif operation == "tan":
            result = math.tan(math.radians(value))
        elif operation == "log":
            result = math.log10(value)
        elif operation == "sqrt":
            result = math.sqrt(value)
        elif operation == "exp":
            result = math.exp(value)
        else:
            result = "Invalid Operation"
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("(", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), (")", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("^", 4, 4),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), ("sqrt", 5, 4),
    ("exp", 6, 0), ("π", 6, 1), ("e", 6, 2), ("←", 6, 3), ("%", 6, 4)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), bg="lightblue", command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), bg="lightcoral", command=clear_display)
    elif text in ["sin", "cos", "tan", "log", "sqrt", "exp"]:
        button = tk.Button(root, text=text, font=("Arial", 18), bg="lightgreen", command=lambda t=text: advanced_operation(t))
    elif text == "π":
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda: update_display(str(math.pi)))
    elif text == "e":
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda: update_display(str(math.e)))
    elif text == "←":
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda: display.delete(len(display.get()) - 1, tk.END))
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: update_display(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Run the application
root.mainloop()