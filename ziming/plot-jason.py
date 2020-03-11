import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 1

t = np.linspace(0,np.pi,100)
k = np.linspace(0,np.pi,100)

x = a*np.sin(t)+b*np.sin(k)
y = a*np.cos(t)+b*np.cos(k)

plt.plot(x,y)
plt.plot(0,0)

plt.style.use('ggplot')
plt.show()
