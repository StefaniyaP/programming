import os
import tkinter as tk

root = tk.Tk()
root.title('Выбор фреймворка')


def button_toga():
    os.system('python lab.py')


def button_tk():
    os.system('python medium.py')


tk_button = tk.Button(root, text="Tkinter", command=button_tk)
toga_button = tk.Button(root, text="Toga", command=button_toga)

tk_button.pack()
toga_button.pack()

root.mainloop()
