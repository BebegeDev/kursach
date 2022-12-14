import tkinter as tk
from tkinter import ttk, filedialog
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image
from PIL import ImageTk


class interface:

    def __init__(self):
        self.panelA = None
        self.panelB = None
        self.path = None
        self.s = None
        self.a = None
        self.b = None

        self.root = tk.Tk()

        # Первый FRAME
        self.f1 = tk.Frame(self.root)
        self.f1.grid(row=0, column=0)
        # Второй FRAME
        self.f2 = tk.Frame(self.root)
        self.f2.grid(row=0, column=1)

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
        b1 = tk.Button(self.f1, text="Укажите файл с характеристикой", command=self.select_image)
        b1.grid(column=0, row=0, sticky='ew', columnspan=3)

        # Button НАПОР
        b2 = tk.Button(self.f1, text="Задать напор")
        b2.grid(column=2, row=1, sticky='ew')


        # Table
        columns = ['N', 'ny']
        self.table = ttk.Treeview(self.f1, columns=columns, show='headings', height=20)
        self.table.heading("N", text="Мощность, МВт")
        self.table.heading("ny", text="КПД, %")
        self.table.grid(column=0, row=3, columnspan=3, sticky='ew')

        self.root.mainloop()


    def get_s(self):
        return self.s

    def select_image(self):
        self.path = filedialog.askopenfilename()

        if self.path:
            image = cv2.imread(self.path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)

            image = ImageTk.PhotoImage(image)


            if self.a is None or self.b is None:
                self.panelA = tk.Label(self.f2, image=image)
                self.panelA.image = image
                self.panelA.grid()


            else:
                self.panelA.configure(image=image)
                self.panelA.image = image



obj_interface = interface()
