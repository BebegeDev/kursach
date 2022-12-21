import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image
from PIL import ImageTk
from Haracteristiki import InitProg, Approximation
import pandas as pd
class interface:

    def __init__(self, root):
        self.root = root
        self.index = []
        self.e = None
        self.index_e = None
        self.H = None
        self.panelA = None
        self.path = None
        self.s = None
        self.a = None
        option_list = ["Агрегат №8"]

        # Первый FRAME
        self.f1 = tk.Frame(self.root,)
        self.f1.grid(row=0, column=0)

        # Второй FRAME
        self.f2 = tk.Frame(self.root,)
        self.f2.grid(row=0, column=1, rowspan=2)

        # Третий FRAME
        self.f3 = tk.Frame(self.root,)
        self.f3.grid(row=0, column=2, rowspan=2)

        # Четвертый FRAME
        # self.f4 = tk.Frame(self.root, bg='yellow')
        # self.f4.grid(row=1, column=1, sticky='ew', columnspan=2, rowspan=2)

        # Пятый FRAME
        self.f5 = tk.Frame(self.root)
        self.f5.grid(row=1, sticky='ew',)

        # 6 FRAME
        self.f6 = tk.Frame(self.root)
        self.f6.grid(row=0, column=3, sticky='ew',)

        # Entry
        self.e_H = tk.Entry(self.f1)
        self.e_H.grid(column=1, row=1, sticky='ew',)

        # Label 1 АГРЕГАТ
        self.l1 = tk.Label(self.f1, text="Выберите агрегат")
        self.l1.grid(column=0, row=0, sticky='ew')

        # Label 2 НАПОР
        self.l2 = tk.Label(self.f1, text="Введите напор H, м")
        self.l2.grid(column=0, row=1, sticky='ew')

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
        b2 = tk.Button(self.f5, text="Рассчитать", command=self.rr)
        b2.grid(column=0, row=19, sticky='ew', columnspan=4)

        self.canvas2 = tk.Canvas(self.f2, height=610, width=1050,)
        self.canvas2.grid(column=1, row=0)

        # self.canvas4 = tk.Canvas(self.f4, height=450, width=1500, bg='red')
        # self.canvas4.grid(column=0, row=0)

        self.comboExample = ttk.Combobox(self.f1, values=option_list)
        self.comboExample.grid(column=1, row=0, sticky='w')

        # Button НАПОР
        b3 = tk.Button(self.f1, text="Задать напор", command=self.pressure)
        b3.grid(column=4, row=1, sticky='ew')

        # Table 2
        columns1 = ['ny', 'N']
        self.table2 = ttk.Treeview(self.f3, columns=columns1, show='headings', height=28)
        self.table2.heading("ny", text="КПД, %")
        self.table2.heading("N", text="Мощность, МВт")
        self.table2.grid(column=0, row=1, sticky='ew')

        treeScroll = ttk.Scrollbar(self.root, orient="vertical", command=self.table2.yview)
        treeScroll.place(x=1890, y=50, height=560)
        self.table2.configure(yscrollcommand=treeScroll.set)
        self.table_entry()

    def focus(self, event, e):
        e = str(e)[-2:]
        if e == "ry":
            e = 0
        else:
            e = [i for i in e if i.isdigit()]
            if len(e) == 2:
                e = int(e[0] + e[1]) - 1
            else:
                e = int(e[0]) - 1
        self.e = e
        return self.e

    def select_image(self):
        try:
            self.selection = self.comboExample.get()
            path_Ag = {"Агрегат №8": "Graf/Ag8.png"}
            image = Image.open(path_Ag[self.selection])
            resize_image = image.resize((1050, 610))
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
            try:
                self.list_e[self.e].delete(0, 'end')
                self.list_e[self.e].insert(0, self.num)
            except TypeError:
                pass

    def table_entry(self):
        self.list_e = []
        count_list_e = 0
        c = 0
        d = 1
        k = 2
        for i in range(2):
            for j in range(16):
                if count_list_e + 70 <= 90:
                    self.create_list_e(count_list_e, i, j, c, d, 0)
                    count_list_e += 1
                else:
                    self.create_list_e(count_list_e, i, j, c, d, k)
                    k += 2
                    count_list_e += 1
            c = 1
            d = 2

    def table_end(self, N, ny):
        self.table2.delete(*self.table2.get_children())
        for i in range(len(N)):
            self.table2.insert('', tk.END, values=(ny.iloc[i], N.iloc[i]))

    def create_list_e(self, count_list_e, i, j, c, d, *args):
        self.list_e.append(tk.Entry(self.f5, width=10, fg='blue', font=('Arial', 16, 'bold')))
        self.list_e[count_list_e].bind("<Button-1>",
                                       lambda event, e=self.list_e[count_list_e]: self.focus(event, e))
        self.list_e[count_list_e].grid(row=j + 3, column=i + d, sticky='ew')
        tk.Label(self.f5, text=f"{70 + count_list_e - args[0]}%", width=11).grid(column=i + c, row=3 + j, )

    def pressure(self):
        try:
            int(self.e_H.get())
            self.H = self.e_H.get()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите численное значение")

    def rr(self):
        data_ny = []
        data_N = []
        c = 1
        for a in self.list_e:
            if str(a.get()).replace(" ", ""):
                index_ny = self.focus(None, a)
                if index_ny == 0:
                    data_ny.append(70,)
                    data_N.append(int(a.get()))
                elif index_ny <= 20:
                    data_ny.append(70 + index_ny)
                    data_N.append(int(a.get()))
                else:
                    data_ny.append(110 - index_ny)
                    data_N.append(int(a.get()))
                    c += 1


        data = {'ny': data_ny, 'N': data_N}
        data = pd.DataFrame(data)
        ag_init = InitProg(data)
        dN, ny, N = ag_init.get_dN()
        if len(data['N']) > 5:
            ag_aprox = Approximation(N, ny, dN)
            N, ny, _ = ag_aprox.approximation()
            N = pd.Series(N)
            ny = pd.Series(ny)
            self.table_end(N, ny)
            ag_aprox.mapping_aproks()
        else:
            messagebox.showerror('Ошибка', "Пожалуйста укажите больше 10 значений")


def main():
    root = tk.Tk()
    root.geometry('1920x1080')
    obj_interface = interface(root)
    root.mainloop()

if __name__ == '__main__':
    main()