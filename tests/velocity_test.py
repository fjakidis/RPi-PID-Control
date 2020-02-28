import gpiozero as gp
import curses 
import time

# Constants

initial_phase 	= 0
phase_past 	= 0
count 		= -1

A		= 1
B		= 2
C		= 3

# Define a phase mapping
pmap = {
	110: A,
	10 : A,
	11 : B,
	1  : B,
	101: C,
	100: C,
	111: 0,
	0  : 0
	}



# Motor 1
HS11 = gp.DigitalInputDevice(11)		# board pin 23
HS21 = gp.DigitalInputDevice(0)			# board pin 27
HS31 = gp.DigitalInputDevice(4)			# board pin 7

# Setup

dir = 'None'		# direction string variable

index = 100*HS11.value + 10*HS21.value + HS31.value

# Hall direction sensing algorithm
def readingHall(pin1,pin2,pin3):

	## global variables 
	global phase
	global phase_past
	global count
	global dir
	global diff

	# initialize phase difference
	diff = 0

	# save current hall sensor values
	hall = (pin1.value, pin2.value, pin3.value)

	# calulate index
	index = 100*hall[0] + 10*hall[1] + hall[2]

	# map index to phase
	phase = pmap[index]

	# if motor phase changes
	if(phase != phase_past):
		
		count += 1
		
		diff = phase - phase_past

	if(diff == 1 or diff == -2):
		dir = 'Forward'
	else: 
		dir = 'Backward'
	
	# reset phase_pst
	phase_past = phase
	
		
	return 0

# TUI
hall = (HS11.value,HS21.value,HS31.value)
direction = 0
screen = curses.initscr()
dims = screen.getmaxyx()
ind = 0
while True:
	screen.clear()
	readingHall(HS11,HS21,HS31)
	screen.addstr('-------------INPUTS---------\n')
	screen.addstr('Motor 1\n')
	screen.addstr('----------\n')
	screen.addstr('Hall Sensor 1 : {0}\n'.format(HS11.value))
	screen.addstr('Hall Sensor 2 : {0}\n'.format(HS21.value))
	screen.addstr('Hall Sensor 3 : {0}\n'.format(HS31.value))
	screen.addstr('\nDirection {0}'.format(dir))
	#screen.addstr('\nPhase {0}'.format(phase))
	#screen.addstr('\nPhase Past {0}'.format(phase_past))
	#screen.addstr('\nCount {0}'.format(count))
	screen.addstr('\nDiff {0}'.format(diff))
	screen.refresh()
	time.sleep(0.05)
screen.getch()
curses.endwin()


