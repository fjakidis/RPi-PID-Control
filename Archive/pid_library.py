import wiringpi as wp
import time

### Const

## I/O
INPUT  = 0
OUTPUT = 1

## Wiring Pi # - Board Pin - Converstion

# Inputs
WP8  = 3
WP9  = 5
WP7  = 7
WP0  = 11
WP2  = 13
WP3  = 15
WP12 = 19
WP13 = 21

# Outputs
WP14 = 23
WP30 = 27

# Other
WP21 = 29
WP22 = 31
WP23 = 33
WP24 = 35
WP25 = 37
WP15 = 15
WP16 = 16
WP1  = 1
WP4  = 4
WP5  = 5
WP6  = 6
WP10 = 10
WP11 = 11
WP31 = 31
WP26 = 26
WP27 = 27
WP28 = 28
WP29 = 29

# Pin functions
HALL_11 = WP8
HALL_21 = WP9
HALL_31 = WP7

HALL_12 = WP0
HALL_22 = WP2
HALL_32 = WP3

ENCODER_1 = WP12
ENCODER_2 = WP13

OUTPUT_1 = WP23
OUTPUT_2 = WP27



### Classes

### Helper functions
def setupPin(pin,val):
	wp.pinMode(pin,val)
def read(pin):
	return wp.digitalRead(pin)
def changeValue(pin):
	val = read(pin)
	print(val)
	if(val==1):
		wp.digitalWrite(pin,1)
	else:
		wp.digitalWrite(pin,0)

###