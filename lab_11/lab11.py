import tkinter as tk
from tkinter import messagebox
import random


def generate_password():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = random.randint(8, 13)
    password = ''
    for n in range(length):
        password += random.choice(chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)


def save_password():
    saved_password = password_entry.get()
    messagebox.showinfo("Сохранено", "Пароль сохранен: {}".format(saved_password))


# Создание главного окна приложения
root = tk.Tk()
root.title("Менеджер паролей")

# Создание элементов интерфейса
password_label = tk.Label(root, text="Пароль:")
password_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
save_button = tk.Button(root, text="Сохранить пароль", command=save_password)

# Размещение элементов на главном окне
password_label.pack()
password_entry.pack()
generate_button.pack()
save_button.pack()

# Запуск главного цикла приложения
root.mainloop()
