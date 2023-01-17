import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Approximation:

    def __init__(self, N, ny, dN, k):
        self.N = N
        self.ny = ny
        self.dN = dN
        self.k = k


    def approximation(self):
        self.new_N = np.arange(min(self.N), max(self.N))
        model_N_ny = np.polyfit(self.N, self.ny, self.k)
        model_N_dN = np.polyfit(self.N, self.dN, self.k)
        predict_N_ny = np.poly1d(model_N_ny)
        predict_N_dN = np.poly1d(model_N_dN)
        func1 = predict_N_ny(self.new_N)
        func2 = predict_N_dN(self.new_N)
        return self.new_N, func1, func2


    def mapping_aproks(self):
        new_N, func1, func2 = self.approximation()
        fig, ax = plt.subplots()
        ax.plot(self.N, self.ny, 'o', new_N, func1, '-', label='fit')
        plt.xlabel("N, кВт")
        plt.ylabel('ny, %')
        plt.grid()
        plt.legend()
        plt.savefig("Chart_1.png")
        fig, ax = plt.subplots()
        ax.plot(self.N, self.dN, 'o', new_N, func2, '-', label='fit')
        plt.xlabel("N, кВт")
        plt.ylabel('dN, кВт')
        plt.grid()
        plt.legend()
        plt.savefig("Chart_2.png")

    def new_image(self):
        img = Image.new('RGB', (1200, 480), "white")

        img1 = Image.open("Chart_1.png")
        img2 = Image.open("Chart_2.png")

        img_size = img1.resize((525, 360))
        img1_size = img2.resize((525, 360))

        img.paste(img1, (0, 0))
        img.paste(img2, (580, 0))

        img.save("Chart_3.png")

    def return_N(self):
        return self.N


class InitProg:

    def __init__(self, data):
        self.ny = data["ny"]
        self.N = data["N"]


    def get_dN(self):
        dN = pd.Series(map(lambda N, ny: N * (100 - ny) / ny, self.N, self.ny))

        # for i in range (0, 5):
        #     dN [i] = dN[5] + (dN[5] / 2 - dN[i])

        return dN, self.ny, self.N