import tkinter as tk
from tkinter import messagebox
from modules import iron_mod, tv_mod, washing_machine_mod

# Создание главного окна приложения
root = tk.Tk()
root.title("Расчет электропотребления и его стоимости")


def calculating():
    e_app_val = str(e_app_entry.get())
    power_val = float(power_entry.get())
    usage_time_val = usage_time_entry.get()
    n_val = int(n_entry.get())
    cost_val = float(cost_entry.get())
    usage_time = usage_time_val
    cost = cost_val
    n = n_val
    power = power_val
    if e_app_val == 'утюг':
        print('ok')
        c = iron_mod.Calc(usage_time, cost, n, power)
        r = c.power_consumption()
        res = c.price()
        m = f'Электропотребление: {round(r, 2)}, Cтоимость: {round(res, 2)} руб.'
        return messagebox.showinfo('Результаты расчетов', '{}'.format(m))
    elif e_app_val == 'телевизор':
        c = tv_mod.Calc(usage_time, cost, n, power)
        r = c.power_consumption()
        res = c.price()
        m = f'Электропотребление: {round(r, 2)}, Cтоимость: {round(res, 2)} руб.'
        return messagebox.showinfo('Результаты расчетов', '{}'.format(m))
    elif e_app_val == 'стиральная машина':
        c = washing_machine_mod.Calc(usage_time, cost, n, power)
        r = c.power_consumption()
        res = c.price()
        m = f'Электропотребление: {round(r, 2)}, Cтоимость: {round(res, 2)} руб.'
        return messagebox.showinfo('Результаты расчетов', '{}'.format(m))


# Создание элементов интерфейса
e_app_label = tk.Label(root, text="Для какого электроприбора необходимо произвести расчеты?")
e_app_entry = tk.Entry(root)

power_label = tk.Label(root, text="Укажите мощность электроприбора (в кВт)")
power_entry = tk.Entry(root)

usage_time_label = tk.Label(root, text="Укажите период времени, в течение которого использовался электроприбор")
usage_time_entry = tk.Entry(root)

n_label = tk.Label(root, text="Количество дней/месяцев/лет")
n_entry = tk.Entry(root)

cost_label = tk.Label(root, text="Укажите стоимость 1 кВт*ч")
cost_entry = tk.Entry(root)

calc_button = tk.Button(root, text="Рассчитать", command=calculating)

# Размещение элементов на главном окне
e_app_label.pack()
e_app_entry.pack()
power_label.pack()
power_entry.pack()
usage_time_label.pack()
usage_time_entry.pack()
n_label.pack()
n_entry.pack()
cost_label.pack()
cost_entry.pack()

calc_button.pack()

# Запуск главного цикла приложения
root.mainloop()
