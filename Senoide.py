import numpy as np
import matplotlib.pyplot as plt

#Código que ilustra uma senoide de 95 Hz amostrada a 100 Hz

fs=100 # freq. amostragem, Hz
fa=95  # freq. sinal analógico, Hz
T=0.2  # duracao em segundos
t=np.arange(T*fs+1)/fs # tempo discreto
ta=np.arange(T*fs*100)/(fs*100) # tempo
pi = np.pi
sd=np.cos(2*pi*(fs-fa)*t)  # sinal discreto
sa=np.cos(2*pi*fa*ta)      # sinal analógico
plt.figure(figsize=(12,15))
plt.subplot(311)
plt.plot(ta,sa,color='k'), plt.grid()
plt.title("Sinal analógico, senoide de %g Hz" % fa)
plt.xlabel("t, s")
plt.subplot(312)
plt.stem(t,sd)
plt.hold(True)
plt.plot(ta,sa,color='k')
plt.plot(t,sd, ':')
plt.hold(False), plt.grid()
plt.xlabel("t, s")
plt.title("Senoide de %g Hz amostrada a %g Hz" % (fa, fs))
plt.subplot(313)
plt.stem(np.arange(T*fs+1),sd)
plt.title("Sinal discreto")
plt.xlabel("n")
plt.show()