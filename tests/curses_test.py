import curses
import time

screen = curses.initscr()
dims = screen.getmaxyx()
while True:
	screen.clear()
	screen.addstr(10,0, 'Hello')
	screen.refresh()
	time.sleep(0.5)
screen.getch()
curses.endwin()

while True:

	print('-------------INPUTS---------')
	print('Motor 1')
	print('Hall Sensor 1 : {0}'.format(HS11.value))
	print('Hall Sensor 2 : {0}'.format(HS21.value))
	print('Hall Sensor 3 : {0}'.format(HS31.value))
	print('Encoder       : {0}'.format(ENC1.value))
	print()
	print('Motor 2')
	print('Hall Sensor 1 : {0}'.format(HS12.value))
	print('Hall Sensor 2 : {0}'.format(HS22.value))
	print('Hall Sensor 3 : {0}'.format(HS32.value))
	print('Encoder       : {0}'.format(ENC2.value))
	print()
	print('------------OUTPUTS---------')
	print('Motor 1')
	print('Phase 1 : {0}'.format(PH11.value))
	print('Phase 2 : {0}'.format(PH21.value))
	print('Phase 3 : {0}'.format(PH31.value))
	print()
	print('Motor 2')
	print('Phase 1 : {0}'.format(PH12.value))
	print('Phase 2 : {0}'.format(PH22.value))
	print('Phase 3 : {0}'.format(PH32.value))

	os.system('clear')