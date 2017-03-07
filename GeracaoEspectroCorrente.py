import numpy as np
import matplotlib.pyplot as plt

class GeraEspectroCorrente:

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

    # geracao de espectros
    Y=abs(np.fft.fft(y))
    Yn=abs(np.fft.fft(yn))
    f=np.arange(0,len(Y))*fs/len(Y)
    # ou: f=arange(0,fs,fs/len(Y))
    df=int(200*len(Y)/fs) # observação até 200Hz
    plt.subplot(211)
    plt.plot(f[:df],Y[:df])
    plt.ylabel('|Y(f)|'), plt.grid()
    plt.subplot(212)
    plt.plot(f[:df],Yn[:df])
    plt.ylabel('|Yn(f)|'), plt.grid()
    plt.xlabel('f, Hz')
    plt.show()