import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import TestTk

class Approximation:

    def __init__(self, N, ny, dN, flag):
        self.N = N
        self.ny = ny
        self.dN = dN
        self.flag = flag

    def approximation(self):
        assert self.flag == 1 or self.flag == 2, "Ошибка с флагом кнопки"
        new_N = np.arange(min(self.N), max(self.N))
        model_N_ny = np.polyfit(self.N, self.ny, 3)
        model_N_dN = np.polyfit(self.N, self.dN, 4)
        predict_N_ny = np.poly1d(model_N_ny)
        predict_N_dN = np.poly1d(model_N_dN)
        func1 = predict_N_ny(new_N)
        func2 = predict_N_dN(new_N)
        return new_N, func1, func2


    def mapping_aproks(self, flag):
            new_N, func1, func2 = self.approximation()
            fig, ax = plt.subplots()
            ax.plot(self.N, self.ny, 'o', new_N, func1, '-', label='fit')
            plt.xlabel("N, кВт")
            plt.ylabel('ny, %')
            plt.grid()
            plt.legend()
            plt.show()
            fig, ax = plt.subplots()
            ax.plot(self.N, self.dN, 'o', new_N, func2, '-', label='fit')
            plt.xlabel("N, кВт")
            plt.ylabel('dN, кВт')
            plt.grid()
            plt.legend()
            plt.show()


class InitProg:

    def __init__(self):
        data, flag = TestTk.data_re
        self.ny = data["ny"]
        self.N = data["N"]
        self.flag = flag


    def get_dN(self):
        dN = pd.Series(map(lambda N, ny: N * (100 - ny) / ny, self.N, self.ny))

        for i in range (0, 5):
            dN [i] = dN[5] + (dN[5] / 2 - dN[i])

        return dN, self.ny, self.N, self.flag


def main():
    ag_init = InitProg()
    dN, ny, N, flag = ag_init.get_dN()
    ag_aprox = Approximation(N, ny, dN, flag)
    ag_aprox.mapping_aproks(flag)
    TestTk.writer_d(ny, N, dN)


if __name__ == '__main__':
    main()