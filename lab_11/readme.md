# Прог. Лабораторная работа №11
## Задание
1. Реализовать приложение с GUI (приложения-игры допускается делать с использованием TUI-пакетов) по своему варианту.
Список GUI фреймворков:
    - appJar
    - Tkinter
    - Flet
    - wxPython
    - PySimpleGUI
    - Pyforms
    - Toga
    - PyGObject
    - guizero
    - guietta
    - PySide6
    - Dear PyGui
    - PyGame
2. Оформить ```readme.md```, который должен содержать:
    - название приложения
    - описание
    - инструкции к запуску
    - краткую справку
## Мой вариант (7)
Менеджер паролей.
## Решение

Менеджер паролей был написан с помощью GUI фреймворка ```Tkinter```.

```Python
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
```

После запуска появляется окно:

![img.png](img.png)

Мы можем написать пароль вручную и сохранить его, а можем воспользоваться
генератором паролей, нажав кнопку "Cгенерировать пароль":

![img_1.png](img_1.png)

Сохраняем пароль, нажав кнопку "Сохранить пароль":

![img_2.png](img_2.png)

