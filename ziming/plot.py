import datetime as dt
import matplotlib.pyplot as plt
import serial as sl
import matplotlib.animation as animation

arduino = sl.Serial('/dev/cu.usbmodem14101',9600)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax = plt.axes(xlim=(0,100),ylim=(0,100))
x_read= 0
y_read = 0
x = []
y = []
def animate(i,x,y):
    x_read = arduino.readline(100)
    #while arduino.read() != 'y':
       #1
    y_read = arduino.readline(100)
    x.append(x_read)
    y.append(y_read)
     
    x = x[-20:]
    y = y[-20:]

    ax.clear()
    ax.plot(x, y)

    # Format plot
  #  plt.xticks(rotation=45, ha='right')
  #  plt.subplots_adjust(bottom=0.30)

ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=1000)
plt.show()
