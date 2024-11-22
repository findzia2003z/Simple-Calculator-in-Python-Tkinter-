from tkinter import *


root = Tk()
root.title("Simple Calculator")
root.configure(bg="#2C2F48")

entry = Entry(root, font=("Arial", 24), bg="#1C1F30", fg="#FFFFFF",
              justify="right", bd=0, highlightthickness=0)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="nsew")

# Global variables for calculations
calculation = ""


# Functions for button actions
def buttonClicked(number):
    global calculation
    calculation += str(number)
    entry.delete(0, END)
    entry.insert(END, calculation)


def buttonOperation(op):
    global calculation
    if calculation:
        # If the last character is an operator, replace it
        if calculation[-1] in "+-*/%":
            calculation = calculation[:-1] + op
        else:
            # Calculate the result so far and append the operator
            try:
                calculation = str(eval(calculation)) + op
            except Exception:
                calculation = "Error"
        entry.delete(0, END)
        entry.insert(END, calculation)


def buttonClear():
    global calculation
    calculation = ""
    entry.delete(0, END)


def buttonDelete():
    global calculation
    calculation = calculation[:-1]
    entry.delete(0, END)
    entry.insert(END, calculation)


def buttonEqual():
    global calculation
    try:
        calculation = str(eval(calculation))
        entry.delete(0, END)
        entry.insert(END, calculation)
    except Exception:
        calculation = ""
        entry.delete(0, END)
        entry.insert(END, "Error")


# Button colors
button_bg = "#E0E0E0"
button_fg = "#000000"
operator_bg = "#FF5E5B"
special_bg = "#6C63FF"
delete_bg = "#FFBC42"

# Create buttons
button7=Button(root, text="7", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(7))
button7.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

button8=Button(root, text="8", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(8))
button8.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

button9=Button(root, text="9", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(9))
button9.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

buttonDEL=Button(root, text="DEL", bg=delete_bg, fg="#FFFFFF", font=("Arial", 16),
       command=buttonDelete)
buttonDEL.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

button4=Button(root, text="4", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(4))
button4.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

button5=Button(root, text="5", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(5))
button5.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

button6=Button(root, text="6", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(6))
button6.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

buttonADD=Button(root, text="+", bg=operator_bg, fg="#FFFFFF", font=("Arial", 16),
       command=lambda: buttonOperation("+"))
buttonADD.grid(row=2, column=3, sticky="nsew", padx=5, pady=5)


button1=Button(root, text="1", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(1))
button1.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

button2=Button(root, text="2", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(2))
button2.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

button3=Button(root, text="3", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(3))
button3.grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

buttonSUB=Button(root, text="-", bg=operator_bg, fg="#FFFFFF", font=("Arial", 16),
       command=lambda: buttonOperation("-"))
buttonSUB.grid(row=3, column=3, sticky="nsew", padx=5, pady=5)


buttonDEC=Button(root, text=".", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked("."))
buttonDEC.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

button0=Button(root, text="0", bg=button_bg, fg=button_fg, font=("Arial", 16),
       command=lambda: buttonClicked(0))
button0.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

buttonRESET=Button(root, text="RESET", bg=special_bg, fg="#FFFFFF", font=("Arial", 16),
       command=buttonClear)
buttonRESET.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

buttonMUL=Button(root, text="*", bg=operator_bg, fg="#FFFFFF", font=("Arial", 16),
       command=lambda: buttonOperation("*"))
buttonMUL.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)


buttonEQUAL=Button(root, text="=", bg=operator_bg, fg="#FFFFFF", font=("Arial", 16),
       command=buttonEqual)
buttonEQUAL.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

buttonDIV=Button(root, text="/", bg=operator_bg, fg="#FFFFFF", font=("Arial", 16),
       command=lambda: buttonOperation("/"))
buttonDIV.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)

buttonMOD=Button(root, text="%", bg=operator_bg, fg="#FFFFFF", font=("Arial", 16),
       command=lambda: buttonOperation("%"))
buttonMOD.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
