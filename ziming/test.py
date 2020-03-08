import tkinter as tk
import serial as sl
from tkinter import simpledialog as sd
arduino = sl.Serial('/dev/cu.usbmodem14101',9600)
parent = tk.Tk()
parent.overrideredirect(1)
parent.iconbitmap("PythonIcon.ico")
parent.withdraw()

while 1:
 direction = sd.askstring("Direction","Forward(F) or Backward(B)", parent=parent)
 arduino.write(direction.encode());
 #while direction_finished = sl.read() == 0
 phase_num = sd.askinteger("Phase", "Phase number for rotation", minvalue = 0, maxvalue = 99, parent = parent)
 arduino.write(str(phase_num).encode())
