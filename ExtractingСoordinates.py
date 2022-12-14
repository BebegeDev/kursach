import tkinter as tk
from tkinter import ttk, filedialog
import cv2
import PIL.Image, PIL.ImageTk
from PIL import Image
from PIL import ImageTk


class PPP:

    def __init__(self):
        self.root = tk.Tk()
        self.a = None
        self.b = None

        self.f1 = tk.Frame(self.root)
        self.f1.grid(row=0, column=0)

        # Button АГРЕГАТ
        b1 = tk.Button(self.f1, text="Выбрать агрегат", command=self.select_image)
        b1.grid()

        self.root.mainloop()

    def select_image(self):
        self.path = filedialog.askopenfilename()

        if self.path:
            image = cv2.imread(self.path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 50, 100)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            edged = Image.fromarray(edged)
            image = ImageTk.PhotoImage(image)
            edged = ImageTk.PhotoImage(edged)

            if self.a is None or self.b is None:
                self.panelA = tk.Label(self.f1, image=image)
                self.panelA.image = image
                self.panelA.grid(column=3, row=0)

                self.panelB = tk.Label(self.f1, image=edged)
                self.panelB.image = edged
                self.panelB.grid(column=3, row=0)
            else:
                self.panelA.configure(image=image)
                self.panelB.configure(image=edged)
                self.panelA.image = image
                self.panelB.image = edged

PPP()