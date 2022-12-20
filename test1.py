import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image
from PIL import ImageTk

class interface:

    def __init__(self):
        self.e = None
        self.index_e = None
        self.H = None
        self.panelA = None
        self.path = None
        self.s = None
        self.a = None
        option_list = ["Агрегат №8"]
        self.root = tk.Tk()

        # Первый FRAME
        self.f1 = tk.Frame(self.root)
        self.f1.grid(row=0, column=0)

        # Второй FRAME
        self.f2 = tk.Frame(self.root)
        self.f2.grid(row=0, column=1, rowspan=2)

        # Третий FRAME
        self.f3 = tk.Frame(self.root)
        self.f3.grid(row=0, column=2, rowspan=2)

        # Четвертый FRAME
        self.f4 = tk.Frame(self.root)
        self.f4.grid(row=2, columnspan=3, sticky='ew')

        # Пятый FRAME
        self.f5 = tk.Frame(self.root)
        self.f5.grid(row=1, sticky='ew',)

        # Entry
        self.e_H = tk.Entry(self.f1)
        self.e_H.grid(column=1, row=1, sticky='ew',)

        # Label 1 АГРЕГАТ
        self.l1 = tk.Label(self.f1, text="Выберите агрегат")
        self.l1.grid(column=0, row=0, sticky='w')

        # Label 2 НАПОР
        self.l2 = tk.Label(self.f1, text="Введите напор H, м")
        self.l2.grid(column=0, row=1, sticky='w')

        # Label 3
        self.l3 = tk.Label(self.f5, text="Укажите значения мощности соот-му КПД")
        self.l3.grid(column=0, row=2, sticky='ew', columnspan=4)

        # Label 4
        self.l4 = tk.Label(self.f3, text="Рассчитанные значения")
        self.l4.grid(column=0, row=0, sticky='ew', columnspan=3)

        # Button АГРЕГАТ
        b1 = tk.Button(self.f1, text="Выбрать", command=self.select_image)
        b1.grid(column=4, row=0, sticky='ew')

        # Button РАСЧЕТ
        b2 = tk.Button(self.f5, text="Рассчитать")
        b2.grid(column=0, row=17, sticky='ew', columnspan=4)

        self.canvas = tk.Canvas(self.f2, height=490, width=1100)
        self.canvas.grid(column=1, row=0)

        self.canvas = tk.Canvas(self.f4, height=450, width=1920)
        self.canvas.grid(column=0, row=0)

        self.comboExample = ttk.Combobox(self.f1, values=option_list)
        self.comboExample.grid(column=1, row=0, sticky='w')

        # Button НАПОР
        b3 = tk.Button(self.f1, text="Задать напор", command=self.pressure)
        b3.grid(column=4, row=1, sticky='w')

        # Table 2
        columns1 = ['N', 'ny']
        self.table2 = ttk.Treeview(self.f3, columns=columns1, show='headings', height=24)
        self.table2.heading("N", text="Мощность, МВт")
        self.table2.heading("ny", text="КПД, %")
        self.table2.grid(column=0, row=1, sticky='ew')
        self.table_entry()
        self.root.mainloop()

    def focus(self, event, e):

            print(e)
            print(e.focus_get)
            e = str(e)[-2:]
            if e == "ry":
                e = 0
            else:
                e = [i for i in e if i.isdigit()]
                if len(e) == 1:
                    e = int(e[0]) - 1
                else:
                    e = int(e[0] + e[1]) - 1
            self.e = e

    def get_s(self):
        return self.s

    def select_image(self):
        try:
            self.selection = self.comboExample.get()
            path_Ag = {"Агрегат №8": "Graf/Ag8.png"}
            image = Image.open(path_Ag[self.selection])
            resize_image = image.resize((1100, 519))
            image = ImageTk.PhotoImage(resize_image)

            if self.panelA is None:
                self.panelA = tk.Label(self.f2, image=image)
                self.panelA.bind("<Button-1>", self.callback)
                self.panelA.image = image
                self.panelA.grid(column=1, row=0)

            else:
                self.panelA.configure(image=image)
                self.panelA.image = image
                self.panelA.bind("<Button-1>", self.callback)

        except KeyError:
            messagebox.showerror("Ошибка", "Выберете агрегат")

    def callback(self, event):
        if self.selection == "Агрегат №8":
            self.num = str(event.x * 118)
            self.list_e[self.e].delete(0, 'end')
            self.list_e[self.e].insert(0, self.num)

    def table_entry(self):
        self.list_e = []
        count_list_e = 0
        c = 0
        d = 1
        for i in range(2):
            for j in range(11 - i):
                self.list_e.append(tk.Entry(self.f5, width=10, fg='blue', font=('Arial', 16, 'bold')))
                self.list_e[count_list_e].bind("<Button-1>",
                                               lambda event, e=self.list_e[count_list_e], k=0: self.focus(event, e))
                self.list_e[count_list_e].bind("<Tab>",
                                               lambda event, e=self.list_e[count_list_e], k=1: self.focus(event, e))
                self.list_e[count_list_e].grid(row=j + 3, column=i + d, sticky='ew')
                tk.Label(self.f5, text=f"{70 + count_list_e}%", width=11).grid(column=i + c, row=3 + j,)
                count_list_e += 1
            c = 1
            d = 2

    def pressure(self):
        try:
            int(self.e_H.get())
            self.H = self.e_H.get()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите численное значение")


obj_interface = interface()
