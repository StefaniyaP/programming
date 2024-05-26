import toga
from lab_10.medium.modules import function, nd_array
from toga.style.pack import COLUMN, Pack


class My_App(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        main_box.add(toga.Label("Выбор модуля", style=Pack(padding=5, text_align='center', font_size=20)))
        main_box.add(toga.Label("Выберете модуль, которым хотите воспользоваться:\n"
                                "1. модуль для создания n-мерного массива\n"
                                "2. модуль для рассчета значения функции\n", style=Pack(padding=5, font_size=12)))
        main_box.add(toga.TextInput(placeholder='"1", "2"',
                                    on_change=self.widget_value))   # введенное слово принимает функция widget_value
        main_box.add(toga.Button('Далее', on_press=self.next_window))  # при нажатии кнопки вызывается функция
                                                                       # next_window

        self.main_window = toga.MainWindow()
        self.main_window.content = main_box
        self.main_window.show()

    def widget_value(self, widget):
        self.wv = widget.value

    def next_window(self, widget):
        w_values = ['1', '2']
        if widget.text == 'Далее' and (self.wv in w_values):
            self.to_input_values()

    # создает окно, в котором пользователь вводит необходимые для рассчета данные, их получает функция received_values
    def to_input_values(self):
        box = toga.Box(style=Pack(direction=COLUMN))
        if self.wv == '1':
            box.add(toga.Label("Укажите размерность массива (макс. 3 на 3)", style=Pack(padding=5, font_size=12)))
            box.add(toga.Label("m:", style=Pack(padding=5, font_size=10)))
            box.add(toga.TextInput(placeholder='m', on_change=self.received_values))

            box.add(toga.Label("n:",
                               style=Pack(padding=5, font_size=10)))
            box.add(toga.TextInput(placeholder='n', on_change=self.received_values))

        elif self.wv == '2':
            box.add(toga.Label("Укажите значения x и k для рассчета значения функции", style=Pack(padding=5,
                                                                                                  font_size=12)))
            box.add(toga.Label("x:", style=Pack(padding=5, font_size=10)))
            box.add(toga.TextInput(placeholder='x', on_change=self.received_values))

            box.add(toga.Label("k:",
                               style=Pack(padding=5, font_size=10)))
            box.add(toga.TextInput(placeholder='k', on_change=self.received_values))

        box.add(toga.Button('Получить результат', on_press=self.calculation))

        self.main_window.content = box

    def received_values(self, widget):
        if widget.placeholder == 'm':
            self.m = int(widget.value)
        elif widget.placeholder == "n":
            self.n = int(widget.value)
        elif widget.placeholder == 'x':
            self.x = int(widget.value)
        elif widget.placeholder == 'k':
            self.k = int(widget.value)

    # производит расчеты, пользуясь подключенными для этого модулями и выводит их в новом созданном окне
    def calculation(self, *args, **kwargs):
        global res, r
        box = toga.Box(style=Pack(direction=COLUMN))
        if self.wv == '1':
            c = nd_array.Calc(self.m, self.n)
            res = c.create_n_dim_array()
        elif self.wv == '2':
            c = function.Calc(self.x, self.k)
            res = c.y()

        box.add(toga.Label(f"Результат: \n"
                           f"{res}", style=Pack(padding=5, font_size=14)))

        self.main_window.content = box


def main():
    return My_App("Модули", "org.beeware.toga.tutorial")


if __name__ == "__main__":
    main().main_loop()
