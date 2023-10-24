# CALCULATOR :

import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=('Helvetica', 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [  '0', '1', '2', '/',
             '3', '4', '5', '*',
             '6', '7', '8', '-',
             '9', '.', '=', '+'  ]
       

row, col = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 18), command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 18), command=lambda button=button: button_click(button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Helvetica', 18), command=clear).grid(row=row, column=col)

root.mainloop()
