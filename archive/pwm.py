import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(19,GPIO.OUT)

p = GPIO.PWM(19,100)

# GPIO18 as PWM with 100Hz frequency
p.start(0)

while 1:

	for x in range(100):
		p.ChangeDutyCycle(x)
		time.sleep(0.01)

	for x in range(100):
		p.ChangeDutyCycle(100-x)
		time.sleep(0.01)