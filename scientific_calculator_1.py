import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("520x650")

# Entry widget for display
equation = tk.StringVar()
display = tk.Entry(root, textvariable=equation, font=("Arial", 18), bd=10, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=8, sticky="nsew")

# Memory and history
memory = 0
history = []

# Functions
def press(num):
    equation.set(equation.get() + str(num))
    display.icursor(tk.END)

def equalpress():
    try:
        result = str(eval(equation.get()))
        history.append(equation.get() + " = " + result)
        equation.set(result)
        display.icursor(tk.END)
    except ZeroDivisionError:
        equation.set("Math Error (÷0)")
        display.icursor(tk.END)
    except ValueError:
        equation.set("Invalid Input")
        display.icursor(tk.END)
    except Exception:
        equation.set("Error")
        display.icursor(tk.END)

def clear():
    equation.set("")

def backspace():
    equation.set(equation.get()[:-1])

def show_history():
    if history:
        equation.set(history[-1])
        display.icursor(tk.END)

def move_cursor_left():
    pos = display.index(tk.INSERT)
    if pos > 0:
        display.icursor(pos - 1)

def move_cursor_right():
    pos = display.index(tk.INSERT)
    if pos < len(equation.get()):
        display.icursor(pos + 1)

def scientific(func):
    try:
        expr = equation.get()
        if func == "sqrt":
            equation.set(str(math.sqrt(float(expr))))
        elif func == "log":
            equation.set(str(math.log10(float(expr))))
        elif func == "ln":
            equation.set(str(math.log(float(expr))))
        elif func == "sin":
            equation.set(str(math.sin(math.radians(float(expr)))))
        elif func == "cos":
            equation.set(str(math.cos(math.radians(float(expr)))))
        elif func == "tan":
            equation.set(str(math.tan(math.radians(float(expr)))))
        elif func == "pi":
            equation.set(equation.get() + str(math.pi))
        elif func == "e":
            equation.set(equation.get() + str(math.e))
        elif func == "!":
            equation.set(str(math.factorial(int(expr))))
        display.icursor(tk.END)
    except:
        equation.set("Error")
        display.icursor(tk.END)

# Memory functions
def memory_add():
    global memory
    try:
        memory += float(equation.get())
    except:
        equation.set("Error")

def memory_sub():
    global memory
    try:
        memory -= float(equation.get())
    except:
        equation.set("Error")

def memory_recall():
    equation.set(equation.get() + str(memory))
    display.icursor(tk.END)

def memory_clear():
    global memory
    memory = 0

# Keyboard shortcuts
def keypress(event):
    char = event.char
    if char == "\r":  # Enter key
        equalpress()
    elif char == "\x08":  # Backspace
        backspace()

root.bind("<Key>", keypress)

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3), ('sin',1,4), ('cos',1,5),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3), ('tan',2,4), ('sqrt',2,5),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3), ('log',3,4), ('ln',3,5),
    ('C',4,0), ('0',4,1), ('=',4,2), ('/',4,3), ('pi',4,4), ('e',4,5),
    ('^',5,0), ('!',5,1), ('(',5,2), (')',5,3), ('M+',5,4), ('M-',5,5),
    ('MR',6,0), ('MC',6,1), ('DEL',6,2), ('CHECK',6,3), ('←',6,4), ('→',6,5),
]

# Color themes
def get_button_color(text):
    if text.isdigit():  # Digits
        return {"bg":"white", "fg":"black"}
    elif text in ["+","-","*","/","^"]:  # Operators
        return {"bg":"lightgray", "fg":"black"}
    elif text in ["sin","cos","tan","sqrt","log","ln","pi","e","!"]:  # Scientific functions
        return {"bg":"steelblue", "fg":"white"}
    elif text in ["M+","M-","MR","MC"]:  # Memory functions
        return {"bg":"lightgray", "fg":"black"}
    elif text == "C":  # Clear
        return {"bg":"darkred", "fg":"white"}
    elif text == "=":  # Equals
        return {"bg":"darkgreen", "fg":"white"}
    elif text in ["DEL","CHECK","←","→"]:  # Utility buttons
        return {"bg":"gray", "fg":"white"}
    else:  # Parentheses and others
        return {"bg":"lightgray", "fg":"black"}

# Create buttons dynamically with colors
for (text, row, col) in buttons:
    colors = get_button_color(text)
    if text == "=":
        tk.Button(root, text=text, width=6, height=2, **colors, command=equalpress).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "C":
        tk.Button(root, text=text, width=6, height=2, **colors, command=clear).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "DEL":
        tk.Button(root, text=text, width=6, height=2, **colors, command=backspace).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "CHECK":
        tk.Button(root, text=text, width=6, height=2, **colors, command=show_history).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "←":
        tk.Button(root, text=text, width=6, height=2, **colors, command=move_cursor_left).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "→":
        tk.Button(root, text=text, width=6, height=2, **colors, command=move_cursor_right).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text in ["sin","cos","tan","sqrt","log","ln","pi","e","!"]:
        tk.Button(root, text=text, width=6, height=2, **colors, command=lambda t=text: scientific(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "M+":
        tk.Button(root, text=text, width=6, height=2, **colors, command=memory_add).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "M-":
        tk.Button(root, text=text, width=6, height=2, **colors, command=memory_sub).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "MR":
        tk.Button(root, text=text, width=6, height=2, **colors, command=memory_recall).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == "MC":
        tk.Button(root, text=text, width=6, height=2, **colors, command=memory_clear).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(root, text=text, width=6, height=2, **colors, command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make layout resizable
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
