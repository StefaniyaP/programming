# from abc import ABC, abstractmethod
# import modules
import tkinter as tk
from tkinter import ttk


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        super().__init__()
        self.wm_title('Рассчет электропотребления')

        container = tk.Frame(self, height=800, width=600)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Для какого электроприбора необходимо произвести рассчеты?")
        label.pack(padx=10, pady=10)
        electrical_appliance = tk.Entry()
        electrical_appliance.pack()
        
        def show(self):
            label["text"] = electrical_appliance.get()

        get_name = tk.Button(self, text='Нажмите, чтобы ввести значение', command=show)
        switch_window_button = tk.Button(
            self,
            text="Далее",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)


        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()
