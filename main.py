'''
	************************************************
	PID Control with Python and Raspberry Pi
	----------------------------------------

	Author				: Jason Fakidis
	Team  				: 101
	Contributions: 		: Ziming Wu, Estalin Alvares, Jason Fakidis, Nicole Zhang

	************************************************

	Functional Description
	---------------------

	motor.py
	- Set I/O pin's as required



'''
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from time import sleep

SAMPLE_TIME = 1



### (1)

# enumerate all possible pins, 27 in total
pins = ( 2, 3, 4,17,27,22,10, 9,11,
		 6,13,19,26,14,15,18,23,24,
		25, 8, 7,12,16,20,21, 5)


# assign pins to I/O's


 


