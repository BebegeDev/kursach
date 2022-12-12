import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import pandas as pd


def writer_d(ny, N, dN):
    data_writer = {'N': N, 'ny': ny, 'dN': dN}
    df = pd.DataFrame(data_writer)
    wr = pd.ExcelWriter('OUT_ter.xlsx', engine='xlsxwriter')
    df.to_excel(wr, "Sheet1")
    wr.close()


class Windows:

    def __init__(self):
        self.N = None
        self.ny = None
        self.dN = None
        self.data = None
        self.columns = None
        self.flag_button = None
        self.windows_main = tk.Tk()

        # создание тайтла
        self.windows_main.title('Пробное окно программы')

        # создание окна приложения
        self.windows_main.rowconfigure(0, minsize=500, weight=1)
        self.windows_main.columnconfigure(1, minsize=400, weight=1)

        # создание рамки
        btn_frm = tk.Frame(self.windows_main)

        # кнопка выбор характеристики
        self.btn_gt = tk.Button(btn_frm, text='Э. Хар. ГТ', command=self.flag_setting_button_Gt)
        self.btn_rab = tk.Button(btn_frm, text='Рабочая ГА', command=self.flag_setting_button_rab)

        # таблица
        columns = ['ny', 'N']
        self.table = ttk.Treeview(self.windows_main, columns=columns, show='headings')
        self.table.grid(column=1, row=0, padx=10, pady=5, sticky='nw')
        self.table.heading("ny", text="КПД, %")
        self.table.heading("N", text="Мощность, МВт")
        self.table.grid(column=1, row=0, padx=10, pady=5, sticky='nw')

        # кнопка выбрать файл
        btn_open = tk.Button(btn_frm, text='Выбрать', command=self.open_file)

        lb_har = tk.Label(btn_frm, text='Выберите характеристику')
        lb_open = tk.Label(btn_frm, text='Выберите файл')

        # размещение ярлыков
        btn_frm.grid(column=0, row=0, sticky='ns')
        self.btn_gt.grid(column=1, row=0, padx=5, pady=5, sticky='ew')
        self.btn_rab.grid(column=2, row=0, padx=5, pady=5, sticky='ew')
        btn_open.grid(column=1, row=1, padx=5, pady=5, sticky='ew')
        lb_har.grid(column=0, row=0)
        lb_open.grid(column=0, row=1)

        tk.mainloop()

    def data_table(self, data_table):
        columns = list(c for c in data_table.columns)
        self.table = ttk.Treeview(self.windows_main, columns=columns, show='headings')
        self.table.heading("ny", text="КПД, %")
        self.table.heading("N", text="Мощность, МВт")

        for i in range(len(data_table)):
            self.table.insert('', tk.END, values=[data_table['ny'].iloc[i], data_table['N'].iloc[i]])

        self.table.grid(column=1, row=0, padx=10, pady=5, sticky='nw')

    def open_file(self):
        filepath = fd.askopenfilename(filetypes=[('Excel', '*.xlsx')])
        if not filepath:
            return
        with open(filepath, 'r'):
            xls = pd.ExcelFile(f'{filepath}')
            df = xls.parse()
            self.data = pd.DataFrame(df)
            self.data_table(self.data)

    def flag_setting_button_Gt(self):
        self.flag_button = 1
        self.btn_gt.configure(background="#FFFF3E")

    def flag_setting_button_rab(self):
        self.flag_button = 2

    def return_Data(self):
        return self.data, self.flag_button


data = Windows()
data_re = data.return_Data()
