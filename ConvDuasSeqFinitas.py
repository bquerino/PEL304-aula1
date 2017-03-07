import numpy as np
import matplotlib.pyplot as plt

h=[1,1,1,1,0,0]
x=[1,1,1,0,0,0]
y=np.convolve(h,x)
n=np.arange(len(x))
plt.subplot(311),
plt.stem(n,h), plt.ylabel('h(n)'),
plt.subplot(312),
plt.stem(n,x), plt.ylabel('x(n)'),
plt.subplot(313),
plt.stem(n,y[:len(x)]), plt.ylabel('y(n)'),
plt.xlabel('n'), plt.grid()
plt.show()