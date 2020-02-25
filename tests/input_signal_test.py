'''
	Test 1
	------

	- Test input pins with function generator signals. 

	- Use digital outputs to test inputs

'''

import gpiozero as gp
import curses 
import time

'''Setup I/O's '''

### Inputs

## Motor 1
HS11 = gp.DigitalInputDevice(11)		# board pin 23
HS21 = gp.DigitalInputDevice(0)			# board pin 27
HS31 = gp.DigitalInputDevice(4)			# board pin 7
ENC1 = gp.DigitalInputDevice(17)		# board pin 11

## Motor 2
HS12 = gp.DigitalInputDevice(27)		# board pin 13
HS22 = gp.DigitalInputDevice(22)		# board pin 15
HS32 = gp.DigitalInputDevice(10)		# board pin 19
ENC2 = gp.DigitalInputDevice(9)			# board pin 21

### Outputs


## Motor 1
PH11 = gp.DigitalOutputDevice(14)		# board pin 8
PH21 = gp.DigitalOutputDevice(15)		# board pin 10
PH31 = gp.DigitalOutputDevice(18)		# board pin 12

## Motor 2
PH12 = gp.DigitalInputDevice(23)		# board pin 16
PH22 = gp.DigitalInputDevice(24)		# board pin 18
PH32 = gp.DigitalInputDevice(26)		# board pin 22

'''Create Data structures for pins'''

## Hall Sensors



'''TUI '''
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
	screen.addstr('Encoder       : {0}\n'.format(ENC1.value))
	screen.addstr('\n')
	screen.addstr('Motor 2\n')
	screen.addstr('----------\n')
	screen.addstr('Hall Sensor 1 : {0}\n'.format(HS12.value))
	screen.addstr('Hall Sensor 2 : {0}\n'.format(HS22.value))
	screen.addstr('Hall Sensor 3 : {0}\n'.format(HS32.value))
	screen.addstr('Encoder       : {0}\n'.format(ENC2.value))
	screen.addstr('\n')
	screen.addstr('------------OUTPUTS---------\n')
	screen.addstr('Motor 1\n')
	screen.addstr('----------\n')	
	screen.addstr('Phase 1 : {0}\n'.format(PH11.value))
	screen.addstr('Phase 2 : {0}\n'.format(PH21.value))
	screen.addstr('Phase 3 : {0}\n'.format(PH31.value))
	screen.addstr('\n')
	screen.addstr('Motor 2\n')
	screen.addstr('----------\n')
	screen.addstr('Phase 1 : {0}\n'.format(PH12.value))
	screen.addstr('Phase 2 : {0}\n'.format(PH22.value))
	screen.addstr('Phase 3 : {0}\n'.format(PH32.value))
	screen.refresh()
	time.sleep(0.05)
screen.getch()
curses.endwin()


