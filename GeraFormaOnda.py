import numpy as np
import matplotlib.pyplot as plt


class GeraFormaOnda:

        # construtor dos valores
        # geracao de forma de onda
        fs = 1000  # freq. amostragem, Hz
        T = 1  # duracao em segundos
        t = np.arange(fs * T) / fs  # tempo
        f1 = 50  # freq sinal 1 em Hz
        f2 = 120  # freq sinal 2 em Hz
        pi = np.pi
        y = np.sin(2 * pi * f1 * t) + np.sin(2 * pi * f2 * t)
        yn = y + 0.3 * np.random.randn(len(t))  # y+ruido
        dt = 50  # faixa de observacao

        plt.subplot(211)
        plt.plot(t[:dt], y[:dt])
        plt.title('y(t)')
        plt.grid()
        plt.subplot(212)
        plt.plot(t[:dt], yn[:dt])
        plt.title('yn(t)')
        plt.grid()
        plt.xlabel('t, s')
        plt.show()