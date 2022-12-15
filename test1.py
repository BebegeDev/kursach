import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


class interface:

    def __init__(self):
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
        self.f2.grid(row=0, column=1)

        # Третий FRAME
        self.f3 = tk.Frame(self.root)
        self.f3.grid(row=0, column=2)

        # Entry
        self.e = tk.Entry(self.f1)
        self.e.grid(column=1, row=1, sticky='ew')

        # Label АГРЕГАТ
        self.l1 = tk.Label(self.f1, text="Выберите агрегат")
        self.l1.grid(column=0, row=0, sticky='ew')

        # Label НАПОР
        self.l2 = tk.Label(self.f1, text="Введите напор H, м")
        self.l2.grid(column=0, row=1, sticky='ew')

        # Label 3
        self.l2 = tk.Label(self.f1, text="Укажите значению мощности КПД через запятую")
        self.l2.grid(column=0, row=2, sticky='ew', columnspan=3)

        # Button АГРЕГАТ
        b1 = tk.Button(self.f1, text="Выбрать", command=self.select_image)
        b1.grid(column=2, row=0, sticky='ew')

        # Button РАСЧЕТ
        b1 = tk.Button(self.f1, text="Рассчитать")
        b1.grid(column=0, row=17, sticky='ew', columnspan=3)

        self.canvas = tk.Canvas(self.f2, height=490, width=1100)
        self.canvas.grid(column=1, row=0)

        self.comboExample = ttk.Combobox(self.f1, values=option_list)
        self.comboExample.grid(column=1, row=0, sticky='ew')

        # Button НАПОР
        b2 = tk.Button(self.f1, text="Задать напор")
        b2.grid(column=2, row=1, sticky='ew')

        # # Table 1
        # columns = ['N', 'ny']
        # self.table = ttk.Treeview(self.f1, columns=columns, show='headings', height=21)
        # self.table.heading("N", text="Мощность, МВт")
        # self.table.heading("ny", text="КПД, %")
        # self.table.grid(column=0, row=3, columnspan=3, sticky='ew')
        for i in range(3):
            for j in range(13):
                self.e = tk.Entry(self.f1, width=10, fg='blue', font=('Arial', 16, 'bold'))

                self.e.grid(row=j + 3, column=i,)

        # Table 2
        columns1 = ['N', 'ny']
        self.table2 = ttk.Treeview(self.f3, columns=columns1, show='headings', height=25)
        self.table2.heading("N", text="Мощность, МВт")
        self.table2.heading("ny", text="КПД, %")
        self.table2.grid(column=0, row=0, sticky='ew')

        self.root.mainloop()

    def get_s(self):
        return self.s

    def select_image(self):
        # self.path = filedialog.askopenfilename()
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

    def callback(self, event):
        if self.selection == "Агрегат №8":
            print(event.x, event.y)
            x = 72.0
            x1 = 1158
            y = event.y
            if 75 < event.y < 437:
                self.canvas.create_line(x, y, x1, y)


obj_interface = interface()
