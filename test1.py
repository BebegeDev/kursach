import tkinter as tk
from tkinter import ttk


class interface:

    def __init__(self, root):
        self.s = None
        self.root = root

        # Первый FRAME
        self.f1 = tk.Frame(self.root)
        self.f1.grid(row=0, column=0)

        # Entry
        self.e = tk.Entry(self.f1)
        self.e.grid(column=1, row=1, sticky='ew')

        # Label АГРЕГАТ
        self.l1 = tk.Label(self.f1, text="Выберите агрегат")
        self.l1.grid(column=0, row=0, sticky='ew')

        # Label НАПОР
        self.l2 = tk.Label(self.f1, text="Введите напор H, м")
        self.l2.grid(column=0, row=1, sticky='ew')

        # Button АГРЕГАТ
        b1 = tk.Button(self.f1, text="Выбрать агрегат")
        b1.grid(column=2, row=0, sticky='ew')

        # Button НАПОР
        b2 = tk.Button(self.f1, text="Задать напор")
        b2.grid(column=2, row=1, sticky='ew')

        # Button Combobox
        b2 = tk.Button(self.f1, text="Выбрать агрегат")
        b2.grid(column=2, row=0, sticky='ew')

        # Combobox
        self.comboExample = ttk.Combobox(self.f1,
                                         values=[
                                             "Агрегат 7",
                                             "Агрегат 8",
                                             "Агрегат 9",
                                             "Агрегат 10"])

        self.comboExample.bind("<<ComboboxSelected>>", self.getcomboExample)
        self.comboExample.grid(column=1, row=0)

        # Table
        columns = ['N', 'ny']
        self.table = ttk.Treeview(self.root, columns=columns, show='headings', height=20)
        self.table.heading("N", text="Мощность, МВт")
        self.table.heading("ny", text="КПД, %")
        self.table.grid(column=0, row=3, columnspan=2, sticky='ew')
        self.root.mainloop()

    def getcomboExample(self, event):
        self.s = self.comboExample.get()
        print(self.s)

    def get_s(self):
        return self.s


root = tk.Tk()
obj_interface = interface(root)
root.mainloop()

