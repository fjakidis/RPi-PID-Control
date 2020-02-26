import gpiozero as gp
import curses 
import time

out1 = gp.DigitalOutputDevice(16)
out2 = gp.DigitalOutputDevice(20)
out3 = gp.DigitalOutputDevice(21)

## Motor 1
HS11 = gp.DigitalInputDevice(11)		# board pin 23
HS21 = gp.DigitalInputDevice(0)			# board pin 27
HS31 = gp.DigitalInputDevice(4)

'''TUI '''
hall = (HS11.value,HS21.value,HS31.value)
direction = 0
screen = curses.initscr()
dims = screen.getmaxyx()
while True:

	screen.clear()
	screen.addstr('-------------INPUTS---------\n')
	screen.addstr('Motor 1\n')
	screen.addstr('----------\n')
	screen.addstr('Hall Sensor 1 : {0}\n'.format(HS11.value))
	screen.addstr('Hall Sensor 2 : {0}\n'.format(HS21.value))
	screen.addstr('Hall Sensor 3 : {0}\n'.format(HS31.value))
	screen.addstr('hall {0}'.format(hall))
	if(HS11.value==1 and HS21.value==1 and HS31.value==0):
		screen.addstr('\nYes')
		if(HS11.value==1 and HS21.value==0 and HS31.value==1):
			direction = 1
		else:
			direction = 0
	else: 
		screen.addstr('\nNo')
	screen.addstr('\nDirection {0}'.format(direction))
	screen.refresh()
	time.sleep(0.05)
screen.getch()
curses.endwin()


